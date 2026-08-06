# Lab Environment

One virtualenv and one service stack for all 78 weeks.

---

## Quick Start

```bash
cd bootstrap/environment
make setup          # creates bootstrap/.venv and installs the base toolchain
make test           # green (everything skipped — you're on week 0)
make week W=1       # advance to week 1
make test           # week 1 tests now run, and fail, because you haven't written the code
```

That last step is the point. The tests are the specification. Make them pass.

---

## The Week Gate

`bootstrap/CURRENT_WEEK` holds a single integer. Tests are tagged with
`@pytest.mark.week(n)` and skipped when `n` is greater than the current week.

This keeps the suite green as a matter of course while still letting you run
`make test-all` to see the full scope of what you will eventually implement.

```bash
make week W=14      # advance
make test           # runs weeks 1-14
make test-week W=14 # runs week 14 only
make test-all       # runs everything, including unwritten weeks
make status         # where you are, and how much is still NotImplementedError
```

**Advance the week only after your check-in.** The counter is a commitment
device, not a decoration.

---

## Commands

| Command | What it does |
| ------- | ------------ |
| `make setup` | Create the venv, install the toolchain |
| `make test` | Run tests through the current week |
| `make lint` | ruff |
| `make typecheck` | mypy (non-blocking by default) |
| `make check` | lint + typecheck + test. **Run before every commit.** |
| `make cov` | Coverage report to `htmlcov/` |
| `make format` | ruff format + autofix |
| `make notebook` | JupyterLab in the bootstrap workspace |
| `make kernel` | Register the venv as a Jupyter kernel |
| `make freeze` | Snapshot exact versions to `requirements.lock.txt` |
| `make db-up` / `make db-down` | Postgres + pgvector |
| `make db-shell` | psql into the lab database |
| `make services-up` | Postgres, MLflow, Prometheus, Grafana, Redis |
| `make clean` / `make nuke` | Caches / caches + venv |

---

## Progressive Dependencies

`requirements.txt` installs only the scientific stack, testing tools, and
notebook support. Everything heavier is commented out with the month that needs
it. Uncomment as you go.

**Why:** installing PyTorch, Transformers, and Ray in Month 1 means 6GB of disk
and a 15-minute install for libraries you will not import for three months. It
also hides which dependencies each project actually needs, which matters when
you write the capstone READMEs.

**Re-pin at each phase boundary** (Months 4, 7, 10, 13, 16):

```bash
make freeze
git add requirements.lock.txt
git commit -m "env: re-pin dependencies at Month N boundary"
```

Note the change in your monthly review. Managing dependency drift over 18 months
is itself a production-engineering skill worth demonstrating.

---

## PyTorch Installation

Not in `requirements.txt` because the correct wheel depends on your hardware.

```bash
source ../.venv/bin/activate

# Apple Silicon (gives you the MPS backend)
pip install torch torchvision

# Linux + NVIDIA CUDA 12.x
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# CPU only
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

Verify:

```python
import torch

print(torch.__version__)
print(torch.backends.mps.is_available())  # macOS
print(torch.cuda.is_available())  # Linux + NVIDIA
```

Do this in Month 4, not before.

---

## Services

Nothing here is needed before Month 7.

### Postgres + pgvector

```bash
make db-up
make db-shell
```

Connection string:

```text
postgresql://airoadmap:airoadmap@localhost:5432/airoadmap
```

The init script creates `vector`, `pg_stat_statements`, `pg_trgm`, and
`pgstattuple`, plus three schemas: `labs`, `telemetry`, `evals`.

The server is deliberately configured with small `shared_buffers` and `work_mem`.
This is not an oversight — in Month 11 you will generate performance incidents
against this instance, and a well-tuned server is a bad teaching instrument.
`log_min_duration_statement=200` means slow queries land in the logs where your
agent can read them.

### MLflow, Prometheus, Grafana, Redis

```bash
make services-up
```

| Service | URL | Used in |
| ------- | --- | ------- |
| MLflow | http://localhost:5000 | Months 5, 14 |
| Prometheus | http://localhost:9090 | Weeks 56, 60 |
| Grafana | http://localhost:3000 (admin/admin) | Week 56 |
| Redis | localhost:6379 | Week 59 |

---

## Secrets

API keys go in `bootstrap/.env`, which is gitignored. Never in code, never in a
notebook, never in a config file you commit.

```bash
cat > ../.env <<'EOF'
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
DATABASE_URL=postgresql://airoadmap:airoadmap@localhost:5432/airoadmap
EOF
```

Load with `python-dotenv`. Before the first commit of Month 10, install a
pre-commit secret scanner — leaking a key in a public portfolio repository is a
visible, searchable, and entirely avoidable mistake.

---

## Cost Control

From Month 10 you will spend real money on API calls. Two habits, adopted early:

1. **Cache every LLM response during development.** A simple content-addressed
   disk cache keyed on the prompt hash. You will re-run the same eval dozens of
   times; paying for it dozens of times is a choice.
2. **Log token counts and estimated cost on every call.** By Month 13 you will
   need a cost report anyway, and retrofitting instrumentation is worse than
   building it in.

Budget: roughly $20-50/month for Months 10-17. If you are exceeding that, the
cause is almost always an uncached evaluation loop.

---

## Troubleshooting

**`make setup` fails on Python version**
Requires 3.11+. Check with `python3 --version`. On macOS: `brew install python@3.12`.

**Tests can't import from `src/`**
Each lab's `tests/conftest.py` puts its sibling `src/` on `sys.path`. If you add
a new lab, copy that file.

**`make test` collects zero tests**
Expected on week 0. Run `make week W=1`.

**Docker commands fail**
Docker Desktop or Colima must be running. Nothing before Month 7 needs it.

**Postgres won't start after a config change**
`make db-reset` destroys the volume and rebuilds. You will lose the lab data,
which is regenerable by design.
