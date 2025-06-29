#!/usr/bin/env python3
"""
Demo script for the Weapons Detection Web UI
This script demonstrates how to use the web interface
"""

import os
import webbrowser
import time
import requests
from pathlib import Path

def check_web_ui_status():
    """Check if the web UI is running"""
    try:
        response = requests.get('http://localhost:5000/health', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Web UI is running!")
            print(f"   Status: {data['status']}")
            print(f"   Model: {data['model']}")
            return True
    except requests.exceptions.RequestException:
        pass
    return False

def open_web_ui():
    """Open the web UI in the default browser"""
    url = "http://localhost:5000"
    print(f"🌐 Opening web UI at: {url}")
    webbrowser.open(url)

def test_with_sample_image():
    """Test the web UI with the existing sample image"""
    sample_image = "./Results/teste.jpg"
    
    if not os.path.exists(sample_image):
        print(f"❌ Sample image not found: {sample_image}")
        return False
    
    print(f"📸 Testing with sample image: {sample_image}")
    
    try:
        with open(sample_image, 'rb') as f:
            files = {'file': f}
            response = requests.post('http://localhost:5000/upload', files=files, timeout=30)
            
        if response.status_code == 200:
            result = response.json()
            print("✅ Test successful!")
            print(f"   Total detections: {result.get('total_detections', 0)}")
            if 'detections' in result:
                print(f"   Objects found: {len(result['detections'])}")
                for detection in result['detections']:
                    print(f"     - {detection['class']}: {detection['confidence']:.2f}")
            return True
        else:
            print(f"❌ Test failed: {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

def main():
    """Main demo function"""
    print("🎬 Weapons Detection Web UI - Demo")
    print("=" * 50)
    
    # Check if web UI is running
    if not check_web_ui_status():
        print("❌ Web UI is not running!")
        print("Please start the web UI first:")
        print("   python run_web_ui.py")
        print("   or")
        print("   python app.py")
        return
    
    # Open web UI in browser
    open_web_ui()
    
    print("\n📋 Demo Instructions:")
    print("1. The web UI should now be open in your browser")
    print("2. You can upload images or videos for weapon detection")
    print("3. Try dragging and dropping files onto the upload area")
    print("4. Watch the real-time processing and results")
    
    # Wait a moment for browser to open
    time.sleep(2)
    
    # Test with sample image
    print("\n🧪 Running automated test...")
    if test_with_sample_image():
        print("✅ Automated test completed successfully!")
    else:
        print("⚠️  Automated test failed, but you can still use the web UI manually")
    
    print("\n🎯 Features to try:")
    print("• Upload different image formats (JPG, PNG, GIF)")
    print("• Upload video files (MP4, AVI, MOV)")
    print("• Drag and drop files directly")
    print("• View detailed detection statistics")
    print("• Download processed results")
    
    print("\n🔧 Tips:")
    print("• Keep file sizes under 16MB for best performance")
    print("• Processing time depends on file size and complexity")
    print("• Results are automatically saved in static/results/")
    print("• The interface is mobile-friendly")
    
    print("\n🚀 Happy detecting!")

if __name__ == '__main__':
    main() 