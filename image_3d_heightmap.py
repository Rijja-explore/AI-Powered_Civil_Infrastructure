"""
================================================================================
  INFRASTRUCTURE CRACK 3D VISUALIZATION PIPELINE
  Transform 2D crack images into interactive 3D models for web viewing
================================================================================

MAIN OBJECTIVE:
    Take a normal 2D image of a crack (or any surface), process it into a
    clean and enhanced representation, and convert it into a 3D height-based
    model that you can view, rotate, and zoom inside a React web app.

PIPELINE WORKFLOW:
    1. INPUT: Normal 2D image (e.g., wall crack photo)
    
    2. IMAGE PROCESSING (Function: make_processed_image)
       • Convert to grayscale
       • Generate heatmap from intensity values
       • Extract edges using Canny algorithm
       • Combine all three into one enhanced overlay image
         → makes crack clearer and reduces noise
         → this becomes the COLOR TEXTURE for the 3D model
    
    3. 3D MODEL GENERATION (Function: make_3d_glb)
       • Convert grayscale → height values (invert for cracks to pop out)
       • Build 3D mesh using those height values
       • Apply color from processed overlay image
       • Center mesh for proper web display
       • Export as fully-colored GLB 3D file
    
    4. FRONTEND DISPLAY (React + Three.js)
       • Load GLB model in web viewer
       • User can ROTATE, ZOOM, INSPECT the crack in 3D
       • Interactive exploration without expensive hardware

WHY THIS IS USEFUL:
    ✓ Visualizes crack depth and structure in 3D
    ✓ Helps in infrastructure inspection and documentation
    ✓ Enables interactive 3D viewing in standard web browser
    ✓ Fast pipeline with NO GPU required
    ✓ Converts simple 2D photos into professional 3D models

DEPENDENCIES:
    pip install pillow numpy scipy opencv-python trimesh
================================================================================
"""

import numpy as np
from PIL import Image
import cv2
from scipy.ndimage import gaussian_filter
import trimesh
import os


# ==============================================================
# FUNCTION 1: CREATE HEATMAP + CANNY + ORIGINAL OVERLAY
# ==============================================================

def make_processed_image(input_path, resize_to=(300, 300)):
    """
    Transform 2D crack image into enhanced overlay for coloring the 3D model.
    
    PROCESS:
        1. Load image and resize
        2. Convert to grayscale (for height calculation)
        3. Generate heatmap (shows intensity variations)
        4. Extract edges (highlights cracks with Canny algorithm)
        5. Combine all three into one enhanced image
           → Reduces noise
           → Makes cracks clearer
           → Becomes the COLOR TEXTURE for 3D mesh
    
    Args:
        input_path: Path to input 2D image
        resize_to: Resolution tuple (width, height) for processing
    
    Returns:
        combined: Enhanced RGB image (H, W, 3) - used as vertex colors
        gray: Grayscale image (H, W) - used to compute heights
    """
    # --- Load image and resize ---
    img = Image.open(input_path).convert("RGB")
    img = img.resize(resize_to, Image.LANCZOS)
    img_np = np.array(img)                     # (H, W, 3), uint8

    # --- Grayscale for depth/height ---
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)  # (H, W), uint8

    # --- Heatmap from grayscale ---
    heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)   # BGR
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)    # convert to RGB

    # --- Canny edges ---
    edges = cv2.Canny(gray, 80, 160)          # (H, W), 0–255
    edges_rgb = np.zeros_like(img_np)
    edges_rgb[..., 0] = edges                 # put edges in RED channel

    # --- Combine: original + heatmap + edges ---
    combined = (
        0.6 * img_np.astype(float) +       # base image (60%)
        0.3 * heatmap.astype(float) +      # color boost (30%)
        0.7 * edges_rgb.astype(float)      # strong cracks (70%)
    )
    combined = np.clip(combined, 0, 255).astype(np.uint8)

    combined_img = Image.fromarray(combined)
    combined_img.save("processed_overlay.png")
    # combined_img.show()  # Optional: show preview

    return combined, gray


# ==============================================================
# FUNCTION 2: CONVERT TO 3D HEIGHTMAP + ADD TEXTURE COLORS
# ==============================================================

def make_3d_glb(
    gray_img,
    color_img,
    output_path="output.glb",
    height_scale=10.0,
    smooth_sigma=2.0,
    flip_y=True
):
    """
    Convert 2D images into a 3D textured GLB model for web viewing.
    
    PROCESS:
        1. Invert grayscale so dark cracks become HEIGHT (pop out)
        2. Clamp small values to reduce noise in background
        3. Apply Gaussian smoothing for smooth surfaces
        4. Build 3D mesh vertices and triangle faces
        5. Apply color from processed overlay as vertex colors
        6. Center mesh for proper web display
        7. Export as GLB (binary GLTF format)

    Args:
        gray_img    : (H, W) uint8 - grayscale image for heights
        color_img   : (H, W, 3) uint8 - color from processed overlay
        output_path : path to .glb file to save
        height_scale: multiplier for 3D height (larger = more pronounced)
        smooth_sigma: Gaussian blur strength for smooth surface (>0 = less noise)
        flip_y      : flip Y axis so mesh appears upright in viewers
    """

    # --- convert & invert so cracks (dark) become higher ---
    gray = gray_img.astype(float)
    gray = 255.0 - gray      # dark cracks → high values

    # optional: flatten background a bit
    arr_min, arr_max = gray.min(), gray.max()
    norm = (gray - arr_min) / (arr_max - arr_min + 1e-9)

    # clamp very small values (background) to reduce noise
    norm[norm < 0.2] = 0.2

    # smooth
    if smooth_sigma > 0:
        norm = gaussian_filter(norm, sigma=smooth_sigma)

    height = norm * height_scale
    h, w = height.shape

    # --- Create vertices (grid) ---
    verts = np.zeros((h * w, 3), dtype=float)
    for y in range(h):
        for x in range(w):
            z = float(height[y, x])
            idx = y * w + x
            if flip_y:
                verts[idx] = [x, (h - 1 - y), z]
            else:
                verts[idx] = [x, y, z]

    # --- Create faces (two triangles per pixel-square) ---
    faces = []
    for y in range(h - 1):
        for x in range(w - 1):
            i = y * w + x
            a = i
            b = i + 1
            c = i + w
            d = i + w + 1
            faces.append([a, b, c])
            faces.append([b, d, c])
    faces = np.array(faces, dtype=np.int64)

    # --- Flatten color image into vertex colors (RGBA) ---
    color_img = color_img.reshape(-1, 3)
    colors = np.hstack([color_img, np.full((color_img.shape[0], 1), 255, dtype=np.uint8)])

    # --- Build mesh & center it ---
    mesh = trimesh.Trimesh(
        vertices=verts,
        faces=faces,
        vertex_colors=colors,
        process=False
    )

    # center the mesh so it’s not off to one side in React
    mesh.vertices -= mesh.vertices.mean(axis=0)

    mesh.export(output_path)
    print(f"[SUCCESS] Saved 3D GLB model to: {os.path.abspath(output_path)}")


# ==============================================================
# WRAPPER FUNCTIONS FOR API INTEGRATION
# Purpose: High-level interfaces for Flask backend
# ==============================================================

def generate_3d_glb_from_image(
    input_image_path,
    output_glb_path,
    resize_to=(300, 300),
    height_scale=12.0,
    smooth_sigma=1.2
):
    """
    High-level function to generate 3D GLB from image file.
    
    Used by Flask API to process uploaded images and generate 3D models.
    
    Args:
        input_image_path: Path to input 2D image
        output_glb_path: Path for output GLB file
        resize_to: Resolution tuple (width, height) for processing
        height_scale: Height multiplier (larger = more pronounced cracks)
        smooth_sigma: Gaussian smoothing strength (higher = smoother)
    
    Returns:
        output_glb_path: Path to generated file
    """
    # Process image (creates overlay + grayscale)
    combined, gray = make_processed_image(
        input_image_path,
        resize_to=resize_to
    )
    
    # Generate 3D model with vertex colors
    make_3d_glb(
        gray,
        combined,
        output_path=output_glb_path,
        height_scale=height_scale,
        smooth_sigma=smooth_sigma,
        flip_y=True
    )
    
    return output_glb_path


def generate_3d_glb_from_arrays(
    height_array,
    color_array,
    output_glb_path,
    height_scale=12.0,
    smooth_sigma=1.2
):
    """
    Generate 3D GLB directly from numpy arrays.
    
    For advanced cases where preprocessing is already done externally.
    
    Args:
        height_array: 2D numpy array for heights
        color_array: 3D numpy array for colors (H x W x 3)
        output_glb_path: Path for output GLB
        height_scale: Height scale factor
        smooth_sigma: Smoothing parameter
    
    Returns:
        output_glb_path: Path to generated file
    """
    # Ensure proper data types
    height_array = np.array(height_array).astype(float)
    color_array = np.array(color_array).astype(np.uint8)
    
    make_3d_glb(
        height_array,
        color_array,
        output_path=output_glb_path,
        height_scale=height_scale,
        smooth_sigma=smooth_sigma,
        flip_y=True
    )
    
    return output_glb_path
