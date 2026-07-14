"""Pydantic models for API requests and responses"""

from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum


class RegionEnum(str, Enum):
    """Supported regions"""
    URBAN = "urban"
    RURAL = "rural"
    SUBURBAN = "suburban"


class CustomerTypeEnum(str, Enum):
    """Customer types"""
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"


class PredictionRequest(BaseModel):
    """Request model for bill prediction"""
    units_consumed: float = Field(..., gt=0, description="Units consumed in kWh")
    month: str = Field(..., description="Month name")
    region: RegionEnum = Field(..., description="Customer region")
    customer_type: CustomerTypeEnum = Field(..., description="Customer type")
    year: int = Field(default=2024, description="Year")
    
    class Config:
        schema_extra = {
            "example": {
                "units_consumed": 150,
                "month": "July",
                "region": "urban",
                "customer_type": "residential",
                "year": 2024
            }
        }


class PredictionResponse(BaseModel):
    """Response model for bill prediction"""
    predicted_bill: float = Field(..., description="Predicted bill amount")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score")
    analysis: str = Field(..., description="Analysis of the prediction")
    recommendations: List[str] = Field(default_factory=list, description="Cost-saving recommendations")
    units_consumed: float
    month: str
    region: str
    estimated_daily_cost: float


class HistoryRequest(BaseModel):
    """Request for historical data"""
    customer_id: str = Field(..., description="Customer ID")
    months: int = Field(default=12, ge=1, le=60, description="Number of months to retrieve")


class PatternAnalysisResponse(BaseModel):
    """Response for pattern analysis"""
    average_consumption: float
    peak_consumption: float
    low_consumption: float
    trend: str  # "increasing", "decreasing", "stable"
    anomalies: List[dict]
    recommendations: List[str]
