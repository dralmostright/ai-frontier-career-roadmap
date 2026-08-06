-- Runs once, on first container start, against the airoadmap database.
--
-- Extensions you need across Months 7, 10, 11, and 17.

-- Vector similarity search (Months 7, 10, 11).
CREATE EXTENSION IF NOT EXISTS vector;

-- Query statistics. This is what the DBA agent reads in Month 11 — it is the
-- single most useful view in a production PostgreSQL instance and you should
-- know every column in it cold.
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Trigram matching, for the lexical half of hybrid retrieval (Week 38).
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Table/index bloat estimation, used by the DBA agent's health checks.
CREATE EXTENSION IF NOT EXISTS pgstattuple;

-- Schemas: keep course work separated from anything you experiment with.
CREATE SCHEMA IF NOT EXISTS labs;      -- Months 7, 10: documents and embeddings
CREATE SCHEMA IF NOT EXISTS telemetry; -- Month 11: synthetic incident data
CREATE SCHEMA IF NOT EXISTS evals;     -- Months 10-17: evaluation sets and results

COMMENT ON SCHEMA labs IS 'Documents, chunks, and embeddings for retrieval labs';
COMMENT ON SCHEMA telemetry IS 'Synthetic PostgreSQL telemetry for the DBA agent';
COMMENT ON SCHEMA evals IS 'Evaluation datasets and recorded results';
