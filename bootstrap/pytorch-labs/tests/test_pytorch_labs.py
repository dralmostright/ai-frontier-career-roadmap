"""Weeks 17-24 — PyTorch engineering and computer vision.

These tests skip automatically when torch is not installed, so the suite
stays green until you reach Month 4 and install it.
"""

from __future__ import annotations

import pytest

torch = pytest.importorskip("torch", reason="install torch in Month 4")

from cnn import ResidualBlock, SimpleCNN, output_shape, receptive_field  # noqa: E402
from config import capture_environment, set_seed, verify_reproducibility  # noqa: E402
from data import TabularDataset, collate_variable_length, make_loaders  # noqa: E402
from models import count_parameters, freeze_layers, initialize_weights  # noqa: E402
from tensor_labs import (  # noqa: E402
    autograd_walkthrough,
    gradient_accumulation_demo,
    no_grad_vs_detach,
)
from train import Trainer, estimate_memory  # noqa: E402


@pytest.mark.week(17)
class TestAutograd:
    def test_walkthrough_reports_the_right_gradient(self):
        # y = (x+1)^2 * 3 at x=2  ->  dy/dx = 6*(x+1) = 18
        assert autograd_walkthrough(2.0)["grad"] == pytest.approx(18.0)

    def test_gradients_accumulate_without_zero_grad(self):
        result = gradient_accumulation_demo()
        assert result["second_backward"] == pytest.approx(2 * result["first_backward"])

    def test_no_grad_builds_no_graph(self):
        result = no_grad_vs_detach()
        assert result["no_grad_requires_grad"] is False
        assert result["detached_requires_grad"] is False

    def test_detach_shares_storage(self):
        """The subtlety: mutating the detached tensor mutates the original."""
        assert no_grad_vs_detach()["detach_shares_storage"] is True


@pytest.mark.week(18)
class TestData:
    def test_dataset_contract(self):
        X = torch.randn(50, 4)
        y = torch.randint(0, 2, (50,))
        dataset = TabularDataset(X, y)
        assert len(dataset) == 50
        item = dataset[0]
        assert len(item) == 2

    def test_loaders_are_constructed(self):
        X, y = torch.randn(64, 4), torch.randint(0, 2, (64,))
        train, val = make_loaders(
            TabularDataset(X, y), TabularDataset(X, y), batch_size=16, num_workers=0
        )
        assert len(next(iter(train))[0]) == 16
        assert val is not None

    def test_variable_length_collate_pads_and_masks(self):
        batch = [(torch.ones(3), 0), (torch.ones(5), 1), (torch.ones(2), 0)]
        padded, mask, labels = collate_variable_length(batch)
        assert padded.shape == (3, 5)
        assert mask.sum().item() == 10  # 3 + 5 + 2 real positions
        assert labels.shape == (3,)

    def test_mask_marks_padding_as_false(self):
        batch = [(torch.ones(2), 0), (torch.ones(4), 1)]
        _, mask, _ = collate_variable_length(batch)
        assert mask[0, 2:].sum().item() == 0


@pytest.mark.week(18)
class TestModels:
    def test_parameter_count(self):
        from torch import nn

        model = nn.Linear(10, 5)
        counts = count_parameters(model)
        assert counts["total"] == 55  # 10*5 weights + 5 biases

    def test_he_initialization_has_the_expected_scale(self):
        from torch import nn

        layer = nn.Linear(256, 256)
        initialize_weights(layer, scheme="he")
        assert layer.weight.std().item() == pytest.approx((2 / 256) ** 0.5, rel=0.2)

    def test_biases_are_initialized_to_zero(self):
        from torch import nn

        layer = nn.Linear(64, 32)
        initialize_weights(layer, scheme="he")
        assert layer.bias.abs().max().item() == pytest.approx(0.0)

    def test_freeze_layers_stops_gradients(self):
        from torch import nn

        model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 2))
        frozen = freeze_layers(model, ["0."])
        assert frozen > 0
        assert not model[0].weight.requires_grad
        assert model[2].weight.requires_grad


@pytest.mark.week(19)
class TestTraining:
    def test_trainer_reduces_loss(self):
        from torch import nn
        from torch.utils.data import DataLoader, TensorDataset

        X = torch.randn(128, 4)
        y = (X[:, 0] > 0).long()
        loader = DataLoader(TensorDataset(X, y), batch_size=16)
        model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 2))

        trainer = Trainer(
            model=model,
            train_loader=loader,
            optimizer=torch.optim.Adam(model.parameters(), lr=0.01),
            loss_fn=nn.CrossEntropyLoss(),
        )
        first = trainer.train_epoch()["loss"]
        for _ in range(5):
            last = trainer.train_epoch()["loss"]
        assert last < first

    def test_gradient_accumulation_matches_a_large_batch(self):
        """Four steps of batch 8 must equal one step of batch 32.

        If they differ, you forgot to divide the loss by the accumulation
        count, and your effective learning rate is 4x what you think.
        """
        from torch import nn
        from torch.utils.data import DataLoader, TensorDataset

        torch.manual_seed(0)
        X, y = torch.randn(32, 4), torch.randint(0, 2, (32,))

        def run(batch_size, accum):
            torch.manual_seed(0)
            model = nn.Linear(4, 2)
            loader = DataLoader(TensorDataset(X, y), batch_size=batch_size, shuffle=False)
            trainer = Trainer(
                model=model,
                train_loader=loader,
                optimizer=torch.optim.SGD(model.parameters(), lr=0.1),
                loss_fn=nn.CrossEntropyLoss(),
                grad_accum_steps=accum,
            )
            trainer.train_epoch()
            return model.weight.detach().clone()

        torch.testing.assert_close(run(32, 1), run(8, 4), rtol=1e-4, atol=1e-6)

    def test_checkpoint_roundtrip_preserves_optimizer_state(self, tmp_path):
        """Weights-only checkpoints produce a visible jump on resume."""
        from torch import nn
        from torch.utils.data import DataLoader, TensorDataset

        X, y = torch.randn(32, 4), torch.randint(0, 2, (32,))
        model = nn.Linear(4, 2)
        trainer = Trainer(
            model=model,
            train_loader=DataLoader(TensorDataset(X, y), batch_size=8),
            optimizer=torch.optim.Adam(model.parameters(), lr=0.01),
            loss_fn=nn.CrossEntropyLoss(),
            checkpoint_dir=tmp_path,
        )
        trainer.train_epoch()
        trainer.save_checkpoint(tmp_path / "ckpt.pt")
        state = trainer.load_checkpoint(tmp_path / "ckpt.pt")
        assert state.global_step > 0

    def test_memory_estimate_uses_the_16n_rule(self):
        """params + grads + Adam moments = 16 bytes per parameter in fp32."""
        from torch import nn

        model = nn.Linear(1000, 1000)  # ~1e6 parameters
        estimate = estimate_memory(model, batch_size=1, input_shape=(1000,))
        expected_mb = 1_001_000 * 16 / 1e6
        assert estimate["total_mb"] == pytest.approx(expected_mb, rel=0.3)


@pytest.mark.week(20)
class TestReproducibility:
    def test_seeding_makes_runs_identical(self):
        set_seed(42)
        a = torch.randn(10)
        set_seed(42)
        torch.testing.assert_close(a, torch.randn(10))

    def test_environment_capture_includes_the_git_sha(self):
        env = capture_environment()
        assert {"python", "torch", "git_sha"} <= env.keys()

    def test_two_short_runs_produce_identical_losses(self):
        """**The Month 5 capstone gate.** Identical, not close."""
        from torch import nn
        from torch.utils.data import DataLoader, TensorDataset

        X, y = torch.randn(64, 4), torch.randint(0, 2, (64,))

        def train_fn(config):
            set_seed(config.seed if hasattr(config, "seed") else 0)
            model = nn.Linear(4, 2)
            trainer = Trainer(
                model=model,
                train_loader=DataLoader(TensorDataset(X, y), batch_size=8, shuffle=True),
                optimizer=torch.optim.Adam(model.parameters(), lr=0.01),
                loss_fn=nn.CrossEntropyLoss(),
            )
            return [trainer.train_epoch()["loss"] for _ in range(3)]

        result = verify_reproducibility(train_fn, config=None, steps=50)
        assert result["reproducible"], f"diverged at step {result['first_divergence_step']}"


@pytest.mark.week(21)
class TestCNN:
    def test_output_shape_formula(self):
        assert output_shape(32, kernel=3, stride=1, padding=1) == 32  # 'same'
        assert output_shape(32, kernel=3, stride=2, padding=1) == 16  # halved
        assert output_shape(28, kernel=5, stride=1, padding=0) == 24  # 'valid'

    def test_receptive_field_of_three_3x3_layers(self):
        """Three stacked 3x3 convolutions see 7x7. The VGG argument."""
        layers = [{"kernel": 3, "stride": 1}] * 3
        assert receptive_field(layers)["receptive_field"] == 7

    def test_stride_grows_the_receptive_field_faster(self):
        plain = receptive_field([{"kernel": 3, "stride": 1}] * 4)["receptive_field"]
        strided = receptive_field([{"kernel": 3, "stride": 1}, {"kernel": 3, "stride": 2}] * 2)[
            "receptive_field"
        ]
        assert strided > plain

    def test_cnn_forward_shape(self):
        model = SimpleCNN(num_classes=10)
        assert model.forward(torch.randn(4, 3, 32, 32)).shape == (4, 10)


@pytest.mark.week(22)
class TestResidual:
    def test_block_preserves_shape_at_stride_one(self):
        block = ResidualBlock(32, 32, stride=1)
        x = torch.randn(2, 32, 16, 16)
        assert block.forward(x).shape == x.shape

    def test_block_projects_the_skip_when_shape_changes(self):
        block = ResidualBlock(32, 64, stride=2)
        assert block.forward(torch.randn(2, 32, 16, 16)).shape == (2, 64, 8, 8)

    def test_identity_path_carries_gradient(self):
        """1 + F'(x). The identity term is why depth stops hurting."""
        block = ResidualBlock(16, 16)
        x = torch.randn(2, 16, 8, 8, requires_grad=True)
        block.forward(x).sum().backward()
        assert x.grad is not None
        assert x.grad.abs().mean().item() > 1e-6
