from pydantic import BaseModel

from enum import Enum


class Priority(Enum):
    HIGH = "HIGH"
    MODERATE = "MODERATE"
    LOW = "LOW"

class Todo(BaseModel):
    id: int
    priority: Priority
    description: str 