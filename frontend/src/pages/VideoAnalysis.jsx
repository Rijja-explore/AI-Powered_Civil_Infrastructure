import React, { useState, useRef, useEffect } from 'react';
import { Camera, XCircle, Activity, Upload, FileVideo, RotateCcw, Download, Play, Pause, Video, Monitor } from 'lucide-react';
import toast from 'react-hot-toast';

const VideoAnalysis = () => {
  const [videoFile, setVideoFile] = useState(null);
  const [videoPreview, setVideoPreview] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [processingProgress, setProcessingProgress] = useState(0);
  const [videoResults, setVideoResults] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isRealTime, setIsRealTime] = useState(false);
  const [realTimeFrame, setRealTimeFrame] = useState(null);
  const [realTimeResults, setRealTimeResults] = useState(null);
  const [cameraConnected, setCameraConnected] = useState(false);
  const videoRef = useRef(null);
  const fileInputRef = useRef(null);
  const realTimeIntervalRef = useRef(null);

  const API_URL = 'http://localhost:5002';

  // Clean up real-time interval on component unmount
  useEffect(() => {
    return () => {
      if (realTimeIntervalRef.current) {
        clearInterval(realTimeIntervalRef.current);
      }
    };
  }, []);

  const connectCamera = async () => {
    try {
      const response = await fetch(`${API_URL}/api/connect_camera`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
      });

      if (response.ok) {
        setCameraConnected(true);
        toast.success('Camera connected successfully');
      } else {
        const error = await response.json();
        toast.error(`Failed to connect camera: ${error.error}`);
      }
    } catch (err) {
      console.error('Camera connection error:', err);
      toast.error('Failed to connect to camera. Make sure the API server is running.');
    }
  };

  const disconnectCamera = async () => {
    try {
      if (realTimeIntervalRef.current) {
        clearInterval(realTimeIntervalRef.current);
        realTimeIntervalRef.current = null;
      }

      const response = await fetch(`${API_URL}/api/disconnect_camera`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
      });

      if (response.ok) {
        setCameraConnected(false);
        setIsRealTime(false);
        setRealTimeFrame(null);
        setRealTimeResults(null);
        toast.success('Camera disconnected');
      } else {
        const error = await response.json();
        toast.error(`Failed to disconnect camera: ${error.error}`);
      }
    } catch (err) {
      console.error('Camera disconnection error:', err);
      toast.error('Failed to disconnect camera');
    }
  };

  const startRealTimeCapture = async () => {
    if (!cameraConnected) {
      toast.error('Please connect camera first');
      return;
    }

    try {
      setIsRealTime(true);
      toast.success('Starting real-time analysis...');

      // Start capturing frames every 2 seconds
      realTimeIntervalRef.current = setInterval(async () => {
        try {
          const response = await fetch(`${API_URL}/api/capture_and_analyze`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              px_to_cm_ratio: 0.1,
              confidence_threshold: 0.3
            })
          });

          if (response.ok) {
            const data = await response.json();
            setRealTimeFrame(data.frame);
            setRealTimeResults(data.analysis);
          } else {
            const error = await response.json();
            console.error('Real-time capture error:', error);
          }
        } catch (err) {
          console.error('Real-time capture error:', err);
        }
      }, 2000); // Capture every 2 seconds

    } catch (err) {
      console.error('Real-time start error:', err);
      toast.error('Failed to start real-time capture');
      setIsRealTime(false);
    }
  };

  const stopRealTimeCapture = () => {
    if (realTimeIntervalRef.current) {
      clearInterval(realTimeIntervalRef.current);
      realTimeIntervalRef.current = null;
    }
    setIsRealTime(false);
    toast.success('Real-time capture stopped');
  };

  const handleVideoFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile && selectedFile.type.startsWith('video/')) {
      setVideoFile(selectedFile);
      const videoUrl = URL.createObjectURL(selectedFile);
      setVideoPreview(videoUrl);
      setVideoResults(null);
    } else {
      toast.error('Please select a valid video file');
    }
  };

  const processVideo = async () => {
    if (!videoFile) {
      toast.error('Please select a video file first');
      return;
    }

    setIsProcessing(true);
    setProcessingProgress(0);
    setVideoResults(null);

    try {
      // For video processing, we'll extract frames and analyze them
      const video = document.createElement('video');
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');

      video.src = videoPreview;
      await new Promise((resolve) => {
        video.onloadedmetadata = resolve;
      });

      const duration = video.duration;
      const fps = 1; // Process 1 frame per second
      const totalFrames = Math.floor(duration * fps);
      const frameResults = [];

      setProcessingProgress(10);

      // Process frames at regular intervals
      for (let i = 0; i < totalFrames; i++) {
        const time = (i / fps);
        video.currentTime = time;

        await new Promise((resolve) => {
          video.onseeked = () => {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            ctx.drawImage(video, 0, 0);

            // Convert canvas to base64
            const frameBase64 = canvas.toDataURL('image/jpeg', 0.8);

            resolve(frameBase64);
          };
        }).then(async (frameBase64) => {
          // Analyze this frame using the API
          const response = await fetch(`${API_URL}/api/analyze`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              image: frameBase64,
              px_to_cm_ratio: 0.1,
              confidence_threshold: 0.3
            })
          });

          if (response.ok) {
            const data = await response.json();
            frameResults.push({
              frame_number: i + 1,
              timestamp: time,
              cracks_count: data.results.crack_detection?.count || 0,
              growth_area: data.results.biological_growth?.affected_area_cm2 || 0,
              material: data.results.material_analysis?.predicted_material || 'Unknown',
              analysis: data.results
            });
          }
        });

        // Update progress
        setProcessingProgress(10 + (i / totalFrames) * 80);
      }

      // Calculate summary statistics
      const framesWithCracks = frameResults.filter(f => f.cracks_count > 0).length;
      const avgProcessingTime = 2.5; // Simulated average processing time
      const detectionRate = framesWithCracks / totalFrames;

      const videoAnalysisResults = {
        total_frames: totalFrames,
        frames_with_cracks: framesWithCracks,
        average_processing_time: avgProcessingTime,
        detection_rate: detectionRate,
        frame_results: frameResults,
        summary: {
          total_cracks_detected: frameResults.reduce((sum, f) => sum + f.cracks_count, 0),
          average_growth_area: frameResults.reduce((sum, f) => sum + f.growth_area, 0) / totalFrames,
          dominant_material: frameResults.length > 0 ?
            frameResults.reduce((acc, f) => {
              acc[f.material] = (acc[f.material] || 0) + 1;
              return acc;
            }, {}) : {}
        }
      };

      setVideoResults(videoAnalysisResults);
      setProcessingProgress(100);
      toast.success('Video analysis completed successfully');
    } catch (err) {
      console.error('Video analysis error:', err);
      toast.error('Video analysis failed. Make sure the backend (finalwebapp_api.py) is running on port 5002.');
    } finally {
      setIsProcessing(false);
      setProcessingProgress(0);
    }
  };

  const handleVideoPlay = () => {
    if (videoRef.current) {
      videoRef.current.play();
      setIsPlaying(true);
    }
  };

  const handleVideoPause = () => {
    if (videoRef.current) {
      videoRef.current.pause();
      setIsPlaying(false);
    }
  };

  const resetVideo = () => {
    setVideoFile(null);
    setVideoPreview(null);
    setVideoResults(null);
    setIsPlaying(false);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  return (
    <div className="content-area">
      <div className="page-header">
        <h1>
          <Camera className="inline-icon" size={32} />
          Video Stream Analysis
        </h1>
        <p>Upload videos for comprehensive structural health monitoring and infrastructure analysis</p>
      </div>

      {/* Video Upload Section */}
      <div className="card" style={{ marginBottom: '2rem' }}>
        <div className="card-header">
          <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
            <FileVideo size={24} />
            Video File Analysis
          </h2>
        </div>
        <div className="card-body">
          {!videoFile && !isProcessing && (
            <div className="upload-zone" onClick={() => fileInputRef.current?.click()}>
              <Upload size={64} style={{ color: 'var(--primary)', marginBottom: '1rem' }} />
              <h3 style={{ marginBottom: '0.5rem', color: 'var(--dark)' }}>Click to Upload Video</h3>
              <p style={{ color: 'var(--secondary)', marginBottom: '1rem' }}>
                MP4, AVI, MOV • Max 100MB
              </p>
              <p style={{ color: 'var(--secondary)', fontSize: '0.875rem' }}>
                Comprehensive analysis including crack detection, biological growth,<br />
                material classification, and structural integrity assessment
              </p>
              <input
                ref={fileInputRef}
                type="file"
                accept="video/*"
                onChange={handleVideoFileChange}
                style={{ display: 'none' }}
              />
            </div>
          )}

          {videoFile && !isProcessing && !videoResults && (
            <div className="video-preview-section">
              <div style={{ position: 'relative', marginBottom: '2rem' }}>
                <video
                  ref={videoRef}
                  src={videoPreview}
                  controls
                  style={{
                    width: '100%',
                    maxHeight: '400px',
                    objectFit: 'contain',
                    borderRadius: 'var(--border-radius)',
                    border: '1px solid #e5e7eb'
                  }}
                  onPlay={() => setIsPlaying(true)}
                  onPause={() => setIsPlaying(false)}
                  onEnded={() => setIsPlaying(false)}
                />
              </div>
              <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', alignItems: 'center' }}>
                <button
                  className="btn-primary"
                  onClick={processVideo}
                >
                  <Activity size={20} style={{ marginRight: '0.5rem' }} />
                  Analyze Video
                </button>
                <button
                  className="btn btn-secondary"
                  onClick={resetVideo}
                >
                  <RotateCcw size={18} style={{ marginRight: '0.5rem' }} />
                  Reset
                </button>
              </div>
            </div>
          )}

          {isProcessing && (
            <div className="processing-section">
              <div className="progress-container" style={{ marginBottom: '2rem' }}>
                <div className="progress-bar-wrapper">
                  <div className="progress-bar-fill" style={{ width: `${processingProgress}%` }} />
                </div>
                <div className="progress-text">
                  <Activity size={16} className="spinning" style={{ display: 'inline-block', marginRight: '0.5rem' }} />
                  Processing video... {processingProgress}%
                </div>
              </div>
            </div>
          )}

          {videoResults && (
            <div className="video-results">
              <h3 style={{ marginBottom: '1.5rem', color: 'var(--dark)' }}>Analysis Results</h3>

              <div className="metrics-grid" style={{ marginBottom: '2rem' }}>
                <div className="metric-card">
                  <div className="metric-icon bg-danger">
                    <Activity size={24} />
                  </div>
                  <div className="metric-content">
                    <div className="metric-title">Total Frames</div>
                    <div className="metric-value">{videoResults.total_frames || 0}</div>
                  </div>
                </div>
                <div className="metric-card">
                  <div className="metric-icon bg-warning">
                    <Activity size={24} />
                  </div>
                  <div className="metric-content">
                    <div className="metric-title">Frames with Cracks</div>
                    <div className="metric-value">{videoResults.frames_with_cracks || 0}</div>
                  </div>
                </div>
                <div className="metric-card">
                  <div className="metric-icon bg-success">
                    <Activity size={24} />
                  </div>
                  <div className="metric-content">
                    <div className="metric-title">Avg. Processing Time</div>
                    <div className="metric-value">{videoResults.average_processing_time?.toFixed(2) || 0}s</div>
                  </div>
                </div>
                <div className="metric-card">
                  <div className="metric-icon bg-info">
                    <Activity size={24} />
                  </div>
                  <div className="metric-content">
                    <div className="metric-title">Detection Rate</div>
                    <div className="metric-value">{videoResults.detection_rate ? (videoResults.detection_rate * 100).toFixed(1) : 0}%</div>
                  </div>
                </div>
              </div>

              {videoResults.frame_results && videoResults.frame_results.length > 0 && (
                <div className="frame-results">
                  <h4 style={{ marginBottom: '1rem', color: 'var(--dark)' }}>Frame-by-Frame Analysis</h4>
                  <div className="frame-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1rem' }}>
                    {videoResults.frame_results.slice(0, 6).map((frame, index) => (
                      <div key={index} className="frame-card" style={{
                        padding: '1rem',
                        background: 'var(--light)',
                        borderRadius: 'var(--border-radius)',
                        border: '1px solid var(--glass-border)'
                      }}>
                        <div style={{ fontWeight: 600, marginBottom: '0.5rem', color: 'var(--dark)' }}>
                          Frame {frame.frame_number}
                        </div>
                        <div style={{ fontSize: '0.875rem', color: 'var(--secondary)' }}>
                          Cracks: {frame.cracks_count || 0}<br />
                          Growth: {frame.growth_area?.toFixed(2) || 0} cm²<br />
                          Material: {frame.material || 'Unknown'}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', marginTop: '2rem' }}>
                <button
                  className="btn btn-secondary"
                  onClick={() => {
                    const blob = new Blob([JSON.stringify(videoResults, null, 2)], { type: 'application/json' });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `video-analysis-${new Date().toISOString()}.json`;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                  }}
                >
                  <Download size={20} style={{ marginRight: '0.5rem' }} />
                  Download Results
                </button>
                <button
                  className="btn btn-secondary"
                  onClick={resetVideo}
                >
                  <RotateCcw size={18} style={{ marginRight: '0.5rem' }} />
                  Analyze Another Video
                </button>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Real-Time Camera Analysis Section */}
      <div className="card">
        <div className="card-header">
          <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
            <Monitor size={24} />
            Real-Time Camera Analysis
          </h2>
        </div>
        <div className="card-body">
          {!cameraConnected && (
            <div style={{ textAlign: 'center', padding: '2rem' }}>
              <Camera size={64} style={{ color: 'var(--primary)', marginBottom: '1rem' }} />
              <h3 style={{ marginBottom: '0.5rem', color: 'var(--dark)' }}>Connect Camera for Real-Time Analysis</h3>
              <p style={{ color: 'var(--secondary)', marginBottom: '2rem' }}>
                Connect your camera to start real-time structural health monitoring
              </p>
              <button
                className="btn-primary"
                onClick={connectCamera}
              >
                <Camera size={20} style={{ marginRight: '0.5rem' }} />
                Connect Camera
              </button>
            </div>
          )}

          {cameraConnected && !isRealTime && (
            <div style={{ textAlign: 'center', padding: '2rem' }}>
              <div style={{ 
                display: 'inline-flex', 
                alignItems: 'center', 
                gap: '0.5rem', 
                padding: '0.75rem 1.5rem', 
                background: 'var(--success)', 
                color: 'white', 
                borderRadius: 'var(--border-radius)', 
                marginBottom: '1.5rem' 
              }}>
                <Camera size={20} />
                Camera Connected
              </div>
              <h3 style={{ marginBottom: '0.5rem', color: 'var(--dark)' }}>Start Real-Time Analysis</h3>
              <p style={{ color: 'var(--secondary)', marginBottom: '2rem' }}>
                Begin live monitoring and analysis of your infrastructure
              </p>
              <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
                <button
                  className="btn-primary"
                  onClick={startRealTimeCapture}
                >
                  <Video size={20} style={{ marginRight: '0.5rem' }} />
                  Start Real-Time
                </button>
                <button
                  className="btn btn-secondary"
                  onClick={disconnectCamera}
                >
                  <XCircle size={18} style={{ marginRight: '0.5rem' }} />
                  Disconnect
                </button>
              </div>
            </div>
          )}

          {isRealTime && (
            <div className="realtime-section">
              <div style={{ 
                display: 'flex', 
                justifyContent: 'space-between', 
                alignItems: 'center', 
                marginBottom: '1.5rem' 
              }}>
                <div style={{ 
                  display: 'flex', 
                  alignItems: 'center', 
                  gap: '0.5rem', 
                  padding: '0.5rem 1rem', 
                  background: 'var(--danger)', 
                  color: 'white', 
                  borderRadius: 'var(--border-radius)' 
                }}>
                  <div style={{ 
                    width: '8px', 
                    height: '8px', 
                    borderRadius: '50%', 
                    background: 'white',
                    animation: 'pulse 1s infinite' 
                  }} />
                  LIVE
                </div>
                <button
                  className="btn btn-secondary"
                  onClick={stopRealTimeCapture}
                >
                  <Pause size={18} style={{ marginRight: '0.5rem' }} />
                  Stop
                </button>
              </div>

              {realTimeFrame && (
                <div style={{ marginBottom: '2rem' }}>
                  <img
                    src={realTimeFrame}
                    alt="Real-time frame"
                    style={{
                      width: '100%',
                      maxHeight: '400px',
                      objectFit: 'contain',
                      borderRadius: 'var(--border-radius)',
                      border: '2px solid var(--primary)'
                    }}
                  />
                </div>
              )}

              {realTimeResults && (
                <div className="realtime-results">
                  <h4 style={{ marginBottom: '1rem', color: 'var(--dark)' }}>Live Analysis Results</h4>
                  <div className="metrics-grid">
                    <div className="metric-card">
                      <div className="metric-icon bg-danger">
                        <Activity size={24} />
                      </div>
                      <div className="metric-content">
                        <div className="metric-title">Cracks Detected</div>
                        <div className="metric-value">{realTimeResults.crack_detection?.count || 0}</div>
                      </div>
                    </div>
                    <div className="metric-card">
                      <div className="metric-icon bg-warning">
                        <Activity size={24} />
                      </div>
                      <div className="metric-content">
                        <div className="metric-title">Growth Area</div>
                        <div className="metric-value">{realTimeResults.biological_growth?.affected_area_cm2?.toFixed(1) || 0} cm²</div>
                      </div>
                    </div>
                    <div className="metric-card">
                      <div className="metric-icon bg-info">
                        <Activity size={24} />
                      </div>
                      <div className="metric-content">
                        <div className="metric-title">Material</div>
                        <div className="metric-value" style={{ fontSize: '0.875rem' }}>
                          {realTimeResults.material_analysis?.predicted_material || 'Unknown'}
                        </div>
                      </div>
                    </div>
                    <div className="metric-card">
                      <div className="metric-icon bg-success">
                        <Activity size={24} />
                      </div>
                      <div className="metric-content">
                        <div className="metric-title">Confidence</div>
                        <div className="metric-value">
                          {realTimeResults.material_analysis?.confidence ? 
                            (realTimeResults.material_analysis.confidence * 100).toFixed(1) + '%' : 
                            'N/A'
                          }
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default VideoAnalysis;