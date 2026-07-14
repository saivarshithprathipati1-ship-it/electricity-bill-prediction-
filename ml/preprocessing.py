"""Data preprocessing utilities"""

import pandas as pd
import numpy as np
from typing import Tuple


def preprocess_data(df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
    """Preprocess data for model training"""
    
    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))
    
    # Feature engineering
    df['month_number'] = df['month'].apply(month_to_number)
    df['seasonal_factor'] = df['month'].apply(get_seasonal_factor)
    df['region_factor'] = df['region'].apply(get_region_factor)
    df['customer_factor'] = df['customer_type'].apply(get_customer_factor)
    
    # Select features
    feature_cols = [
        'units_consumed',
        'seasonal_factor',
        'region_factor',
        'customer_factor',
        'month_number'
    ]
    
    X = df[feature_cols].values
    y = df['bill_amount'].values
    
    return X, y


def month_to_number(month: str) -> int:
    """Convert month name to number"""
    months = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    return months.get(month, 1)


def get_seasonal_factor(month: str) -> float:
    """Get seasonal multiplier"""
    factors = {
        'January': 1.15, 'February': 1.12, 'March': 1.05,
        'April': 0.95, 'May': 1.10, 'June': 1.25,
        'July': 1.30, 'August': 1.28, 'September': 1.08,
        'October': 0.95, 'November': 1.05, 'December': 1.20
    }
    return factors.get(month, 1.0)


def get_region_factor(region: str) -> float:
    """Get region multiplier"""
    factors = {'urban': 1.0, 'suburban': 0.95, 'rural': 0.85}
    return factors.get(region.lower(), 1.0)


def get_customer_factor(customer_type: str) -> float:
    """Get customer type multiplier"""
    factors = {'residential': 1.0, 'commercial': 1.2, 'industrial': 0.8}
    return factors.get(customer_type.lower(), 1.0)
