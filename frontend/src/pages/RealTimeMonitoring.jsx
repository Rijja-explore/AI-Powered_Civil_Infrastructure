import React, { useState, useEffect, useRef } from 'react';
import { 
  Activity, 
  Video, 
  Wifi,
  TrendingUp,
  Settings,
  AlertTriangle,
  Maximize2,
  PauseCircle,
  Play,
  RefreshCw
} from 'lucide-react';

const RealTimeMonitoring = () => {
  const [isStreaming, setIsStreaming] = useState(false);
  const [streamUrl, setStreamUrl] = useState(null);
  const [error, setError] = useState(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [metrics, setMetrics] = useState({
    fps: 0,
    detections: 0,
    processingTime: 0,
    lastUpdate: new Date(),
    biological_growth_detected: false,
    biological_growth_area: 0,
    material: 'Unknown',
    frame_number: 0
  });
  const [cameraConnected, setCameraConnected] = useState(false);

  const containerRef = useRef(null);
  const streamRef = useRef(null);

  const connectToCamera = async () => {
    try {
      const response = await fetch('http://localhost:5002/api/connect_camera', {
        method: 'POST'
      });
      const data = await response.json();
      
      if (data.success) {
        setCameraConnected(true);
        setError(null);
        // Show success message or update UI
      } else {
        setError('Failed to connect to camera');
      }
    } catch (err) {
      setError('Could not connect to camera: ' + err.message);
    }
  };

  const disconnectCamera = async () => {
    try {
      await fetch('http://localhost:5002/api/disconnect_camera', {
        method: 'POST'
      });
      setCameraConnected(false);
    } catch (err) {
      setError('Error disconnecting camera: ' + err.message);
    }
  };

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      containerRef.current.requestFullscreen();
      setIsFullscreen(true);
    } else {
      document.exitFullscreen();
      setIsFullscreen(false);
    }
  };

  const startStream = async () => {
    try {
      const response = await fetch('http://localhost:5002/api/start_stream', {
        method: 'POST'
      });
      const data = await response.json();
      
      if (data.stream_url) {
        setStreamUrl(data.stream_url);
        setIsStreaming(true);
        setError(null);
      } else {
        setError('Failed to start video stream');
      }
    } catch (err) {
      setError('Could not connect to camera stream: ' + err.message);
    }
  };

  const stopStream = async () => {
    try {
      await fetch('http://localhost:5002/api/stop_stream', {
        method: 'POST'
      });
      setIsStreaming(false);
      setStreamUrl(null);
    } catch (err) {
      setError('Error stopping stream: ' + err.message);
    }
  };

  useEffect(() => {
    let metricsInterval;
    
    if (isStreaming) {
      metricsInterval = setInterval(async () => {
        try {
          const response = await fetch('http://localhost:5002/api/stream_metrics');
          const data = await response.json();
          setMetrics(prevMetrics => ({
            ...prevMetrics,
            ...data,
            lastUpdate: new Date()
          }));
        } catch (err) {
          console.error('Error fetching metrics:', err);
        }
      }, 1000);
    }

    return () => {
      if (metricsInterval) {
        clearInterval(metricsInterval);
      }
    };
  }, [isStreaming]);

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

  return (
    <div className="content-area" ref={containerRef}>
      {error && (
        <div className="alert alert-error" style={{ marginBottom: '2rem' }}>
          <AlertTriangle size={18} style={{ marginRight: '0.5rem' }} />
          {error}
          <button className="close-btn" onClick={() => setError(null)} style={{ marginLeft: '1rem', background: 'none', border: 'none', color: 'var(--danger)', cursor: 'pointer', fontSize: '1.2rem' }}>×</button>
        </div>
      )}

      <div className="page-header">
        <h1>
          <Activity className="inline-icon" size={32} />
          Real-Time Infrastructure Monitoring
        </h1>
        <p>Live camera feed with AI-powered structural health analysis and continuous monitoring</p>
      </div>

      <div className="monitoring-grid">
        <div className="card">
          <div className="card-header">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                <Video size={24} />
                Live Stream
              </h2>
              <div style={{ display: 'flex', gap: '0.5rem' }}>
                <button className="btn btn-secondary" onClick={toggleFullscreen} style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}>
                  <Maximize2 size={16} style={{ marginRight: '0.25rem' }} />
                  {isFullscreen ? 'Exit' : 'Fullscreen'}
                </button>
                <button className="btn btn-secondary" style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}>
                  <Settings size={16} style={{ marginRight: '0.25rem' }} />
                  Settings
                </button>
              </div>
            </div>
          </div>
          <div className="card-body">
            <div className="stream-container" ref={streamRef} style={{ marginBottom: '2rem' }}>
              {isStreaming && streamUrl ? (
                <img
                  src={streamUrl}
                  alt="Live stream"
                  className="stream-feed"
                />
              ) : (
                <div className="stream-placeholder">
                  <Video size={48} />
                  <p>Stream not active</p>
                  <button 
                    className="btn-primary"
                    onClick={startStream}
                    style={{ marginTop: '1rem' }}
                  >
                    <Play size={20} style={{ marginRight: '0.5rem' }} />
                    Start Stream
                  </button>
                </div>
              )}
            </div>
            {isStreaming && (
              <div className="stream-controls" style={{ display: 'flex', justifyContent: 'center', flexDirection: 'column', gap: '1rem' }}>
                <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem' }}>
                  <button 
                    className="btn btn-danger"
                    onClick={stopStream}
                  >
                    <PauseCircle size={20} style={{ marginRight: '0.5rem' }} />
                    Stop Stream
                  </button>
                  <div className="stream-status" style={{ marginLeft: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--secondary)' }}>
                    <Wifi size={18} style={{ color: isStreaming ? 'var(--success)' : 'var(--secondary)' }} />
                    Status: {isStreaming ? 'Active' : 'Inactive'}
                  </div>
                </div>

                {/* Camera Connection Controls */}
                <div className="camera-controls" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '1rem', padding: '1rem', background: 'var(--light)', borderRadius: 'var(--border-radius)', border: '1px solid var(--glass-border)' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <div style={{
                      width: '12px',
                      height: '12px',
                      borderRadius: '50%',
                      background: cameraConnected ? 'var(--success)' : 'var(--secondary)',
                      boxShadow: cameraConnected ? '0 0 8px rgba(16, 185, 129, 0.4)' : 'none'
                    }} />
                    <span style={{ fontSize: '0.875rem', color: 'var(--secondary)' }}>
                      Camera: {cameraConnected ? 'Connected' : 'Disconnected'}
                    </span>
                  </div>

                  {!cameraConnected ? (
                    <button
                      className="btn-primary"
                      onClick={connectToCamera}
                      style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}
                    >
                      <Video size={16} style={{ marginRight: '0.5rem' }} />
                      Connect Camera
                    </button>
                  ) : (
                    <button
                      className="btn btn-secondary"
                      onClick={disconnectCamera}
                      style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}
                    >
                      <Video size={16} style={{ marginRight: '0.5rem' }} />
                      Disconnect Camera
                    </button>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="results-sidebar">
          <div className="card">
            <div className="card-header">
              <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                <Activity size={24} />
                Live Metrics
              </h2>
            </div>
            <div className="card-body">
              <div className="metrics-grid">
                <MetricCard
                  icon={Activity}
                  title="FPS"
                  value={metrics.fps.toFixed(1)}
                  color="primary"
                />
                <MetricCard
                  icon={AlertTriangle}
                  title="Crack Detections"
                  value={metrics.detections}
                  color="warning"
                />
                <MetricCard
                  icon={TrendingUp}
                  title="Processing Time"
                  value={`${metrics.processingTime.toFixed(2)}ms`}
                  color="success"
                />
                <MetricCard
                  icon={RefreshCw}
                  title="Biological Growth"
                  value={metrics.biological_growth_detected ? `${metrics.biological_growth_area.toFixed(0)}px` : 'None'}
                  color={metrics.biological_growth_detected ? 'danger' : 'success'}
                />
                <MetricCard
                  icon={Activity}
                  title="Material Type"
                  value={metrics.material}
                  color="info"
                />
                <MetricCard
                  icon={RefreshCw}
                  title="Frame Number"
                  value={metrics.frame_number}
                  subtitle="Processed"
                  color="secondary"
                />
              </div>
            </div>
          </div>

          <div className="card" style={{ marginTop: '2rem' }}>
            <div className="card-header">
              <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                <Activity size={24} />
                Recent Detections
              </h2>
            </div>
            <div className="card-body">
              <div className="detection-history" style={{ maxHeight: '300px', overflowY: 'auto', paddingRight: '0.5rem' }}>
                {/* Add detection history items here */}
                <div style={{ textAlign: 'center', color: 'var(--secondary)', padding: '2rem' }}>
                  No recent detections
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RealTimeMonitoring;
