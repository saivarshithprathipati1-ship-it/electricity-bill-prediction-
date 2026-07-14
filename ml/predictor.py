"""ML Model wrapper for predictions"""

import joblib
import numpy as np
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)


class BillPredictor:
    """Wrapper for trained ML model"""
    
    def __init__(self):
        self.model = None
        self.scaler = None
        
    def load_model(self, model_path: str):
        """Load trained model from disk"""
        try:
            self.model = joblib.load(model_path)
            logger.info(f"Model loaded from {model_path}")
        except FileNotFoundError:
            logger.error(f"Model file not found: {model_path}")
            raise
    
    def load_scaler(self, scaler_path: str):
        """Load feature scaler from disk"""
        try:
            self.scaler = joblib.load(scaler_path)
            logger.info(f"Scaler loaded from {scaler_path}")
        except FileNotFoundError:
            logger.warning(f"Scaler file not found: {scaler_path}")
    
    def predict(self, features: List[float]) -> float:
        """Make prediction for single sample"""
        if self.model is None:
            raise ValueError("Model not loaded")
        
        # Scale features if scaler available
        if self.scaler:
            features = self.scaler.transform([features])
        else:
            features = [features]
        
        prediction = self.model.predict(features)[0]
        return max(0, prediction)  # Ensure non-negative
    
    def predict_batch(self, features_list: List[List[float]]) -> List[float]:
        """Make predictions for multiple samples"""
        if self.model is None:
            raise ValueError("Model not loaded")
        
        # Scale features if scaler available
        if self.scaler:
            features_list = self.scaler.transform(features_list)
        
        predictions = self.model.predict(features_list)
        return [max(0, pred) for pred in predictions]
    
    def get_feature_importance(self) -> dict:
        """Get feature importance scores"""
        if not hasattr(self.model, 'feature_importances_'):
            return {}
        
        importances = self.model.feature_importances_
        feature_names = [
            "units_consumed",
            "seasonal_factor",
            "region_factor",
            "customer_factor",
            "month_number"
        ]
        
        return dict(zip(feature_names, importances))
