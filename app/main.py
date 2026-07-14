"""FastAPI application for electricity bill prediction"""

import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import PredictionRequest, PredictionResponse, PatternAnalysisResponse
from app.agent import ElectricityBillAgent

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Electricity Bill Prediction Agent",
    description="AI-powered agent for predicting and analyzing electricity bills",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI agent
agent = ElectricityBillAgent()


@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    logger.info("Electricity Bill Prediction Agent started")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Electricity Bill Prediction AI Agent",
        "version": "0.1.0",
        "endpoints": {
            "predict": "/predict",
            "health": "/health",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "electricity-bill-agent"}


@app.post("/predict", response_model=PredictionResponse)
async def predict_bill(request: PredictionRequest) -> PredictionResponse:
    """
    Predict electricity bill based on consumption and parameters
    
    Example:
    ```
    {
        "units_consumed": 150,
        "month": "July",
        "region": "urban",
        "customer_type": "residential"
    }
    ```
    """
    try:
        logger.info(f"Prediction request: {request}")
        
        result = agent.predict_bill(
            units=request.units_consumed,
            month=request.month,
            region=request.region.value,
            customer_type=request.customer_type.value
        )
        
        prediction = PredictionResponse(**result)
        logger.info(f"Prediction successful: {prediction.predicted_bill}")
        return prediction
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/batch-predict")
async def batch_predict(requests: list[PredictionRequest]):
    """
    Predict bills for multiple customers at once
    """
    try:
        results = []
        for request in requests:
            result = agent.predict_bill(
                units=request.units_consumed,
                month=request.month,
                region=request.region.value,
                customer_type=request.customer_type.value
            )
            results.append(result)
        
        logger.info(f"Batch prediction completed: {len(results)} predictions")
        return {"predictions": results, "count": len(results)}
        
    except Exception as e:
        logger.error(f"Batch prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/analysis/seasons")
async def seasonal_analysis():
    """
    Get seasonal adjustment factors and analysis
    """
    seasonal_factors = {
        "January": 1.15, "February": 1.12, "March": 1.05,
        "April": 0.95, "May": 1.10, "June": 1.25,
        "July": 1.30, "August": 1.28, "September": 1.08,
        "October": 0.95, "November": 1.05, "December": 1.20
    }
    
    high_consumption = [m for m, f in seasonal_factors.items() if f > 1.15]
    low_consumption = [m for m, f in seasonal_factors.items() if f < 0.95]
    
    return {
        "seasonal_factors": seasonal_factors,
        "high_consumption_months": high_consumption,
        "low_consumption_months": low_consumption,
        "analysis": "Use this to understand seasonal variations in your consumption patterns"
    }


@app.get("/analysis/regions")
async def regional_analysis():
    """
    Get regional pricing and factors
    """
    return {
        "regions": {
            "urban": {
                "base_rate_per_unit": 8.50,
                "factor": 1.0,
                "characteristics": "Higher consumption due to commercial areas"
            },
            "suburban": {
                "base_rate_per_unit": 7.50,
                "factor": 0.95,
                "characteristics": "Medium consumption patterns"
            },
            "rural": {
                "base_rate_per_unit": 6.50,
                "factor": 0.85,
                "characteristics": "Lower consumption, agricultural areas"
            }
        }
    }


@app.get("/recommendations/tips")
async def energy_tips():
    """
    Get general energy-saving tips
    """
    return {
        "tips": [
            "Switch to LED bulbs - saves up to 80% energy",
            "Use programmable thermostats - saves 10-15%",
            "Unplug devices when not in use - phantom load prevention",
            "Use energy-efficient appliances (ENERGY STAR certified)",
            "Use natural lighting during daytime",
            "Regular maintenance of HVAC systems",
            "Insulate your home properly",
            "Use cold water for laundry when possible",
            "Air dry clothes instead of using dryer",
            "Close doors to unused rooms"
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
