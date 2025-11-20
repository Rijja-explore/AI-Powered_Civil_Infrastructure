# AI-Powered Civil Infrastructure Monitoring

## Overview
This project leverages AI to monitor and analyze the structural health of civil infrastructure. It integrates advanced computer vision, machine learning, and statistical analysis to provide predictive maintenance, automated damage detection, and data-driven decision-making.

---

## Key Features

### Image Analysis
- Crack detection with severity classification
- Material identification (e.g., concrete, wood, metal)
- Biological growth detection (e.g., moss, algae)
- Edge detection and segmentation
- Depth estimation
- PDF report generation

### Video Analysis
- Frame-by-frame structural analysis
- Temporal trend detection
- Aggregated statistics
- Critical issue identification

### Real-Time Monitoring
- Live camera feed integration
- Instant damage detection and alerting
- Dashboard metrics visualization

### 3D Heightmap Generator
- Convert 2D images to 3D heightmaps
- Interactive 3D viewer with rotation, zoom, and pan
- STL file export for CAD and 3D printing

### Analytics Dashboard
- Infrastructure health scoring
- Severity distribution visualization
- Predictive deterioration trends
- Environmental impact charts

---

## Installation

### Prerequisites
- **Python 3.8+**
- **Node.js 16+**
- **npm 8+**

### Backend Setup
```bash
pip install -r requirements.txt
python finalwebapp_api.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

---

## Usage

### Access the Application
- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **Backend API**: [http://localhost:5002](http://localhost:5002)

### 3D Heightmap Generator
1. Navigate to the "3D Heightmap" tab.
2. Upload a 2D image.
3. View the interactive 3D model.
4. Download the STL file.

---

## API Endpoints

### POST `/api/analyze`
Analyze an image for structural defects.

### POST `/api/generate-3d-heightmap`
Generate a 3D heightmap from a 2D image.

---

## File Structure
```
AI-Powered_-Civil_Infrastructure/
├── backend/
│   ├── finalwebapp_api.py
│   ├── image_to_heightmap.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── package.json
│   └── public/
└── README.md
```

---

## Troubleshooting

### Common Issues
- **Port Already in Use**: Kill the process using the port.
- **Dependency Errors**: Reinstall dependencies using `pip` or `npm`.
- **CORS Issues**: Ensure the backend allows requests from the frontend.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- YOLOv8 for object detection
- React for the frontend framework
- Flask for the backend API
- Open Source Community for contributions
