import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_all_quotes(client):
    """Test the /api/quotes endpoint."""
    response = client.get('/api/quotes')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

def test_get_random_quote(client):
    """Test the /api/quotes/random endpoint."""
    response = client.get('/api/quotes/random')
    assert response.status_code == 200
    assert "quote" in response.json
    assert "author" in response.json

def test_get_quote_by_id(client):
    """Test the /api/quotes/<id> endpoint."""
    response = client.get('/api/quotes/1')
    assert response.status_code == 200
    assert response.json["id"] == 1
    assert "quote" in response.json
    assert "author" in response.json

def test_get_quote_not_found(client):
    """Test non-existent quote ID."""
    response = client.get('/api/quotes/999')
    assert response.status_code == 404
    assert response.json == {"error": "Quote not found"}
