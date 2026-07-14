import React, { useState } from 'react';
import Card from '../components/Card';
import LoadingSpinner from '../components/LoadingSpinner';
import { apiService } from '../services/api';
import { PredictionRequest, PredictionResponse } from '../types';
import { FaCheckCircle } from 'react-icons/fa';
import './PredictionPage.css';

const PredictionPage: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [formData, setFormData] = useState<PredictionRequest>({
    units_consumed: 150,
    month: 'July',
    region: 'urban',
    customer_type: 'residential',
    year: 2024,
  });

  const months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ];

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'units_consumed' || name === 'year' ? parseFloat(value) : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await apiService.predictBill(formData);
      setResult(response);
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || 'Failed to get prediction');
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="prediction-page">
      <h1>Predict Your Electricity Bill</h1>

      <div className="prediction-container">
        <Card className="form-card">
          <h2>Enter Your Details</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="units_consumed">Units Consumed (kWh)</label>
              <input
                type="number"
                id="units_consumed"
                name="units_consumed"
                value={formData.units_consumed}
                onChange={handleChange}
                min="0"
                step="10"
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label htmlFor="month">Month</label>
                <select
                  id="month"
                  name="month"
                  value={formData.month}
                  onChange={handleChange}
                >
                  {months.map(month => (
                    <option key={month} value={month}>{month}</option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="region">Region</label>
                <select
                  id="region"
                  name="region"
                  value={formData.region}
                  onChange={handleChange}
                >
                  <option value="urban">Urban</option>
                  <option value="rural">Rural</option>
                  <option value="suburban">Suburban</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="customer_type">Customer Type</label>
              <select
                id="customer_type"
                name="customer_type"
                value={formData.customer_type}
                onChange={handleChange}
              >
                <option value="residential">Residential</option>
                <option value="commercial">Commercial</option>
                <option value="industrial">Industrial</option>
              </select>
            </div>

            <button type="submit" className="submit-btn" disabled={loading}>
              {loading ? 'Predicting...' : 'Get Prediction'}
            </button>
          </form>
        </Card>

        {loading && (
          <Card>
            <LoadingSpinner />
          </Card>
        )}

        {error && (
          <Card className="error-card">
            <h3>❌ Error</h3>
            <p>{error}</p>
          </Card>
        )}

        {result && (
          <Card className="result-card">
            <div className="result-header">
              <FaCheckCircle className="success-icon" />
              <h2>Prediction Result</h2>
            </div>

            <div className="result-main">
              <div className="bill-amount">
                <span className="label">Predicted Bill</span>
                <span className="amount">₹{result.predicted_bill.toFixed(2)}</span>
              </div>
              <div className="daily-cost">
                <span className="label">Daily Cost</span>
                <span className="amount">₹{result.estimated_daily_cost.toFixed(2)}</span>
              </div>
              <div className="confidence">
                <span className="label">Confidence</span>
                <span className={`score ${result.confidence > 0.8 ? 'high' : result.confidence > 0.5 ? 'medium' : 'low'}`}>
                  {(result.confidence * 100).toFixed(0)}%
                </span>
              </div>
            </div>

            <div className="result-section">
              <h3>Analysis</h3>
              <p>{result.analysis}</p>
            </div>

            <div className="result-section">
              <h3>Recommendations</h3>
              <ul className="recommendations">
                {result.recommendations.map((rec, idx) => (
                  <li key={idx}>{rec}</li>
                ))}
              </ul>
            </div>

            <div className="result-details">
              <p><strong>Region:</strong> {result.region}</p>
              <p><strong>Month:</strong> {result.month}</p>
              <p><strong>Units Consumed:</strong> {result.units_consumed} kWh</p>
              <p><strong>Timestamp:</strong> {new Date(result.timestamp).toLocaleString()}</p>
            </div>
          </Card>
        )}
      </div>
    </div>
  );
};

export default PredictionPage;
