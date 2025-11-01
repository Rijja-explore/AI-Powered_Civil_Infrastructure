# 🏛 Heritage Site Health Monitoring System - Startup Guide

## 📋 Project Overview

This project is an AI-powered conservation technology system that provides real-time analysis and predictive insights for heritage site monitoring. It consists of:

- **Backend**: Python Streamlit application (`finalwebapp.py`)
- **Frontend**: React application with Bootstrap UI
- **ML Models**: YOLO for object detection, segmentation models, and material classification

---

## 🚀 Quick Start

### **Option 1: Run Streamlit Backend Only (Recommended for Initial Testing)**

```bash
# Navigate to project directory
cd d:\Projects\AI-Powered_Heritage_Site_Health_Monitoring

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run finalwebapp.py
```

The app will open at: `http://localhost:8501`

---

### **Option 2: Run React Frontend + Backend (Full Setup)**

#### **Step 1: Install Backend Dependencies**

```bash
# From project root
pip install -r requirements.txt
```

#### **Step 2: Install Frontend Dependencies**

```bash
# Navigate to frontend
cd frontend

# Install Node packages
npm install

# If you encounter issues, try:
npm install --legacy-peer-deps
```

#### **Step 3: Start Backend (Streamlit)**

```bash
# From project root
streamlit run finalwebapp.py
```

Backend will run at: `http://localhost:8501`

#### **Step 4: Start Frontend (React)**

```bash
# Open new terminal/PowerShell
cd frontend

# Start development server
npm start
```

Frontend will run at: `http://localhost:3000`

---

## 📦 Project Structure

```
AI-Powered_Heritage_Site_Health_Monitoring/
│
├── finalwebapp.py                 # Main Streamlit application
├── segmentation_with_localisation.py  # Segmentation module
├── depth_estimation.ipynb         # Depth analysis notebook
├── camera_capture.py              # Camera capture functionality
├── pdf_report.py                  # PDF report generation
├── requirements.txt               # Python dependencies
│
├── frontend/                      # React application
│   ├── src/
│   │   ├── App.js                # Main React component
│   │   ├── components/
│   │   │   └── MainDashboard.jsx # Main dashboard component
│   │   ├── styles/
│   │   │   └── professional.css   # Application styles
│   │   └── index.js              # React entry point
│   ├── package.json              # Node dependencies
│   └── public/
│
├── segmentation_model/           # Pre-trained segmentation model
│   └── weights/
│       └── best.pt
│
└── runs/                         # YOLO training outputs
    └── detect/
```

---

## 🔧 System Requirements

### **Python Requirements**
- Python 3.9 or higher
- pip (Python package manager)

### **Node Requirements**
- Node.js 14.0 or higher
- npm 6.0 or higher

### **GPU (Optional but Recommended)**
- CUDA-capable GPU for faster inference
- GPU Available indicator will show in System Status

### **Models**
The system uses three pre-trained models:
1. **YOLO Object Detection** - For crack and damage detection
2. **YOLO Segmentation** - For detailed analysis
3. **MobileNetV2** - For material classification

---

## 🎯 Features

### **Image Analysis Tab**
- Upload heritage site images (PNG, JPG, JPEG)
- Crack detection and severity classification
- Biological growth detection
- Material classification
- Depth estimation
- Edge detection analysis

### **Video Analysis Tab**
- Frame-by-frame video analysis
- Temporal damage tracking
- PDF reports for each frame

### **Real-time Tab**
- Live camera feed monitoring
- Continuous analysis

### **Data Analytics Tab**
- Historical trend analysis
- Performance metrics
- Time-series visualization

### **Environmental Analysis Tab**
- Carbon footprint calculation
- Water usage estimation
- Material impact assessment

---

## 📊 Configuration

### **Analysis Settings (Left Sidebar)**

- **Pixel to CM Ratio** (0.01 - 1.0)
  - Adjusts the scale for measurements
  - Default: 0.1

- **Detection Confidence** (0.1 - 0.9)
  - Minimum confidence threshold for detections
  - Higher = fewer false positives
  - Default: 0.3

### **System Status Indicators**
- **Models Loaded**: Shows how many ML models are ready (3/3 optimal)
- **GPU Available**: Indicates GPU availability for acceleration
- **Processing Queue**: Number of pending analyses

---

## 🔌 API Endpoints (If Using React Frontend)

The React frontend communicates with the backend via these endpoints:

```
POST /api/analyze
- Accepts: multipart/form-data (file, settings)
- Returns: Analysis results with processed images

GET /api/download-pdf
- Returns: PDF report file

POST /api/video-analyze
- Accepts: video file
- Returns: Frame-by-frame analysis

GET /api/environmental-stats
- Returns: Environmental impact data
```

---

## 🐛 Troubleshooting

### **Issue: "Models not loading"**
```bash
# Solution: Ensure model files are in correct path
# Check paths in finalwebapp.py around lines 50-80
```

### **Issue: "CUDA/GPU not detected"**
```bash
# Solution: Verify CUDA installation
python -c "import torch; print(torch.cuda.is_available())"

# If False, reinstall PyTorch with CUDA:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### **Issue: "Port 8501 already in use"**
```bash
# Solution: Use different port
streamlit run finalwebapp.py --server.port 8502
```

### **Issue: "npm install fails"**
```bash
# Solution: Clear cache and retry
npm cache clean --force
npm install --legacy-peer-deps
```

---

## 📝 Usage Example

### **Step 1: Start Backend**
```bash
streamlit run finalwebapp.py
```

### **Step 2: Upload Image**
- Click on file uploader in left panel
- Select heritage site image

### **Step 3: Adjust Settings (Optional)**
- Set Pixel to CM Ratio (default 0.1 is good for most images)
- Set Confidence Threshold (0.3-0.5 recommended)

### **Step 4: Click "Start Analysis"**
- Wait for processing to complete
- View results and visualizations

### **Step 5: Generate Report**
- Click "Download PDF Report" button
- Save report for documentation

---

## 🌐 Environment Variables (Optional)

Create a `.env` file in the project root:

```
MODEL_PATH=./segmentation_model/weights/best.pt
YOLO_PATH=./runs/detect/train3/weights/best.pt
API_PORT=8501
```

---

## 📚 Technical Stack

### **Backend**
- Streamlit - Web framework
- PyTorch - Deep learning
- OpenCV - Image processing
- YOLO - Object detection
- SciPy - Scientific computing
- Plotly - Visualizations
- ReportLab - PDF generation

### **Frontend**
- React 18 - UI framework
- Bootstrap 5 - Styling
- Axios - HTTP client
- React-Bootstrap - Components

---

## 🚨 Performance Tips

1. **For Real-time Analysis**: Use lower resolution images (< 1080p)
2. **For Accuracy**: Use high resolution images with good lighting
3. **GPU Acceleration**: Ensure CUDA is properly installed
4. **Model Caching**: Models are cached after first load
5. **Batch Processing**: Process multiple images sequentially

---

## 📞 Support & Documentation

- Check `README.md` for project overview
- Review `PROJECT_DOCUMENTATION.md` for detailed documentation
- Examine `finalwebapp.py` for backend implementation
- Check `frontend/src/components/MainDashboard.jsx` for frontend logic

---

## ✅ Verification Checklist

- [ ] Python 3.9+ installed
- [ ] Node.js 14+ installed (if using React)
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Model files present in `segmentation_model/weights/`
- [ ] YOLO weights in `runs/detect/train3/weights/`
- [ ] Port 8501 available (or specified port)
- [ ] GPU drivers updated (if using GPU)

---

## 🎉 You're Ready!

Once everything is set up, you should see:
- ✅ All 3 models loaded
- ✅ GPU status indicator
- ✅ File upload interface
- ✅ Sidebar configuration panel
- ✅ Analysis tabs ready

Happy analyzing! 🏛️
