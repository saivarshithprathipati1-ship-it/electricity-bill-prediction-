"""Generate sample electricity data for training and testing"""

import pandas as pd
import numpy as np
import os

def generate_sample_data(num_records: int = 1000) -> pd.DataFrame:
    """Generate realistic sample electricity consumption data"""
    
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    regions = ['urban', 'suburban', 'rural']
    customer_types = ['residential', 'commercial', 'industrial']
    
    data = []
    
    for _ in range(num_records):
        month = np.random.choice(months)
        region = np.random.choice(regions)
        customer_type = np.random.choice(customer_types)
        
        # Base consumption
        base_consumption = {
            'residential': np.random.uniform(50, 300),
            'commercial': np.random.uniform(200, 1000),
            'industrial': np.random.uniform(500, 3000)
        }
        units = base_consumption.get(customer_type, 150)
        
        # Seasonal adjustment
        seasonal_factors = {
            'January': 1.15, 'February': 1.12, 'March': 1.05,
            'April': 0.95, 'May': 1.10, 'June': 1.25,
            'July': 1.30, 'August': 1.28, 'September': 1.08,
            'October': 0.95, 'November': 1.05, 'December': 1.20
        }
        seasonal_factor = seasonal_factors.get(month, 1.0)
        
        # Regional pricing
        pricing = {
            'urban': {'residential': 8.5, 'commercial': 10.0, 'industrial': 7.0},
            'suburban': {'residential': 7.5, 'commercial': 9.0, 'industrial': 6.5},
            'rural': {'residential': 6.5, 'commercial': 8.0, 'industrial': 5.5}
        }
        base_rate = pricing.get(region, {}).get(customer_type, 8.0)
        
        # Calculate bill
        bill = units * base_rate * seasonal_factor + np.random.normal(0, 50)
        bill = max(0, bill)  # Ensure non-negative
        
        data.append({
            'month': month,
            'region': region,
            'customer_type': customer_type,
            'units_consumed': round(units, 2),
            'bill_amount': round(bill, 2)
        })
    
    return pd.DataFrame(data)


if __name__ == "__main__":
    print("Generating sample data...")
    
    df = generate_sample_data(1000)
    
    # Create data directory if not exists
    os.makedirs("data/raw", exist_ok=True)
    
    # Save to CSV
    df.to_csv("data/raw/electricity_data.csv", index=False)
    print(f"Sample data saved to data/raw/electricity_data.csv")
    print(f"Generated {len(df)} records")
    print(f"\nData preview:\n{df.head()}")
    print(f"\nData statistics:\n{df.describe()}")
