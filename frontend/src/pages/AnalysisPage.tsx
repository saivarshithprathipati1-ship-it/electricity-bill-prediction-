import React, { useState, useEffect } from 'react';
import Card from '../components/Card';
import LoadingSpinner from '../components/LoadingSpinner';
import { apiService } from '../services/api';
import { SeasonalAnalysis, RegionalAnalysis } from '../types';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import './AnalysisPage.css';

const AnalysisPage: React.FC = () => {
  const [seasonalData, setSeasonalData] = useState<SeasonalAnalysis | null>(null);
  const [regionalData, setRegionalData] = useState<RegionalAnalysis | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchAnalysisData();
  }, []);

  const fetchAnalysisData = async () => {
    try {
      const [seasonal, regional] = await Promise.all([
        apiService.getSeasonalAnalysis(),
        apiService.getRegionalAnalysis(),
      ]);
      setSeasonalData(seasonal);
      setRegionalData(regional);
    } catch (err: any) {
      setError(err.message || 'Failed to fetch analysis data');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <Card>
        <LoadingSpinner />
      </Card>
    );
  }

  if (error) {
    return (
      <Card className="error-card">
        <h3>❌ Error</h3>
        <p>{error}</p>
      </Card>
    );
  }

  const chartData = seasonalData
    ? Object.entries(seasonalData.seasonal_factors).map(([month, factor]) => ({
        month: month.slice(0, 3),
        factor: factor * 100 - 100,
      }))
    : [];

  const regionChartData = regionalData
    ? Object.entries(regionalData.regions).map(([name, info]) => ({
        name: name.charAt(0).toUpperCase() + name.slice(1),
        rate: info.base_rate_per_unit,
        factor: info.factor * 100,
      }))
    : [];

  return (
    <div className="analysis-page">
      <h1>Electricity Analysis</h1>

      <div className="analysis-container">
        {seasonalData && (
          <Card>
            <h2>Seasonal Factors</h2>
            <p className="card-description">{seasonalData.analysis}</p>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="month" />
                <YAxis label={{ value: 'Change (%)', angle: -90, position: 'insideLeft' }} />
                <Tooltip formatter={(value) => `${value.toFixed(1)}%`} />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="factor"
                  stroke="#3b82f6"
                  strokeWidth={2}
                  dot={{ fill: '#3b82f6', r: 4 }}
                  activeDot={{ r: 6 }}
                  name="Seasonal Factor Change"
                />
              </LineChart>
            </ResponsiveContainer>

            <div className="analysis-details">
              <div className="detail-box">
                <h3>High Consumption Months</h3>
                <p>{seasonalData.high_consumption_months.join(', ')}</p>
              </div>
              <div className="detail-box">
                <h3>Low Consumption Months</h3>
                <p>{seasonalData.low_consumption_months.join(', ')}</p>
              </div>
            </div>
          </Card>
        )}

        {regionalData && (
          <Card>
            <h2>Regional Analysis</h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={regionChartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis yAxisId="left" label={{ value: 'Base Rate (₹/unit)', angle: -90, position: 'insideLeft' }} />
                <YAxis yAxisId="right" orientation="right" label={{ value: 'Factor (%)', angle: 90, position: 'insideRight' }} />
                <Tooltip />
                <Legend />
                <Bar yAxisId="left" dataKey="rate" fill="#3b82f6" name="Base Rate" />
                <Bar yAxisId="right" dataKey="factor" fill="#10b981" name="Factor (%)" />
              </BarChart>
            </ResponsiveContainer>

            <div className="regions-grid">
              {Object.entries(regionalData.regions).map(([key, region]) => (
                <div key={key} className="region-card">
                  <h3>{key.charAt(0).toUpperCase() + key.slice(1)}</h3>
                  <p><strong>Base Rate:</strong> ₹{region.base_rate_per_unit}/unit</p>
                  <p><strong>Factor:</strong> {region.factor}</p>
                  <p><strong>Characteristics:</strong> {region.characteristics}</p>
                </div>
              ))}
            </div>
          </Card>
        )}
      </div>
    </div>
  );
};

export default AnalysisPage;
