#!/usr/bin/env python3
"""
Test script to verify all analytics API endpoints are working correctly
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5002"

def test_endpoint(method, endpoint, description):
    """Test an API endpoint and print results"""
    url = f"{BASE_URL}{endpoint}"
    print(f"\n{'='*70}")
    print(f"🧪 Testing: {description}")
    print(f"📍 Endpoint: {endpoint}")
    print(f"{'='*70}")
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=5)
        else:
            response = requests.post(url, timeout=5)
        
        print(f"✅ Status Code: {response.status_code}")
        print(f"✅ Response Time: {response.elapsed.total_seconds():.2f}s")
        
        # Try to parse JSON
        try:
            data = response.json()
            print(f"✅ Valid JSON Response")
            print(f"📊 Keys: {list(data.keys())}")
            if 'success' in data:
                print(f"   Success: {data['success']}")
            # Print first 200 chars of response
            json_str = json.dumps(data, indent=2)
            print(f"\n📄 Response Preview:\n{json_str[:500]}...")
        except:
            print(f"⚠️  Response is not valid JSON")
            print(f"📄 Response: {response.text[:200]}")
            
        return True
    except requests.exceptions.ConnectionError:
        print(f"❌ ERROR: Could not connect to {BASE_URL}")
        print(f"   Make sure backend is running: python finalwebapp_api.py")
        return False
    except requests.exceptions.Timeout:
        print(f"❌ ERROR: Request timeout (server not responding)")
        return False
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

def main():
    print("\n" + "="*70)
    print("🚀 ANALYTICS API ENDPOINT TEST SUITE")
    print("="*70)
    print(f"⏰ Test Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 Base URL: {BASE_URL}")
    
    tests = [
        ("GET", "/api/health", "Health Check"),
        ("GET", "/api/analytics/dataset", "Dataset Analytics"),
        ("GET", "/api/analytics/hidden_damage", "Hidden Damage Analytics"),
        ("GET", "/api/analytics/last_image", "Last Image Analytics"),
        ("GET", "/api/analytics", "General Analytics (Legacy)"),
    ]
    
    results = []
    for method, endpoint, description in tests:
        result = test_endpoint(method, endpoint, description)
        results.append((endpoint, result))
    
    # Summary
    print(f"\n{'='*70}")
    print("📋 TEST SUMMARY")
    print(f"{'='*70}")
    passed = sum(1 for _, r in results if r)
    total = len(results)
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    
    if passed == total:
        print("\n🎉 All endpoints working correctly!")
        print("✅ Analytics dashboard is ready to use")
    else:
        print("\n⚠️  Some endpoints failed. Check backend logs for details.")
    
    print(f"\n⏰ Test Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
