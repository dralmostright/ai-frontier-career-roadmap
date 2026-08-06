# bootstrap

The code you write. Ten lab packages, 78 weeks, one virtualenv.

---

## Start Here

```bash
cd environment
make setup      # create .venv, install the toolchain
make test       # green — everything is gated behind week 0
make week W=1   # advance
make test       # 63 failures. That is the starting line.
```

Those 63 failing tests are the Week 1 specification. Make them pass.

---

## The Week Gate

`CURRENT_WEEK` holds one integer. Tests carry `@pytest.mark.week(n)` and skip
when `n` exceeds it. The suite stays green as you progress instead of drowning
you in failures for material you have not reached.

```bash
make test            # weeks 1..CURRENT_WEEK
make test-week W=14  # week 14 only
make test-all        # everything, including unwritten weeks
make status          # where you are, and how much is left
```

Advance the week only after your Sunday check-in. It is a commitment device,
not a decoration.

Note: `-m "week(14)"` does **not** work — pytest's `-m` takes marker names, not
marker calls. Use `--only-week`, which `make test-week` does for you.

---

## The Labs

| Lab | Weeks | What you build |
| --- | ----- | -------------- |
| `math-labs` | 1-4 | Linear algebra, SVD/PCA, autodiff, probability, information theory |
| `ml-from-scratch` | 5-16 | Classical ML, then a full NumPy deep learning framework |
| `pytorch-labs` | 17-24 | PyTorch engineering, reproducibility, CNNs, ViT, serving |
| `llm-labs` | 25-36, 45-48 | Tokenizers, attention, Mini-GPT, LM training, LoRA |
| `rag-systems` | 37-40 | pgvector retrieval, chunking, reranking, RAG evaluation |
| `agent-systems` | 41-44 | Tools, agent loops, safety, agent evaluation |
| `ai-dba-agent` | 43-44 | ⭐ The flagship: autonomous PostgreSQL diagnostics |
| `mlops-platform` | 53-60 | Registry, monitoring, drift, CI/CD, Kubernetes |
| `research-reproduction` | 61-68 | Paper reproduction and original research |
| `environment` | — | venv, services, Makefile |

Each lab has a README explaining why it exists, what to build, the traps, and
the interview drills attached to it. Read it before starting the month.

---

## Rules

**Do not call the function you are implementing.** `dot_product` may not use
`np.dot`; `metrics.py` may not import `sklearn.metrics`. The tests compare
against those references, so using them makes the tests vacuous.

Tests may use anything — NumPy, SciPy, and sklearn are the reference oracles.

Two deliberate exceptions: Week 2 may use `np.linalg.eigh` and `np.linalg.svd`,
and from Month 5 you use PyTorch as a framework rather than reimplementing it.
By then you will have written the pieces yourself and know what it is doing.

---

## Layout

```text
bootstrap/
  conftest.py       week gating, shared fixtures, capability skips
  pytest.ini        pytest config (here, so rootdir is bootstrap/)
  CURRENT_WEEK      one integer
  environment/      venv, requirements, Makefile, docker-compose
  <ten lab dirs>/   README.md, src/, tests/
```

Each lab's `tests/conftest.py` puts its sibling `src/` on `sys.path`. Copy that
file if you add a lab.

---

## Shared Fixtures

From `conftest.py`, available in every lab:

| Fixture | What it gives you |
| ------- | ----------------- |
| `rng` | Seeded `np.random.Generator`. Use it instead of `np.random.*`. |
| `seed` | The seed integer |
| `tol` | `{"tight": 1e-10, "loose": 1e-4, "grad": 1e-5}` |
| `assert_close` | `assert_allclose` with a useful message |
| `database_url` | Lab Postgres DSN; skips if it is not running |

Markers that skip automatically when unavailable: `db`, `gpu`, `llm`, plus
`slow` and `network` for filtering.

---

## Before Every Commit

```bash
cd environment && make check    # lint + typecheck + test
```

Clean commits are portfolio material. A reviewer who opens your history sees
how you work.
