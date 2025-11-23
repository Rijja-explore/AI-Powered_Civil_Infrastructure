# 🚀 InfraVision AI - API Setup Guide

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation](#installation)
3. [Backend API Setup](#backend-api-setup)
4. [Frontend Setup](#frontend-setup)
5. [Running the Application](#running-the-application)
6. [API Endpoints](#api-endpoints)
7. [Troubleshooting](#troubleshooting)

---

## 🖥️ System Requirements

### Hardware
- **CPU**: Intel i5 or equivalent (with GPU support recommended for faster inference)
- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: 5GB free space minimum
- **GPU**: NVIDIA GPU with CUDA support (optional but recommended for 10x faster processing)

### Software
- **Python**: 3.8 or higher
- **Node.js**: 14.0 or higher
- **npm**: 6.0 or higher
- **Git**: Latest version

---

## 📥 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Rijja-explore/AI-Powered_-Civil_Infrastructure.git
cd "AI-Powered_-Civil_Infrastructure"
```

### 2. Create Python Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install Node.js Dependencies
```bash
cd frontend
npm install
cd ..
```

---

## 🔧 Backend API Setup

### Configuration

#### Step 1: Environment Variables
Create a `.env` file in the project root:
```env
# Flask API Configuration
FLASK_ENV=development
FLASK_DEBUG=True
API_PORT=5002
CORS_ORIGINS=*

# Image Processing
MAX_IMAGE_SIZE_MB=50
ALLOWED_EXTENSIONS=jpg,jpeg,png,gif,bmp

# Model Configuration
CONFIDENCE_THRESHOLD=0.3
PIXEL_TO_CM_RATIO=0.1

# Database (optional)
DATABASE_URL=sqlite:///infravis_ai.db
```

#### Step 2: Download Pre-trained Models
```bash
# YOLOv8 models will auto-download on first run
# Models will be cached in ~/.yolo/

# Expected disk space:
# - YOLOv8n (nano): ~7MB
# - YOLOv8s (small): ~27MB
# - YOLOv8m (medium): ~49MB
```

### Starting the Backend API

```bash
# Option 1: Direct Python execution
python finalwebapp_api.py

# Option 2: Using Gunicorn (production)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5002 finalwebapp_api:app

# Expected output:
# ✅ PyTorch/TorchVision loaded successfully
# ✅ Flask running on http://localhost:5002
# ✅ CORS enabled
```

**Backend Status Check:**
```bash
curl http://localhost:5002/health
# Expected response: {"status": "ok"}
```

---

## 🎨 Frontend Setup

### Configuration

#### Step 1: Environment Variables
Create `frontend/.env`:
```env
REACT_APP_API_URL=http://localhost:5002
REACT_APP_API_TIMEOUT=60000
```

#### Step 2: Start Development Server
```bash
cd frontend
npm start
```

**Frontend Status:**
- Application opens at: `http://localhost:3000`
- Hot reload enabled for live editing

---

## 🏃 Running the Application

### Complete Startup Sequence

#### Terminal 1: Backend API
```bash
# Activate Python environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Start API
python finalwebapp_api.py
```

#### Terminal 2: Frontend
```bash
cd frontend
npm start
```

#### Access the Application
- **Frontend UI**: http://localhost:3000
- **Backend API**: http://localhost:5002
- **Analytics Dashboard**: http://localhost:3000/analytics

---

## 📡 API Endpoints

### Image Analysis
```
POST /api/analyze
Content-Type: application/json

Request:
{
  "image": "base64_encoded_image_string",
  "px_to_cm_ratio": 0.1,
  "confidence_threshold": 0.3
}

Response:
{
  "results": {
    "metrics": {
      "crack_density": 0.45,
      "vegetation_coverage": 0.12,
      "risk_score": 0.65,
      "avg_confidence": 0.78,
      "detection_count": 24
    },
    "detections": [
      {
        "type": "crack",
        "severity": "High",
        "confidence": 0.95,
        "location": "center",
        "bbox": [100, 100, 200, 200]
      }
    ]
  },
  "output_images": [
    "base64_annotated_image",
    ...
  ]
}
```

### Health Check
```
GET /health

Response:
{
  "status": "ok",
  "models_loaded": true,
  "processing_time_avg": 2.5
}
```

### PDF Report Generation
```
POST /api/download-pdf
Content-Type: application/json

Request:
{
  "analysis_date": "2025-11-23T10:30:00Z",
  "site_analysis": {...}
}

Response: PDF file (binary)
```

---

## 🐛 Troubleshooting

### Issue 1: Backend API Fails to Start

**Error**: `ModuleNotFoundError: No module named 'cv2'`
```bash
# Solution: Install OpenCV
pip install opencv-python==4.8.0.74
```

**Error**: `ImportError: cannot import name YOLO`
```bash
# Solution: Install ultralytics
pip install ultralytics==8.0.189
```

**Error**: CUDA/GPU not available
```bash
# The API will still work with CPU, but slower
# To enable GPU: install CUDA toolkit and cuDNN
# https://docs.nvidia.com/cuda/cuda-installation-guide/
```

### Issue 2: Frontend Can't Connect to Backend

**Error**: `CORS error` or `Failed to fetch from http://localhost:5002`
```
1. Verify backend is running: http://localhost:5002/health
2. Check firewall settings
3. Verify REACT_APP_API_URL in frontend/.env
4. Restart backend with CORS enabled
```

### Issue 3: Large Image Processing Timeout

**Error**: `Request timeout after 60s`
```
1. Increase REACT_APP_API_TIMEOUT in frontend/.env
2. Reduce image resolution
3. Upgrade hardware (especially GPU)
```

### Issue 4: Out of Memory

**Error**: `MemoryError` or `CUDA out of memory`
```
1. Close other applications
2. Reduce batch size in API
3. Use smaller YOLOv8 model (nano instead of large)
4. Increase available RAM/VRAM
```

### Issue 5: Models Not Loading

**Error**: `Model files not found` or `download timeout`
```bash
# Clear model cache and force re-download
rm -rf ~/.yolo/
# Run API again to auto-download models
python finalwebapp_api.py
```

---

## 📊 Dataset Analytics

The application includes pre-computed dataset analytics from **7,562 images**:

- **Crack Images**: 6,500 (86%)
- **Vegetation Images**: 1,062 (14%)
- **Split**: Train 66%, Test 10%, Valid 10%

**Statistics Included**:
- Mean, Median, Std Dev for all metrics
- Quartiles (Q1, Q2, Q3)
- Min/Max values
- Distribution histograms
- Correlation matrices

**Located in**: `/dataset_analytics.json`

---

## 🎯 Performance Benchmarks

### Processing Time (per image)
- **Small GPU (RTX 3060)**: ~0.5-1.5 seconds
- **CPU (i7)**: ~3-5 seconds
- **Large GPU (RTX 4090)**: ~0.2-0.5 seconds

### Memory Usage
- **GPU**: ~4-6GB VRAM
- **CPU**: ~2-3GB RAM

### Model Sizes
- **YOLOv8 Nano**: 7MB
- **YOLOv8 Small**: 27MB
- **YOLOv8 Medium**: 49MB

---

## 📝 Requirements File

The `requirements.txt` includes:

### Core Dependencies
- **Flask** 2.3.3 - Web framework
- **Flask-CORS** 4.0.0 - Cross-origin support
- **NumPy** 1.24.3 - Numerical computing
- **Pandas** 2.0.3 - Data manipulation
- **SciPy** 1.11.2 - Scientific computing
- **scikit-learn** 1.3.0 - Machine learning

### Computer Vision
- **OpenCV** 4.8.0.74 - Image processing
- **Pillow** 10.0.0 - Image library
- **scikit-image** 0.21.0 - Advanced image processing
- **YOLOv8 (ultralytics)** 8.0.189 - Object detection

### Deep Learning
- **PyTorch** 2.0.1 - Neural networks
- **TensorFlow** 2.13.0 - Deep learning
- **TorchVision** 0.15.2 - Computer vision models

### Data Visualization
- **Matplotlib** 3.7.2 - Plotting
- **Seaborn** 0.12.2 - Statistical visualization
- **Plotly** 5.17.0 - Interactive charts

### Reporting
- **ReportLab** 4.0.4 - PDF generation
- **PyPDF2** 3.0.1 - PDF processing

---

## 🚀 Next Steps

1. ✅ Install dependencies
2. ✅ Start backend API
3. ✅ Start frontend
4. 📊 Upload images for analysis
5. 📈 View results in Analytics dashboard
6. 📥 Export PDF reports

---

## 📞 Support

For issues or questions:
1. Check **Troubleshooting** section above
2. Review logs in console
3. Check API health: `curl http://localhost:5002/health`
4. Verify network connectivity

---

## 📄 License

This project is licensed under MIT License.

---

**Last Updated**: November 23, 2025
**Status**: ✅ Production Ready
