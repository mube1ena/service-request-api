
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
