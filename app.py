from services import LedgerService
from fastapi import FastAPI, HTTPException
from schemas import TransactionCreate, TransactionUpdate, TransactionResponse
from typing import List
app = FastAPI(
    title="Ledger REST API",
    description="REST API for managing financial transactions",
    version='1.0'
)

@app.post("/ledger/{ledger_name}/transactions", response_model=TransactionResponse)
def create_transaction(ledger_name: str, data: TransactionCreate):
    ledger_instance = LedgerService(ledger_name)
    transaction = ledger_instance.add_transaction(
        amount=data.amount,
        category=data.category,
        transaction_type=data.transaction_type
    )
    return transaction.to_dict()


@app.get("/ledger/{ledger_name}/transactions", response_model=List[TransactionResponse])
def display_transaction(ledger_name: str):
    ledger_instance = LedgerService(ledger_name)
    return [t.to_dict() for t in ledger_instance.get_all()]

@app.get("/ledger/{ledger_name}/balance")
def display_balance(ledger_name: str):
    ledger_instance = LedgerService(ledger_name)
    return {
        "balance": ledger_instance.get_balance()
    }

@app.delete("/ledger/{ledger_name}/transactions/{transaction_id}")
def delete_transaction(ledger_name: str, transaction_id: str):
    ledger_instance = LedgerService(ledger_name)
    removed = ledger_instance.delete(transaction_id)
    if removed is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction ID not found"
        )
    return {
        "message": "Transaction Deleted"
    }

@app.patch("/ledger/{ledger_name}/transactions/{transaction_id}")
def edit_transaction(ledger_name: str, transaction_id: str, data: TransactionUpdate):
    ledger_instance = LedgerService(ledger_name)
    edition = ledger_instance.edit(
        transaction_id,
        amount=data.amount,
        category=data.category,
        transaction_type=data.transaction_type
    )

    if edition:
        return {
            "message": "Transaction edited."
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )

