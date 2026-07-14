import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import PredictionPage from './pages/PredictionPage';
import AnalysisPage from './pages/AnalysisPage';
import TipsPage from './pages/TipsPage';
import HomePage from './pages/HomePage';

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/predict" element={<PredictionPage />} />
            <Route path="/analysis" element={<AnalysisPage />} />
            <Route path="/tips" element={<TipsPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
