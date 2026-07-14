export interface PredictionRequest {
  units_consumed: number;
  month: string;
  region: 'urban' | 'rural' | 'suburban';
  customer_type: 'residential' | 'commercial' | 'industrial';
  year?: number;
}

export interface PredictionResponse {
  predicted_bill: number;
  confidence: number;
  analysis: string;
  recommendations: string[];
  units_consumed: number;
  month: string;
  region: string;
  estimated_daily_cost: number;
  timestamp: string;
}

export interface SeasonalAnalysis {
  seasonal_factors: Record<string, number>;
  high_consumption_months: string[];
  low_consumption_months: string[];
  analysis: string;
}

export interface RegionalAnalysis {
  regions: Record<string, RegionInfo>;
}

export interface RegionInfo {
  base_rate_per_unit: number;
  factor: number;
  characteristics: string;
}

export interface EnergyTips {
  tips: string[];
}
