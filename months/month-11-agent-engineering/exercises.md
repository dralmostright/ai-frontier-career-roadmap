# Month 11 Exercises

Every exercise in one place. The **core** set is required — it is what the tests
check. **Extensions** are optional, ordered by value.

---

## Week 41 — Tool Calling and Function Interfaces

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 41.1 | `ToolResult` and the `Tool` protocol | 1h | Easy |
| 41.2 | The `@tool` decorator | 2h | Hard |
| 41.3 | `validate_arguments` | 1h | Medium |
| 41.4 | Instructive error messages | 1h | Medium |
| 41.5 | `RiskLevel` and classification | 1h | Medium |
| 41.6 | `ToolRegistry` with risk enforcement | 1.5h | Medium |
| 41.7 | `truncate_result` | 1h | Medium |
| 41.8 | Write five real database tools | 2h | Medium |
| 41.9 | The misuse experiment | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 41.E1 | Expose the tools as an MCP server | 3h | **High** — directly relevant, and a strong interview talking point |
| 41.E2 | Build a tool-use trace analyzer: which tools get called, in what order, how often uselessly | 2.5h | High |
| 41.E3 | Implement tool result caching by argument hash | 1.5h | Medium — saves real money |

## Week 42 — Planning, Reflection, and State

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 42.1 | `Step` and `AgentRun` records | 45m | Easy |
| 42.2 | `build_system_prompt` | 1.5h | Medium |
| 42.3 | The basic loop | 2h | Medium |
| 42.4 | Budgets: steps, tokens, cost | 1h | Medium |
| 42.5 | `_detect_no_progress` | 1h | Medium |
| 42.6 | `_handle_tool_error` | 1h | Medium |
| 42.7 | `ConversationState` with pinning | 1.5h | Hard |
| 42.8 | `Scratchpad` with `ruled_out` | 1h | Medium |
| 42.9 | **The reflection experiment** | 1.5h | Hard |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 42.E1 | Implement a plan-then-execute agent and compare against ReAct | 3h | High — a genuinely different architecture |
| 42.E2 | Context compaction with summarization; measure quality impact | 2.5h | High |
| 42.E3 | Multi-agent: a diagnostician and a skeptic. Measure whether the skeptic helps. | 3h | High — and be prepared for the answer to be 'not much' |

## Week 43 — Database Diagnostic Tools

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 43.1 | `collect_slow_queries` | 1.5h | Medium |
| 43.2 | `collect_index_usage` | 1.5h | Medium |
| 43.3 | `collect_table_stats` | 1h | Medium |
| 43.4 | `collect_locks` | 1.5h | Hard |
| 43.5 | `collect_bloat`, `collect_connections`, `collect_replication`, `collect_settings` | 2h | Medium |
| 43.6 | `snapshot` and `diff_snapshots` | 1.5h | Medium |
| 43.7 | `generate_hypotheses` and `KNOWN_PATTERNS` | 2h | Hard |
| 43.8 | `gather_evidence` seeking disconfirmation | 1.5h | Hard |
| 43.9 | `explain_query_plan` | 2h | Hard |
| 43.10 | `format_diagnosis` with evidence validation | 1h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 43.E1 | Spin out the plan explainer as a standalone tool with a web UI | 4h | **Highest** — Flagship #9. Small, useful, shareable, might get real users. |
| 43.E2 | Add Oracle telemetry collectors alongside PostgreSQL | 3h | High — broadens the claim, uses your other expertise |
| 43.E3 | Anomaly detection on telemetry using Week 8's isolation forest | 2.5h | High — a cheap, defensible way to decide whether current state is abnormal |

## Week 44 — Agent Evaluation and Safety

### Core

| # | Exercise | Time | Difficulty |
| --- | --- | --- | --- |
| 44.1 | `IncidentScenario` schema | 45m | Easy |
| 44.2 | **Build 30-50 scenarios** | 6h | Hard |
| 44.3 | `build_benchmark` with fixed seeds | 1.5h | Medium |
| 44.4 | `score_outcome` with acceptable diagnoses | 1h | Medium |
| 44.5 | `score_trajectory` | 1.5h | Medium |
| 44.6 | `score_safety` | 1.5h | Medium |
| 44.7 | `ApprovalGate` | 1.5h | Medium |
| 44.8 | `AuditLog` with run reconstruction | 1h | Medium |
| 44.9 | `detect_prompt_injection` and the architectural defenses | 1.5h | Medium |
| 44.10 | `classify_action_risk` | 1.5h | Medium |
| 44.11 | **Run the full evaluation, 5x per scenario** | 3h | Hard |
| 44.12 | `blast_radius` and the safety document | 1.5h | Medium |

### Extensions

| # | Exercise | Time | Value |
| --- | --- | --- | --- |
| 44.E1 | Red-team your own agent: craft injection attempts in query comments and table names | 3h | **Highest** — a real security exercise with a real write-up |
| 44.E2 | Ablate agent configurations: reflection, model size, tool set, step budget | 3h | High — the ablation table |
| 44.E3 | Compare against a non-LLM baseline (rule-based heuristics) | 2.5h | **High** — and be prepared for the baseline to win on some scenarios. That is a finding. |

---

## If You Finish Early

There is no 'early' this month — put spare hours into the benchmark. More scenarios, more difficulty stratification, and the red-team write-up are all worth more than anything else you could do with the time. If the benchmark is genuinely complete, do the non-LLM baseline comparison.
