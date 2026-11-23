# Service Request API

## About the Project

While working with Callsouq, I noticed a problem faced by the customer support team.

The team received more than 100 customer calls every day. These calls included complaints, technical issues, service problems and customer feedback.

Tracking all these issues manually was difficult. It was also hard to identify which problems customers faced most often.

To solve this problem, I built a Service Request API using Python and FastAPI.

The API helps organise customer complaints, issues and feedback in one place. It also creates a structured record of customer problems that the product team can use to identify areas for improvement.

## The Problem

- The support team received more than 100 calls every day.
- Customer complaints and feedback were difficult to track manually.
- Repeated problems were difficult to identify.
- The product team needed better information about customer issues.

## The Solution

I built a backend API that allows the team to:

- Create tickets for customer issues.
- View all recorded tickets.
- Filter tickets by status.
- Update the status of existing tickets.
- Store ticket information in a database.

## Impact

Within one month, we built a structured database of customer-reported issues and feedback.

This helped the product team understand the problems customers were facing and identify areas where the application could be improved.

The project connected customer support operations with product improvement.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Building the API |
| SQLite | Storing ticket information |
| SQLAlchemy | Connecting Python to the database |
| Pydantic | Validating incoming data |
| Uvicorn | Running the application |
| Pytest | Testing the API |
| HTTPX | Sending test requests |
| Docker | Running the application in a container |
| Git and GitHub | Managing code |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tickets` | Create a new ticket |
| GET | `/tickets` | View all tickets |
| GET | `/tickets?status=Open` | Filter tickets by status |
| PATCH | `/tickets/{ticket_id}` | Update a ticket's status |

## Example API Request

### Create a Ticket

**POST** `/tickets`

Request:

```json
{
  "title": "Payment failure",
  "priority": "High",
  "status": "Open"
}
```

Example response:

```json
{
  "id": 1,
  "title": "Payment failure",
  "priority": "High",
  "status": "Open"
}
```

## Project Structure

```text
service-request-api/
├── main.py
├── database.py
├── models.py
├── test_main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/mube1ena/service-request-api.git

cd service-request-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
uvicorn main:app --reload
```

Open the application at:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

## Running Tests

Run the tests using:

```bash
pytest -v
```

The current test suite checks:

1. Creating a new ticket.
2. Rejecting a request without a title.
3. Filtering tickets by status.
4. Handling updates for tickets that do not exist.

**Current test result: 4 passed.**

## Running with Docker

Build the Docker image:

```bash
docker build -t service-request-api .
```

Run the container:

```bash
docker run -d -p 8000:8000 --name service-request-api-container service-request-api
```

Open the API documentation at:

`http://localhost:8000/docs`

## What I Learned

- Building REST APIs using FastAPI.
- Connecting applications to databases.
- Managing customer service requests.
- Handling errors and invalid requests.
- Writing automated tests.
- Running applications using Docker.
- Understanding how backend systems support business operations.

## Project Repository

[Service Request API on GitHub](https://github.com/mube1ena/service-request-api)

## About Me

**Mubeena K P**

GitHub: [@mube1ena](https://github.com/mube1ena)
