# Enterprise Event Platform

A hands-on distributed-systems project for an AI Solutions Engineer / Forward Deployed Engineer portfolio.

## Business scenario

A fictional B2B fulfilment company receives order, inventory and shipment events from multiple systems. The platform validates and normalizes events, processes them asynchronously, tracks business state, and makes failures recoverable.

All data is synthetic. This project is independent and is not connected to any employer system.

## What this project is intended to demonstrate

- Event ingestion through FastAPI
- Durable asynchronous processing with Redpanda (Kafka API)
- PostgreSQL persistence and transactional outbox
- Idempotent consumers and duplicate-event handling
- Event schema versioning and validation
- Retry policy and dead-letter queue (DLQ)
- Replay of failed or historical events
- Reconciliation between source events and derived business state
- Metrics, traces, structured logs and operational dashboards
- Load and failure-injection tests

The LLM is deliberately not part of the critical event-processing path. A later optional operations assistant may summarize incidents, but deterministic code owns business state changes.

## Planned architecture

```text
Synthetic Producers
       |
       v
FastAPI Ingestion API ---- PostgreSQL (inbox + outbox)
       |                              |
       v                              v
  Validation                    Outbox Publisher
                                      |
                                      v
                                Redpanda Topics
                                      |
                          +-----------+-----------+
                          |                       |
                          v                       v
                    Order Worker            Shipment Worker
                          |                       |
                          +-----------+-----------+
                                      |
                                      v
                              PostgreSQL State
                                      |
                        +-------------+-------------+
                        |                           |
                        v                           v
                   Retry / DLQ                 Reconciliation
                        |                           |
                        +-------------+-------------+
                                      |
                                      v
                           Metrics / Traces / API
```

## Status

Starter specification and repository scaffold. Features are not claimed as implemented until code, tests and run instructions are added and verified.

## Planned stack

- Python 3.12
- FastAPI + Pydantic
- PostgreSQL
- Redpanda (Kafka-compatible local broker)
- SQLAlchemy + Alembic
- Pytest
- OpenTelemetry + Prometheus
- Docker Compose
- GitHub Actions

## First run

The initial milestone is to bring up PostgreSQL and Redpanda with Docker Compose, then implement the health endpoint and event contract. See `docs/roadmap.md`.
