"""Model training module"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import logging

logger = logging.getLogger(__name__)


class BillPredictor:
    """Model trainer for electricity bill prediction"""
    
    def __init__(self, random_state: int = 42):
        self.model = None
        self.scaler = StandardScaler()
        self.random_state = random_state
        self.metrics = {}
    
    def train(self, X: np.ndarray, y: np.ndarray, test_size: float = 0.2):
        """Train the model"""
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=15,
            random_state=self.random_state,
            n_jobs=-1
        )
        
        self.model.fit(X_train_scaled, y_train)
        logger.info("Model training completed")
        
        # Evaluate
        self._evaluate(X_test_scaled, y_test)
        
        return self.metrics
    
    def _evaluate(self, X_test: np.ndarray, y_test: np.ndarray):
        """Evaluate model performance"""
        y_pred = self.model.predict(X_test)
        
        self.metrics = {
            "mae": mean_absolute_error(y_test, y_pred),
            "mse": mean_squared_error(y_test, y_pred),
            "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
            "r2": r2_score(y_test, y_pred)
        }
        
        logger.info(f"Model Metrics: {self.metrics}")
    
    def save_model(self, model_path: str):
        """Save trained model"""
        joblib.dump(self.model, model_path)
        logger.info(f"Model saved to {model_path}")
    
    def save_scaler(self, scaler_path: str):
        """Save feature scaler"""
        joblib.dump(self.scaler, scaler_path)
        logger.info(f"Scaler saved to {scaler_path}")
