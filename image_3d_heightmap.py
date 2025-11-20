"""
FINAL PIPELINE: 2D image → processed overlay → 3D colored GLB heightmap

What it does:
    1) Load a normal 2D image
    2) Create:
        - heatmap from grayscale
        - Canny edge map
        - overlay = original + heatmap + edges
    3) Use grayscale as heightmap → build 3D mesh
    4) Use overlay image as vertex colors
    5) Export .glb you can view & rotate (e.g. Blender, Three.js, React Three Fiber)
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
    Process input image to create a colored texture map with Canny edges overlaid on heatmap.
    
    Creates striking visualization by:
    1. Generating colorful JET heatmap as background (blue→green→yellow→red)
    2. Detecting Canny edges (sharp boundaries)
    3. Overlaying edges as dark/magenta lines ON TOP of heatmap
    
    This creates the effect seen in thermal/satellite imagery where structure
    boundaries are clearly visible over the colored temperature/elevation map.
    
    Args:
        input_path: Path to input image
        resize_to: Tuple (width, height) for resizing
    
    Returns:
        combined: RGB image with heatmap + Canny edges overlay (final texture for 3D)
        gray: Grayscale version for heightmap Z-coordinate generation
    """
    
    # --- Load and resize image ---
    img = Image.open(input_path).convert("RGB")
    img = img.resize(resize_to, Image.LANCZOS)
    img_np = np.array(img, dtype=np.uint8)    # (H, W, 3), uint8

    # --- Convert to grayscale (used for both heatmap and heightmap) ---
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)  # (H, W), uint8

    # --- Create colorful JET heatmap background ---
    heatmap_bgr = cv2.applyColorMap(gray, cv2.COLORMAP_JET)   # BGR format from intensity
    heatmap_rgb = cv2.cvtColor(heatmap_bgr, cv2.COLOR_BGR2RGB)  # Convert to RGB

    # --- Detect Canny edges (sharp, high-contrast boundaries) ---
    edges_binary = cv2.Canny(gray, 80, 160)   # (H, W), binary: 255 where edge, 0 elsewhere

    # --- Create edge overlay with magenta/purple tone for striking contrast ---
    # Start with the heatmap as base
    combined = heatmap_rgb.astype(np.float32)
    
    # Where edges exist, overlay with dark magenta/purple
    # This creates the striking effect of dark lines over colored background
    edge_mask = edges_binary / 255.0  # Convert to 0-1 range
    edge_mask = edge_mask[:, :, np.newaxis]  # Add channel dimension (H, W, 1)
    
    # Define edge color: dark purple/magenta for maximum contrast
    edge_color = np.array([80, 0, 150], dtype=np.float32)  # Dark purple: R=80, G=0, B=150
    
    # Blend: where edge_mask=1, use edge_color; where edge_mask=0, use heatmap
    combined = combined * (1 - edge_mask) + edge_color * edge_mask
    
    # Clamp and convert back to uint8
    combined = np.clip(combined, 0, 255).astype(np.uint8)

    return combined, gray


# ==============================================================
# FUNCTION 2: CONVERT TO 3D HEIGHTMAP + ADD TEXTURE COLORS
# ==============================================================

def make_3d_glb(
    gray_img,
    color_img,
    output_path="output.glb",
    height_scale=12.0,
    smooth_sigma=1.2,
    flip_y=True
):
    """
    Converts grayscale heightmap → 3D mesh (GLB) with vertex colors from color_img.

    Args:
        gray_img    : (H, W) uint8 or float, used as height
        color_img   : (H, W, 3) uint8, used as vertex colors
        output_path : path to .glb file to save
        height_scale: how tall the displacement will be
        smooth_sigma: Gaussian blur strength (0 = no smoothing)
        flip_y      : flip Y axis so mesh appears upright in many viewers
    """

    # Ensure numpy arrays
    gray = np.array(gray_img).astype(float)
    color = np.array(color_img).astype(np.uint8)

    h, w = gray.shape
    assert color.shape[0] == h and color.shape[1] == w, \
        "gray_img and color_img must have same height/width"

    # --- Smooth height to reduce noise ---
    if smooth_sigma > 0:
        gray = gaussian_filter(gray, sigma=smooth_sigma)

    # --- Normalize height 0..1 ---
    arr_min, arr_max = gray.min(), gray.max()
    norm = (gray - arr_min) / (arr_max - arr_min + 1e-9)
    height = norm * height_scale

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
    color_flat = color.reshape(-1, 3)                 # (N, 3)
    alpha = np.full((color_flat.shape[0], 1), 255,
                    dtype=np.uint8)                   # (N, 1)
    colors = np.hstack([color_flat, alpha])           # (N, 4)

    # --- Build mesh & export GLB ---
    mesh = trimesh.Trimesh(
        vertices=verts,
        faces=faces,
        vertex_colors=colors,
        process=False
    )

    mesh.export(output_path)
    print(f"[INFO] Saved 3D GLB model to: {os.path.abspath(output_path)}")


# ==============================================================
# WRAPPER FUNCTIONS FOR API INTEGRATION
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
    
    Args:
        input_image_path: Path to input image
        output_glb_path: Path for output GLB file
        resize_to: Resolution tuple (width, height)
        height_scale: Height multiplier
        smooth_sigma: Gaussian smoothing strength
    
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
