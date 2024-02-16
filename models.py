from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field

class TurfTypeEnum(str, Enum):
    natural = "Natural"
    artificial = "Artificial"
    hybrid = "Hybrid"

class Pitch(BaseModel):
    name: str = Field(..., title="Pitch Name")
    location: str
    turf_type: TurfTypeEnum
    last_maintenance_date: datetime
    next_maintenance_date: datetime
    current_condition: int = Field(..., ge=0, le=10)
    replacement_date: datetime
