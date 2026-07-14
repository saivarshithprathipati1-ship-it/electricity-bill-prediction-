"""Train the electricity bill prediction model"""

import os
import sys
import pandas as pd
import numpy as np

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ml.preprocessing import preprocess_data
from ml.trainer import BillPredictor

def main():
    print("Electricity Bill Prediction Model Training")
    print("=" * 50)
    
    # Load or generate data
    data_path = "data/raw/electricity_data.csv"
    
    if not os.path.exists(data_path):
        print(f"Data file not found at {data_path}")
        print("Generating sample data first...")
        from scripts.generate_data import generate_sample_data
        df = generate_sample_data(1000)
        os.makedirs("data/raw", exist_ok=True)
        df.to_csv(data_path, index=False)
        print(f"Sample data generated and saved")
    else:
        print(f"Loading data from {data_path}")
        df = pd.read_csv(data_path)
    
    print(f"Data shape: {df.shape}")
    print(f"\nData preview:\n{df.head()}")
    
    # Preprocess data
    print("\nPreprocessing data...")
    X, y = preprocess_data(df)
    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    
    # Train model
    print("\nTraining model...")
    trainer = BillPredictor(random_state=42)
    metrics = trainer.train(X, y, test_size=0.2)
    
    print("\nTraining completed!")
    print("\nModel Metrics:")
    for metric, value in metrics.items():
        print(f"  {metric.upper()}: {value:.4f}")
    
    # Save model and scaler
    print("\nSaving model and scaler...")
    os.makedirs("data/models", exist_ok=True)
    trainer.save_model("data/models/model.pkl")
    trainer.save_scaler("data/models/scaler.pkl")
    
    print("\nModel training complete!")
    print("Model saved to: data/models/model.pkl")
    print("Scaler saved to: data/models/scaler.pkl")
    print("\nYou can now run the API with: python -m uvicorn app.main:app --reload")

if __name__ == "__main__":
    main()
