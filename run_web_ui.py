#!/usr/bin/env python3
"""
Weapons Detection Web UI - Startup Script
This script checks dependencies and launches the web application
"""

import os
import sys
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'flask',
        'ultralytics', 
        'opencv-python',
        'numpy',
        'werkzeug'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        spec = importlib.util.find_spec(package)
        if spec is None:
            missing_packages.append(package)
        else:
            print(f"✅ {package} is installed")
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✅ All packages installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages. Please run:")
            print(f"pip install {' '.join(missing_packages)}")
            return False
    
    return True

def check_model():
    """Check if the trained model exists"""
    model_path = './runs/detect/Normal_Compressed/weights/best.pt'
    
    if os.path.exists(model_path):
        print(f"✅ Model found: {model_path}")
        return True
    else:
        print(f"⚠️  Warning: Model not found at {model_path}")
        print("The web UI will still work but detection features may not function properly.")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        'uploads',
        'static/results',
        'templates'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Directory ready: {directory}")

def main():
    """Main startup function"""
    print("🔫 Weapons Detection Web UI - Startup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check model
    check_model()
    
    # Create directories
    create_directories()
    
    print("\n🚀 Starting web server...")
    print("=" * 50)
    
    try:
        # Import and run the Flask app
        from app import app
        
        print("✅ Web UI is ready!")
        print("🌐 Open your browser and go to: http://localhost:5000")
        print("📱 The interface is mobile-friendly")
        print("⏹️  Press Ctrl+C to stop the server")
        print("=" * 50)
        
        # Run the Flask app
        app.run(debug=False, host='0.0.0.0', port=5000)
        
    except ImportError as e:
        print(f"❌ Error importing app: {e}")
        print("Make sure app.py exists in the current directory")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Web UI stopped by user")
    except Exception as e:
        print(f"❌ Error starting web UI: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 