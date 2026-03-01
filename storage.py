import json
import os
from models import Transaction

class JSONStorage:
    def __init__(self, filename: str):
        self.filename = filename

    def save(self, transactions: list[Transaction]) -> None:
        """Creates a JSON file with a list of Transaction objects
            in a dict format"""

        data = [t.to_dict() for t in transactions]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self) -> list[Transaction]:
        """Checks if the ledger file already exists and load it with from_dict(),
            if it's not found, start empty"""

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []

        return [Transaction.from_dict(item) for item in data]



