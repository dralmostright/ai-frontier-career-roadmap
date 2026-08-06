# Week 50: Distributed Training Concepts

## Outcome

By Sunday you can explain data, tensor, and pipeline parallelism, all three ZeRO stages, and the communication cost of each — and say which combination fits a given model and cluster.

## Why This Matters For OpenAI/Anthropic-Level Interviews

This week is mostly analytical, and that is appropriate: you will not train a
70B model, but you will be asked to reason about how one is trained.

The ZeRO question is the specific one. Stage 1 shards optimizer state, stage 2
adds gradients, stage 3 adds parameters. Each stage cuts memory further and adds
communication. Being able to state that cleanly, with the memory reduction factor
and the communication cost for each, is a crisp answer to a common question.

The parallelism taxonomy is the other. Data parallelism when the model fits and
you want throughput. Tensor parallelism when a single layer does not fit, and it
demands fast interconnect. Pipeline parallelism when the model does not fit and
the interconnect is slower, at the cost of bubble overhead. Real systems combine
all three, and knowing why is the depth marker.

## Time Budget: 15-20 Hours

- Theory: 6 hours
- Coding: 4 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Data parallelism**
   1. Replicate the model, shard the batch, all-reduce gradients
   2. Communication cost per step
   3. Why effective batch size scales and what that does to the learning rate
   4. DDP versus the older DataParallel
2. **Model parallelism**
   1. Tensor parallelism: shard within a layer, needs fast interconnect
   2. Pipeline parallelism: shard across layers, and the bubble
   3. Micro-batching to shrink the bubble
   4. Sequence parallelism
3. **ZeRO**
   1. Stage 1: shard optimizer state
   2. Stage 2: also shard gradients
   3. Stage 3: also shard parameters
   4. Memory reduction and communication cost per stage
   5. ZeRO-Offload and ZeRO-Infinity
4. **Combining strategies**
   1. 3D parallelism
   2. Choosing based on model size, cluster size, and interconnect
   3. Why the answer differs between 8 GPUs and 8000
5. **Failure at scale**
   1. Nodes will die. Checkpointing frequency as a function of MTBF.
   2. Elastic training
   3. Straggler mitigation
6. **Communication primitives**
   1. All-reduce, all-gather, reduce-scatter
   2. Ring versus tree algorithms
   3. Why interconnect bandwidth is often the binding constraint

## Required Free Resources

- **Primary:** 'ZeRO: Memory Optimizations Toward Training Trillion Parameter Models' — https://arxiv.org/abs/1910.02054 — read sections 1-5
- **Primary:** Hugging Face, 'Model Parallelism' guide — https://huggingface.co/docs/transformers/perf_train_gpu_many — the clearest practical taxonomy
- 'Megatron-LM' — https://arxiv.org/abs/1909.08053 — tensor parallelism
- 'GPipe' — https://arxiv.org/abs/1811.06965 — pipeline parallelism and the bubble
- PyTorch FSDP tutorial — https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html — ZeRO-3 in PyTorch
- The OPT-175B training logbook — https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/chronicles/ — read some of it. Large-scale training is mostly incident response.

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=50
```

1. **Write the reference document** (3h) — Each strategy: what it shards, memory saved, communication added, when to use it. This is the deliverable.
2. **Compute memory for each ZeRO stage** (1h) — For a 7B model on 8 GPUs. Tabulate.
3. **Communication cost analysis** (1.5h) — Bytes moved per step for DP, TP, and each ZeRO stage. Which saturates a 100Gb/s link first?
4. **Run DDP locally on CPU** (1.5h) — Two processes, gloo backend. Verify gradients are synchronized.
5. **Pipeline bubble calculation** (1h) — Bubble fraction against micro-batch count. Plot it.
6. **Checkpointing frequency analysis** (1h) — Given node MTBF and checkpoint cost, what interval minimizes expected wasted work?
7. **Read the OPT logbook** (1.5h) — Note every distinct failure mode. It is a sobering and useful list.

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
d
o
c
s
/
d
i
s
t
r
i
b
u
t
e
d
_
t
r
a
i
n
i
n
g
.
m
d
```

## Tests To Write

Add: a test that a two-process DDP run produces the same gradients as single-process with the equivalent batch size.

## Portfolio Artifact

The reference document. Write it as something you would hand a colleague — it is also your interview preparation for this topic.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (30 min).** Recorded: *Explain ZeRO stages 1, 2, and 3 — what each shards, the memory reduction, and the communication cost.* Then: *When would you use tensor parallelism over pipeline parallelism?*

**System design (30 min).** Design a training cluster for a 7B model. GPUs, interconnect, parallelism strategy, checkpointing, and failure handling.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Run FSDP across two local processes and verify that parameters really are sharded — inspect the local parameter count on each rank. Making ZeRO-3 concrete rather than conceptual is worth the setup effort, and being able to say 'I've run it, here is what the sharding looks like' beats reciting the paper.
