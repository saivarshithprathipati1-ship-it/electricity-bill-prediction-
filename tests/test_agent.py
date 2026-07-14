"""Tests for the AI agent"""

import pytest
from app.agent import ElectricityBillAgent


@pytest.fixture
def agent():
    """Create agent instance for testing"""
    return ElectricityBillAgent()


def test_predict_bill(agent):
    """Test bill prediction"""
    result = agent.predict_bill(
        units=150,
        month="July",
        region="urban",
        customer_type="residential"
    )
    
    assert "predicted_bill" in result
    assert "confidence" in result
    assert "analysis" in result
    assert "recommendations" in result
    assert result["predicted_bill"] > 0
    assert 0 <= result["confidence"] <= 1


def test_seasonal_factors(agent):
    """Test seasonal factor calculation"""
    july_factor = agent._get_seasonal_factor("July")
    april_factor = agent._get_seasonal_factor("April")
    
    assert july_factor > april_factor  # Summer > Spring
    assert july_factor == 1.30
    assert april_factor == 0.95


def test_region_factors(agent):
    """Test region factor calculation"""
    urban = agent._get_region_factor("urban")
    rural = agent._get_region_factor("rural")
    
    assert urban > rural
    assert urban == 1.0
    assert rural == 0.85


def test_generate_recommendations(agent):
    """Test recommendation generation"""
    high_usage = agent._generate_recommendations(400, "July", "urban", "residential")
    low_usage = agent._generate_recommendations(75, "April", "rural", "residential")
    
    assert len(high_usage) > 0
    assert len(low_usage) > 0
    assert len(high_usage) <= 3
    assert len(low_usage) <= 3


def test_confidence_calculation(agent):
    """Test confidence score calculation"""
    confidence_high = agent._calculate_confidence(150, "July", "urban")
    confidence_low = agent._calculate_confidence(10, "April", "rural")
    
    assert 0 <= confidence_high <= 1
    assert 0 <= confidence_low <= 1
