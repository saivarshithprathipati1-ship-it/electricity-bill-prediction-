import React, { useState, useEffect } from 'react';
import Card from '../components/Card';
import LoadingSpinner from '../components/LoadingSpinner';
import { apiService } from '../services/api';
import { FaLightbulb, FaLeaf, FaDollarSign } from 'react-icons/fa';
import './TipsPage.css';

const TipsPage: React.FC = () => {
  const [tips, setTips] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchTips();
  }, []);

  const fetchTips = async () => {
    try {
      const data = await apiService.getEnergyTips();
      setTips(data.tips);
    } catch (err: any) {
      setError(err.message || 'Failed to fetch tips');
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

  const categorizedTips = {
    efficiency: tips.filter(tip => tip.toLowerCase().includes('led') || tip.toLowerCase().includes('efficient')),
    hvac: tips.filter(tip => tip.toLowerCase().includes('thermostat') || tip.toLowerCase().includes('hvac') || tip.toLowerCase().includes('ventilation')),
    habits: tips.filter(tip => tip.toLowerCase().includes('unplug') || tip.toLowerCase().includes('laundry') || tip.toLowerCase().includes('dry')),
    other: tips.filter(tip => !tip.toLowerCase().includes('led') && !tip.toLowerCase().includes('efficient') && !tip.toLowerCase().includes('thermostat') && !tip.toLowerCase().includes('hvac') && !tip.toLowerCase().includes('ventilation') && !tip.toLowerCase().includes('unplug') && !tip.toLowerCase().includes('laundry') && !tip.toLowerCase().includes('dry')),
  };

  return (
    <div className="tips-page">
      <h1>Energy Saving Tips</h1>
      <p className="tips-intro">Save money on your electricity bills with these practical energy-saving tips</p>

      <div className="tips-container">
        {categorizedTips.efficiency.length > 0 && (
          <Card className="tips-card">
            <div className="card-header">
              <FaLightbulb className="card-icon" />
              <h2>Energy-Efficient Appliances</h2>
            </div>
            <ul className="tips-list">
              {categorizedTips.efficiency.map((tip, idx) => (
                <li key={idx}>{tip}</li>
              ))}
            </ul>
          </Card>
        )}

        {categorizedTips.hvac.length > 0 && (
          <Card className="tips-card">
            <div className="card-header">
              <FaLeaf className="card-icon" />
              <h2>Climate Control</h2>
            </div>
            <ul className="tips-list">
              {categorizedTips.hvac.map((tip, idx) => (
                <li key={idx}>{tip}</li>
              ))}
            </ul>
          </Card>
        )}

        {categorizedTips.habits.length > 0 && (
          <Card className="tips-card">
            <div className="card-header">
              <FaDollarSign className="card-icon" />
              <h2>Daily Habits</h2>
            </div>
            <ul className="tips-list">
              {categorizedTips.habits.map((tip, idx) => (
                <li key={idx}>{tip}</li>
              ))}
            </ul>
          </Card>
        )}

        {categorizedTips.other.length > 0 && (
          <Card className="tips-card">
            <div className="card-header">
              <FaLightbulb className="card-icon" />
              <h2>Additional Tips</h2>
            </div>
            <ul className="tips-list">
              {categorizedTips.other.map((tip, idx) => (
                <li key={idx}>{tip}</li>
              ))}
            </ul>
          </Card>
        )}
      </div>

      <Card className="benefits-card">
        <h2>Benefits of Energy Saving</h2>
        <div className="benefits-grid">
          <div className="benefit">
            <h3>💰 Lower Bills</h3>
            <p>Reduce your monthly electricity expenses significantly</p>
          </div>
          <div className="benefit">
            <h3>🌍 Reduce Carbon Footprint</h3>
            <p>Contribute to environmental conservation and sustainability</p>
          </div>
          <div className="benefit">
            <h3>⚡ Better Equipment Lifespan</h3>
            <p>Energy-efficient practices extend appliance life and reduce replacements</p>
          </div>
          <div className="benefit">
            <h3>🏡 Improved Comfort</h3>
            <p>Optimize your home environment while saving energy</p>
          </div>
        </div>
      </Card>
    </div>
  );
};

export default TipsPage;
