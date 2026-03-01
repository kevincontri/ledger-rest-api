## Ledger REST API
#### A backend service in a REST-style for managing financial transactions using `FastAPI`.
This project demonstrates fundamental concepts in backend, such as:
- RESTful routing
- Layered architecture (API -> Service -> Storage -> Model)
- Request/response validation
- JSON persistence
- Proper handling of HTTP status

#### Project Structure:
- `app.py` # API layer (input/output validation and HTTP routes)
- `services.py` # Business rules
- `storage.py` # JSON persistence
- `models.py` # Domain entities
- `schemas.py` # Pydantic Request & Response validation
- `requirements.txt` # Dependencies

#### Installation:
Clone the repository:
```git clone https://github.com/kevincontri/projects.git```


