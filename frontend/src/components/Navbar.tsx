import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaBolt, FaHome, FaChartBar, FaLightbulb } from 'react-icons/fa';
import './Navbar.css';

const Navbar: React.FC = () => {
  const location = useLocation();

  const isActive = (path: string) => location.pathname === path;

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <FaBolt className="logo-icon" />
          <span>BillPredictor</span>
        </Link>
        <ul className="nav-menu">
          <li className="nav-item">
            <Link to="/" className={`nav-link ${isActive('/') ? 'active' : ''}`}>
              <FaHome /> Home
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/predict" className={`nav-link ${isActive('/predict') ? 'active' : ''}`}>
              <FaBolt /> Predict
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/analysis" className={`nav-link ${isActive('/analysis') ? 'active' : ''}`}>
              <FaChartBar /> Analysis
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/tips" className={`nav-link ${isActive('/tips') ? 'active' : ''}`}>
              <FaLightbulb /> Tips
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
