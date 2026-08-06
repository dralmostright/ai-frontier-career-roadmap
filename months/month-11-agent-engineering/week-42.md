# Week 42: Planning, Reflection, and State

## Outcome

By Sunday you have an agent loop with step, token, and cost budgets, no-progress detection, error recovery, and context management that does not silently lose the original task.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The loop itself is thirty lines. The hard parts are termination, budgets, and
context management, and those are what separate a demo from something you would
leave running.

Termination specifically: a step cap alone is insufficient, because the agent
burns the whole budget on a task it finished at step three. You need no-progress
detection (same tool, same arguments, twice) and an explicit way for the agent to
say "I cannot determine this." Without that last one, agents invent answers
rather than admit failure, which is the worst possible behavior for a diagnostic
tool.

The reflection question — "when does it help?" — has a real answer. Reflection
helps when the agent can *verify* something: re-reading a plan, checking whether
the evidence supports the conclusion. It is theater when the agent re-asserts its
previous answer more confidently. Measure it before believing in it; it doubles
your token cost.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **The ReAct loop**
   1. Think, act, observe, repeat
   2. Why the structure works
   3. Where the model's output is parsed and what can go wrong
2. **Termination**
   1. Step, token, and cost budgets
   2. No-progress detection
   3. Explicit 'I cannot determine this'
   4. Why an agent without a give-up option confabulates
3. **Error recovery**
   1. Transient versus permanent failures
   2. Retry with backoff, and never for destructive actions
   3. Turning errors into recoverable guidance
4. **Context management**
   1. The window as a hard constraint
   2. Pinning the system prompt and the task
   3. Summarize-the-middle, externalize, or selectively retain
   4. Why an agent that loses its first half changes behavior mysteriously
5. **Reflection**
   1. When self-critique verifies something and when it does not
   2. The cost: roughly double the tokens
   3. Measuring it rather than assuming it
6. **Scratchpads**
   1. External working memory
   2. Recording ruled-out hypotheses — the underrated field
   3. Why it reduces wasted steps

## Required Free Resources

- **Primary:** 'ReAct: Synergizing Reasoning and Acting' — https://arxiv.org/abs/2210.03629
- **Primary:** Anthropic, 'Building effective agents' — reread the sections on workflows versus agents
- 'Reflexion' — https://arxiv.org/abs/2303.11366 — read critically; the gains are real and narrower than the abstract suggests
- LangGraph docs — https://langchain-ai.github.io/langgraph/ — read for the state-machine framing, then build yours
- Lilian Weng, 'LLM Powered Autonomous Agents' — https://lilianweng.github.io/posts/2023-06-23-agent/ — the best survey

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=42
```

1. **`Step` and `AgentRun` records** (45m) — Keep the whole trajectory. You need it for audit, evaluation, and debugging.
2. **`build_system_prompt`** (1.5h) — Role, tools, constraints, the evidence requirement, and explicit permission to say 'I don't know'.
3. **The basic loop** (2h) — Call, parse, execute, observe.
4. **Budgets: steps, tokens, cost** (1h) — Enforce all three. An agent in a loop is a bill.
5. **`_detect_no_progress`** (1h) — Repeated identical calls. Stop or force a different approach.
6. **`_handle_tool_error`** (1h) — Backoff for transient, guidance for permanent, never for destructive.
7. **`ConversationState` with pinning** (1.5h) — Never compact away the system prompt or the task.
8. **`Scratchpad` with `ruled_out`** (1h) — The field that stops the agent re-checking the same hypothesis three times.
9. ****The reflection experiment**** (1.5h) — Same scenarios with and without reflection. Cost and accuracy. Report honestly.

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
a
g
e
n
t
-
s
y
s
t
e
m
s
/
s
r
c
/
a
g
e
n
t
_
l
o
o
p
.
p
y


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
a
g
e
n
t
-
s
y
s
t
e
m
s
/
s
r
c
/
s
t
a
t
e
.
p
y
```

## Tests To Write

Week-42 blocks. The no-progress detection tests are the important ones.

## Portfolio Artifact

`src/agent_loop.py`, `src/state.py`, and the reflection experiment result — with cost and accuracy, reported whichever way it came out.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (25 min).** Recorded: *When does reflection help an agent, and when is it theater?* Answer with your own measurement. Then: *How do you stop an agent looping?*

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Run a multi-agent experiment: a diagnostician agent and a skeptic agent that argues against the diagnosis. Measure whether the skeptic improves accuracy, and at what cost. Be prepared for the answer to be 'marginally, for double the price' — and report that honestly. A negative result carefully measured is more valuable than an uncritical adoption of a popular pattern.
