import React, { useState, useRef } from 'react';
import { Bar } from '@ant-design/plots';
import { useAnalysis } from '../contexts/AnalysisContext';
import { Camera, Upload, Play, Loader, PieChart, Target, Activity, TrendingUp, CheckCircle, AlertTriangle, BarChart3, Wind, Droplet, Zap, Leaf, Download } from 'lucide-react';

const ImageAnalysis = () => {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const [outputImages, setOutputImages] = useState(null);
  const fileInputRef = useRef(null);
  const { updateAnalysis, clearAnalysis } = useAnalysis();
  
  const [settings, setSettings] = useState({
    confidenceThreshold: 0.3,
    pixelToCmRatio: 0.1
  });

  const API_URL = 'http://localhost:5002';

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      const reader = new FileReader();
      reader.onloadend = () => setPreview(reader.result);
      reader.readAsDataURL(selectedFile);
      setResults(null);
      setOutputImages(null);
      setError(null);
    }
  };

  const handleAnalyze = async () => {
    if (!file) {
      setError('Please select a file first');
      return;
    }

    setLoading(true);
    setError(null);
    setProgress(0);
    
    try {
      const reader = new FileReader();
      const fileBase64Promise = new Promise((resolve, reject) => {
        reader.onload = () => resolve(reader.result);
        reader.onerror = (error) => reject(error);
      });
      reader.readAsDataURL(file);
      const fileBase64 = await fileBase64Promise;

      // Simulate progress
      const progressInterval = setInterval(() => {
        setProgress(prev => Math.min(prev + 10, 90));
      }, 300);

      const response = await fetch(`${API_URL}/api/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: fileBase64,
          px_to_cm_ratio: settings.pixelToCmRatio,
          confidence_threshold: settings.confidenceThreshold
        })
      });

      clearInterval(progressInterval);
      
      if (!response.ok) {
        throw new Error('Analysis failed');
      }

      const data = await response.json();
      setResults(data.results);
      setOutputImages(data.output_images);
      updateAnalysis(data.results); // Store in context for persistence
      setProgress(100);
      setLoading(false);
    } catch (err) {
      console.error('Analysis error:', err);
      setError('Analysis failed. Make sure the backend (finalwebapp_api.py) is running on port 5002.');
      setLoading(false);
      setProgress(0);
    }
  };

  const handleDownloadPDF = async () => {
    if (!results) return;
    
    try {
      const response = await fetch(`${API_URL}/api/download-pdf`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          analysis_date: new Date().toISOString(),
          site_analysis: results,
        })
      });
      
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'heritage-analysis-report.pdf');
        document.body.appendChild(link);
        link.click();
        link.parentNode.removeChild(link);
      }
    } catch (err) {
      console.error('PDF download error:', err);
      alert('PDF generation failed. Feature may not be available.');
    }
  };

  const MetricCard = ({ icon: Icon, title, value, subtitle, color = 'primary' }) => (
    <div className="metric-card">
      <div className={`metric-icon bg-${color}`}>
        <Icon size={24} />
      </div>
      <div className="metric-content">
        <div className="metric-title">{title}</div>
        <div className="metric-value">{value}</div>
        {subtitle && <div className="metric-subtitle">{subtitle}</div>}
      </div>
    </div>
  );

  const SeverityBadge = ({ severity }) => {
    const colors = {
      'Minor': 'success',
      'Moderate': 'warning',
      'Severe': 'danger',
      'Critical': 'danger'
    };
    return <span className={`badge bg-${colors[severity] || 'secondary'}`}>{severity}</span>;
  };

  // Material Confidence Chart Component
  const MaterialConfidenceChart = ({ materialData }) => {
    if (!materialData || !materialData.probabilities || typeof materialData.probabilities !== 'object') {
      return null;
    }

    try {
      const materials = Object.keys(materialData.probabilities);
      const probabilities = Object.values(materialData.probabilities);

      // Ensure we have valid arrays
      if (!Array.isArray(materials) || !Array.isArray(probabilities) || materials.length === 0) {
        return null;
      }

      // Define colors for different materials
      const materialColors = {
        'concrete': '#60a5fa',
        'steel': '#ef4444',
        'brick': '#f59e0b',
        'wood': '#10b981',
        'glass': '#8b5cf6',
        'stone': '#6b7280',
        'asphalt': '#374151',
        'plastic': '#ec4899'
      };

      // Prepare data for bar chart with comprehensive validation
      const chartData = materials
        .filter(material => material && typeof material === 'string' && material.trim() !== '') // Filter out null/undefined/empty materials
        .map((material, index) => {
          const confidence = probabilities[index];
          if (typeof confidence !== 'number' || isNaN(confidence)) {
            return null; // Skip invalid confidence values
          }
          return {
            material: material.charAt(0).toUpperCase() + material.slice(1), // Capitalize first letter
            confidence: Math.max(0, Math.min(100, confidence * 100)), // Ensure confidence is between 0-100
            color: materialColors[material.toLowerCase()] || '#60a5fa'
          };
        })
        .filter(item => item !== null); // Remove any null entries

      // If no valid data after filtering, don't render the chart
      if (!chartData || chartData.length === 0) {
        return null;
      }

      const config = {
        data: chartData,
        xField: 'material',
        yField: 'confidence',
        colorField: 'color', // Use the color field directly
        label: {
          position: 'middle',
          style: {
            fill: '#FFFFFF',
            opacity: 0.8,
            fontSize: 12,
            fontWeight: 500
          },
          formatter: (datum) => `${datum.confidence?.toFixed(1) || 0}%`
        },
        xAxis: {
          label: {
            style: {
              fill: '#64748b',
              fontSize: 12
            }
          }
        },
        yAxis: {
          label: {
            formatter: (v) => `${v}%`,
            style: {
              fill: '#64748b',
              fontSize: 12
            }
          }
        },
        barStyle: {
          radius: [4, 4, 0, 0]
        }
      };

      return (
        <div className="material-confidence-chart" style={{ marginTop: '2rem' }}>
          <h6 style={{ marginBottom: '1rem', fontWeight: 700, color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Target size={18} />
            Material Confidence Analysis
          </h6>
          <Bar {...config} />
        </div>
      );
    } catch (error) {
      console.error('Error rendering Material Confidence Chart:', error);
      return null;
    }
  };

  return (
    <div className="content-area">
      {error && (
        <div className="alert alert-error" style={{ marginBottom: '2rem' }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {!file && !loading && !results && (
        <div className="card">
          <div className="card-header">
            <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
              <Camera size={28} />
              Upload Image for Analysis
            </h2>
            <p className="mb-1" style={{ color: 'var(--secondary)', marginTop: '0.25rem' }}>
              Comprehensive structural analysis including crack detection, biological growth, material classification, and environmental impact assessment
            </p>
          </div>
          <div className="card-body">
            <div className="upload-zone" onClick={() => fileInputRef.current?.click()}>
              <Upload size={64} style={{ color: 'var(--primary)', marginBottom: '1rem' }} />
              <h3 style={{ marginBottom: '0.5rem', color: 'var(--dark)' }}>Click to Upload Image</h3>
              <p style={{ color: 'var(--secondary)', marginBottom: '1rem' }}>
                PNG, JPG, JPEG • Max 10MB
              </p>
              <p style={{ color: 'var(--secondary)', fontSize: '0.875rem' }}>
                Comprehensive structural analysis including crack detection, biological growth,<br />
                material classification, and environmental impact assessment
              </p>
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                onChange={handleFileChange}
                style={{ display: 'none' }}
              />
            </div>
          </div>
        </div>
      )}

      {file && !loading && !results && (
        <div className="card">
          <div className="card-header">
            <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
              <Camera size={28} />
              Image Preview & Settings
            </h2>
          </div>
          <div className="card-body">
            <div style={{ position: 'relative', marginBottom: '2rem' }}>
              <img src={preview} alt="Preview" className="preview-image" />
            </div>

            {/* Analysis Settings */}
            <div className="settings-section" style={{ marginBottom: '2rem', padding: '1.5rem', background: 'var(--light)', borderRadius: 'var(--border-radius)', border: '1px solid var(--glass-border)' }}>
              <h4 style={{ margin: '0 0 1rem 0', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Activity size={20} />
                Analysis Settings
              </h4>

              <div className="settings-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1.5rem' }}>
                <div className="setting-item">
                  <label style={{ display: 'block', fontWeight: 600, color: 'var(--dark)', marginBottom: '0.5rem' }}>
                    Pixel to CM Ratio
                  </label>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <input
                      type="range"
                      min="0.01"
                      max="1.0"
                      step="0.01"
                      value={settings.pixelToCmRatio}
                      onChange={(e) => setSettings(prev => ({ ...prev, pixelToCmRatio: parseFloat(e.target.value) }))}
                      style={{ flex: 1 }}
                    />
                    <span style={{ fontSize: '0.875rem', color: 'var(--secondary)', minWidth: '50px', textAlign: 'right' }}>
                      {settings.pixelToCmRatio.toFixed(2)}
                    </span>
                  </div>
                  <div style={{ fontSize: '0.75rem', color: 'var(--secondary)', marginTop: '0.25rem' }}>
                    Lower values = larger measurements
                  </div>
                </div>

                <div className="setting-item">
                  <label style={{ display: 'block', fontWeight: 600, color: 'var(--dark)', marginBottom: '0.5rem' }}>
                    Confidence Threshold
                  </label>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <input
                      type="range"
                      min="0.1"
                      max="0.9"
                      step="0.05"
                      value={settings.confidenceThreshold}
                      onChange={(e) => setSettings(prev => ({ ...prev, confidenceThreshold: parseFloat(e.target.value) }))}
                      style={{ flex: 1 }}
                    />
                    <span style={{ fontSize: '0.875rem', color: 'var(--secondary)', minWidth: '50px', textAlign: 'right' }}>
                      {(settings.confidenceThreshold * 100).toFixed(0)}%
                    </span>
                  </div>
                  <div style={{ fontSize: '0.75rem', color: 'var(--secondary)', marginTop: '0.25rem' }}>
                    Minimum confidence for detections
                  </div>
                </div>
              </div>
            </div>

            <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
              <button 
                className="btn-primary"
                onClick={handleAnalyze}
              >
                <Play size={20} style={{ marginRight: '0.5rem' }} />
                Start Analysis
              </button>
            </div>
          </div>
        </div>
      )}

      {loading && (
        <div className="card">
          <div className="card-body">
            <div className="progress-container" style={{ marginBottom: '2rem' }}>
              <div className="progress-bar-wrapper">
                <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
              </div>
              <div className="progress-text">
                <Loader size={16} className="spinning" style={{ display: 'inline-block', marginRight: '0.5rem' }} />
                Processing... {progress}%
              </div>
            </div>
          </div>
        </div>
      )}

      {results && !loading && (
        <div className="results-section">
          {/* VISUALIZATIONS FIRST - Priority Display */}
          {outputImages && (
            <div className="card" style={{ marginBottom: '2rem' }}>
              <div className="card-header">
                <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                  <PieChart size={24} />
                  Analysis Visualizations
                </h2>
                <p style={{ margin: '0.25rem 0 0 0', color: 'var(--secondary)', fontSize: '0.875rem' }}>
                  AI-powered image analysis results with detailed processing outputs
                </p>
              </div>
              <div className="card-body">
                <div className="image-grid" style={{ 
                  display: 'grid', 
                  gridTemplateColumns: 'repeat(3, 1fr)', 
                  gap: '1.5rem',
                  marginBottom: '1.5rem'
                }}>
                  {outputImages.original && (
                    <div className="image-card" style={{ padding: '1rem', background: 'var(--light)', borderRadius: 'var(--border-radius)', border: '1px solid var(--glass-border)' }}>
                      <div className="image-card-title" style={{ fontWeight: 600, marginBottom: '1rem', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        📸 Original Image
                      </div>
                      <img src={outputImages.original} alt="Original" style={{ width: '100%', borderRadius: 'var(--border-radius)', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }} />
                    </div>
                  )}
                  {outputImages.crack_detection && (
                    <div className="image-card" style={{ padding: '1rem', background: 'var(--light)', borderRadius: 'var(--border-radius)', border: '1px solid var(--glass-border)' }}>
                      <div className="image-card-title" style={{ fontWeight: 600, marginBottom: '1rem', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        🔍 Crack Detection
                        <span style={{ fontSize: '0.875rem', color: 'var(--secondary)', fontWeight: 'normal' }}>
                          ({results.crack_detection?.count || 0} detected)
                        </span>
                      </div>
                      <img src={outputImages.crack_detection} alt="Crack Detection" style={{ width: '100%', borderRadius: 'var(--border-radius)', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }} />
                    </div>
                  )}
                  {outputImages.biological_growth && (
                    <div className="image-card" style={{ padding: '1rem', background: 'var(--light)', borderRadius: 'var(--border-radius)', border: '1px solid var(--glass-border)' }}>
                      <div className="image-card-title" style={{ fontWeight: 600, marginBottom: '1rem', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        🌿 Biological Growth
                        <span style={{ fontSize: '0.875rem', color: 'var(--secondary)', fontWeight: 'normal' }}>
                          ({results.biological_growth?.growth_percentage?.toFixed(1)}% coverage)
                        </span>
                      </div>
                      <img src={outputImages.biological_growth} alt="Biological Growth" style={{ width: '100%', borderRadius: 'var(--border-radius)', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }} />
                    </div>
                  )}
                </div>
                
                {/* Second row with 2 centered images */}
                <div className="image-grid-second-row" style={{ 
                  display: 'grid', 
                  gridTemplateColumns: 'repeat(2, 1fr)', 
                  gap: '1.5rem',
                  maxWidth: '66.666%',
                  margin: '0 auto'
                }}>
                  {outputImages.segmentation && (
                    <div className="image-card" style={{ padding: '1rem', background: 'var(--light)', borderRadius: 'var(--border-radius)', border: '1px solid var(--glass-border)' }}>
                      <div className="image-card-title" style={{ fontWeight: 600, marginBottom: '1rem', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        🎯 AI Segmentation
                      </div>
                      <img src={outputImages.segmentation} alt="Segmentation" style={{ width: '100%', borderRadius: 'var(--border-radius)', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }} />
                    </div>
                  )}
                  {outputImages.depth_estimation && (
                    <div className="image-card" style={{ padding: '1rem', background: 'var(--light)', borderRadius: 'var(--border-radius)', border: '1px solid var(--glass-border)' }}>
                      <div className="image-card-title" style={{ fontWeight: 600, marginBottom: '1rem', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        📊 Depth Analysis
                      </div>
                      <img src={outputImages.depth_estimation} alt="Depth Estimation" style={{ width: '100%', borderRadius: 'var(--border-radius)', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }} />
                    </div>
                  )}
                </div>
              </div>
            </div>
          )}

          {/* Dynamic Analytics Dashboard */}
          <div className="card" style={{ marginBottom: '2rem' }}>
            <div className="card-header">
              <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                <BarChart3 size={24} />
                Dynamic Analytics Dashboard
              </h2>
              <p style={{ margin: '0.25rem 0 0 0', color: 'var(--secondary)', fontSize: '0.875rem' }}>
                Real-time analysis metrics based on your uploaded image
              </p>
            </div>
            <div className="card-body">
              {/* Key Performance Indicators */}
              <div className="kpi-section" style={{ marginBottom: '2rem' }}>
                <h4 style={{ marginBottom: '1rem', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <TrendingUp size={20} />
                  Key Performance Indicators
                </h4>
                <div className="metrics-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
                  <MetricCard
                    icon={CheckCircle}
                    title="Structural Health"
                    value={`${results.data_science_insights?.statistical_summary?.structural_health_score?.toFixed(1) || 'N/A'}/100`}
                    subtitle="Overall condition"
                    color={results.data_science_insights?.statistical_summary?.structural_health_score > 70 ? 'success' : results.data_science_insights?.statistical_summary?.structural_health_score > 40 ? 'warning' : 'danger'}
                  />
                  <MetricCard
                    icon={AlertTriangle}
                    title="Risk Level"
                    value={results.data_science_insights?.predictive_analytics?.risk_assessment || 'Low'}
                    subtitle="Based on analysis"
                    color={results.data_science_insights?.predictive_analytics?.risk_assessment === 'Critical' ? 'danger' : results.data_science_insights?.predictive_analytics?.risk_assessment === 'Moderate' ? 'warning' : 'success'}
                  />
                  <MetricCard
                    icon={Leaf}
                    title="Sustainability"
                    value={`${results.environmental_impact_assessment?.sustainability_score?.toFixed(1) || 'N/A'}/10`}
                    subtitle="Environmental rating"
                    color={results.environmental_impact_assessment?.sustainability_score > 7 ? 'success' : results.environmental_impact_assessment?.sustainability_score > 4 ? 'warning' : 'danger'}
                  />
                  <MetricCard
                    icon={Activity}
                    title="Maintenance Urgency"
                    value={results.data_science_insights?.statistical_summary?.maintenance_urgency || 'Low'}
                    subtitle="Recommended action"
                    color={results.data_science_insights?.statistical_summary?.maintenance_urgency === 'High' ? 'danger' : results.data_science_insights?.statistical_summary?.maintenance_urgency === 'Medium' ? 'warning' : 'success'}
                  />
                </div>
              </div>

              {/* Material Analysis with Dynamic Confidence Chart */}
              <div className="material-analysis-section" style={{ marginBottom: '2rem' }}>
                <h4 style={{ marginBottom: '1rem', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <Target size={20} />
                  Material Analysis & Classification
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
                  <div className="material-metrics">
                    <div className="metrics-grid" style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '1rem' }}>
                      <MetricCard
                        icon={Activity}
                        title="Primary Material"
                        value={results.material_analysis?.predicted_material || 'Unknown'}
                        subtitle={`Confidence: ${results.material_analysis?.confidence?.toFixed(1)}%`}
                        color="primary"
                      />
                      <MetricCard
                        icon={BarChart3}
                        title="Material Density"
                        value={results.material_analysis?.material_properties?.density || 'N/A'}
                        subtitle="g/cm³"
                        color="info"
                      />
                      <MetricCard
                        icon={TrendingUp}
                        title="Durability Score"
                        value={results.material_analysis?.material_properties?.durability_score || 'N/A'}
                        subtitle="/10"
                        color="success"
                      />
                      <MetricCard
                        icon={Leaf}
                        title="Environmental Impact"
                        value={results.material_analysis?.material_properties?.environmental_rating || 'N/A'}
                        subtitle="Eco-rating"
                        color="warning"
                      />
                    </div>
                  </div>
                  <div className="material-confidence-viz">
                    <MaterialConfidenceChart materialData={results.material_analysis} />
                  </div>
                </div>
              </div>

              {/* Environmental Impact with Dynamic Values */}
              <div className="environmental-impact-section">
                <h4 style={{ marginBottom: '1rem', color: 'var(--dark)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <Wind size={20} />
                  Environmental Impact Assessment
                </h4>
                <div className="metrics-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
                  <MetricCard
                    icon={Wind}
                    title="Carbon Footprint"
                    value={`${results.environmental_impact_assessment?.carbon_footprint_kg?.toFixed(2)} kg`}
                    subtitle="CO₂ Equivalent"
                    color="danger"
                  />
                  <MetricCard
                    icon={Droplet}
                    title="Water Footprint"
                    value={`${results.environmental_impact_assessment?.water_footprint_liters?.toFixed(2)} L`}
                    color="info"
                  />
                  <MetricCard
                    icon={Zap}
                    title="Energy Consumption"
                    value={`${results.environmental_impact_assessment?.energy_consumption_kwh?.toFixed(2)} kWh`}
                    color="warning"
                  />
                  <MetricCard
                    icon={Leaf}
                    title="Eco-Efficiency"
                    value={`${results.environmental_impact_assessment?.eco_efficiency_rating?.toFixed(1)}/10`}
                    subtitle="Efficiency rating"
                    color="success"
                  />
                </div>

                {/* Environmental Recommendations */}
                {results.environmental_impact_assessment?.recommendations && (
                  <div className="recommendations-section" style={{ marginTop: '2rem' }}>
                    <h6 style={{ marginBottom: '1rem', fontWeight: 700, color: 'var(--dark)' }}>Environmental Recommendations</h6>
                    <div className="recommendations-list" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1rem' }}>
                      {results.environmental_impact_assessment.recommendations.map((rec, idx) => (
                        <div key={idx} style={{
                          padding: '1rem',
                          background: 'var(--light)',
                          borderRadius: 'var(--border-radius)',
                          border: '1px solid var(--glass-border)',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '0.75rem'
                        }}>
                          <CheckCircle size={18} style={{ color: 'var(--primary)', flexShrink: 0 }} />
                          <span style={{ fontSize: '0.875rem', color: 'var(--dark)' }}>{rec}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Detailed Analysis Sections */}
          <div className="detailed-analysis" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))', gap: '2rem' }}>
            {/* Crack Detection Details */}
            <div className="card">
              <div className="card-header">
                <h3 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                  <AlertTriangle size={20} />
                  Crack Detection Details
                </h3>
              </div>
              <div className="card-body">
                <div className="metrics-grid" style={{ marginBottom: '1.5rem' }}>
                  <MetricCard
                    icon={AlertTriangle}
                    title="Total Cracks"
                    value={results.crack_detection?.count || 0}
                    color="danger"
                  />
                  <MetricCard
                    icon={BarChart3}
                    title="Total Area"
                    value={`${results.crack_detection?.statistics?.total_area_cm2?.toFixed(2) || 0} cm²`}
                    color="warning"
                  />
                  <MetricCard
                    icon={TrendingUp}
                    title="Average Size"
                    value={`${results.crack_detection?.statistics?.average_size_cm2?.toFixed(2) || 0} cm²`}
                    color="info"
                  />
                </div>

                {results.crack_detection?.details?.length > 0 && (
                  <div className="crack-details">
                    <h6 style={{ marginBottom: '1rem', fontWeight: 700, color: 'var(--dark)' }}>
                      Detected Cracks ({results.crack_detection.details.length})
                    </h6>
                    <div style={{ maxHeight: '300px', overflowY: 'auto' }}>
                      {results.crack_detection.details.slice(0, 10).map((crack, idx) => (
                        <div key={idx} className="crack-item" style={{
                          marginBottom: '0.75rem',
                          padding: '0.75rem',
                          background: 'var(--light)',
                          borderRadius: 'var(--border-radius)',
                          border: '1px solid #e5e7eb',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center'
                        }}>
                          <span style={{ fontWeight: 600, color: 'var(--dark)' }}>
                            Crack {idx + 1}: {crack.width_cm?.toFixed(2)} × {crack.length_cm?.toFixed(2)} cm
                          </span>
                          <SeverityBadge severity={crack.severity} />
                        </div>
                      ))}
                      {results.crack_detection.details.length > 10 && (
                        <div style={{ textAlign: 'center', padding: '1rem', color: 'var(--secondary)', fontSize: '0.875rem' }}>
                          ... and {results.crack_detection.details.length - 10} more cracks detected
                        </div>
                      )}
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Biological Growth Details */}
            <div className="card">
              <div className="card-header">
                <h3 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                  <Leaf size={20} />
                  Biological Growth Analysis
                </h3>
              </div>
              <div className="card-body">
                <div className="metrics-grid">
                  <MetricCard
                    icon={Leaf}
                    title="Growth Detected"
                    value={results.biological_growth?.growth_detected ? 'Yes' : 'No'}
                    color={results.biological_growth?.growth_detected ? 'warning' : 'success'}
                  />
                  <MetricCard
                    icon={BarChart3}
                    title="Coverage Area"
                    value={`${results.biological_growth?.growth_percentage?.toFixed(2)}%`}
                    color="success"
                  />
                  <MetricCard
                    icon={TrendingUp}
                    title="Affected Area"
                    value={`${results.biological_growth?.affected_area_cm2?.toFixed(2)} cm²`}
                    color="info"
                  />
                </div>

                {/* Growth Trend Visualization */}
                {results.biological_growth?.growth_percentage > 0 && (
                  <div className="growth-trend" style={{ marginTop: '2rem' }}>
                    <h6 style={{ marginBottom: '1rem', fontWeight: 700, color: 'var(--dark)' }}>Growth Coverage Trend</h6>
                    <div style={{
                      width: '100%',
                      height: '60px',
                      background: 'linear-gradient(90deg, var(--success), var(--warning), var(--danger))',
                      borderRadius: '30px',
                      position: 'relative',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center'
                    }}>
                      <div style={{
                        position: 'absolute',
                        left: `${Math.min(results.biological_growth.growth_percentage, 100)}%`,
                        transform: 'translateX(-50%)',
                        width: '4px',
                        height: '40px',
                        background: 'var(--dark)',
                        borderRadius: '2px'
                      }} />
                      <span style={{
                        color: 'white',
                        fontWeight: 'bold',
                        textShadow: '0 0 4px rgba(0,0,0,0.5)',
                        zIndex: 1
                      }}>
                        {results.biological_growth.growth_percentage.toFixed(1)}%
                      </span>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '0.5rem', fontSize: '0.75rem', color: 'var(--secondary)' }}>
                      <span>0%</span>
                      <span>50%</span>
                      <span>100%</span>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="card" style={{ marginTop: '2rem' }}>
            <div className="card-body">
              <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', flexWrap: 'wrap' }}>
                <button
                  className="btn-primary"
                  onClick={() => {
                    setFile(null);
                    setPreview(null);
                    setResults(null);
                    setOutputImages(null);
                    setError(null);
                    clearAnalysis(); // Clear from context as well
                  }}
                >
                  <Upload size={18} style={{ marginRight: '0.5rem' }} />
                  Analyze Another Image
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {preview && !results && !loading && (
        <div className="card">
          <div className="card-header">
            <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
              <Camera size={24} />
              Image Preview
            </h2>
          </div>
          <div className="card-body">
            <img src={preview} alt="Preview" className="preview-image" />
          </div>
        </div>
      )}
    </div>
  );
};

export default ImageAnalysis;