from pydantic import BaseModel, Field
from typing import Literal, Optional

class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    category: str
    transaction_type: Literal["income", "expense"]

class TransactionUpdate(BaseModel):
    amount: Optional[float] = Field(
        default=None,
        gt=0,
        description="Amount must be greater than 0 if provided"
    )
    category: Optional[str] = None
    transaction_type: Optional[Literal["income", "expense"]] = None

class TransactionResponse(BaseModel):
    id: str
    amount: float
    category: str
    transaction_type: str
    timestamp: str
