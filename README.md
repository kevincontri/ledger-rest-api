## Ledger REST API
#### A backend service in a REST-style for managing financial transactions using `FastAPI`.
This project demonstrates fundamental concepts in backend, such as:
- RESTful routing
- Layered architecture (API -> Service -> Storage -> Model)
- Request/response validation
- JSON persistence
- Handling HTTP status

#### Stack:
- Python
- FastAPI
- Pydantic
- Uvicorn

#### Project Structure:
- `app.py` - API layer (input/output validation and HTTP routes)
- `services.py` - Business rules
- `storage.py` - JSON persistence
- `models.py` - Domain entities
- `schemas.py` - Pydantic Request & Response validation
- `requirements.txt` - Dependencies

#### Installation:
Clone the repository:<br>
```git clone https://github.com/kevincontri/ledger-rest-api.git``` <br>
```cd ledger-rest-api```<br><br>
Create and activate virtual environment:<br>
```python -m venv venv```<br>
```venv\Scripts\activate```<br><br>
Install dependencies:<br>
```pip install -r requirements.txt```

#### Run the server:
```uvicorn app:app --reload```<br><br>
Open in browser with interactive docs:<br>
http://127.0.0.1:8000/docs

#### API Endpoints:
##### Create transaction:
`POST /ledger/{ledger_name}/transactions`<br>
Request body:
```
{ 
  "amount": 100,
  "category": "food",
  "transaction_type": "expense"
}
```

##### Get all transactions:
`GET /ledger/{ledger_name}/transactions`

##### Get ledger balance:
`GET /ledger/{ledger_name}/balance`
Response body: <br>
```
{
  "balance": 1400
}
```

##### Delete a transaction:
`DELETE /ledger/{ledger_name}/transactions/{transaction_id}`

##### Edit a transaction:
`PATCH /ledger/{ledger_name}/transactions/{transaction_id}` 
Request body (any combination of fields):<br>
```
{
  "amount": 200,
  "category": "rent"
}
```

#### Future improvements
- Replace JSON storage with database (SQL)
- Add authentication (JWT)
- Dockerize application

