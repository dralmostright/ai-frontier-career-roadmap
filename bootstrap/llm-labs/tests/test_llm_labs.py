"""Weeks 25-36 — tokenization, attention, transformers, sampling.

Skips automatically until torch is installed.
"""

from __future__ import annotations

import math

import pytest

torch = pytest.importorskip("torch", reason="install torch in Month 4")

from attention import (  # noqa: E402
    MultiHeadAttention,
    causal_mask,
    kv_cache_memory,
    padding_mask,
    scaled_dot_product_attention,
)
from mini_gpt import GPTConfig, MiniGPT  # noqa: E402
from sampling import apply_temperature, greedy, top_k_filter, top_p_filter  # noqa: E402
from tokenizer import BPETokenizer, compression_ratio  # noqa: E402


@pytest.mark.week(25)
class TestBPE:
    @pytest.fixture
    def trained(self):
        corpus = [
            "the quick brown fox jumps over the lazy dog. " * 20,
            "the rain in spain falls mainly on the plain. " * 20,
        ]
        return BPETokenizer(vocab_size=400).train(corpus, verbose=False)

    def test_roundtrip(self, trained):
        text = "the quick brown fox"
        assert trained.decode(trained.encode(text)) == text

    def test_roundtrip_with_unicode_and_emoji(self, trained):
        """Byte-level BPE must handle anything. No unknown token, ever."""
        for text in ["café", "日本語", "hello 👋 world", "  leading and trailing  "]:
            assert trained.decode(trained.encode(text)) == text

    def test_never_produces_an_unknown_token(self, trained):
        ids = trained.encode("zzqxjk unseen gibberish ᚠᚢᚦ")
        assert all(isinstance(i, int) for i in ids)
        assert len(ids) > 0

    def test_merges_reduce_token_count(self, trained):
        """A trained tokenizer must beat raw bytes on its training distribution."""
        text = "the quick brown fox"
        assert len(trained.encode(text)) < len(text.encode("utf-8"))

    def test_compression_ratio_is_reported(self, trained):
        stats = compression_ratio(trained, "the quick brown fox jumps")
        assert stats["chars_per_token"] > 1.0

    def test_save_and_load(self, trained, tmp_path):
        trained.save(tmp_path / "tok.json")
        reloaded = BPETokenizer.load(tmp_path / "tok.json")
        assert reloaded.encode("the quick") == trained.encode("the quick")


@pytest.mark.week(29)
class TestAttention:
    def test_output_shape(self):
        q = torch.randn(2, 5, 16)
        k = torch.randn(2, 7, 16)
        v = torch.randn(2, 7, 32)
        out, weights = scaled_dot_product_attention(q, k, v)
        assert out.shape == (2, 5, 32)
        assert weights.shape == (2, 5, 7)

    def test_weights_form_a_distribution(self):
        q, k, v = torch.randn(2, 4, 8), torch.randn(2, 6, 8), torch.randn(2, 6, 8)
        _, weights = scaled_dot_product_attention(q, k, v)
        torch.testing.assert_close(weights.sum(dim=-1), torch.ones(2, 4))
        assert (weights >= 0).all()

    def test_matches_pytorch_reference(self):
        q, k, v = torch.randn(2, 4, 8), torch.randn(2, 6, 8), torch.randn(2, 6, 8)
        mine, _ = scaled_dot_product_attention(q, k, v)
        reference = torch.nn.functional.scaled_dot_product_attention(q, k, v)
        torch.testing.assert_close(mine, reference, rtol=1e-4, atol=1e-5)

    def test_identical_keys_produce_uniform_attention(self):
        """A sanity check with an obvious right answer."""
        q = torch.randn(1, 1, 8)
        k = torch.ones(1, 4, 8)
        v = torch.randn(1, 4, 8)
        _, weights = scaled_dot_product_attention(q, k, v)
        torch.testing.assert_close(weights, torch.full((1, 1, 4), 0.25), rtol=1e-5, atol=1e-6)

    def test_causal_mask_is_lower_triangular(self):
        mask = causal_mask(4)
        assert mask.shape == (4, 4)
        assert bool(mask[0, 0]) and not bool(mask[0, 1])
        assert bool(mask[3, 0]) and bool(mask[3, 3])

    def test_causal_mask_blocks_the_future(self):
        """Position i must not attend to anything after i."""
        q = k = v = torch.randn(1, 5, 8)
        _, weights = scaled_dot_product_attention(q, k, v, mask=causal_mask(5))
        upper = torch.triu(weights[0], diagonal=1)
        assert upper.abs().max().item() < 1e-8

    def test_changing_a_future_token_cannot_change_the_present(self):
        """The strongest possible test of causality."""
        x = torch.randn(1, 6, 8)
        out_a, _ = scaled_dot_product_attention(x, x, x, mask=causal_mask(6))
        y = x.clone()
        y[0, 5] = torch.randn(8)  # perturb the last position only
        out_b, _ = scaled_dot_product_attention(y, y, y, mask=causal_mask(6))
        torch.testing.assert_close(out_a[0, :5], out_b[0, :5], rtol=1e-5, atol=1e-6)

    def test_scaling_prevents_softmax_saturation(self):
        """Why the sqrt(d). Without it, high-dimensional scores saturate."""
        d = 512
        q, k, v = torch.randn(1, 4, d), torch.randn(1, 4, d), torch.randn(1, 4, d)
        _, scaled = scaled_dot_product_attention(q, k, v)
        unscaled = torch.softmax(q @ k.transpose(-2, -1), dim=-1)
        assert scaled.max().item() < unscaled.max().item()

    def test_fully_masked_row_does_not_produce_nan(self):
        """Use a large negative number, not -inf. Padding creates this case."""
        q, k, v = torch.randn(1, 2, 8), torch.randn(1, 3, 8), torch.randn(1, 3, 8)
        mask = torch.zeros(1, 2, 3, dtype=torch.bool)
        mask[0, 0] = True
        out, _ = scaled_dot_product_attention(q, k, v, mask=mask)
        assert not torch.isnan(out).any()

    def test_padding_mask_shape(self):
        mask = padding_mask(torch.tensor([2, 4, 3]), max_len=5)
        assert mask.shape == (3, 5)
        assert mask[0].sum().item() == 2


@pytest.mark.week(30)
class TestMultiHeadAttention:
    def test_preserves_shape(self):
        mha = MultiHeadAttention(d_model=64, n_heads=8)
        x = torch.randn(2, 10, 64)
        assert mha.forward(x).shape == x.shape

    def test_rejects_indivisible_head_count(self):
        with pytest.raises((ValueError, AssertionError)):
            MultiHeadAttention(d_model=64, n_heads=7)

    def test_heads_learn_different_patterns(self):
        """One head is one attention pattern. That is why we use several."""
        torch.manual_seed(0)
        mha = MultiHeadAttention(d_model=32, n_heads=4)
        mha.forward(torch.randn(1, 8, 32))
        # after a forward pass the module should expose per-head weights
        assert hasattr(mha, "last_attention_weights")
        weights = mha.last_attention_weights
        assert weights.shape[1] == 4
        assert not torch.allclose(weights[0, 0], weights[0, 1], atol=1e-3)


@pytest.mark.week(32)
class TestMiniGPT:
    @pytest.fixture
    def tiny(self):
        return MiniGPT(GPTConfig(vocab_size=128, block_size=32, n_layer=2, n_head=2, d_model=32))

    def test_forward_shape(self, tiny):
        idx = torch.randint(0, 128, (2, 16))
        logits, loss = tiny.forward(idx)
        assert logits.shape == (2, 16, 128)
        assert loss is None

    def test_initial_loss_is_ln_vocab_size(self, tiny):
        """**The check to run before touching any hyperparameter.**

        An untrained model over V classes must report ln(V). Anything else
        means labels, initialization, or the loss are wrong.
        """
        idx = torch.randint(0, 128, (4, 16))
        _, loss = tiny.forward(idx, targets=idx)
        assert loss.item() == pytest.approx(math.log(128), abs=0.5)

    def test_weight_tying_shares_the_matrix(self, tiny):
        assert tiny.config.tie_weights
        assert tiny.token_embedding.weight.data_ptr() == tiny.lm_head.weight.data_ptr()

    def test_weight_tying_saves_parameters(self):
        tied = MiniGPT(GPTConfig(vocab_size=1000, n_layer=2, d_model=64, tie_weights=True))
        untied = MiniGPT(GPTConfig(vocab_size=1000, n_layer=2, d_model=64, tie_weights=False))
        assert tied.num_parameters["total"] < untied.num_parameters["total"]

    def test_generation_extends_the_sequence(self, tiny):
        out = tiny.generate(torch.randint(0, 128, (1, 4)), max_new_tokens=10)
        assert out.shape == (1, 14)

    def test_generation_crops_to_block_size(self, tiny):
        """Beyond block_size there are no positional embeddings."""
        long_prompt = torch.randint(0, 128, (1, 40))  # block_size is 32
        out = tiny.generate(long_prompt, max_new_tokens=5)
        assert out.shape[1] == 45

    def test_kv_cache_produces_identical_output(self, tiny):
        """Caching is an optimization, not a behavior change."""
        torch.manual_seed(0)
        prompt = torch.randint(0, 128, (1, 8))
        with_cache = tiny.generate(prompt, max_new_tokens=10, temperature=0.0, use_cache=True)
        torch.manual_seed(0)
        without = tiny.generate(prompt, max_new_tokens=10, temperature=0.0, use_cache=False)
        torch.testing.assert_close(with_cache, without)

    def test_kv_cache_memory_math(self):
        """The Week 32 interview calculation, verified."""
        result = kv_cache_memory(
            n_layers=32, n_kv_heads=32, head_dim=128, seq_len=8192, dtype_bytes=2
        )
        expected_gb = 2 * 32 * 32 * 128 * 8192 * 2 / 1e9
        assert result["gb"] == pytest.approx(expected_gb, rel=0.01)
        assert result["gb"] > 4.0, "a single 8k sequence costs several GB — hence PagedAttention"

    def test_parameter_breakdown_is_reported(self, tiny):
        counts = tiny.num_parameters
        assert counts["total"] > 0
        assert "attention" in counts or "blocks" in counts


@pytest.mark.week(35)
class TestSampling:
    def test_greedy_picks_the_argmax(self):
        logits = torch.tensor([[1.0, 5.0, 2.0]])
        assert greedy(logits).item() == 1

    def test_temperature_sharpens_and_flattens(self):
        logits = torch.tensor([[1.0, 2.0, 3.0]])
        cold = torch.softmax(apply_temperature(logits, 0.1), dim=-1)
        hot = torch.softmax(apply_temperature(logits, 5.0), dim=-1)
        assert cold.max() > 0.9
        assert hot.max() < 0.5

    def test_low_temperature_approaches_greedy(self):
        logits = torch.tensor([[1.0, 2.0, 3.0]])
        assert torch.softmax(apply_temperature(logits, 0.01), dim=-1).argmax().item() == 2

    def test_top_k_keeps_exactly_k(self):
        filtered = top_k_filter(torch.tensor([[1.0, 5.0, 2.0, 4.0, 3.0]]), k=2)
        assert torch.isfinite(filtered).sum().item() == 2

    def test_top_p_is_adaptive(self):
        """The advantage over top-k: the nucleus size tracks confidence."""
        peaked = torch.tensor([[10.0, 1.0, 1.0, 1.0, 1.0]])
        flat = torch.tensor([[1.0, 1.0, 1.0, 1.0, 1.0]])
        assert (
            torch.isfinite(top_p_filter(peaked, 0.9)).sum()
            < torch.isfinite(top_p_filter(flat, 0.9)).sum()
        )

    def test_top_p_always_keeps_at_least_one_token(self):
        assert torch.isfinite(top_p_filter(torch.tensor([[10.0, 1.0, 1.0]]), p=0.01)).sum() >= 1
