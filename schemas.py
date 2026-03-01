from pydantic import BaseModel, Field
from typing import Literal, Optional

class TransactionCreate(BaseModel):
    """Validation for a new transaction"""
    amount: float = Field(gt=0)
    category: str
    transaction_type: Literal["income", "expense"]

class TransactionUpdate(BaseModel):
    """Validation for an edit of a transaction"""
    amount: Optional[float] = Field(
        default=None,
        gt=0,
        description="Amount must be greater than 0 if provided"
    )
    category: Optional[str] = None
    transaction_type: Optional[Literal["income", "expense"]] = None

class TransactionResponse(BaseModel):
    """Validation for the Transaction response"""
    id: str
    amount: float
    category: str
    transaction_type: str
    timestamp: str

