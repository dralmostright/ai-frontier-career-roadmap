# Interview Rubric

Use this to score mock interviews and recorded drills. Score the recording, not
your memory of the recording — memory is generous.

Every section uses the same underlying scale:

```text
1  No hire.        Missing fundamentals.
2  Weak.           Gets there with heavy help.
3  Borderline.     Correct but slow, or fast but shallow.
4  Hire.           Correct, clear, appropriately deep.
5  Strong hire.    Correct, clear, deep, and taught the interviewer something.
```

Frontier labs hire at 4+. Consistently landing at 3 means you are close and not
there. Plan accordingly.

---

## Track 1: Coding Interview

**Format:** 45 minutes, 1-2 problems, whiteboard or shared editor, no autocomplete.

| Dimension | 1 | 3 | 5 |
| --------- | - | - | - |
| **Problem clarification** | Starts coding immediately | Asks one or two questions | Restates the problem, confirms constraints, identifies edge cases before coding |
| **Approach articulation** | Silent, or narrates keystrokes | States the approach after finding it | States 2 approaches, compares complexity, justifies the choice — before typing |
| **Implementation** | Doesn't compile / fundamental errors | Works after debugging | Correct on the first pass, clean, idiomatic Python |
| **Complexity analysis** | Cannot state it | States it when asked | States it unprompted, including space, and identifies the bottleneck |
| **Testing** | None | Walks through one example | Writes test cases including edge cases, unprompted |
| **Communication** | Long silences, defensive | Explains when asked | Continuous, calm narration including uncertainty |
| **Response to hints** | Doesn't hear them | Takes the hint | Takes the hint, integrates it, and says what it changed |

```text
Coding total: __ /35        Hire bar: 28
```

**Automatic caps:**
- Did not finish a working solution → cap at 2 overall.
- Wrote zero tests → Testing cannot exceed 2.
- Silent for more than 90 consecutive seconds → Communication cannot exceed 2.

---

## Track 2: ML Theory Interview

**Format:** 45 minutes, 3-5 questions escalating in depth.

| Dimension | 1 | 3 | 5 |
| --------- | - | - | - |
| **Definitional accuracy** | Wrong or vague | Correct definitions | Correct, precise, with the assumptions stated |
| **Derivation ability** | Cannot derive | Derives with prompting | Derives cleanly, cold, and explains each step's purpose |
| **Intuition** | Recites | Explains why it works | Explains why, plus when it stops working |
| **Model comparison** | "It depends" | Names tradeoffs | Names tradeoffs and picks one with a stated reason for the scenario |
| **Metric reasoning** | Defaults to accuracy | Picks a reasonable metric | Picks a metric, justifies it against the business cost of errors |
| **Debugging reasoning** | Guesses randomly | Has a checklist | Has a checklist, orders it by likelihood, states what each test rules out |
| **Depth under follow-up** | Collapses at question 2 | Holds for 2 follow-ups | Holds for 4+; says "I don't know" precisely rather than bluffing |

```text
ML theory total: __ /35     Hire bar: 28
```

**Automatic caps:**
- Bluffed on something you didn't know → cap overall at 3. Interviewers always
  notice, and it costs more than the gap it hides.
- Could not derive gradient descent for logistic regression → cap Derivation at 1.

---

## Track 3: Deep Learning / LLM Interview

| Dimension | 1 | 3 | 5 |
| --------- | - | - | - |
| **Architecture knowledge** | Knows the diagram | Can implement it | Can implement it and explain what breaks without each component |
| **Attention specifically** | Hand-waves | Derives with the formula in front of them | Derives cold including √d justification, causal masking, and multi-head reasoning |
| **Training mechanics** | Uses defaults | Understands the knobs | Can debug a broken run systematically and explain the failure signature |
| **Inference and serving** | Not considered | Knows KV cache exists | Computes memory costs, discusses batching, quantization, and the prefill/decode split |
| **Modern developments** | GPT-2 era knowledge | Aware of RoPE/GQA/etc | Explains why each replaced its predecessor and what it cost |
| **Evaluation** | "We check the outputs" | Names benchmarks | Designs an eval harness, discusses judge bias and statistical power |
| **Safety** | Not considered | Aware of the issues | Concrete threat model, mitigation, and a way to measure whether it worked |

```text
DL/LLM total: __ /35        Hire bar: 28
```

**Automatic caps:**
- Cannot write scaled dot-product attention → cap overall at 2.
- Cannot explain KV caching → cap Inference at 2.

---

## Track 4: System Design Interview

**Format:** 45-60 minutes, one open-ended design.

| Dimension | 1 | 3 | 5 |
| --------- | - | - | - |
| **Requirements gathering** | Starts drawing immediately | Asks about scale | Establishes functional reqs, non-functional reqs, scale, latency SLO, and cost budget in the first 5 minutes |
| **Success metrics** | Never mentioned | Mentions accuracy | Defines the SLO, the quality metric, and how both are measured in production |
| **High-level design** | Confused or missing pieces | Reasonable architecture | Clean data flow, right components, correct boundaries, drawn clearly |
| **Depth on the hard part** | Stays shallow throughout | Goes deep when pushed | Identifies the genuinely hard component and goes deep unprompted |
| **Scaling** | Not addressed | "We'd add more servers" | Identifies the specific bottleneck at 10x, quantifies it, proposes a targeted fix |
| **Failure modes** | Not addressed | Names a couple | Systematic: what fails, how it's detected, blast radius, recovery, and the alert |
| **Tradeoffs** | Presents one design as correct | Mentions alternatives | Explicitly frames 2-3 decisions as tradeoffs with the reasoning for each choice |
| **Cost** | Never mentioned | Vague awareness | Estimates cost per request and identifies the dominant cost driver |

```text
System design total: __ /40     Hire bar: 32
```

**Your specific opportunity:** Failure modes, scaling, and cost are the three
dimensions where most ML candidates score 1-2 and where your operational
background should put you at 5. If you are not scoring 5 on these, you are
under-using your advantage. Practice narrating them explicitly.

---

## Track 5: Behavioral Interview

| Dimension | 1 | 3 | 5 |
| --------- | - | - | - |
| **Structure** | Rambling, no arc | Recognizable STAR | Tight STAR in 90-120 seconds with a clear result |
| **Specificity** | Generalities | One concrete example | Concrete, with names of systems, numbers, and dates |
| **Quantified impact** | None | "It got much faster" | "p99 went from 4.2s to 300ms, and here's how I measured it" |
| **Ownership** | Blames others or "we" throughout | Mixed "we" and "I" | Clear about personal contribution without diminishing the team |
| **Self-awareness** | No mistakes admitted | Admits a small mistake | Discusses a real failure, what caused it, and the systemic fix |
| **Career narrative** | Defensive about the transition | Explains the transition | Frames it as compounding advantage with technical proof |
| **Company specificity** | Generic enthusiasm | Knows what they do | References their actual work and connects it to your specific skills |

```text
Behavioral total: __ /35    Hire bar: 26
```

**Automatic caps:**
- Disparaged a previous employer → cap overall at 2.
- Could not give a specific number in any story → cap Quantified impact at 1.
- Career-change answer took more than 90 seconds → cap Career narrative at 2.

---

## Full Loop Scoring

A frontier lab onsite is typically 4-5 rounds. Simulate it in Week 76.

```text
Round 1  Coding                __ /35   (bar 28)
Round 2  ML theory             __ /35   (bar 28)
Round 3  DL / LLM depth        __ /35   (bar 28)
Round 4  System design         __ /40   (bar 32)
Round 5  Behavioral            __ /35   (bar 26)
------------------------------------------------
         Total                 __ /180  (bar 142)
```

**Interpretation:**

| Total | Reading |
| ----- | ------- |
| < 100 | Not ready. Identify the two weakest rounds and spend 8 weeks there. |
| 100-125 | Would fail most loops. 4-6 weeks of targeted work. |
| 126-141 | Borderline. Would pass some loops, fail others. Apply to second-tier targets first to gain loop experience. |
| 142-160 | Ready. Apply broadly. |
| 160+ | Strong. Apply to your top choices first while you're sharp. |

**One round below its bar is survivable.** Two is not — most loops require a
majority of positive signals with no strong negative.

---

## Post-Mock Protocol

Within 24 hours of every mock:

1. **Score it from the recording,** not from memory.
2. **Timestamp every failure.** "14:32 — couldn't remember why √d." Those
   timestamps are your study list.
3. **Categorize each failure:**
   - *Knowledge gap* → schedule study time
   - *Recall gap* → you knew it but couldn't retrieve it under pressure → more reps
   - *Communication gap* → you knew it and explained it badly → practice out loud
   - *Process gap* → you skipped a step in the framework → rehearse the framework
4. **Pick exactly one thing** to fix before the next mock. One. Trying to fix
   seven things fixes zero.
5. **Log it** in `coach/mocks/mock-YYYY-MM-DD.md`.

---

## Calibration Check

Every quarter, compare:

- Your average weekly self-score in `SCORECARD.md`
- Your most recent mock interview total

If your weekly scores average 8/10 and your mock total is 110/180, your
self-scoring is inflated by roughly two points. Adjust every future score down by
that amount until the two align. Calibration is the whole point of scoring; an
uncalibrated score is worse than no score because it produces false confidence.
