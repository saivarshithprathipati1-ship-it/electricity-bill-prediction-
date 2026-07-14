import axios from 'axios';
import { PredictionRequest, PredictionResponse, SeasonalAnalysis, RegionalAnalysis, EnergyTips } from '../types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiService = {
  // Predictions
  predictBill: async (data: PredictionRequest): Promise<PredictionResponse> => {
    const response = await api.post<PredictionResponse>('/predict', data);
    return response.data;
  },

  batchPredict: async (data: PredictionRequest[]): Promise<{ predictions: PredictionResponse[]; count: number }> => {
    const response = await api.post('/batch-predict', data);
    return response.data;
  },

  // Analysis
  getSeasonalAnalysis: async (): Promise<SeasonalAnalysis> => {
    const response = await api.get<SeasonalAnalysis>('/analysis/seasons');
    return response.data;
  },

  getRegionalAnalysis: async (): Promise<RegionalAnalysis> => {
    const response = await api.get<RegionalAnalysis>('/analysis/regions');
    return response.data;
  },

  // Recommendations
  getEnergyTips: async (): Promise<EnergyTips> => {
    const response = await api.get<EnergyTips>('/recommendations/tips');
    return response.data;
  },

  // Health check
  healthCheck: async (): Promise<{ status: string; service: string }> => {
    const response = await api.get('/health');
    return response.data;
  },
};

export default api;
