from pydantic import BaseModel, Field
from uuid import uuid4

class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    sku: str = Field(..., min_length=1)
    qty: int = Field(..., gt=0)
