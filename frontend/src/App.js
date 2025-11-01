import React, { useState, useEffect } from 'react';
import { Camera, Video, Activity, BarChart3, Leaf, Shield, Zap, Eye, Wifi, WifiOff, Clock, AlertTriangle } from 'lucide-react';
import './styles/main.css';

// Import pages
import ImageAnalysis from './pages/ImageAnalysis';
import VideoAnalysis from './pages/VideoAnalysis';
import RealTimeMonitoring from './pages/RealTimeMonitoring';
import Analytics from './pages/Analytics';
import About from './pages/About';
import { AnalysisProvider } from './contexts/AnalysisContext';
  

function App() {
  const [activeTab, setActiveTab] = useState('video-analysis');
  const [systemStatus, setSystemStatus] = useState({
    backendConnected: false,
    lastAnalysis: null,
    activeStreams: 0,
    alertsCount: 0
  });

  // Simulate real-time status updates
  useEffect(() => {
    const interval = setInterval(() => {
      setSystemStatus(prev => ({
        ...prev,
        backendConnected: Math.random() > 0.1, // 90% uptime
        lastAnalysis: new Date(),
        activeStreams: Math.floor(Math.random() * 3),
        alertsCount: Math.floor(Math.random() * 5)
      }));
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const routes = [
    { id: 'image-analysis', label: 'Image Analysis', Icon: Camera, Component: ImageAnalysis, description: 'AI-powered crack detection & material analysis' },
    { id: 'video-analysis', label: 'Video Analysis', Icon: Video, Component: VideoAnalysis, description: 'Real-time video monitoring & processing' },
    { id: 'analytics', label: 'Analytics', Icon: BarChart3, Component: Analytics, description: 'Comprehensive data insights & statistics' },
    { id: 'about', label: 'About', Icon: Shield, Component: About, description: 'About our technology & methodology' }
  ];

  const features = [
    { icon: Shield, title: 'AI-Powered Analysis', desc: 'Advanced ML models for infrastructure assessment' },
    { icon: Eye, title: 'Real-time Monitoring', desc: 'Continuous surveillance & instant alerts' },
    { icon: Zap, title: 'Instant Insights', desc: 'Rapid assessment & actionable reports' }
  ];

  return (
    <AnalysisProvider>
      <div className="app-container">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-overlay"></div>
        <div className="hero-content">
          <div className="hero-text">
            <h1 className="hero-title">
              <Shield className="hero-icon" size={48} />
              InfraVision AI
            </h1>
            <p className="hero-subtitle">
              Intelligent Structural Health Monitoring & Advanced Infrastructure Analysis
            </p>
            <div className="hero-features">
              {features.map((feature, index) => (
                <div key={index} className="hero-feature">
                  <feature.icon className="feature-icon" size={24} />
                  <div>
                    <h3>{feature.title}</h3>
                    <p>{feature.desc}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div className="hero-visual">
            <div className="floating-elements">
              <div className="floating-card card-1">
                <Camera size={32} />
                <span>Live Analysis</span>
              </div>
              <div className="floating-card card-2">
                <Activity size={32} />
                <span>Real-time Data</span>
              </div>
              <div className="floating-card card-3">
                <BarChart3 size={32} />
                <span>Smart Insights</span>
              </div>
            </div>
          </div>
        </div>

        {/* Real-time Status Bar */}
        <div className="status-bar">
          <div className="status-item">
            {systemStatus.backendConnected ? (
              <Wifi className="status-icon connected" size={16} />
            ) : (
              <WifiOff className="status-icon disconnected" size={16} />
            )}
            <span className="status-text">
              Backend: {systemStatus.backendConnected ? 'Connected' : 'Disconnected'}
            </span>
          </div>
          <div className="status-item">
            <Clock className="status-icon" size={16} />
            <span className="status-text">
              Last Analysis: {systemStatus.lastAnalysis ? systemStatus.lastAnalysis.toLocaleTimeString() : 'Never'}
            </span>
          </div>
          <div className="status-item">
            <Activity className="status-icon" size={16} />
            <span className="status-text">
              Active Streams: {systemStatus.activeStreams}
            </span>
          </div>
          <div className="status-item">
            <AlertTriangle className={`status-icon ${systemStatus.alertsCount > 0 ? 'alert' : ''}`} size={16} />
            <span className="status-text">
              Alerts: {systemStatus.alertsCount}
            </span>
          </div>
        </div>
      </section>

      {/* Main Dashboard */}
      <div className="dashboard-container">
        {/* Navigation */}
        <nav className="nav-tabs-container">
          <div className="nav-tabs">
            {routes.map(({ id, label, Icon, description }) => (
              <button
                key={id}
                className={`nav-tab ${activeTab === id ? 'active' : ''}`}
                onClick={() => setActiveTab(id)}
                title={description}
              >
                <Icon size={20} />
                <span className="nav-label">{label}</span>
                <span className="nav-desc">{description}</span>
              </button>
            ))}
          </div>
        </nav>

        {/* Main Content */}
        <main className="main-content-frame">
          <div className="content-frame">
            {routes.map(({ id, Component }) =>
              activeTab === id && <Component key={id} />
            )}
          </div>
        </main>
      </div>

      {/* Footer */}
      <footer className="app-footer">
        <div className="footer-content">
          <div className="footer-section">
            <h4>AI-Powered Structural Health Monitor</h4>
            <p>Advanced AI technology for civil infrastructure health assessment and monitoring worldwide.</p>
            <div className="footer-links">
              <a href="#privacy">Privacy Policy</a>
              <a href="#terms">Terms of Service</a>
              <a href="#contact">Contact Us</a>
            </div>
          </div>
          <div className="footer-section">
            <h4>Technology</h4>
            <p>Built with React, Python, and advanced AI/ML models for structural health monitoring.</p>
            <div className="tech-stack">
              <span className="tech-badge">YOLOv8</span>
              <span className="tech-badge">OpenCV</span>
              <span className="tech-badge">TensorFlow</span>
              <span className="tech-badge">Flask</span>
            </div>
          </div>
          <div className="footer-section">
            <h4>Connect</h4>
            <p>Follow us for updates on structural health monitoring technology.</p>
            <div className="social-links">
              <a href="#github" className="social-link">GitHub</a>
              <a href="#linkedin" className="social-link">LinkedIn</a>
              <a href="#research" className="social-link">Research</a>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 AI-Powered Structural Health Monitor. All rights reserved. | Powered by AI for Infrastructure Safety</p>
        </div>
      </footer>
    </div>
    </AnalysisProvider>
  );
}

export default App;
