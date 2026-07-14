"""AI Agent for electricity bill prediction and analysis"""

import logging
from typing import List, Dict, Any
import yaml
from datetime import datetime

logger = logging.getLogger(__name__)


class ElectricityBillAgent:
    """Intelligent AI agent for electricity bill prediction and analysis"""
    
    def __init__(self, model_path: str = "data/models/model.pkl"):
        """Initialize the agent with trained model"""
        self.model = None
        self.model_path = model_path
        self.config = self._load_config()
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def _load_config(self) -> dict:
        """Load configuration from YAML file"""
        try:
            with open("config.yaml", "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            self.logger.warning("Config file not found, using defaults")
            return {}
    
    def load_model(self, model):
        """Load a pre-trained model"""
        self.model = model
        self.logger.info("Model loaded successfully")
    
    def predict_bill(self, units: float, month: str, region: str, 
                    customer_type: str) -> Dict[str, Any]:
        """Predict electricity bill with analysis"""
        
        # Extract features
        features = self._extract_features(units, month, region, customer_type)
        
        # Make prediction
        if self.model:
            predicted_bill = self.model.predict([features])[0]
        else:
            predicted_bill = self._estimate_bill(units, month, region, customer_type)
        
        # Generate confidence score
        confidence = self._calculate_confidence(units, month, region)
        
        # Analyze consumption
        analysis = self._analyze_consumption(units, month, region, customer_type)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(units, month, region, customer_type)
        
        daily_cost = predicted_bill / self._get_days_in_month(month)
        
        return {
            "predicted_bill": round(predicted_bill, 2),
            "confidence": round(confidence, 3),
            "analysis": analysis,
            "recommendations": recommendations,
            "units_consumed": units,
            "month": month,
            "region": region,
            "estimated_daily_cost": round(daily_cost, 2),
            "timestamp": datetime.now().isoformat()
        }
    
    def _extract_features(self, units: float, month: str, region: str, 
                         customer_type: str) -> list:
        """Extract features for the model"""
        seasonal_factor = self._get_seasonal_factor(month)
        region_factor = self._get_region_factor(region)
        customer_factor = self._get_customer_factor(customer_type)
        
        return [
            units,
            seasonal_factor,
            region_factor,
            customer_factor,
            self._month_to_number(month),
        ]
    
    def _estimate_bill(self, units: float, month: str, region: str, 
                      customer_type: str) -> float:
        """Estimate bill using rule-based system"""
        pricing = {
            "urban": {"residential": 8.5, "commercial": 10.0, "industrial": 7.0},
            "rural": {"residential": 6.5, "commercial": 8.0, "industrial": 5.5},
            "suburban": {"residential": 7.5, "commercial": 9.0, "industrial": 6.5},
        }
        
        base_rate = pricing.get(region, {}).get(customer_type, 8.0)
        seasonal_factor = self._get_seasonal_factor(month)
        
        bill = units * base_rate * seasonal_factor
        return bill
    
    def _calculate_confidence(self, units: float, month: str, region: str) -> float:
        """Calculate prediction confidence"""
        base_confidence = 0.75
        
        # Adjust based on seasonality consistency
        if month in ["June", "July", "August", "December", "January"]:
            base_confidence += 0.10
        
        # Adjust based on reasonable consumption
        if 50 <= units <= 500:
            base_confidence += 0.05
        
        return min(0.99, base_confidence)
    
    def _analyze_consumption(self, units: float, month: str, region: str, 
                            customer_type: str) -> str:
        """Analyze consumption patterns"""
        seasonal_factor = self._get_seasonal_factor(month)
        
        if seasonal_factor > 1.15:
            season_note = "This is a high-consumption season. "
        elif seasonal_factor < 0.95:
            season_note = "This is a low-consumption season. "
        else:
            season_note = ""
        
        if units > 300:
            usage_note = "Your consumption is quite high."
        elif units < 100:
            usage_note = "Your consumption is relatively low."
        else:
            usage_note = "Your consumption is within average range."
        
        return f"{season_note}Region: {region.capitalize()}. {usage_note}"
    
    def _generate_recommendations(self, units: float, month: str, region: str, 
                                 customer_type: str) -> List[str]:
        """Generate cost-saving recommendations"""
        recommendations = []
        
        seasonal_factor = self._get_seasonal_factor(month)
        
        if seasonal_factor > 1.20:
            recommendations.append("Switch to energy-efficient appliances for peak season")
            recommendations.append("Use natural ventilation instead of AC during off-peak hours")
        
        if units > 300:
            recommendations.append("Consider an energy audit to identify power-hungry devices")
            recommendations.append("Install solar panels to reduce grid dependency")
            recommendations.append("Use LED bulbs throughout your home")
        
        if region == "urban":
            recommendations.append("Check if you're eligible for urban energy rebate programs")
        
        if not recommendations:
            recommendations.append("Your consumption is efficient. Keep up the good work!")
        
        return recommendations[:3]  # Return top 3
    
    @staticmethod
    def _get_seasonal_factor(month: str) -> float:
        """Get seasonal multiplier for a month"""
        factors = {
            "January": 1.15, "February": 1.12, "March": 1.05,
            "April": 0.95, "May": 1.10, "June": 1.25,
            "July": 1.30, "August": 1.28, "September": 1.08,
            "October": 0.95, "November": 1.05, "December": 1.20
        }
        return factors.get(month, 1.0)
    
    @staticmethod
    def _get_region_factor(region: str) -> float:
        """Get region multiplier"""
        factors = {"urban": 1.0, "suburban": 0.95, "rural": 0.85}
        return factors.get(region, 1.0)
    
    @staticmethod
    def _get_customer_factor(customer_type: str) -> float:
        """Get customer type multiplier"""
        factors = {"residential": 1.0, "commercial": 1.2, "industrial": 0.8}
        return factors.get(customer_type, 1.0)
    
    @staticmethod
    def _month_to_number(month: str) -> int:
        """Convert month name to number"""
        months = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }
        return months.get(month, 1)
    
    @staticmethod
    def _get_days_in_month(month: str) -> int:
        """Get days in a month"""
        days = {
            "January": 31, "February": 28, "March": 31, "April": 30,
            "May": 31, "June": 30, "July": 31, "August": 31,
            "September": 30, "October": 31, "November": 30, "December": 31
        }
        return days.get(month, 30)
