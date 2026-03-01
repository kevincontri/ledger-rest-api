from models import Transaction
from storage import JSONStorage
from typing import List

class LedgerService:
    def __init__(self, name: str):
        self.name = name
        self.storage = JSONStorage(f"{name.lower()}_transactions.json")
        self.transactions = self.storage.load()

    def add_transaction(self, amount: float, category: str, transaction_type: str):
        """Creates a Transaction object from the arguments provided"""

        transaction = Transaction(amount, category, transaction_type)
        self.transactions.append(transaction)
        self.storage.save(self.transactions)
        return transaction

    def get_all(self) -> List[Transaction]:
        """Retrieve all stored transactions."""

        return self.transactions

    def get_balance(self):
        """Calculate and return the current balance."""
        
        balance = 0
        for t in self.transactions:
            if t.transaction_type == "income":
                balance += t.amount
            elif t.transaction_type == "expense":
                balance -= t.amount
        return balance

    def delete(self, transaction_id: str):
        """Remove a transaction by its ID and return it."""
        
        for index, transaction in enumerate(self.transactions):
            if transaction.id == transaction_id:
                removed = self.transactions.pop(index)
                self.storage.save(self.transactions)
                return removed
        return None

    def edit(self, transaction_id: str, amount=None, category=None, transaction_type=None):
        """Update fields of a transaction by ID and save changes."""
        
        edited = False
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                if amount is not None:
                    transaction.amount = amount
                    edited = True

                if category is not None:
                    transaction.category = category
                    edited = True

                if transaction_type is not None:
                    transaction.transaction_type = type
                    edited = True

                self.storage.save(self.transactions)

                return edited

        return edited
