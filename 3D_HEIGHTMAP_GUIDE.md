# 🎨 3D Heightmap Generator - Quick Start Guide

## What's New

✅ **Reduced UI Display Size**: 3D viewer now displays at **450px height** (was 700px)  
✅ **Enhanced Texture Mapping**: Better thermal visualization with heatmap + edge detection  
✅ **Format Selector**: Switch between GLB (textured) and STL (monochrome) formats  
✅ **Improved Image Processing**: Better color weighting for richer 3D models  

---

## How to Use

### Step 1: Access the 3D Heightmap Generator
Navigate to the **Heightmap3D** page in your application

### Step 2: Select Output Format
```
Format Dropdown:
├─ 🎨 GLB (Textured) - Recommended [DEFAULT]
└─ ⚪ STL (Monochrome)
```

### Step 3: (Optional) Adjust Advanced Settings
Click **Advanced** to customize:
- **Resolution**: 100-500px (default: 300)
- **Height Scale**: 2-30 units (default: 12.0)
- **Smoothing**: 0-5 sigma (default: 1.2)

### Step 4: Upload Image
- Drag & drop or click "Choose File"
- Supported formats: JPG, PNG, GIF, BMP

### Step 5: View Result
- 3D model loads in interactive viewer (450px canvas)
- Rotate, zoom, and pan with mouse controls
- Format info displayed below viewer

### Step 6: Download
Click **📥 Download** to save as `.glb` or `.stl`

---

## Technical Details

### GLB (Recommended)
**Use When**: Visual inspection, presentations, web viewing
```
Texture Layers:
├─ 50% JET Heatmap (thermal colors: blue → red)
└─ 100% Edge Detection (red lines for structures)
```

**Best For**:
- Thermal imaging visualization
- Structural health assessment
- Interactive 3D presentations
- Web-based viewers (Three.js, Babylon.js)

### STL (Traditional)
**Use When**: 3D printing, CAD software, mechanical analysis
```
Texture: Single color/monochrome
Geometry: Pure height-based mesh
```

**Best For**:
- CAD software import
- 3D printing preparation
- FEA analysis
- Traditional 3D modeling

---

## Settings Explained

| Setting | Range | Default | Impact |
|---------|-------|---------|--------|
| **Resolution** | 100-500px | 300 | Higher = more detail, slower processing |
| **Height Scale** | 2-30 units | 12.0 | Controls vertical exaggeration |
| **Smoothing (σ)** | 0-5 | 1.2 | Higher = smoother surface, less detail |

### Recommended Presets

**High Detail** (Slow)
- Resolution: 500px
- Height Scale: 15
- Smoothing: 0.8

**Balanced** (Recommended)
- Resolution: 300px
- Height Scale: 12
- Smoothing: 1.2

**Fast Performance**
- Resolution: 200px
- Height Scale: 10
- Smoothing: 1.5

---

## Color Interpretation

### Heatmap Colors (GLB Format)
```
🔵 BLUE   → Low intensity / Low height
🟢 GREEN  → Medium intensity
🟡 YELLOW → High intensity
🔴 RED    → Very high intensity / High height
```

### Edge Overlay
```
🔴 RED LINES → Detected edges/cracks/boundaries
```

---

## Troubleshooting

### Model looks monochrome
- ❌ Format might be STL
- ✅ Switch to GLB format
- ✅ Check "Advanced" settings

### Model is too smooth/flat
- ❌ Smoothing is too high
- ✅ Reduce smoothing (σ) value
- ✅ Increase height scale

### Model is too jagged/noisy
- ❌ Smoothing is too low
- ✅ Increase smoothing (σ) value
- ✅ Reduce resolution

### Performance is slow
- ❌ Resolution is too high
- ✅ Lower resolution (200-300px)
- ✅ Increase smoothing
- ✅ Reduce height scale

### Model won't load in 3D viewer
- ❌ Browser compatibility issue
- ✅ Try different browser
- ✅ Clear cache
- ✅ Check console for errors

---

## API Endpoints

### Generate GLB (Recommended)
```bash
POST /api/generate-3d-glb
Content-Type: multipart/form-data

Parameters:
- image: [file] (required)
- resize_to: 300 (optional, 100-500)
- height_scale: 12.0 (optional, 2-30)
- smooth_sigma: 1.2 (optional, 0-5)

Response: Binary GLB file
```

### Generate STL
```bash
POST /api/generate-3d-heightmap
Content-Type: multipart/form-data

Parameters:
- image: [file] (required)

Response: Binary STL file
```

---

## Example Workflow

### 📸 Infrastructure Monitoring
1. Capture image of building/bridge facade
2. Select **GLB (Textured)**
3. Use **Balanced** preset
4. Generate 3D model
5. Inspect thermal patterns and crack patterns
6. Download for documentation

### 🖨️ 3D Printing Preparation
1. Use **STL** format
2. Upload building cross-section
3. Set **High Detail** preset
4. Download STL
5. Import into slicing software

### 📊 Environmental Analysis
1. Satellite/drone imagery
2. Use **GLB** format
3. Adjust **Height Scale** for terrain emphasis
4. Analyze color patterns
5. Export for GIS software

---

## Tips & Tricks

💡 **Pro Tips**:
1. For best results, use clear, well-lit images
2. Grayscale conversion affects height mapping - higher brightness = higher elevation
3. Edge detection highlights structural features - cracks appear as red lines
4. Experiment with smoothing for different terrain representations
5. Keep resolution ≤ 400px for web performance

⚙️ **Advanced**:
- Lower smoothing + lower resolution = fast processing
- Higher smoothing + lower resolution = good balance
- Higher smoothing + high resolution = best quality (slowest)

🎨 **Color Optimization**:
- Enhance image contrast before upload for better visualization
- Remove shadows/highlights for consistent height mapping
- Use BW filter for clearer height determination

---

## Browser Requirements

✅ **Supported**:
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

⚠️ **Requirements**:
- WebGL support enabled
- 4GB+ RAM recommended
- 1080p+ display recommended for 450px viewer

---

## Export & Sharing

### Share GLB Models
1. Download `.glb` file
2. Open in:
   - 🌐 Sketchfab.com
   - 🌐 Three.js Editor
   - 🌐 Babylon.js Viewer
   - 📱 Mobile AR viewers

### Share STL Models
1. Download `.stl` file
2. Open in:
   - 🖥️ Blender
   - 🖥️ Fusion 360
   - 🖥️ SolidWorks
   - 🖨️ Cura (3D printing)

---

## Questions?

Check the API documentation: `/api/health`  
Test endpoint: `GET /api/health`

**Last Updated**: November 21, 2025  
**Version**: 1.0  
**Status**: ✅ Production Ready
