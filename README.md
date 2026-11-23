# Service Request API

A RESTful API for managing service requests and support tickets, built using Python, FastAPI, SQLAlchemy, and SQLite.

## Features

- Create service tickets.
- Retrieve all tickets.
- Filter tickets by status.
- Update ticket status.
- Validate incoming request data using Pydantic.
- Store ticket records using SQLite and SQLAlchemy.
- Automated API tests using pytest.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest
- HTTPX

## Project Structure

```text
service-request-api/
├── main.py
├── database.py
├── models.py
├── test_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mube1ena/service-request-api.git
cd service-request-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m uvicorn main:app --reload
```

API URL: `http://127.0.0.1:8000`

Interactive API documentation: `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tickets` | Create a ticket |
| GET | `/tickets` | Retrieve all tickets |
| GET | `/tickets?status=Open` | Filter tickets by status |
| PATCH | `/tickets/{ticket_id}` | Update ticket status |

### Example: Create a ticket

Request:

```json
{
  "title": "Login not working",
  "priority": "High",
  "status": "Open"
}
```

Response: `201 Created`

```json
{
  "id": 1,
  "title": "Login not working",
  "priority": "High",
  "status": "Open"
}
```

## Running Tests

Execute:

```bash
python -m pytest -v
```

The initial test suite covers:
- Successful ticket creation (`201 Created`).
- Missing required fields (`422 Unprocessable Entity`).

## Database

The application uses SQLite with SQLAlchemy ORM. The database file is created locally when the application initializes.

## Learning Objectives

This project was developed to practice:

- Python application structure.
- REST API development.
- SQL database integration.
- ORM fundamentals.
- HTTP status codes.
- Request validation.
- Automated API testing.

## Author

Mubeena K P

GitHub: https://github.com/mube1ena
