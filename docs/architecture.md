# Architecture and Design Notes

## Components

- **Ingestion API:** validates producer requests and assigns correlation metadata.
- **PostgreSQL inbox:** stores received event IDs and processing status.
- **Transactional outbox:** stores messages in the same transaction as accepted business changes.
- **Outbox publisher:** publishes pending records to Redpanda and marks successful publication.
- **Broker:** transports events to independent consumer groups.
- **Consumers:** apply deterministic business rules and update projections.
- **Retry/DLQ handler:** separates transient errors from poison messages.
- **Replay service:** re-enqueues selected failures while retaining replay history.
- **Reconciliation worker:** compares derived state with synthetic source snapshots.
- **Observability:** exposes metrics, traces and structured logs.

## Event envelope

Every event should contain:
- `event_id`: globally unique stable identifier
- `event_type`: domain event name
- `schema_version`: integer schema version
- `occurred_at`: source timestamp
- `received_at`: platform timestamp
- `producer`: source system name
- `correlation_id`: workflow trace identifier
- `aggregate_id`: order or shipment identifier
- `sequence`: monotonic sequence within an aggregate where available
- `payload`: validated event-specific data

## Delivery semantics

The broker and consumers may deliver a message more than once. The application therefore aims for **at-least-once delivery with idempotent processing**, not a blanket exactly-once guarantee.

The consumer records the event ID and applies the business state transition transactionally. A repeated event ID must not repeat the transition.

## Failure handling

- Invalid schema: reject at ingestion with a clear validation response.
- Temporary database/broker issue: retry with bounded exponential backoff.
- Repeated processing failure: move to DLQ and preserve error metadata.
- Consumer crash after database commit but before acknowledgement: redelivery is safe because of persistent idempotency.
- Out-of-order event: apply documented sequence/version policy; do not silently overwrite newer state.
- Replay: require an operator action, record actor/reason/time, and preserve the original event identity plus replay metadata.

## Key design questions to resolve in ADRs

1. Redpanda vs RabbitMQ for this learning objective.
2. Inbox/outbox schema and transaction boundaries.
3. Partition key and ordering requirements.
4. Retry ownership: consumer, broker, or both.
5. DLQ retention and replay policy.
6. Event schema compatibility policy.
