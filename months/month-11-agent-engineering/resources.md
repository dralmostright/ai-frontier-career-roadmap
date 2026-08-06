# Month 11 Resources

Organized by week. **Do not attempt all of it.** Each week names one or two
primary resources; the rest is reference material for when you are stuck.

Theory stays capped at 30% of your hours.

---

## The Ones Worth Doing In Full

**Anthropic, 'Building effective agents'** — https://www.anthropic.com/engineering/building-effective-agents
The best practical writing on agent design. Read it in Week 41 and again in
Week 44.

**PostgreSQL EXPLAIN documentation** (Week 43) — https://www.postgresql.org/docs/current/using-explain.html
You know this material; the exercise is encoding your judgment into tools.

**Google SRE Book, postmortem culture** (Week 44) — https://sre.google/sre-book/postmortem-culture/
The framing for your safety documentation and the blast-radius analysis.

**OWASP Top 10 for LLM Applications** (Week 44) — https://owasp.org/www-project-top-10-for-large-language-model-applications/
The injection material, and the vocabulary for the security section.

---

## Week 41 — Tool Calling and Function Interfaces

- **Primary:** Anthropic, 'Building effective agents' — https://www.anthropic.com/engineering/building-effective-agents — the best practical writing on agent design
- **Primary:** Claude tool use docs — https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview
- Model Context Protocol — https://modelcontextprotocol.io/ — worth understanding; exposing your DBA tools as an MCP server is a strong stretch goal
- 'Toolformer' — https://arxiv.org/abs/2302.04761 — background on tool learning
- Pydantic docs — https://docs.pydantic.dev/ — schema generation
## Week 42 — Planning, Reflection, and State

- **Primary:** 'ReAct: Synergizing Reasoning and Acting' — https://arxiv.org/abs/2210.03629
- **Primary:** Anthropic, 'Building effective agents' — reread the sections on workflows versus agents
- 'Reflexion' — https://arxiv.org/abs/2303.11366 — read critically; the gains are real and narrower than the abstract suggests
- LangGraph docs — https://langchain-ai.github.io/langgraph/ — read for the state-machine framing, then build yours
- Lilian Weng, 'LLM Powered Autonomous Agents' — https://lilianweng.github.io/posts/2023-06-23-agent/ — the best survey
## Week 43 — Database Diagnostic Tools

- **Primary:** PostgreSQL EXPLAIN documentation — https://www.postgresql.org/docs/current/using-explain.html
- **Primary:** pg_stat_statements documentation — https://www.postgresql.org/docs/current/pgstatstatements.html
- Use The Index, Luke — https://use-the-index-luke.com/ — for the plan-reading material
- PgHero source — https://github.com/ankane/pghero — prior art worth reading; your agent covers a superset
- PostgreSQL wiki, Slow Query Questions — https://wiki.postgresql.org/wiki/Slow_Query_Questions — the ground truth for incident scenarios
## Week 44 — Agent Evaluation and Safety

- **Primary:** Anthropic, 'Building effective agents' — the evaluation section
- **Primary:** Google SRE Book, postmortem culture — https://sre.google/sre-book/postmortem-culture/ — the framing for your safety documentation
- 'SWE-bench' — https://arxiv.org/abs/2310.06770 — a well-constructed agent benchmark; read how they built it
- OWASP Top 10 for LLM Applications — https://owasp.org/www-project-top-10-for-large-language-model-applications/ — the injection material
- 'Prompt Injection' writing by Simon Willison — the clearest treatment of why this is architecturally hard

---

## Tools

| Tool | Link | Used for |
| --- | --- | --- |
| pgvector | https://github.com/pgvector/pgvector | Months 10-11 |
| FastAPI | https://fastapi.tiangolo.com/ | Serving |
| Claude API | https://docs.claude.com/ | Months 10-12 |
| Hugging Face PEFT | https://huggingface.co/docs/peft/index | Month 12 |
| pytest | https://docs.pytest.org/ | The workspace |
| NeetCode 150 | https://neetcode.io/practice | Weekly drills |
| MCP | https://modelcontextprotocol.io/ | Week 41 stretch |
| pg_stat_statements | https://www.postgresql.org/docs/current/pgstatstatements.html | Week 43 |
| PgHero | https://github.com/ankane/pghero | Prior art |

---

## Deliberately Omitted

- **Multi-agent frameworks (CrewAI, AutoGen).** Week 42's stretch goal covers
  the idea. Framework-shaped projects are hard to distinguish from tutorials.
- **Agent memory systems and vector-backed long-term memory.** Week 42's
  scratchpad covers what this project needs.
- **Reinforcement learning for agents.** A research area; not applicable at this
  scale.
- **Browser and computer-use agents.** Different domain, and it would dilute the
  differentiation.
