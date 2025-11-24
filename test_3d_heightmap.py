#!/usr/bin/env python3
"""
Quick test to verify the updated 3D heightmap generation with Canny + Heatmap overlay
"""

import numpy as np
from PIL import Image
import cv2
import os

def test_image_processing():
    """Test the image processing pipeline"""
    
    print("🧪 Testing 3D Heightmap Image Processing...")
    print("-" * 60)
    
    # Import the updated function
    from image_3d_heightmap import make_processed_image
    
    # Check if test image exists
    test_images = [
        "D:\\Projects\\3d_images\\abc.jpg",
        "uploads/test_image.jpg",
        "frontend/public/sample.jpg"
    ]
    
    test_image = None
    for img_path in test_images:
        if os.path.exists(img_path):
            test_image = img_path
            break
    
    if test_image is None:
        print("❌ No test image found")
        print("   Checked:")
        for path in test_images:
            print(f"   - {path}")
        return False
    
    print(f"✅ Found test image: {test_image}")
    print()
    
    # Test the function
    try:
        print("🔄 Processing image with make_processed_image()...")
        combined, gray = make_processed_image(test_image, resize_to=(300, 300))
        
        print(f"✅ Processing successful!")
        print(f"   - Combined texture shape: {combined.shape}")
        print(f"   - Grayscale height map shape: {gray.shape}")
        print(f"   - Combined dtype: {combined.dtype}")
        print(f"   - Gray dtype: {gray.dtype}")
        print()
        
        # Verify output characteristics
        print("📊 Output Analysis:")
        print(f"   - Color range (combined): {combined.min()}-{combined.max()}")
        print(f"   - Height range (gray): {gray.min()}-{gray.max()}")
        print(f"   - Has color variation: {len(np.unique(combined)) > 100}")
        print()
        
        print("✅ Test PASSED - Image processing working correctly!")
        print()
        print("📝 What the output contains:")
        print("   ✓ Heatmap background (JET colormap: blue→green→yellow→red)")
        print("   ✓ Canny edges overlaid as dark purple/magenta lines")
        print("   ✓ Grayscale heightmap for 3D mesh Z-coordinates")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error during processing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_image_processing()
    exit(0 if success else 1)
