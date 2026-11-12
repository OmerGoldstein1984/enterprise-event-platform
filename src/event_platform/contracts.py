from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field


class EventEnvelope(BaseModel):
    event_id: str = Field(min_length=1)
    event_type: str = Field(min_length=1)
    schema_version: int = Field(ge=1)
    occurred_at: datetime
    producer: str = Field(min_length=1)
    correlation_id: str = Field(min_length=1)
    aggregate_id: str = Field(min_length=1)
    sequence: int = Field(ge=0)
    payload: dict[str, Any]
