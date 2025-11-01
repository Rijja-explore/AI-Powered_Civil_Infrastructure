import React, { useState, useEffect } from 'react';
import { Leaf, Wind, Droplet, Zap, BarChart3, TrendingUp, AlertTriangle, CheckCircle } from 'lucide-react';

const Environmental = () => {
  const [environmentalData, setEnvironmentalData] = useState(null);
  const [loading, setLoading] = useState(false);

  // Fetch environmental data from backend
  useEffect(() => {
    let isMounted = true;

    const fetchData = async () => {
      try {
        await fetchEnvironmentalData();
      } catch (error) {
        if (isMounted) {
          console.error('Failed to fetch environmental data:', error);
        }
      }
    };

    fetchData();

    return () => {
      isMounted = false;
    };
  }, []);

  const fetchEnvironmentalData = async () => {
    if (loading) return;
    setLoading(true);
    try {
      // Try to fetch from backend API first
      const response = await fetch('http://localhost:5002/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAhEAACAQMDBQAAAAAAAAAAAAABAgMABAUGIWGRkqGx0f/EABUBAQEAAAAAAAAAAAAAAAAAAAMF/8QAGhEAAgIDAAAAAAAAAAAAAAAAAAECEgMRkf/aAAwDAQACEQMRAD8AltJagyeH0AthI5xdrLcNM91BF5pX2HaH9bcfaSXWGaRmknyJckliyjqTzSlT54b6bk+h0R+IRjWjBqO6O2mhP//Z', // Placeholder base64 image
          px_to_cm_ratio: 0.1,
          confidence_threshold: 0.3
        })
      });

      if (response.ok) {
        const data = await response.json();
        if (data.results && data.results.environmental_impact_assessment) {
          const envData = data.results.environmental_impact_assessment;
          const materialData = data.results.material_analysis || {};

          setEnvironmentalData({
            carbon_footprint_kg: envData.carbon_footprint_kg || 0,
            water_footprint_liters: envData.water_footprint_liters || 0,
            energy_consumption_kwh: envData.energy_consumption_kwh || 0,
            eco_efficiency_rating: envData.eco_efficiency_rating || 0,
            material_analysis: {
              dominant_material: materialData.predicted_material || 'Unknown',
              material_quantity_kg: envData.material_quantity_kg || 0,
              material_confidence: materialData.confidence ? materialData.confidence / 100 : 0
            },
            recommendations: envData.recommendations || [],
            impact_trends: {
              carbon_trend: -5.2,
              water_trend: -8.1,
              energy_trend: -12.3
            },
            sustainability_score: envData.sustainability_score || 0,
            alerts: []
          });
        } else {
          throw new Error('Invalid API response structure');
        }
      } else {
        throw new Error('API request failed');
      }
    } catch (error) {
      console.error('Error fetching environmental data:', error);
      // Fallback to mock data if API is not available
      const mockData = {
        carbon_footprint_kg: 245.8,
        water_footprint_liters: 1250.5,
        energy_consumption_kwh: 380.2,
        eco_efficiency_rating: 7.5,
        material_analysis: {
          dominant_material: 'Stone',
          material_quantity_kg: 1250.0,
          material_confidence: 0.85
        },
        recommendations: [
            "Implement natural ventilation to reduce energy consumption by 15%",
            "Install rainwater harvesting system to reduce water footprint",
            "Consider solar panels for renewable energy generation",
            "Use eco-friendly construction materials with low VOC emissions",
            "Implement LED lighting to reduce energy consumption by 30%",
            "Use locally sourced construction materials to minimize transport emissions"
        ],
        impact_trends: {
          carbon_trend: -5.2,
          water_trend: -8.1,
          energy_trend: -12.3
        },
        sustainability_score: 78,
        alerts: [
          {
            type: 'warning',
            message: 'Carbon footprint above sustainable threshold',
            severity: 'medium'
          },
          {
            type: 'success',
            message: 'Water usage optimization showing positive results',
            severity: 'low'
          }
        ]
      };
      setEnvironmentalData(mockData);
    } finally {
      setLoading(false);
    }
  };

  const MetricCard = ({ icon: Icon, title, value, subtitle, color = 'primary', trend }) => (
    <div className="metric-card">
      <div className={`metric-icon bg-${color}`}>
        {Icon && <Icon size={24} />}
      </div>
      <div className="metric-content">
        <div className="metric-title">{title}</div>
        <div className="metric-value">{value}</div>
        {subtitle && <div className="metric-subtitle">{subtitle}</div>}
        {trend !== undefined && trend !== null && (
          <div className={`trend ${trend > 0 ? 'positive' : 'negative'}`}>
            <TrendingUp size={14} />
            {Math.abs(trend)}% {trend > 0 ? 'increase' : 'decrease'}
          </div>
        )}
      </div>
    </div>
  );

  const AlertCard = ({ alert }) => {
    if (!alert || !alert.type || !alert.message) return null;
    return (
      <div className={`alert-card ${alert.type}`}>
        {alert.type === 'warning' ? <AlertTriangle size={20} /> : <CheckCircle size={20} />}
        <div className="alert-content">
          <div className="alert-message">{alert.message}</div>
          <div className="alert-severity">{alert.severity || 'info'}</div>
        </div>
      </div>
    );
  };

  if (loading) {
    return (
      <div className="content-area environmental-page">
        <div className="loading-state">
          <div className="spinner"></div>
          <p>Loading environmental assessment...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="content-area environmental-page">
      <div className="page-header glass-header">
        <div className="header-content">
          <h1>
            <Leaf className="inline-icon glow-icon" size={32} />
            Environmental Impact Assessment
          </h1>
          <p>Comprehensive environmental analysis and sustainability metrics for infrastructure development and maintenance</p>
        </div>
        <div className="header-backdrop"></div>
      </div>

      <div className="environmental-content">
        {/* Key Metrics */}
        <div className="metrics-frame glass-panel">
          <div className="metrics-grid">
            <MetricCard
              icon={Wind}
              title="Carbon Footprint"
              value={`${environmentalData?.carbon_footprint_kg?.toFixed(2) || '0.00'} kg CO₂e`}
              subtitle="Equivalent CO₂ emissions"
              color="blue"
              trend={environmentalData?.impact_trends?.carbon_trend}
            />
            <MetricCard
              icon={Droplet}
              title="Water Footprint"
              value={`${environmentalData?.water_footprint_liters?.toFixed(2) || '0.00'} L`}
              subtitle="Water consumption impact"
              color="azure"
              trend={environmentalData?.impact_trends?.water_trend}
            />
            <MetricCard
              icon={Zap}
              title="Energy Usage"
              value={`${environmentalData?.energy_consumption_kwh?.toFixed(2) || '0.00'} kWh`}
              subtitle="Energy consumption"
              color="indigo"
              trend={environmentalData?.impact_trends?.energy_trend}
            />
            <MetricCard
              icon={Leaf}
              title="Eco Efficiency"
              value={`${environmentalData?.eco_efficiency_rating?.toFixed(1) || '0.0'}/10`}
              subtitle="Sustainability rating"
              color="cyan"
            />
          </div>
        </div>

        {/* Material Analysis */}
        <div className="material-analysis-section glass-panel">
          <div className="panel-header">
            <h2>
              <BarChart3 className="header-icon" size={24} />
              Material Analysis & Impact
            </h2>
          </div>
          <div className="panel-body">
            <div className="material-metrics">
              <div className="metric-card">
                <div className="metric-icon bg-primary">
                  <BarChart3 size={24} />
                </div>
                <div className="metric-content">
                  <div className="metric-title">Dominant Material</div>
                  <div className="metric-value">{environmentalData?.material_analysis?.dominant_material || 'Unknown'}</div>
                  <div className="metric-subtitle">Primary construction material</div>
                </div>
              </div>
              <div className="metric-card">
                <div className="metric-icon bg-success">
                  <TrendingUp size={24} />
                </div>
                <div className="metric-content">
                  <div className="metric-title">Material Quantity</div>
                  <div className="metric-value">{environmentalData?.material_analysis?.material_quantity_kg?.toFixed(1) || '0.0'} kg</div>
                  <div className="metric-subtitle">Estimated material mass</div>
                </div>
              </div>
              <div className="metric-card">
                <div className="metric-icon bg-warning">
                  <CheckCircle size={24} />
                </div>
                <div className="metric-content">
                  <div className="metric-title">Analysis Confidence</div>
                  <div className="metric-value">{environmentalData?.material_analysis?.material_confidence ? (environmentalData.material_analysis.material_confidence * 100).toFixed(1) : '0.0'}%</div>
                  <div className="metric-subtitle">Material identification accuracy</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Sustainability Score */}
        <div className="sustainability-score glass-panel">
          <div className="panel-header">
            <h2>
              <CheckCircle className="header-icon" size={24} />
              Sustainability Score
            </h2>
          </div>
          <div className="panel-body">
            <div className="score-display">
              <div className="score-circle">
                <div className="score-value">{environmentalData?.sustainability_score || 0}</div>
                <div className="score-label">/100</div>
              </div>
              <div className="score-description">
                <h3>Environmental Performance</h3>
                <p>Based on carbon footprint, water usage, energy consumption, and material efficiency</p>
              </div>
            </div>
          </div>
        </div>

        {/* Environmental Recommendations */}
        <div className="recommendations-section glass-panel">
          <div className="panel-header">
            <h2>
              <span className="header-icon">💡</span>
              Environmental Recommendations
            </h2>
          </div>
          <div className="panel-body">
            <div className="recommendations-grid">
              {(environmentalData?.recommendations || []).map((rec, idx) => (
                <div key={idx} className="recommendation-card glass-panel">
                  <div className="recommendation-icon">{idx + 1}</div>
                  <span className="recommendation-text">{rec}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Environmental Alerts */}
        {environmentalData?.alerts?.length > 0 && (
          <div className="alerts-section glass-panel">
            <div className="panel-header">
              <h2>
                <AlertTriangle className="header-icon" size={24} />
                Environmental Alerts
              </h2>
            </div>
            <div className="panel-body">
              <div className="alerts-list">
                {environmentalData.alerts.map((alert, idx) => (
                  <AlertCard key={idx} alert={alert} />
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Impact Trends Chart Placeholder */}
        <div className="charts-frame">
          <div className="chart-panel glass-panel">
            <div className="panel-header">
              <h3>
                <TrendingUp className="header-icon" size={20} />
                Environmental Impact Trends
              </h3>
            </div>
            <div className="panel-body">
              <div className="chart-container with-gradient">
                <div className="chart-placeholder">
                  <BarChart3 size={48} />
                  <p>Environmental impact trends visualization</p>
                  <small>Carbon, water, and energy consumption over time</small>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Environmental;