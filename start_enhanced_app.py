#!/usr/bin/env python3
"""
InfraVision AI - Enhanced Startup Script
Advanced startup script with comprehensive analytics and professional UI
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path
import threading

def print_banner():
    """Print enhanced application banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║        🏗️  INFRAVISION AI - INTELLIGENT INFRASTRUCTURE MONITORING           ║
║                                                                              ║
║     🔬 Advanced Data Analytics Suite                                        ║
║     🎨 Professional Glass-UI Design                                         ║
║     🧠 Enhanced Computer Vision                                              ║
║     📈 Comprehensive Statistical Analysis                                   ║
║     ⚡ Real-time Infrastructure Monitoring                                   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

🚀 Starting InfraVision AI Application Suite...

📊 ADVANCED ANALYTICS FEATURES:
   ✅ Descriptive Analytics & Visualization
   ✅ Inferential Statistics & Hypothesis Testing
   ✅ Analysis of Variance (ANOVA)
   ✅ Predictive Analytics & Machine Learning
   ✅ Comprehensive Statistical Reporting

🎨 ENHANCED UI FEATURES:
   ✅ Professional Glass-Morphism Design
   ✅ InfraVision AI Branding
   ✅ Creative Infrastructure Backgrounds
   ✅ Enhanced Visual Components
   ✅ Real-time Status Indicators

🏗️ INFRASTRUCTURE MONITORING:
   ✅ Structural Health Assessment
   ✅ Crack Detection & Analysis
   ✅ Material Classification
   ✅ Environmental Impact Analysis
   ✅ Real-time Monitoring Dashboard
"""
    print(banner)

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'flask', 'streamlit', 'opencv-python', 'ultralytics', 
        'numpy', 'pandas', 'scipy', 'scikit-learn', 'matplotlib', 
        'seaborn', 'statsmodels', 'plotly'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            missing.append(package)
            print(f"❌ {package} - Missing")
    
    if missing:
        print(f"\n📦 Installing missing packages: {', '.join(missing)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing)
            print("✅ All dependencies installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies. Please install manually.")
            return False
    
    return True

def start_backend_server():
    """Start the Flask API backend"""
    print("\n🔧 Starting Flask API Backend...")
    try:
        backend_process = subprocess.Popen([
            sys.executable, 'finalwebapp_api.py'
        ], cwd=Path(__file__).parent)
        print("✅ Flask API Backend started successfully!")
        return backend_process
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        return None

def start_streamlit_app():
    """Start the Streamlit application"""
    print("\n🌐 Starting Streamlit Application...")
    try:
        streamlit_process = subprocess.Popen([
            sys.executable, '-m', 'streamlit', 'run', 'finalwebapp.py', 
            '--server.port=8501', '--server.headless=true'
        ], cwd=Path(__file__).parent)
        print("✅ Streamlit Application started successfully!")
        return streamlit_process
    except Exception as e:
        print(f"❌ Failed to start Streamlit: {e}")
        return None

def start_react_frontend():
    """Start the React frontend development server"""
    print("\n⚛️  Starting React Frontend...")
    frontend_path = Path(__file__).parent / 'frontend'
    
    if not frontend_path.exists():
        print("❌ Frontend directory not found!")
        return None
    
    try:
        # Check if npm is available
        subprocess.check_call(['npm', '--version'], stdout=subprocess.DEVNULL)
        
        # Install dependencies if needed
        if not (frontend_path / 'node_modules').exists():
            print("📦 Installing React dependencies...")
            subprocess.check_call(['npm', 'install'], cwd=frontend_path)
        
        # Start React development server
        react_process = subprocess.Popen([
            'npm', 'start'
        ], cwd=frontend_path)
        print("✅ React Frontend started successfully!")
        return react_process
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  npm not found. Skipping React frontend.")
        return None

def open_applications():
    """Open applications in browser after startup delay"""
    print("\n⏳ Waiting for servers to initialize...")
    time.sleep(5)
    
    urls = [
        "http://localhost:8501",  # Streamlit
        "http://localhost:3000",  # React (if available)
        "http://localhost:5001/api/health",  # API Health Check
    ]
    
    print("\n🌐 Opening applications in browser...")
    for url in urls:
        try:
            webbrowser.open(url)
            print(f"✅ Opened: {url}")
        except Exception as e:
            print(f"⚠️  Could not open {url}: {e}")

def display_access_info():
    """Display access information for all services"""
    info = """
🌐 INFRAVISION AI APPLICATION ACCESS:

⚛️  REACT FRONTEND (Primary Interface):
   🔗 URL: http://localhost:3000
   📝 Features: InfraVision AI Interface, Modern Glass-UI, Real-time monitoring

📊 STREAMLIT DASHBOARD:
   🔗 URL: http://localhost:8501
   📝 Features: Complete analytics suite, file upload, comprehensive reporting

🔧 FLASK API BACKEND:
   🔗 URL: http://localhost:5001
   📝 Endpoints: /api/analyze, /api/health, /api/analytics
   📋 Health Check: http://localhost:5001/api/health

📊 ADVANCED ANALYTICS FEATURES:
   • Descriptive Analytics & Data Visualization
   • Inferential Statistics & Hypothesis Testing
   • Analysis of Variance (ANOVA)
   • Predictive Analytics & Machine Learning
   • Comprehensive Statistical Reporting
   • Real-time Data Processing

🏗️ INFRASTRUCTURE MONITORING CAPABILITIES:
   • Structural Health Assessment
   • Crack Detection & Classification
   • Material Analysis & Identification
   • Environmental Impact Assessment
   • Real-time Camera Monitoring
   • Video Stream Analysis

💡 TIPS:
   • Use Ctrl+C to stop all services
   • Check console for any errors
   • Ensure camera is connected for real-time monitoring
   • Upload images/videos through the interface for analysis

🆘 TROUBLESHOOTING:
   • If services don't start, check port availability
   • Ensure all dependencies are installed
   • Check Python version compatibility (3.8+)
   • Verify camera permissions for real-time monitoring
"""
    print(info)

def main():
    """Main application startup function"""
    print_banner()
    
    # Check system requirements
    if not check_python_version():
        return
    
    print("\n🔍 Checking dependencies...")
    if not check_dependencies():
        return
    
    processes = []
    
    try:
        # Start backend services
        backend = start_backend_server()
        if backend:
            processes.append(backend)
        
        streamlit = start_streamlit_app()
        if streamlit:
            processes.append(streamlit)
        
        react = start_react_frontend()
        if react:
            processes.append(react)
        
        # Open applications in browser
        threading.Thread(target=open_applications, daemon=True).start()
        
        # Display access information
        display_access_info()
        
        print("\n🎉 All services started successfully!")
        print("🔄 Press Ctrl+C to stop all services...")
        
        # Keep the script running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down services...")
        for process in processes:
            try:
                process.terminate()
                process.wait(timeout=5)
            except:
                process.kill()
        print("✅ All services stopped successfully!")
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        for process in processes:
            try:
                process.kill()
            except:
                pass

if __name__ == "__main__":
    main()