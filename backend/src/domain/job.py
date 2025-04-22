from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel

class CaptionMethod(str, Enum):
    basic = "basic"
    advanced = "advanced"
    custom = "custom"

class Job(BaseModel):
    id: UUID
    epochs: int
    learning_rate: float
    caption_method: CaptionMethod
    status: str = "pending"

    @classmethod
    def create(cls, epochs: int, lr: float, caption_method: CaptionMethod) -> 'Job':
        return cls(id=uuid4(), epochs=epochs, learning_rate=lr, caption_method=caption_method)