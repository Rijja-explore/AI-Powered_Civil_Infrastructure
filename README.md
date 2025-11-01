# 🏗️ InfraVision AI - Intelligent Structural Health Monitoring

A comprehensive AI-driven platform for structural health monitoring, crack detection, and infrastructure analysis using **React frontend** with **Python backend** services, featuring advanced computer vision and data analytics.

## 🏛️ Architecture Overview

### 🖥️ **Primary Interface**: React Frontend
- **Main Application**: Modern React.js web application with professional Glass-UI design
- **Location**: `./frontend/` directory
- **Port**: http://localhost:3000
- **Features**: Interactive dashboards, real-time monitoring, advanced analytics visualization

### 🐍 **Backend Services**: Python APIs
- **Primary Backend**: `finalwebapp.py` - Streamlit application serving as API backend
- **Secondary API**: `finalwebapp_api.py` - Flask REST API for specialized endpoints
- **Analytics Engine**: `advanced_data_analytics.py` - Statistical analysis and ML processing

## 🌟 Enhanced Features

### 📊 Advanced Data Analytics Suite
- **Descriptive Analytics & Visualization**: Comprehensive statistical summaries and data visualization
- **Inferential Statistics**: Hypothesis testing, confidence intervals, and statistical inference
- **Analysis of Variance (ANOVA)**: One-way and two-way ANOVA for group comparisons
- **Predictive Analytics**: Linear/logistic regression, time series analysis, and machine learning
- **Statistical Reporting**: Automated generation of comprehensive analytical reports

### 🎨 Professional React Glass-UI Design
- **Modern Glass-Morphism**: Professional glassmorphism design with backdrop blur effects
- **React Components**: Sophisticated metric cards, status indicators, and progress bars
- **Responsive Design**: Optimized for desktop, tablet, and mobile viewing
- **Real-time Updates**: Live data visualization with animated components
- **Enhanced UX**: Intuitive navigation with React Router and state management

### 🧠 Advanced Computer Vision
- **YOLOv8 Integration**: State-of-the-art object detection for structural defects
- **Multi-class Detection**: Crack detection, material classification, biological growth analysis
- **Real-time Processing**: Live camera feed analysis with instant results
- **Video Analysis**: Comprehensive video stream processing for temporal analysis
- **Confidence Scoring**: Advanced confidence metrics and reliability indicators

## 🚀 Quick Start

### Option 1: Full Stack Launch (Recommended)
```bash
# Install and start React frontend
cd frontend
npm install
npm start

# In a new terminal - Start Python backend
cd ..
python finalwebapp.py

# Optional: Start additional Flask API
python finalwebapp_api.py
```

### Option 2: Enhanced Startup Script
```bash
python start_enhanced_app.py
```

### Option 3: Individual Services
```bash
# React Frontend (Primary UI)
cd frontend
npm install && npm start

# Python Backend (Main API)
python finalwebapp.py

# Flask API (Additional endpoints)
python finalwebapp_api.py
```

## 🌐 Application Access

| Service | URL | Description | Priority |
|---------|-----|-------------|----------|
| **🎯 React Frontend** | http://localhost:3000 | **Primary UI** - Modern React application | **Main Interface** |
| **🐍 Python Backend** | http://localhost:8501 | Streamlit-based backend API | **Core Backend** |
| **🔧 Flask API** | http://localhost:5001 | Additional REST endpoints | **Secondary API** |
| **📊 API Health Check** | http://localhost:5001/api/health | Service status monitoring | **Diagnostics** |

## 📱 Frontend Architecture (React)

### 🏗️ **Project Structure**
```
frontend/
├── public/
│   ├── index.html          # Main HTML template
│   └── manifest.json       # PWA configuration
├── src/
│   ├── App.js              # Main application component
│   ├── index.js            # React DOM entry point
│   ├── components/         # Reusable UI components
│   │   ├── MainDashboard.jsx
│   │   └── Navbar.jsx
│   ├── pages/              # Page components
│   │   ├── ImageAnalysis.jsx
│   │   ├── VideoAnalysis.jsx
│   │   ├── RealTimeMonitoring.jsx
│   │   ├── Analytics.jsx
│   │   ├── Environmental.jsx
│   │   └── About.jsx
│   └── styles/             # CSS styling
│       ├── main.css        # Primary styles
│       ├── globals.css     # Global styling
│       └── *.css          # Component-specific styles
├── package.json            # Dependencies and scripts
└── README.md              # Frontend documentation
```

### ⚛️ **React Features**
- **Component Architecture**: Modular React components with hooks
- **State Management**: React Context and useState for state handling
- **Routing**: React Router for navigation between pages
- **HTTP Client**: Axios/Fetch for API communication
- **UI Library**: Custom Glass-UI components with Lucide React icons
- **Responsive Design**: Mobile-first responsive design principles

### 🎨 **UI Components**
- **Glass-Morphism Cards**: Professional glassmorphism design
- **Interactive Dashboards**: Real-time data visualization
- **File Upload**: Drag-and-drop file upload with preview
- **Progress Indicators**: Advanced progress bars and loading states
- **Metric Cards**: Live updating metric displays
- **Navigation**: Professional sidebar and tab navigation

## � Backend Architecture (Python)

### 🏗️ **Backend Structure**
```
├── finalwebapp.py              # Main Streamlit backend server
├── finalwebapp_api.py          # Flask REST API endpoints
├── advanced_data_analytics.py  # Analytics and ML processing
├── camera_capture.py           # Camera integration utilities
├── pdf_report.py              # Report generation
├── segmentation_with_localisation.py  # Computer vision processing
└── runs/                      # Model outputs and training data
    ├── detect/                # YOLO detection results
    ├── segmentation_model/    # Trained models
    └── segmentation_outputs/  # Processing outputs
```

### 🔧 **Backend Services**

#### **Primary Backend**: `finalwebapp.py` (Streamlit)
- **Framework**: Streamlit application serving as main backend
- **Port**: 8501
- **Purpose**: Core API endpoints, file processing, analytics integration
- **Features**: Image/video upload, real-time processing, analytics dashboard

#### **Secondary API**: `finalwebapp_api.py` (Flask)
- **Framework**: Flask REST API
- **Port**: 5001  
- **Purpose**: Specialized endpoints for React frontend integration
- **Features**: CORS-enabled API, health checks, specialized data endpoints

#### **Analytics Engine**: `advanced_data_analytics.py`
- **Purpose**: Statistical analysis and machine learning processing
- **Capabilities**: Descriptive statistics, ANOVA, predictive modeling
- **Integration**: Used by both Streamlit and Flask backends

### � System Requirements

### 🖥️ **For React Frontend**
- **Node.js**: 16+ (LTS recommended)
- **npm**: 8+ (comes with Node.js)
- **Browser**: Modern browser with ES6+ support
- **Memory**: 2GB RAM minimum for development

### 🐍 **For Python Backend**
- **Python**: 3.8 or higher (3.10+ recommended)
- **pip**: Latest version for package management
- **Memory**: 4GB RAM minimum, 8GB recommended for ML processing
- **Storage**: 2GB free space for models and temporary files

### 🎥 **Optional Hardware**
- **Camera**: USB/IP camera for real-time monitoring
- **GPU**: CUDA-compatible GPU for faster ML processing (optional)

## 📦 Dependencies

### ⚛️ **React Frontend Dependencies**
```json
{
  "react": "^18.0.0",
  "react-dom": "^18.0.0",
  "react-router-dom": "^6.0.0",
  "axios": "^1.0.0",
  "lucide-react": "^0.263.0",
  "react-hot-toast": "^2.4.0"
}
```

### 🐍 **Python Backend Dependencies**
```python
# Core Framework Dependencies
flask>=2.0.0
streamlit>=1.28.0

# Computer Vision & AI
opencv-python>=4.8.0
ultralytics>=8.0.0
pillow>=9.0.0

# Data Science & Analytics
numpy>=1.21.0
pandas>=1.5.0
scipy>=1.9.0
scikit-learn>=1.1.0
matplotlib>=3.5.0
seaborn>=0.11.0
statsmodels>=0.13.0
plotly>=5.0.0

# Utilities
requests>=2.28.0
```

### 📋 **Installation Commands**
```bash
# Install React dependencies
cd frontend
npm install

# Install Python dependencies
pip install -r requirements.txt
# or individual packages:
pip install flask streamlit opencv-python ultralytics numpy pandas scipy scikit-learn matplotlib seaborn statsmodels plotly
```

## 🏗️ Core Features

### 1. Image Analysis
- **Crack Detection**: Automated identification and measurement of structural cracks
- **Material Classification**: AI-powered material type identification
- **Biological Growth**: Detection and analysis of biological growth on structures
- **Environmental Impact**: Assessment of environmental factors affecting infrastructure

### 2. Video Analysis
- **Stream Processing**: Real-time video stream analysis
- **Temporal Detection**: Track changes over time in video sequences
- **Frame-by-Frame Analysis**: Detailed analysis of individual video frames
- **Motion Tracking**: Advanced motion detection for structural monitoring

### 3. Real-Time Monitoring
- **Live Camera Feed**: Continuous monitoring with connected cameras
- **Instant Alerts**: Real-time notifications for detected issues
- **Dashboard Metrics**: Live performance indicators and statistics
- **Historical Data**: Trend analysis and historical comparisons

### 4. Environmental Assessment
- **Carbon Footprint**: Calculate and track carbon emissions
- **Water Impact**: Monitor water usage and conservation metrics
- **Energy Consumption**: Track energy usage patterns
- **Sustainability Scoring**: Comprehensive sustainability assessments

### 5. Advanced Analytics
- **Statistical Analysis**: Comprehensive statistical testing and analysis
- **Predictive Modeling**: Machine learning models for future predictions
- **Data Visualization**: Interactive charts and graphs
- **Report Generation**: Automated analytical report creation

## 🔧 API Endpoints

### Core Analysis
- `POST /api/analyze` - Analyze uploaded images
- `POST /api/analyze-video` - Process video files
- `GET /api/health` - Service health check

### Advanced Analytics
- `POST /api/analytics/descriptive` - Descriptive statistics
- `POST /api/analytics/inferential` - Hypothesis testing
- `POST /api/analytics/anova` - Analysis of variance
- `POST /api/analytics/predictive` - Predictive modeling

### Real-time Monitoring
- `POST /api/connect_camera` - Connect camera feed
- `POST /api/start_stream` - Start video stream
- `GET /api/stream_metrics` - Live metrics

## 📊 Analytics Capabilities

### Descriptive Analytics
- **Data Summaries**: Mean, median, mode, standard deviation
- **Distribution Analysis**: Histograms, box plots, violin plots
- **Correlation Analysis**: Pearson and Spearman correlations
- **Frequency Analysis**: Categorical data distributions

### Inferential Statistics
- **Hypothesis Testing**: t-tests, chi-square tests, Mann-Whitney U
- **Confidence Intervals**: Bootstrap and parametric intervals
- **Effect Size**: Cohen's d, eta-squared, Cramer's V
- **Power Analysis**: Statistical power calculations

### ANOVA
- **One-way ANOVA**: Single factor analysis
- **Two-way ANOVA**: Multi-factor analysis
- **Post-hoc Tests**: Tukey's HSD, Bonferroni correction
- **Assumptions Testing**: Normality and homogeneity tests

### Predictive Analytics
- **Regression Models**: Linear, polynomial, logistic regression
- **Classification**: Random Forest, SVM, Neural Networks
- **Time Series**: ARIMA, seasonal decomposition
- **Model Validation**: Cross-validation, performance metrics

## 🎨 UI Components

### Glass-Morphism Design
- **Backdrop Blur**: Sophisticated blur effects for depth
- **Gradient Overlays**: Subtle color gradients for visual appeal
- **Shadow Effects**: Multi-layer shadows for realistic depth
- **Animation**: Smooth transitions and hover effects

### Interactive Elements
- **Metric Cards**: Real-time data visualization cards
- **Progress Indicators**: Advanced progress bars with animations
- **Status Displays**: Live connection and system status
- **Navigation**: Intuitive tab-based navigation system

## 🛠️ Configuration

### ⚛️ **React Frontend Configuration**
```javascript
// frontend/src/config.js
const config = {
  API_BASE_URL: 'http://localhost:5001',
  STREAMLIT_URL: 'http://localhost:8501',
  UPLOAD_MAX_SIZE: '100MB',
  SUPPORTED_FORMATS: ['jpg', 'jpeg', 'png', 'mp4', 'avi', 'mov']
};
```

### 🐍 **Backend Configuration**
```bash
# Environment Variables
FLASK_PORT=5001
STREAMLIT_PORT=8501
REACT_PORT=3000
CONFIDENCE_THRESHOLD=0.3
PX_TO_CM_RATIO=0.1
```

### 📷 **Camera Configuration**
```python
# Camera settings in finalwebapp_api.py
CAMERA_RESOLUTION = (1920, 1080)
CAMERA_FPS = 30
BUFFER_SIZE = 1
```

## 📈 Performance Optimization

### Backend Optimizations
- **Async Processing**: Non-blocking image/video processing
- **Memory Management**: Efficient memory usage for large files
- **Caching**: Result caching for improved response times
- **Batch Processing**: Efficient handling of multiple requests

### Frontend Optimizations
- **Lazy Loading**: Component-based lazy loading
- **State Management**: Optimized React state handling
- **Image Optimization**: Automatic image compression and resizing
- **Progressive Loading**: Incremental data loading

## 🔒 Security

- **Input Validation**: Comprehensive file type and size validation
- **CORS Configuration**: Secure cross-origin resource sharing
- **Error Handling**: Robust error handling and logging
- **File Sanitization**: Safe file upload and processing

## 🧪 Testing

### ⚛️ **React Frontend Testing**
```bash
cd frontend

# Run unit tests
npm test

# Run tests with coverage
npm run test:coverage

# Run end-to-end tests
npm run test:e2e
```

### 🐍 **Python Backend Testing**
```bash
# Run Python unit tests
python -m pytest tests/

# Run specific test modules
python -m pytest tests/test_analytics.py
python -m pytest tests/test_api.py

# Run with coverage
python -m pytest --cov=.
```

### 🔄 **Integration Testing**
```bash
# Test full stack integration
python test_integration.py

# Test API endpoints
python test_api.py

# Test analytics processing
python test_analytics.py
```

### 📊 **Test Coverage**
- **Frontend Tests**: React component testing with Jest
- **Backend Tests**: Python unit tests with pytest
- **API Tests**: Endpoint testing with requests
- **Integration Tests**: Full workflow testing
- **Performance Tests**: Load and stress testing

## � Development Workflow

### 🔄 **Development Process**
1. **Frontend Development**: Work in `./frontend/` with React hot reloading
2. **Backend Development**: Develop Python APIs with auto-restart
3. **Testing**: Run tests for both frontend and backend
4. **Integration**: Test full stack functionality
5. **Deployment**: Build and deploy both services

### 🛠️ **Development Commands**
```bash
# Start development servers
npm run dev          # React frontend with hot reload
python finalwebapp.py    # Python backend with auto-restart

# Build for production
cd frontend && npm run build    # Build React app
python setup.py build          # Package Python backend

# Development utilities
npm run lint         # ESLint for React
python -m flake8     # Python linting
npm run format       # Prettier formatting
python -m black .    # Python formatting
```

## 📱 **React Frontend Features**

### 🎯 **Core Pages**
- **🏠 HomePage**: Landing page with overview and navigation
- **🖼️ ImageAnalysis**: Upload and analyze structural images
- **🎥 VideoAnalysis**: Process video files for temporal analysis  
- **📡 RealTimeMonitoring**: Live camera feed monitoring
- **📊 Analytics**: Advanced statistical analysis dashboard
- **🌿 Environmental**: Environmental impact assessment
- **ℹ️ About**: Project information and documentation

### 🎨 **UI Features**
- **Glass-Morphism Design**: Professional backdrop blur effects
- **Responsive Layout**: Mobile-first responsive design
- **Dark/Light Theme**: Theme switching capabilities
- **Interactive Charts**: Real-time data visualization
- **File Upload**: Drag-and-drop with progress indicators
- **Live Updates**: WebSocket integration for real-time data
- **Toast Notifications**: User feedback system
- **Loading States**: Professional loading animations

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Documentation

### 📖 **API Documentation**
- **React Frontend**: Component documentation with Storybook
- **Python Backend**: Swagger UI for API endpoints
- **Endpoint Specifications**: Detailed parameter descriptions
- **Example Requests**: Sample API calls and responses
- **Error Codes**: Comprehensive error handling guide

### 👥 **User Guide**
- **Getting Started**: Step-by-step setup for React + Python
- **Feature Tutorials**: Detailed explanations of each page/component
- **Best Practices**: Optimization and usage recommendations
- **Troubleshooting**: Common issues for both frontend and backend

### 🏗️ **Developer Documentation**
- **React Architecture**: Component structure and state management
- **Python API Design**: Backend architecture and data processing
- **Integration Guide**: How frontend communicates with backend
- **Deployment Guide**: Production setup for both services

## 🆘 Support

### 🔧 **Troubleshooting**

#### **React Frontend Issues**
- **Port 3000 conflicts**: Change port in package.json or use different port
- **Build failures**: Clear node_modules and reinstall dependencies
- **API connection**: Verify backend is running on correct ports
- **CORS errors**: Check CORS configuration in Flask API

#### **Python Backend Issues**  
- **Port conflicts**: Ensure ports 5001 and 8501 are available
- **Dependencies**: Run `pip install -r requirements.txt`
- **Camera issues**: Check camera permissions and driver compatibility
- **Memory issues**: Monitor RAM usage during ML processing
- **Model loading**: Verify YOLO models are properly downloaded

#### **Integration Issues**
- **API communication**: Check network connectivity between services
- **Data formatting**: Verify JSON response formats match expected structure
- **File uploads**: Ensure proper MIME types and size limits
- **Real-time features**: Verify WebSocket connections (if implemented)

### 🎯 **Getting Help**
- **GitHub Issues**: Report bugs and request features
- **Frontend Issues**: Tag with `frontend` or `react` labels  
- **Backend Issues**: Tag with `backend` or `python` labels
- **Documentation**: Check comprehensive README and code comments
- **Community**: Join discussions and get support from other developers

## 🙏 Acknowledgments

- **⚛️ React**: Modern frontend framework for building user interfaces
- **🐍 Python**: Backend processing with Streamlit and Flask frameworks
- **🧠 YOLOv8**: Ultralytics for advanced object detection and computer vision
- **👁️ OpenCV**: Computer vision processing capabilities
- **📊 SciPy Ecosystem**: Comprehensive scientific computing tools (NumPy, Pandas, SciPy)
- **📈 Analytics Libraries**: Matplotlib, Seaborn, Plotly for data visualization
- **🔧 Development Tools**: Node.js ecosystem and Python development tools

---

## 🚀 **Project Architecture Summary**

```
🏗️ AI-Powered Structural Health Monitoring
├── 🎯 React Frontend (Primary UI)
│   ├── Modern Glass-UI Design
│   ├── Interactive Dashboards  
│   ├── Real-time Monitoring
│   └── Professional UX/UI
│
├── 🐍 Python Backend (Core Processing)
│   ├── Streamlit Main Server (Port 8501)
│   ├── Flask API Endpoints (Port 5001)
│   ├── Advanced Analytics Engine
│   └── Computer Vision Processing
│
└── 🔗 Integration Layer
    ├── REST API Communication
    ├── File Upload/Processing
    ├── Real-time Data Streaming
    └── Analytics Pipeline
```

**🌟 Star this repository if you find it useful!**

**📧 For questions and support, please open an issue on GitHub with appropriate frontend/backend labels.**