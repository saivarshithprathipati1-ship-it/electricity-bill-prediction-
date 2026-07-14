# Electricity Bill Prediction AI Agent

An intelligent AI agent that predicts electricity bills based on consumption patterns, seasonal factors, and historical data.

## Features

- **Machine Learning Models**: Trained regression models for accurate bill prediction
- **AI Agent Logic**: Intelligent decision-making based on consumption patterns
- **Real-time Predictions**: Get bill predictions instantly
- **Pattern Analysis**: Analyzes consumption trends and anomalies
- **Seasonal Adjustments**: Considers seasonal variations in electricity usage
- **REST API**: Easy-to-use API endpoints for predictions

## Stack

- **Language**: Python 3.9+
- **ML Framework**: scikit-learn, pandas, numpy
- **API**: FastAPI
- **Data**: SQLite (local) / PostgreSQL (production)
- **Deployment**: Docker

## Quick Start

### Prerequisites

- Python 3.9+
- pip or conda
- Docker (optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/saivarshithprathipati1-ship-it/electricity-bill-prediction-.git
cd electricity-bill-prediction-

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Training the Model

```bash
python scripts/train_model.py
```

### Running the API

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Running with Docker

```bash
docker build -t electricity-bill-agent .
docker run -p 8000:8000 electricity-bill-agent
```

## API Endpoints

### Predict Bill

```bash
POST /predict
Content-Type: application/json

{
  "units_consumed": 150,
  "month": "July",
  "region": "urban",
  "customer_type": "residential"
}

Response:
{
  "predicted_bill": 2850.50,
  "confidence": 0.92,
  "analysis": "Your consumption is 20% higher than average for this season",
  "recommendations": ["Consider using LED bulbs", "Use AC in off-peak hours"]
}
```

### Get Historical Data

```bash
GET /history?customer_id=123
```

### Get Pattern Analysis

```bash
GET /analysis/patterns?customer_id=123&months=12
```

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── models.py            # Pydantic models
│   └── agent.py             # AI Agent logic
├── ml/
│   ├── __init__.py
│   ├── predictor.py         # ML model wrapper
│   ├── trainer.py           # Model training logic
│   └── preprocessing.py     # Data preprocessing
├── data/
│   ├── raw/                 # Raw data files
│   ├── processed/           # Processed data
│   └── models/              # Trained models
├── scripts/
│   ├── train_model.py       # Training script
│   ├── generate_data.py     # Sample data generation
│   └── evaluate.py          # Model evaluation
├── tests/
│   ├── test_agent.py
│   ├── test_predictor.py
│   └── test_api.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .gitignore
```

## How It Works

1. **Data Collection**: Gathers user consumption data, seasonal info, and pricing
2. **Feature Engineering**: Extracts relevant features for prediction
3. **Model Prediction**: Uses trained ML model to predict consumption patterns
4. **AI Agent Analysis**: Analyzes patterns and generates recommendations
5. **Response**: Returns prediction with confidence score and advice

## Configuration

Edit `config.yaml` to customize:

- Model parameters
- Seasonal adjustments
- Regional pricing
- Prediction sensitivity

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT
