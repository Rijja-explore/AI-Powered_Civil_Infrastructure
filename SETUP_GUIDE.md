# Heritage Site Health Monitoring - Full Stack Setup Guide

## 🎯 Project Overview

This project converts the Streamlit-based Heritage Site Health Monitoring application to a modern **React + Flask** architecture with professional UI/UX design.

### Architecture

```
├── backend/               # Flask API Server
│   ├── app.py            # Main Flask application
│   ├── requirements.txt  # Python dependencies
│   └── pdf_report.py     # PDF generation (from existing project)
│
├── frontend/             # React Application
│   ├── src/              # Source code
│   ├── public/           # Static files
│   └── package.json      # Node dependencies
│
├── runs/                 # YOLO model weights
├── segmentation_model/   # Segmentation model weights
└── finalwebapp.py        # Original Streamlit app (for reference)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn
- CUDA-capable GPU (optional, for faster processing)

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Flask server
python app.py
```

Backend will run on `http://localhost:5000`

### 2. Frontend Setup

```bash
# Open new terminal
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start React development server
npm start
```

Frontend will open at `http://localhost:3000`

## 📦 Installation Details

### Backend Dependencies

```txt
flask==3.0.0
flask-cors==4.0.0
opencv-python==4.8.1.78
pillow==10.1.0
numpy==1.26.2
torch==2.1.1
torchvision==0.16.1
ultralytics==8.0.227
scikit-learn==1.3.2
scipy==1.11.4
scikit-image==0.22.0
reportlab==4.0.7
```

### Frontend Dependencies

```json
{
  "react": "^18.2.0",
  "react-router-dom": "^6.20.0",
  "axios": "^1.6.2",
  "framer-motion": "^10.16.16",
  "recharts": "^2.10.3",
  "lucide-react": "^0.294.0",
  "react-dropzone": "^14.2.3"
}
```

## 🎨 Features

### Backend (Flask API)

✅ **Image Analysis Endpoint** - Process uploaded images
✅ **Crack Detection** - YOLO-based damage detection
✅ **Material Classification** - MobileNetV2 material recognition
✅ **Biological Growth Detection** - HSV-based growth analysis
✅ **Segmentation** - Advanced image segmentation
✅ **Depth Estimation** - 3D structural analysis
✅ **Edge Detection** - Canny edge detection
✅ **Environmental Metrics** - Carbon & water footprint
✅ **Predictive Analytics** - Crack progression forecasting
✅ **PDF Report Generation** - Downloadable reports

### Frontend (React UI)

✅ **Modern Design** - Professional gradients & animations
✅ **Responsive Layout** - Works on all devices
✅ **Drag & Drop Upload** - Easy image upload
✅ **Real-time Progress** - Live analysis tracking
✅ **Interactive Tabs** - Multiple analysis views
✅ **Data Visualization** - Charts & graphs
✅ **Smooth Animations** - Framer Motion effects
✅ **Glass Morphism** - Modern UI aesthetics
✅ **Dark Theme** - Professional color scheme

## 🎯 Usage Guide

### 1. Upload Image

- Navigate to **Analysis** page
- Drag & drop an image or click to browse
- Supported formats: JPG, PNG, JPEG

### 2. Analyze

- Click "Start Analysis" button
- Watch real-time progress
- Wait for processing (5-15 seconds)

### 3. View Results

Results displayed in tabs:

- **Crack Detection**: Annotated image with severity levels
- **Segmentation**: AI-powered region identification
- **Bio Growth**: Biological growth detection
- **Depth Analysis**: Heatmap visualization
- **Edge Detection**: Structural boundaries

### 4. Review Metrics

- Crack details with dimensions
- Material classification probabilities
- Environmental impact (carbon & water)
- Crack progression forecast

### 5. Download Report

- Click "Download Report" button
- PDF generated with all analysis results
- Save for documentation

## 🔧 Configuration

### Backend Configuration

Edit `backend/app.py`:

```python
# Model paths
yolo_path = "../runs/detect/train3/weights/best.pt"
seg_path = "../segmentation_model/weights/best.pt"

# Server settings
app.run(debug=True, port=5000, host='0.0.0.0')
```

### Frontend Configuration

Edit `frontend/src/pages/AnalysisPage.js`:

```javascript
// API endpoint
const response = await axios.post('http://localhost:5000/api/analyze', formData);
```

## 📊 API Endpoints

### Health Check
```http
GET /api/health
```

### Image Analysis
```http
POST /api/analyze
Content-Type: multipart/form-data

Body:
- image: File
- px_to_cm_ratio: float (default: 0.1)
```

### PDF Generation
```http
POST /api/generate-pdf
Content-Type: application/json

Body: { results: object }
```

## 🎨 UI/UX Design

### Color Palette

- **Primary**: `#667eea` to `#764ba2` (Purple gradient)
- **Success**: `#4ade80` (Green)
- **Warning**: `#fbbf24` (Yellow)
- **Danger**: `#ef4444` (Red)
- **Background**: Linear gradients with purple/blue tones

### Typography

- **Font Family**: Inter, system fonts
- **Headings**: 700-800 weight
- **Body**: 400-500 weight

### Animations

- Fade in on page load
- Scale on hover
- Smooth transitions (0.3s ease)
- Progress bars with motion
- Tab switching animations

## 🚀 Production Deployment

### Backend (Flask)

```bash
# Use Gunicorn for production
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Frontend (React)

```bash
# Build production bundle
npm run build

# Serve with nginx or any static server
serve -s build -p 3000
```

## 🐛 Troubleshooting

### Backend Issues

**Models not loading:**
- Check model paths in `app.py`
- Ensure weights files exist in correct directories
- Verify PyTorch and CUDA installation

**CORS errors:**
- Ensure `flask-cors` is installed
- Check CORS configuration in `app.py`

### Frontend Issues

**Cannot connect to backend:**
- Verify backend is running on port 5000
- Check API endpoint URLs
- Ensure no firewall blocking

**Image upload fails:**
- Check file size (<10MB recommended)
- Verify file format (JPG, PNG, JPEG)
- Check backend file upload limits

## 📝 Comparison: Streamlit vs React

| Feature | Streamlit | React |
|---------|-----------|-------|
| UI Design | Basic | Professional & Modern |
| Animations | None | Smooth & Engaging |
| Customization | Limited | Fully Customizable |
| Performance | Good | Excellent |
| Scalability | Limited | High |
| User Experience | Simple | Rich & Interactive |
| Mobile Support | Basic | Fully Responsive |

## 🔄 Migration from Streamlit

All functionality from `finalwebapp.py` has been preserved:

✅ Image upload and processing
✅ YOLO crack detection
✅ Material classification
✅ Biological growth analysis
✅ Segmentation
✅ Depth estimation
✅ Edge detection
✅ Environmental footprints
✅ Predictive analytics
✅ PDF report generation

**New Features:**
- Modern, professional UI
- Smooth animations
- Interactive visualizations
- Better mobile experience
- Faster performance
- Scalable architecture

## 📚 Documentation

- **Backend API**: See `backend/app.py` docstrings
- **Frontend Components**: See component files in `frontend/src/`
- **Original Logic**: Reference `finalwebapp.py`

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## 📄 License

This project is part of the Heritage Site Health Monitoring system.

## 🎉 Success!

Your application is now running with:
- ✅ Professional React frontend
- ✅ Robust Flask backend
- ✅ All original features preserved
- ✅ Modern UI/UX design
- ✅ Smooth animations
- ✅ Interactive visualizations

**Enjoy monitoring heritage sites with style! 🏛️✨**
