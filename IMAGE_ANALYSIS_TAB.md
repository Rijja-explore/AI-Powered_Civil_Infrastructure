# Image Analysis Tab — Project Description & Flow

This document describes the `Image Analysis` tab: what it does, the user/UI flow, backend integration, parameters, image examples and descriptions, outputs, testing, and troubleshooting. Use this as a concise summary for developers, testers, and stakeholders.

## Quick Summary
- Purpose: automated per-image analysis for structural defects, material identification, and biological growth detection.
- UI location: `frontend/src/pages/ImageAnalysis.jsx` (accessible at `/imageanalysis`).
- Backend endpoint: `POST /api/analyze`.
- Typical input: single JPG/PNG image, phone or DSLR photo of infrastructure surface.
- Typical outputs: JSON analysis results, severity scores, detected item locations, downloadable PDF report.

---

## What the Image Analysis Tab Provides
- Damage detection (cracks, spalling, delamination)
- Material classification (concrete, steel, masonry, wood)
- Biological growth detection (moss, algae)
- Severity scoring and recommendations
- PDF report generation (via `pdf_report.py`)

---

## User Flow (UI)
1. Open the Image Analysis page (`/imageanalysis`).
2. Click "Choose File" or drag-and-drop a JPG/PNG image.
3. Optionally select analysis type: `damage`, `material`, `biological`.
4. Click `Analyze`.
5. UI shows progress spinner while uploading and processing.
6. Results appear: list of detected items, severity score (0–10), annotated image preview, and action recommendations.
7. Option to `Download PDF Report` (calls API to generate and return PDF).

UI elements & labels (from `ImageAnalysis.jsx`):
- File input
- Analysis type selector (dropdown)
- Analyze button
- Annotated image preview (thumbnail)
- Results panel (cards or table)
- Download PDF button

---

## Backend Flow (/api/analyze)

Request:
- Method: POST
- Content-Type: multipart/form-data
- Body fields:
  - `image`: binary file (required)
  - `analysis_type`: string (optional, default `damage`)

Processing steps (server-side `finalwebapp_api.py`):
1. Validate file type and size; save temporary file in `uploads/`.
2. Call analysis routine (wrapping functions in `segmentation_with_localisation.py` and/or custom pipelines):
   - Preprocess: resize, normalize, optionally enhance contrast.
   - Run detector/segmentation: YOLOv8 or model weights in `runs/` or `segmentation_model/weights/`.
   - Postprocess: map detections to pixel coordinates, compute bounding boxes and confidence.
   - Compute severity: heuristic or ML model combining area, confidence, and edge density.
3. Create annotated image overlay (heatmap, boxes, labels) for UI preview.
4. Optionally call `pdf_report.py` to produce PDF with images and metrics.
5. Return JSON with `analysis_results`, `severity_score`, `recommendations`, and preview image URL or base64 blob.

Response (example):
```
{
  "analysis_results": [
    {"type":"crack","severity":7.5,"bbox":[120,45,200,90],"confidence":0.92},
    {"type":"corrosion","severity":5.2,"bbox":[220,160,280,240],"confidence":0.88}
  ],
  "severity_score": 7.1,
  "recommendations": ["Schedule detailed inspection","Monitor monthly"]
}
```

---

## Image Types & Example Descriptions
Provide the user with example image descriptions so they can choose good input images.

- Example A — Cracked Concrete Wall
  - Appearance: light-gray concrete with dark linear cracks
  - Good input: high-contrast, even lighting, minimal shadows
  - Expected analysis: multiple crack detections, high severity in concentrated zones

- Example B — Rusted Steel Plate
  - Appearance: orange/brown corrosion patterns with pits and flaking
  - Good input: close-up of corroded area, avoid reflections
  - Expected analysis: corrosion patches, area calculation for pit coverage

- Example C — Masonry with Biological Growth
  - Appearance: greenish moss/algae patches, color differences from masonry
  - Good input: color image showing growth boundaries
  - Expected analysis: biological growth segmentation, coverage percentage, treatment suggestion

Guidance for images:
- Use well-lit photos, avoid extreme shadows
- Keep camera approximately perpendicular to surface if possible
- Use at least 1024×768 for best detection (system will auto-resize)

---

## Output & Interpretation

Primary outputs:
- `analysis_results`: array of detected items with type, bbox, confidence, severity
- `severity_score`: aggregated score 0–10 for the image
- `annotated_preview`: image with boxes, masks, heatmap overlay
- `pdf_report` (optional): multi-page report containing images, metrics, and recommendations

How to interpret:
- Severity 0–3: Minor, monitor
- Severity 4–6: Moderate, schedule inspection
- Severity 7–10: Severe, immediate action recommended

---

## Parameters & Tuning (for advanced users)
- `resize_to`: target resolution for analysis (default 1024). Higher = more accurate, slower.
- `confidence_threshold`: detection threshold for reporting (default 0.5).
- `min_area_px`: minimum pixel area to accept a detection (filters noise).
- `analysis_type`: selects specialized model or postprocessing (damage/material/biological).

These can be exposed in UI as Advanced Settings or provided as query parameters to the API.

---

## Testing & Validation

Automated tests:
- `test_image_analysis.py` (recommended): tests for API response shapes and end-to-end detection using sample images in `reference_images/`.
- Run: `python test_image_analysis.py` (create if not present).

Manual validation:
- Upload sample images from `reference_images/` and verify detections, severity scores, and PDF contents.

---

## Troubleshooting

- No detections: check image contrast; try increasing `resize_to` or reducing `confidence_threshold`.
- False positives: increase `confidence_threshold` and `min_area_px`.
- Slow processing: lower `resize_to` or run model inference on GPU.
- PDF not generated: ensure `wkhtmltopdf` or required PDF library is installed, check `pdf_report.py` logs.

---

## Implementation Notes (developer pointers)
- Models: YOLOv8 weights are kept in `runs/` or `segmentation_model/weights/`.
- Key backend files: `finalwebapp_api.py` (endpoint wiring), `segmentation_with_localisation.py` (detection + localization), `pdf_report.py` (report generator).
- Keep uploaded files in `uploads/` with periodic cleanup.

---

## How the code files use and handle images

These notes explain where image handling occurs and how `finalwebapp.py`, `finalwebapp_api.py`, and the frontend `ImageAnalysis.jsx` interact with images and the analysis pipeline.

- `finalwebapp_api.py` (Flask API):
  - Receives multipart/form-data POST requests at `/api/analyze` and `/api/generate-3d-glb`.
  - Validates the incoming file (type, size), saves a temporary copy under `uploads/`.
  - Extracts query/form parameters (`resize_to`, `height_scale`, `analysis_type`, etc.).
  - Calls backend processing functions (e.g., functions in `segmentation_with_localisation.py`, `image_3d_heightmap.py`, or wrapped helpers) to run detection/segmentation and generate annotated previews.
  - Packages results: JSON `analysis_results`, aggregated `severity_score`, `recommendations`, and either a preview URL (served from `uploads/`) or an inline base64-encoded preview image.
  - For GLB/STL endpoints, calls `generate_3d_glb_from_image()` and returns a binary response with correct MIME type (`model/gltf-binary` or `model/stl`).

- `finalwebapp.py` (application entry / helpers):
  - Acts as a higher-level runner for CLI/integration tasks (when present in the repo).
  - Contains convenience wrappers to call the same pipeline functions used by the API (useful for local testing or generating files without HTTP).
  - Typical helper functions:
    - `run_analysis_local(input_path, out_json)` — loads image, runs analyze pipeline, writes JSON report
    - `generate_glb_local(input_path, output_glb, **params)` — same pipeline used by `/api/generate-3d-glb`
  - Use `finalwebapp.py` when you want to script batch runs or reproduce results locally.

- `frontend/src/pages/ImageAnalysis.jsx` (UI):
  - Manages file input, analysis type selector, and the Analyze button.
  - On Analyze, builds `FormData()` with `image` and optional params, then `fetch()`/`axios.post()` to `/api/analyze`.
  - Receives JSON response and preview image (URL or base64). The preview is displayed in the UI and results shown in a results panel.
  - For PDF report download, calls an endpoint such as `/api/generate-pdf` (or triggers `/api/analyze` with `report=true`) and streams the returned PDF to the browser.

Example frontend POST (JS):
```javascript
const fd = new FormData();
fd.append('image', fileInput.files[0]);
fd.append('analysis_type', 'damage');

fetch('/api/analyze', { method: 'POST', body: fd })
  .then(res => res.json())
  .then(data => {
    // data.analysis_results, data.severity_score, data.preview (base64)
  });
```

Example backend call (Python requests):
```python
import requests

with open('bridge_crack.jpg','rb') as f:
    r = requests.post('http://localhost:5002/api/analyze', files={'image': f}, data={'analysis_type':'damage'})
    print(r.json())
```

---

## Per-image descriptions (example images)

These sample image descriptions are recommended text to show in the UI (or documentation) for each example image the project uses.

- `bridge_crack.jpg` — Cracked concrete beam
  - Description: Close-up of a concrete bridge beam showing multiple longitudinal and transverse cracks. Lighting is even — good contrast between crack lines and surface.
  - Best practices: Use perpendicular camera angle, avoid motion blur. Increase resolution to 1500 px if available for more accurate localization.
  - Expected analysis: Multiple crack detections with high confidence; severity concentrated along longitudinal streaks. Output: several `crack` items (bbox + mask) and aggregated severity ~6–9 depending on crack width.

- `corrosion_surface.jpg` — Rusted steel plate with pitting
  - Description: Steel surface exhibiting orange/brown corrosion patches and localized pitting. Texture and color variation between rust and intact metal.
  - Best practices: Avoid strong specular highlights; use cross-polarized lighting if available. Capture multiple overlapping shots for larger areas.
  - Expected analysis: Corrosion regions segmented; per-region area reported and pit density measurement. Severity often moderate (4–7) depending on area coverage.

- `facade_damage.jpg` — Building facade weathering and spalling
  - Description: Masonry facade with flaking, discoloration, and small spalls. Good lighting with visible surface texture.
  - Best practices: Capture from orthogonal angle to avoid foreshortening; provide scale reference (ruler) for quantitative reports.
  - Expected analysis: Spalling and flake detections; material classification may label masonry; recommendations include targeted inspection for loose material.

Additional common image examples (mention in UI):
- `bridge_crack.jpg` (alternate crop) — long-span crack network
- `tank_corrosion.jpg` — large-area corrosion mapping
- `masonry_wall.jpg` — historical building crack monitoring

UI text template for any image (short):
"Upload a clear, well-lit image~ (prefer perpendicular camera angle). For best results, include a scale reference and avoid heavy shadows or reflections."

---

If you'd like, I can now:
- Add inline annotated sample images to this file (base64 thumbnails) so the UI doc is visual.
- Create a `test_image_analysis.py` that performs an end-to-end API call against the local server using one sample image and asserts expected JSON fields.
- Update `ImageAnalysis.jsx` to show per-image tip text based on the selected example.

