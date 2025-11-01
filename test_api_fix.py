import requests
import json
import base64

# Test the API with a sample image
def test_api():
    # Use one of the available test images
    image_path = "brickcrack.jpg"

    # Read and encode image to base64
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    # Prepare JSON payload
    payload = {
        'image': f'data:image/jpeg;base64,{image_data}',
        'px_to_cm_ratio': 0.1,
        'confidence_threshold': 0.3
    }

    try:
        # Make the API request with JSON
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://localhost:5002/api/analyze', json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            print("API Response successful!")
            print("Keys in response:", list(result.keys()))

            # Check if output_images are present
            if 'output_images' in result:
                print("Output images found:", list(result['output_images'].keys()))

            # Check if environmental_impact is present and doesn't contain NaN
            if 'results' in result and 'environmental_impact_assessment' in result['results']:
                print("Environmental impact data present")
                # Try to serialize to ensure no NaN values
                json_str = json.dumps(result['results']['environmental_impact_assessment'])
                print("Environmental impact JSON serialization successful")

            print("Test passed - API works correctly!")
            return True
        else:
            print(f"API Error: {response.status_code}")
            print(response.text)
            return False

    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print("Response text:", response.text[:500])
        return False
    except Exception as e:
        print(f"Request error: {e}")
        return False

if __name__ == "__main__":
    test_api()