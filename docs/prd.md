# Product Requirements Document

## 1. Problem

A fictional B2B fulfilment business receives order, inventory and shipment updates from separate systems. Events can arrive late, more than once, out of order, or with invalid payloads. Operators need a reliable way to process events, identify failures and replay work without corrupting business state.

## 2. Goal

Build a locally runnable event-processing platform that demonstrates reliable ingestion, asynchronous processing, persistent idempotency, failure recovery, replay and observability.

## 3. Users

- Operations engineer: investigates failed events and replay status.
- Integration engineer: connects a new event producer.
- Business operator: views order and shipment status.

## 4. Core use cases

1. Submit an event through an authenticated ingestion API.
2. Validate the event schema and required metadata.
3. Persist the event and an outbox record atomically.
4. Publish the outbox record to a broker.
5. Process the event asynchronously and update derived state.
6. Ignore duplicate event IDs without repeating side effects.
7. Retry transient processing failures with bounded backoff.
8. Move repeatedly failing events to a DLQ with a reason.
9. Replay selected DLQ events with an audit record.
10. Reconcile derived order/shipment state against a synthetic source-of-truth snapshot.

## 5. Non-functional requirements

- Local startup through Docker Compose.
- Deterministic tests that do not require paid LLM APIs.
- Structured logs with correlation and event IDs.
- Health/readiness checks for API, database and broker.
- Explicit retry limits and DLQ visibility.
- No secrets or real customer data in the repository.
- Documented throughput and latency measurements from reproducible tests.

## 6. Out of scope

- Real customer integrations.
- Real payment processing.
- Production cloud deployment.
- Claims of exactly-once delivery.
- LLM decisions in the critical processing path.
- Complex Kubernetes deployment before local reliability is proven.

## 7. Acceptance criteria

- Duplicate event submission does not create duplicate business effects.
- Out-of-order events follow documented version/sequence rules.
- Transient failures retry within configured limits.
- Poison events reach the DLQ with a traceable reason.
- Replay is permission-checked and auditable.
- Database state and outbox publication survive process restart.
- Integration tests cover broker and database failure scenarios.
- A benchmark report states workload, environment, throughput, latency and error rate.
