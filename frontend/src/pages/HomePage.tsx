import React from 'react';
import { Link } from 'react-router-dom';
import { FaBolt, FaChartBar, FaLightbulb } from 'react-icons/fa';
import Card from '../components/Card';
import './HomePage.css';

const HomePage: React.FC = () => {
  return (
    <div className="home-page">
      <div className="hero">
        <h1>Electricity Bill Prediction AI</h1>
        <p>Predict your electricity bills with our advanced AI agent powered by machine learning</p>
        <Link to="/predict" className="cta-button">
          Start Predicting
        </Link>
      </div>

      <div className="features-grid">
        <Card className="feature-card">
          <FaBolt className="feature-icon" />
          <h3>Smart Predictions</h3>
          <p>Get accurate electricity bill predictions based on consumption patterns and seasonal factors</p>
          <Link to="/predict" className="feature-link">
            Try Now →
          </Link>
        </Card>

        <Card className="feature-card">
          <FaChartBar className="feature-icon" />
          <h3>Deep Analysis</h3>
          <p>Understand seasonal variations, regional pricing, and consumption trends</p>
          <Link to="/analysis" className="feature-link">
            View Analysis →
          </Link>
        </Card>

        <Card className="feature-card">
          <FaLightbulb className="feature-icon" />
          <h3>Energy Tips</h3>
          <p>Get personalized recommendations to save money on your electricity bills</p>
          <Link to="/tips" className="feature-link">
            Learn More →
          </Link>
        </Card>
      </div>

      <Card className="info-card">
        <h2>How It Works</h2>
        <ol className="steps">
          <li>
            <strong>Enter Your Details:</strong> Provide your consumption units, location, and customer type
          </li>
          <li>
            <strong>AI Processing:</strong> Our machine learning model analyzes your data with seasonal factors
          </li>
          <li>
            <strong>Get Prediction:</strong> Receive accurate bill prediction with confidence score
          </li>
          <li>
            <strong>Get Recommendations:</strong> Receive personalized energy-saving tips
          </li>
        </ol>
      </Card>
    </div>
  );
};

export default HomePage;
