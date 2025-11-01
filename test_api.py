import requests
import base64
import json
import time

def test_api():
    # Start the server in background
    import subprocess
    import sys
    import os

    print("Starting Flask server...")
    server_process = subprocess.Popen([sys.executable, 'finalwebapp_api.py'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    cwd=os.getcwd())

    # Wait for server to start
    time.sleep(10)

    try:
        # Test health endpoint
        print("Testing health endpoint...")
        response = requests.get('http://localhost:5002/api/health', timeout=10)
        print(f"Health check: {response.status_code}")
        if response.status_code == 200:
            print("✅ Health endpoint working")

        # Test analyze endpoint with a simple image
        print("Testing analyze endpoint...")

        # Create a minimal test image (small PNG)
        # This is a 1x1 transparent PNG encoded in base64
        test_image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=='

        data = {
            'image': test_image,
            'px_to_cm_ratio': 0.1,
            'confidence_threshold': 0.3
        }

        response = requests.post('http://localhost:5002/api/analyze', json=data, timeout=60)
        print(f"Analyze response: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("✅ Analysis successful!")
            print(f"Status: {result.get('status')}")
            print(f"Message: {result.get('message')[:100]}...")

            # Check if comprehensive data science results are present and JSON serializable
            if 'results' in result and 'data_science_insights' in result['results']:
                ds_insights = result['results']['data_science_insights']
                if 'comprehensive_data_science' in ds_insights:
                    comp_ds = ds_insights['comprehensive_data_science']
                    print("✅ Comprehensive data science results are JSON serializable")
                    print(f"Keys in comprehensive results: {list(comp_ds.keys())[:5]}...")
                else:
                    print("⚠️ No comprehensive data science results found")
            else:
                print("⚠️ No data science insights found")

        else:
            print(f"❌ Analysis failed: {response.text}")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

    finally:
        # Stop the server
        print("Stopping server...")
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    test_api()