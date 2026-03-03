import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import pytest
from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_add_note(client):
    response = client.post(
        "/notes",
        data=json.dumps({"note": "Test Note"}),
        content_type="application/json"
    )
    assert response.status_code == 201

def test_get_notes(client):
    response = client.get("/notes")
    assert response.status_code == 200