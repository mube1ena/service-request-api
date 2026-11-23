
import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_ticket():
    response = client.post(
        "/tickets",
        json={
            "title": "Payment failure",
            "priority": "High",
            "status": "Open"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Payment failure"


def test_missing_title():
    response = client.post(
        "/tickets",
        json={
            "priority": "High",
            "status": "Open"
        }
    )

    assert response.status_code == 422


def test_filter_tickets_by_status():
    # Create an Open ticket
    open_response = client.post(
        "/tickets",
        json={
            "title": "Open ticket for filtering",
            "priority": "High",
            "status": "Open"
        }
    )

    # Create a Resolved ticket
    resolved_response = client.post(
        "/tickets",
        json={
            "title": "Resolved ticket for filtering",
            "priority": "Medium",
            "status": "Resolved"
        }
    )

    assert open_response.status_code == 201
    assert resolved_response.status_code == 201

    # Retrieve only Open tickets
    response = client.get("/tickets?status=Open")

    assert response.status_code == 200

    tickets = response.json()
    ticket_ids = [ticket["id"] for ticket in tickets]

    assert open_response.json()["id"] in ticket_ids
    assert resolved_response.json()["id"] not in ticket_ids
    assert all(ticket["status"] == "Open" for ticket in tickets)


def test_update_nonexistent_ticket():
    response = client.patch(
        "/tickets/999",
        json={"status": "Resolved"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket not found"

