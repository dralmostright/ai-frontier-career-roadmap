# Week 41: Tool Calling and Function Interfaces

## Outcome

By Sunday you have a tool framework with schema validation, risk classification, result truncation, and instructive error messages — and you can defend every constraint.

## Why This Matters For OpenAI/Anthropic-Level Interviews

The interview question is "design a tool interface an LLM cannot misuse," and
you should answer it better than almost anyone, because it is a permissions
problem and permissions are your professional native language.

The core insight: **an LLM will misuse any tool that can be misused.** Not
maliciously — it will pass arguments you did not anticipate, call tools in orders
you did not plan, and interpret ambiguous parameters creatively. Design as if for
a capable, well-meaning, occasionally confidently-wrong actor.

Error message quality is the underrated part. Compare "psycopg.errors.
UndefinedTable: relation 'user' does not exist" with "Table 'user' not found. Did
you mean 'users'? Call list_tables() to enumerate." The first makes the model
flail; the second lets it recover in one step. Error messages measurably change
agent success rates and they are the cheapest improvement available.

## Time Budget: 15-20 Hours

- Theory: 2.5 hours
- Coding: 8 hours
- Project: 3.5 hours
- Interview practice: 2 hours
- Review/write-up: 1.5 hours

## Theory Lessons

1. **Tool design principles**
   1. Narrow beats general: `get_slow_queries(limit)` over `run_sql(query)`
   2. Validate at the boundary with typed schemas
   3. Read-only by default
   4. Instructive errors
   5. Bound everything: rows, time, tokens, cost
   6. Idempotent where possible, because retries happen
2. **Schemas**
   1. Generating JSON Schema from Pydantic, not by hand
   2. Why hand-written schemas drift and what that costs
   3. Description quality: the only documentation the model gets
3. **Risk classification**
   1. READ, ADVISORY, REVERSIBLE, DESTRUCTIVE
   2. Classifying at design time, not after an incident
   3. Fail closed on unclassified actions
4. **Results**
   1. Structured returns, not strings
   2. Distinguishing failure from empty
   3. Truncation, and why silent truncation produces confident wrong conclusions
5. **The model as untrusted input**
   1. Never interpolate model output into a query
   2. Parameterized queries only
   3. Treating tool arguments the way you treat a web form

## Required Free Resources

- **Primary:** Anthropic, 'Building effective agents' — https://www.anthropic.com/engineering/building-effective-agents — the best practical writing on agent design
- **Primary:** Claude tool use docs — https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview
- Model Context Protocol — https://modelcontextprotocol.io/ — worth understanding; exposing your DBA tools as an MCP server is a strong stretch goal
- 'Toolformer' — https://arxiv.org/abs/2302.04761 — background on tool learning
- Pydantic docs — https://docs.pydantic.dev/ — schema generation

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=41
```

1. **`ToolResult` and the `Tool` protocol** (1h) — Structured returns. Distinguish failure from empty.
2. **The `@tool` decorator** (2h) — Schema from type hints, timeout, row limit, exception handling.
3. **`validate_arguments`** (1h) — Missing required, wrong type, hallucinated parameter. All three have tests.
4. **Instructive error messages** (1h) — Rewrite five stack traces as recoverable guidance. Measure the difference on a real agent run.
5. **`RiskLevel` and classification** (1h) — Fail closed on unknown.
6. **`ToolRegistry` with risk enforcement** (1.5h) — Refuse above the ceiling without approval.
7. **`truncate_result`** (1h) — Informatively. 'Showing 100 of 4,312 rows.'
8. **Write five real database tools** (2h) — Narrow and typed. Start with slow queries, index usage, table stats.
9. **The misuse experiment** (1h) — Give the agent a general `run_sql` tool and see what it does. Instructive and slightly alarming.

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
t
o
o
l
s
.
p
y
```

## Tests To Write

`tests/test_agent_systems.py` week-41 blocks. The risk-ceiling and hallucinated-parameter tests are the important ones.

## Portfolio Artifact

`src/tools.py` and a short write-up of the misuse experiment — what the agent did when given an unrestricted SQL tool.

## Interview Drills

**Coding (45 min).** Two problems.

**ML theory (30 min).** Recorded: *Design a tool interface an LLM cannot misuse.* Give the six principles with a justification each. This is a question where your background should produce a visibly better answer than most.

## Evaluation Rubric

| Score | Standard |
| --- | --- |
| 3 | Barely started. Tests failing. |
| 5 | Tests pass. Cannot explain the mechanism. |
| 7 | All tests pass. Clean code. Can explain every choice. Artifact committed. |
| 9 | Above, plus the stretch analysis done and the interview drill answered cold. |
| 10 | Above, plus you found and fixed something the tests did not catch. |

## Stretch Goal

Expose your database diagnostic tools as an MCP server. It is a small amount of additional work on top of the registry, it makes the tools usable from any MCP client including Claude Code itself, and 'I exposed my DBA tooling over MCP' is a concrete, current, and unusual thing to be able to say in an interview.
