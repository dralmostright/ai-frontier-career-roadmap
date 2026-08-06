# Week 57: Docker Hardening

## Outcome

By Sunday your images are multi-stage, non-root, minimal, and reproducible, with the size reduction documented step by step.

## Why This Matters For OpenAI/Anthropic-Level Interviews

"Your image is 8GB — get it under 1GB" is a real interview question and the
answer is a sequence of specific moves: multi-stage build to drop build
dependencies, a slim base, layer ordering for cache reuse, no model weights baked
in, and no build toolchain in the runtime layer.

The AI-specific parts: PyTorch's CUDA wheels are enormous, so the CPU wheel is
right when you are not using a GPU; and model weights belong in a volume or
object store, not in the image, because they change on a different cadence than
the code.

Security matters too. Non-root, read-only filesystem where possible, no secrets
in layers, and a vulnerability scan in CI. These are table stakes that ML
projects routinely skip.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Layer mechanics**
   1. Layers, caching, and ordering for cache reuse
   2. Why `COPY requirements.txt` before `COPY .` matters
   3. Multi-stage builds
2. **Size reduction**
   1. Slim and distroless bases
   2. Build dependencies in the build stage only
   3. CPU-only PyTorch wheels when there is no GPU
   4. Model weights out of the image
3. **Security**
   1. Non-root user
   2. Read-only root filesystem
   3. No secrets in layers — they persist even if deleted later
   4. Vulnerability scanning in CI
   5. Minimal attack surface
4. **Reproducibility**
   1. Pinned base image digests, not tags
   2. Pinned dependencies
   3. Build args and labels for provenance
5. **Runtime**
   1. Signal handling and graceful shutdown
   2. Health endpoints
   3. Resource awareness inside the container

## Required Free Resources

- **Primary:** Docker best practices — https://docs.docker.com/build/building/best-practices/
- **Primary:** Google distroless images — https://github.com/GoogleContainerTools/distroless
- 'Docker for Python developers' — the multi-stage patterns for Python specifically
- Trivy — https://trivy.dev/ — vulnerability scanning
- OCI image spec labels — for provenance metadata

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=57
```

1. **Measure the naive image** (30m) — Build it badly first. Record the size. That is your baseline.
2. **Multi-stage build** (1.5h) — Build dependencies in stage one, runtime in stage two. Measure.
3. **Slim base and CPU wheels** (1h) — Measure after each change. Document the sequence.
4. **Model weights out of the image** (1h) — Volume mount or object store fetch at startup.
5. **Layer ordering for cache** (45m) — Change one line of code; measure the rebuild time before and after.
6. **Non-root and read-only filesystem** (1h) — Then find what breaks and fix it properly.
7. **Pin base image digests** (30m) — Tags move. Digests do not.
8. **Graceful shutdown** (1h) — SIGTERM handling with an in-flight drain. Test it.
9. **Vulnerability scan in CI** (1h) — Trivy. Fail on high severity.
10. **Document the reduction** (45m) — 8GB to under 1GB, step by step, with the size after each.

## Bootstrap Files To Create

```text
b
o
o
t
s
t
r
a
p
/
m
l
o
p
s
-
p
l
a
t
f
o
r
m
/
i
n
f
r
a
/
d
o
c
k
e
r
/
D
o
c
k
e
r
f
i
l
e


b
o
o
t
s
t
r
a
p
/
m
l
o
p
s
-
p
l
a
t
f
o
r
m
/
i
n
f
r
a
/
d
o
c
k
e
r
/
R
E
A
D
M
E
.
m
d
```

## Tests To Write

Add: a CI check that the built image is under a size threshold; and a test that the container handles SIGTERM by draining rather than dropping requests.

## Portfolio Artifact

The hardened images and the size-reduction table. That table is the answer to the interview question, in artifact form.

## Interview Drills

**Coding (45 min).** Two problems.

**System design (25 min).** Recorded: *Your inference image is 8GB. Get it under 1GB.* Give the sequence with the approximate saving from each step.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Achieve reproducible builds: the same source produces a byte-identical image. It requires pinning everything, controlling timestamps, and eliminating nondeterminism in the build. It is genuinely hard, it connects directly to the Month 5 reproducibility work, and 'my container builds are bit-reproducible' is an unusual and credible claim.
