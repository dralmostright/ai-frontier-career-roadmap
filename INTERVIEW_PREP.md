# Interview Preparation System

Interview prep starts in Week 1 and runs for 78 weeks. Month 18 is not when you
learn to interview; it is when you sharpen what you have been practicing for
seventeen months.

Two hours per week, every week. Non-negotiable.

---

## Why Weekly, Not At The End

Three reasons, all of them learned the hard way by people who deferred:

1. **Explanation is a separate skill from understanding.** You can implement
   backpropagation and be unable to explain it. The only fix is reps.
2. **Interview pressure degrades performance by roughly one skill level.**
   You need to be one level above your target under calm conditions.
3. **Recall decays.** Something you learned in Month 4 and never revisited is
   gone by Month 14. Weekly drills are spaced repetition with a purpose.

---

## The Five Interview Tracks

Frontier AI labs test five things. Every week touches at least two.

```text
1. Coding              Python fluency, data structures, algorithms, clean code
2. ML theory           Derivations, intuition, model comparison, metrics
3. Deep learning / LLM Architecture, training, attention, evaluation, safety
4. System design       RAG, agents, eval platforms, inference, training infra
5. Behavioral          STAR stories, collaboration, judgment, failure handling
```

---

## Track 1: Coding Interviews

**Weekly commitment:** 2-3 problems, timed, from Week 1 through Week 68. Then
40 problems/week during Weeks 69-70.

### Standard
- Medium difficulty in 20-25 minutes including explanation.
- You talk through the approach *before* typing.
- You state complexity without being asked.
- You write at least one test case unprompted.
- Your code is readable: real variable names, small functions, no dead code.

### Topic rotation (repeat every 12 weeks)
| Weeks | Topic |
| ----- | ----- |
| 1-2 | Arrays, two pointers |
| 3-4 | Hash maps, sets, counting |
| 5-6 | Strings, sliding window |
| 7-8 | Sorting, binary search |
| 9-10 | Trees, recursion |
| 11-12 | Graphs, BFS/DFS |

Add during later cycles: heaps, intervals, dynamic programming, tries, matrix
traversal, and — because you should lean into it — problems with a data-structure
or query-processing flavor.

### Your specific advantage and risk
You are strong in Python and in thinking about data at scale. Your risk is that
DBA work does not exercise algorithmic recursion much. Front-load trees, graphs,
and DP; they will feel less natural than the array work.

### AI-flavored coding problems
Increasingly common at labs. Practice these from Month 8:
- Implement scaled dot-product attention in NumPy.
- Implement top-k and nucleus sampling.
- Implement a byte-pair-encoding tokenizer trainer.
- Implement a simple KV cache and show the memory saved.
- Batch a list of variable-length sequences with padding and a mask.
- Implement cosine similarity search over N vectors, then optimize it.
- Write a retry-with-backoff wrapper for a flaky LLM API.

---

## Track 2: ML Theory Interviews

**Weekly commitment:** one derivation, spoken out loud, recorded once a month.

### The core derivation set
You must be able to do all of these on a whiteboard, cold, by Month 12:

1. Gradient of MSE for linear regression; the normal equation and when it fails.
2. Gradient of log loss for logistic regression; why the sigmoid pairs with it.
3. Softmax + cross entropy gradient (the elegant `p - y` result — derive it).
4. Backpropagation for a two-layer MLP.
5. Bias-variance decomposition.
6. Why L2 regularization shrinks weights and L1 induces sparsity.
7. Entropy, cross entropy, KL divergence, and their relationships.
8. PCA via the covariance eigendecomposition and via SVD.
9. Information gain for a decision tree split.
10. Why bagging reduces variance and boosting reduces bias.
11. Scaled dot-product attention, including the √d justification.
12. Layer norm, and why it differs from batch norm for sequences.
13. The LoRA update and its parameter count.
14. The DPO objective and what it replaced.

### Standard question bank

**Fundamentals**
- Explain bias-variance to a product manager, then to a researcher.
- Your model is 99% accurate. Why might that be worthless?
- Difference between parameters and hyperparameters. How do you tune each?
- Why do we split into train/val/test rather than train/test?
- What is cross-validation for and when does it mislead you?
- What is data leakage? Give three ways it sneaks in.

**Metrics**
- Precision vs recall. When do you optimize each?
- ROC-AUC vs PR-AUC. Which for a 0.1% positive rate, and why?
- What is calibration and why do you care?
- Design the metric for a spam filter, a fraud detector, a search ranker.

**Models**
- When would you choose gradient boosting over a neural network?
- Why do random forests rarely overfit with more trees, while boosting does?
- What breaks in k-means and how do you detect it?
- Explain regularization in three different model families.

**Debugging**
- Training loss won't go down. Walk through your checklist.
- Training loss goes down, validation goes up. What now?
- Your model performs well offline and badly in production. Diagnose.

---

## Track 3: Deep Learning and LLM Interviews

**Weekly commitment:** from Month 4 onward, one architectural explanation per week.

### Question bank

**Training mechanics**
- What does `.backward()` do, mechanically?
- Why does batch size affect the learning rate you should use?
- Explain vanishing and exploding gradients. Three fixes each.
- What does gradient clipping do to the optimization trajectory?
- Why mixed precision? What breaks and how does a loss scaler fix it?
- What is gradient accumulation and when do you need it?
- Explain a learning rate warmup and why transformers need one.

**Architecture**
- Derive scaled dot-product attention. Why divide by √d_k?
- Why multi-head instead of one big head?
- What does the causal mask do and how is it implemented?
- Why residual connections? What happens without them at depth 48?
- Pre-norm vs post-norm. Which won and why?
- Why did positional encoding move from sinusoidal to RoPE?
- What is grouped-query attention solving?
- What is SwiGLU and why did it replace ReLU in the FFN?
- Explain weight tying between embedding and output layers.

**Inference**
- Explain KV caching. Compute its memory cost for a given model and context.
- Prefill vs decode. Which is compute-bound, which is memory-bound?
- Why is batch inference so much more efficient than one-at-a-time?
- Explain quantization: INT8, INT4, and what you lose.
- What is speculative decoding?
- Explain continuous batching and why it beats static batching for serving.

**Training regimes**
- Pretraining vs SFT vs RLHF vs DPO. What does each stage fix?
- Why does instruction tuning generalize from so few examples?
- What is reward hacking and how do you detect it?
- Explain Constitutional AI's core idea.
- When is fine-tuning wrong and RAG right? Give three criteria.

**Evaluation and safety**
- How do you evaluate a model with no ground truth?
- What is LLM-as-judge, and what are its known biases?
- How do you detect hallucination programmatically?
- Design a red-team process for an agent with database access.
- What is prompt injection and how do you defend against it in a RAG system?

---

## Track 4: System Design Interviews

**Weekly commitment:** one design sketch (30 min) from Month 9 onward.

### The design framework

Use the same structure every time. Interviewers grade structure as much as content.

```text
1. Requirements       (5 min)  Functional, non-functional, scale, latency, cost
2. Success metrics    (2 min)  How do we know it works? What's the SLO?
3. High-level design  (10 min) Boxes and arrows. Data flow first.
4. Deep dive          (15 min) The interesting component, in detail
5. Scaling            (5 min)  What breaks at 10x? At 100x?
6. Failure modes      (5 min)  What fails, how you detect it, how you recover
7. Tradeoffs          (3 min)  What you'd do differently with more time/money
```

Steps 2, 6, and 7 are where you win. Most candidates skip them. You will not,
because reliability thinking is your background.

### The six designs you must have ready

**1. ChatGPT-like conversational system**
Token streaming, context management, conversation storage, rate limiting,
moderation, multi-turn state, cost per conversation, cache strategy.

**2. Enterprise RAG over 10M documents**
Ingestion pipeline, chunking strategy, embedding refresh, index choice
(HNSW vs IVFFlat), hybrid retrieval, reranking, permission filtering (the part
everyone forgets), citation, eval harness, staleness handling.

**3. LLM evaluation platform**
Eval set management, versioning, judge models, human-in-the-loop, statistical
significance, regression gating in CI, cost control, result storage and query.

**4. Inference serving platform**
Model loading, GPU allocation, continuous batching, KV cache management,
autoscaling on queue depth, p99 latency SLO, multi-model routing, fallbacks.

**5. Training platform**
Job submission, resource scheduling, distributed coordination, checkpointing,
fault tolerance (nodes will die), experiment tracking, data pipeline throughput,
cost attribution.

**6. Database reliability assistant** — *your signature design*
Telemetry ingestion, query plan parsing, incident detection, agent reasoning
loop, tool safety, human approval gates, audit logging, evaluation, and the
blast-radius question: what happens when it's wrong?

### Design questions you should ask back
- What's the read/write ratio? What's the p99 requirement?
- What's the cost budget per query?
- Who are the users and what's their tolerance for a wrong answer?
- Is stale data acceptable? How stale?
- What's the compliance boundary on the data?

---

## Track 5: Behavioral Interviews

**Weekly commitment:** 15 minutes refining one story.

You have an enormous advantage here and most technical candidates squander it.
Fifteen years of production operations means you have real stories with real
stakes. Junior AI candidates have "I worked on a group project."

### The story inventory

Build twelve stories in STAR format (Situation, Task, Action, Result). Write them
in `coach/` and rehearse them until they are 90-120 seconds each.

| # | Theme | Source from your background |
| - | ----- | --------------------------- |
| 1 | Production incident you led | A real outage. Include the numbers. |
| 2 | Performance problem you diagnosed | Query plan regression, index issue |
| 3 | Automation that removed toil | Anything you scripted away |
| 4 | Disagreement with a senior stakeholder | Pushing back on a bad design |
| 5 | Mistake you made | A real one. With the fix and the prevention. |
| 6 | Cross-team collaboration | Working with app teams, SREs, security |
| 7 | Mentoring someone | Bringing up a junior DBA |
| 8 | Learning something hard, fast | This course. Use it. |
| 9 | Ambiguous problem you scoped | Any "make the database faster" request |
| 10 | Building the DBA agent | Month 11. Technical judgment story. |
| 11 | A negative result you reported | Month 17 research. Intellectual honesty. |
| 12 | Why AI, why now, why this lab | Your narrative. See below. |

### The career-change narrative

You will be asked. Have a 60-second answer that is specific, forward-looking, and
does not disparage your current field. Structure:

> "I've spent [N] years keeping [systems] reliable at [scale]. Over the last two
> years I watched AI systems get deployed into production with essentially none
> of the operational rigor we take for granted in database engineering — no
> evaluation harnesses, no rollback plans, no error budgets. That gap is exactly
> where my experience compounds. So I spent 18 months going deep: [specific
> technical proof]. What I want to do now is [specific role] because [specific
> reason tied to this company's actual problems]."

Rules for this answer:
- Never frame it as escaping something. Frame it as compounding into something.
- Include one concrete technical proof point within the first 30 seconds.
- Name the company's actual work. Generic enthusiasm reads as unserious.

### Behavioral questions to prepare
- Tell me about a time you were wrong about a technical decision.
- Describe the hardest bug you have debugged.
- How do you handle being the least experienced person in the room? (Relevant.)
- Tell me about a time you shipped something you weren't proud of.
- How do you decide what to work on when everything is urgent?
- What's something you believe about engineering that most people disagree with?

---

## The Mock Interview Program

### Quarterly mocks (Months 3, 6, 9, 12, 15, 18)

| Quarter | Mock focus |
| ------- | ---------- |
| Q1 (M3) | Coding + ML theory |
| Q2 (M6) | Coding + DL fundamentals |
| Q3 (M9) | Transformers deep dive + coding |
| Q4 (M12) | LLM systems + applied ML |
| Q5 (M15) | Infrastructure system design |
| Q6 (M18) | Full loop simulation ×3 |

### How to run a mock without a partner
1. Pick the question set in advance; do not read it until the timer starts.
2. Record video and audio. Whiteboard on paper, visible in frame.
3. No pausing, no lookups, no restarts. 45 minutes.
4. Watch the recording the same day. Score with `coach/interview_rubric.md`.
5. Note every moment you said "um, I think", stalled, or hand-waved. Those are
   your study list for the next month.

### Finding real partners
- Pramp / interviewing.io for coding and ML.
- Local or virtual ML meetups for design practice.
- A colleague who will play a hostile interviewer for 45 minutes.
- From Month 12, approach people in target roles for informational chats. Ask
  them what they were asked.

---

## Month 18 War Room Schedule

| Week | Focus | Volume |
| ---- | ----- | ------ |
| 69 | Coding sprint 1 | 40 problems: arrays, strings, hash maps, two pointers, sliding window |
| 70 | Coding sprint 2 | 40 problems: trees, graphs, heaps, DP |
| 71 | ML theory | 20 recorded explanations from the derivation set |
| 72 | Deep learning | 15 recorded derivations: backprop, attention, optimization |
| 73 | LLM system design | 6 full designs, written and presented |
| 74 | AI infra system design | 6 full designs, written and presented |
| 75 | Portfolio polish | 9 READMEs, 9 diagrams, 3 demo recordings |
| 76 | Mock loops | 3 full simulated onsites |
| 77 | Application strategy | Target matrix, referrals, outreach, tailored pitches |
| 78 | Final review | Gap closure, hire/no-hire self-assessment |

---

## The Portfolio Walkthrough

You will get four minutes to present your work. Rehearse this until it is
automatic. Structure:

```text
0:00-0:20  Positioning. One sentence on who you are and what you build.
0:20-1:30  The flagship (DBA agent). Problem, approach, one hard technical
           decision, and the measured result.
1:30-2:30  Breadth proof. Mini-GPT and the MLOps platform, 30 seconds each.
2:30-3:30  The research. Question, method, finding — including what surprised you.
3:30-4:00  Why this company specifically. Tie to their actual work.
```

Practice the 4-minute version, then a 90-second version, then a 20-second
version. You will need all three.

---

## Common Failure Modes

| Failure | Symptom | Fix |
| ------- | ------- | --- |
| Silent coding | You stop talking while thinking | Narrate your uncertainty out loud |
| Jumping to code | Typing within 60 seconds | Force yourself to restate the problem first |
| Depth avoidance | "I'd use a vector database" and stopping | Always go one level deeper unprompted |
| No numbers | "It worked well" | Every project claim gets a number attached |
| Over-apologizing | "Sorry, I'm not sure, this might be wrong" | State your reasoning, then your confidence |
| Hiding the DBA past | Leading with the AI coursework | Lead with the operational depth. It's the moat. |
| Memorized answers | Fluent until the follow-up | Practice follow-ups, not just answers |
