"""Tests for the FastAPI endpoints"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create test client"""
    return TestClient(app)


def test_root(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_predict(client):
    """Test prediction endpoint"""
    payload = {
        "units_consumed": 150,
        "month": "July",
        "region": "urban",
        "customer_type": "residential"
    }
    
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "predicted_bill" in data
    assert "confidence" in data
    assert "analysis" in data
    assert "recommendations" in data


def test_seasonal_analysis(client):
    """Test seasonal analysis endpoint"""
    response = client.get("/analysis/seasons")
    assert response.status_code == 200
    
    data = response.json()
    assert "seasonal_factors" in data
    assert "high_consumption_months" in data
    assert "low_consumption_months" in data


def test_regional_analysis(client):
    """Test regional analysis endpoint"""
    response = client.get("/analysis/regions")
    assert response.status_code == 200
    
    data = response.json()
    assert "regions" in data
    assert "urban" in data["regions"]
    assert "rural" in data["regions"]
    assert "suburban" in data["regions"]
