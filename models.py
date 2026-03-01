import uuid
from datetime import datetime
from typing import Self

class Transaction:

    def __init__(self, amount: float, category: str, transaction_type: str):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Converts a transaction into a dictionary."""
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "transaction_type": self.transaction_type,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data) -> Self:
        """Converts a JSON dict into a Transaction object."""
        obj = cls(
            amount=data["amount"],
            category=data["category"],
            transaction_type=data["transaction_type"],
        )
        obj.id = data["id"]
        obj.timestamp = data["timestamp"]
        return obj

