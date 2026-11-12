# Implementation Roadmap

Each milestone must include code, tests, a runnable demo and an explanation you can give in an interview.

## M0 — Foundation
- Python package layout and configuration
- FastAPI health/readiness endpoints
- PostgreSQL connection and migration setup
- Docker Compose for PostgreSQL and Redpanda
- CI for linting and unit tests

## M1 — Event contract and ingestion
- Versioned Pydantic event envelope
- Event validation and producer identity
- Persist inbox and outbox records in one transaction
- API integration tests

## M2 — Broker publishing and consumers
- Outbox publisher
- Redpanda topic and consumer group
- Consumer persistence and idempotency
- Correlation IDs and structured logs

## M3 — Reliability
- Bounded retries and exponential backoff
- DLQ with failure metadata
- Duplicate and out-of-order event tests
- Process restart and broker outage tests

## M4 — Replay and reconciliation
- Audited replay endpoint
- Replay safeguards and idempotency tests
- Synthetic source-of-truth snapshots
- Reconciliation report and mismatch handling

## M5 — Observability and performance
- Prometheus metrics
- OpenTelemetry traces
- Throughput and latency benchmark
- Failure-injection scenarios
- Operational runbook and demo script

## M6 — Optional AI operations assistant
Only after the deterministic platform works:
- Summarize a selected incident using an LLM
- Retrieve runbooks using RAG
- Require citations and abstain when evidence is missing
- Never let the LLM directly mutate event state or bypass operator permissions
