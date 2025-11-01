import React, { useState, useEffect } from 'react';
import { BarChart, TrendingUp, AlertTriangle, Download } from 'lucide-react';
import { Line, Pie, Bar } from '@ant-design/plots';
import toast from 'react-hot-toast';

const Analytics = () => {
  const [dataType, setDataType] = useState('all'); // all, cracks, materials, environmental
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAnalytics();
  }, [dataType]);

  const fetchAnalytics = async () => {
    try {
      setLoading(true);
      const response = await fetch(`http://localhost:5002/analytics/dynamic?type=${dataType}`);
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ message: 'Failed to fetch analytics' }));
        throw new Error(errorData.message || 'Failed to fetch analytics');
      }

      const responseData = await response.json();
      
      // Validate response data structure
      if (!responseData || typeof responseData !== 'object') {
        throw new Error('Invalid data format received from server');
      }

      // Ensure required arrays exist
      const safeData = {
        ...responseData,
        trends: Array.isArray(responseData.trends) ? responseData.trends : [],
        severityDistribution: Array.isArray(responseData.severityDistribution) ? responseData.severityDistribution : [],
        materialDistribution: Array.isArray(responseData.materialDistribution) ? responseData.materialDistribution : [],
        keyFindings: Array.isArray(responseData.keyFindings) ? responseData.keyFindings : [],
        recommendations: Array.isArray(responseData.recommendations) ? responseData.recommendations : [],
      };

      setData(safeData);
    } catch (error) {
      console.error('Analytics fetch error:', error);
      toast.error(error.message || 'Failed to fetch analytics data');
      setData(null);
    } finally {
      setLoading(false);
    }
  };

  const downloadReport = async () => {
    try {
      const response = await fetch(`http://localhost:5002/analytics/report/dynamic?type=${dataType}`);
      if (!response.ok) throw new Error('Failed to generate report');
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `analytics-report-${dataType}-${new Date().toISOString()}.pdf`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Report download error:', error);
      toast.error('Failed to download report');
    }
  };

  const renderChart = () => {
    if (!data || typeof data !== 'object') return null;

    // Validate data structure
    const hasValidData = {
      trends: Array.isArray(data.trends) && data.trends.length > 0,
      severity: Array.isArray(data.severityDistribution) && data.severityDistribution.length > 0,
      materials: Array.isArray(data.materialDistribution) && data.materialDistribution.length > 0
    };

    const defaultChartStyle = {
      label: {
        style: {
          fill: '#64748b',
          fontSize: 12
        }
      },
      grid: {
        line: {
          style: {
            stroke: 'rgba(226, 232, 240, 0.5)',
            lineDash: [4, 4]
          }
        }
      }
    };

    const trendConfig = hasValidData.trends ? {
      data: data.trends,
      xField: 'date',
      yField: 'value',
      seriesField: 'metric',
      smooth: true,
      animation: true,
      legend: { position: 'top' },
      xAxis: { 
        type: 'timeCat', 
        tickCount: 5,
        ...defaultChartStyle.label
      },
      yAxis: { 
        label: { 
          formatter: (v) => `${v}%`,
          ...defaultChartStyle.label.style
        },
        grid: defaultChartStyle.grid
      },
      color: ['#60a5fa', '#818cf8', '#22d3ee', '#38bdf8'],
    } : null;

    const severityConfig = hasValidData.severity ? {
      data: data.severityDistribution,
      angleField: 'value',
      colorField: 'type',
      radius: 0.8,
      label: { 
        type: 'outer',
        ...defaultChartStyle.label
      },
      color: ['#60a5fa', '#22d3ee', '#ef4444', '#f59e0b'],
      interactions: [{ type: 'element-active' }],
      statistic: {
        title: {
          style: {
            fontSize: '16px',
            color: '#1e293b'
          }
        },
        content: {
          style: {
            fontSize: '24px',
            color: '#3b82f6',
            fontWeight: 600
          }
        }
      }
    } : null;

    const materialConfig = hasValidData.materials ? {
      data: data.materialDistribution,
      xField: 'material',
      yField: 'count',
      color: ['l(90) 0:#60a5fa 1:#3b82f6'],
      label: {
        position: 'middle',
        style: { 
          fill: '#FFFFFF',
          opacity: 0.8,
          fontSize: 12,
          fontWeight: 500
        }
      },
      xAxis: {
        ...defaultChartStyle.label
      },
      yAxis: {
        label: defaultChartStyle.label.style,
        grid: defaultChartStyle.grid
      }
    } : null;    return (
      <div className="charts-grid">
        <div className="chart-card">
          <div className="card-header">
            <h3><TrendingUp className="inline-icon" size={20} /> Health Trends</h3>
          </div>
          <div className="card-body">
            {trendConfig ? (
              <Line {...trendConfig} />
            ) : (
              <div className="chart-placeholder">No trend data available</div>
            )}
          </div>
        </div>

        <div className="chart-card">
          <div className="card-header">
            <h3><AlertTriangle className="inline-icon" size={20} /> Issue Severity Distribution</h3>
          </div>
          <div className="card-body">
            {severityConfig ? (
              <Pie {...severityConfig} />
            ) : (
              <div className="chart-placeholder">No severity data available</div>
            )}
          </div>
        </div>

        <div className="chart-card">
          <div className="card-header">
            <h3><BarChart className="inline-icon" size={20} /> Material Distribution</h3>
          </div>
          <div className="card-body">
            {materialConfig ? (
              <Bar {...materialConfig} />
            ) : (
              <div className="chart-placeholder">No material distribution data available</div>
            )}
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="content-area analytics-page">
      <div className="glass-header">
        <div className="header-content">
          <div className="header-main">
            <h1>
              <BarChart className="inline-icon glow-icon" size={32} />
              Analytics & Insights
            </h1>
            <p>Dynamic analysis based on uploaded image data and AI insights</p>
          </div>
          <div className="header-controls">
            <div className="data-type-selector glass-controls">
              <button className={`time-btn ${dataType === 'all' ? 'active' : ''}`} onClick={() => setDataType('all')}>All Data</button>
              <button className={`time-btn ${dataType === 'cracks' ? 'active' : ''}`} onClick={() => setDataType('cracks')}>Cracks</button>
              <button className={`time-btn ${dataType === 'materials' ? 'active' : ''}`} onClick={() => setDataType('materials')}>Materials</button>
              <button className={`time-btn ${dataType === 'environmental' ? 'active' : ''}`} onClick={() => setDataType('environmental')}>Environmental</button>
            </div>
            <button onClick={downloadReport} className="btn btn-glass" title="Download report">
              <Download size={18} /> Export Report
            </button>
          </div>
        </div>
        <div className="header-backdrop"></div>
      </div>
      
      <div className="analytics-content">
        <div className="glass-panel">
          {loading ? (
            <div className="loading-state">
              <div className="pulse-loader"></div>
              <p>Loading analytics data...</p>
            </div>
          ) : (
            renderChart() || <div className="chart-placeholder">No analytics data to show</div>
          )}
        </div>
      </div>

      {data && (data.keyFindings?.length > 0 || data.recommendations?.length > 0) && (
        <div className="insights-grid">
          {data.keyFindings?.length > 0 && (
            <div className="glass-panel findings-panel">
              <div className="panel-header">
                <h2>
                  <span className="header-icon">📊</span>
                  Key Findings
                </h2>
              </div>
              <div className="panel-body">
                <div className="findings-list">
                  {data.keyFindings.map((finding, index) => (
                    <div key={index} className="finding-item">
                      <div className="finding-number">{index + 1}</div>
                      <div className="finding-content">{finding}</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}

          {data.recommendations?.length > 0 && (
            <div className="glass-panel recommendations-panel">
              <div className="panel-header">
                <h2>
                  <span className="header-icon">💡</span>
                  Recommendations
                </h2>
              </div>
              <div className="panel-body">
                <div className="recommendations-list">
                  {data.recommendations.map((rec, index) => (
                    <div key={index} className="recommendation-item">
                      <div className="recommendation-icon">
                        <span>💭</span>
                      </div>
                      <div className="recommendation-content">{rec}</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default Analytics;