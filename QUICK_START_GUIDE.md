# 🚀 Weapons Detection System - Quick Start Guide

Welcome to your professional Weapons and Knife Detection System! This guide will help you get started quickly with both the command-line tools and the new web interface.

## 📋 What You Have

Your project now includes:

1. **🔧 Command-Line Tools** (Original)
   - `detecting-images.py` - Interactive detection script
   - `test_detection.py` - Quick test with sample image
   - `preprocessing-images.py` - Image preprocessing utilities

2. **🌐 Modern Web UI** (New!)
   - Beautiful, responsive web interface
   - Drag-and-drop file upload
   - Real-time processing feedback
   - Mobile-friendly design

## 🎯 Quick Start Options

### Option 1: Web UI (Recommended for Beginners)
```bash
# Start the web interface
python run_web_ui.py

# Then open your browser to: http://localhost:5000
```

### Option 2: Command Line (For Advanced Users)
```bash
# Test the system
python test_detection.py

# Interactive mode
python detecting-images.py
```

### Option 3: Demo Mode
```bash
# Start web UI first, then run demo
python run_web_ui.py
# In another terminal:
python demo_web_ui.py
```

## 🌐 Web UI Features

### ✨ What You Can Do
- **Upload Images**: JPG, PNG, GIF, BMP (up to 16MB)
- **Upload Videos**: MP4, AVI, MOV, MKV (up to 16MB)
- **Drag & Drop**: Simply drag files onto the upload area
- **Real-time Processing**: Watch progress bars and status updates
- **Detailed Results**: See detection statistics and bounding boxes
- **Mobile Friendly**: Works on phones, tablets, and desktops

### 🎨 Interface Highlights
- **Modern Design**: Gradient backgrounds and smooth animations
- **Professional Look**: Clean, intuitive interface
- **Responsive**: Adapts to any screen size
- **Dark Mode Support**: Automatically adapts to system preferences

## 🔧 Command Line Features

### Interactive Mode
```bash
python detecting-images.py
```
Choose from:
1. **Image Detection** - Process any image file
2. **Video Detection** - Process video files
3. **Real-time Display** - Show results in window
4. **Exit** - Close the application

### Quick Test
```bash
python test_detection.py
```
- Uses the existing test image
- Shows results in a window
- Saves output automatically

## 📁 Project Structure

```
weapons-and-knife-detection-system/
├── 🌐 Web UI Files
│   ├── app.py              # Main Flask application
│   ├── run_web_ui.py       # Easy startup script
│   ├── demo_web_ui.py      # Demo and testing
│   ├── templates/index.html # Web interface
│   └── static/style.css    # Custom styles
├── 🔧 Command Line Files
│   ├── detecting-images.py  # Main detection script
│   ├── test_detection.py   # Quick test script
│   └── preprocessing-images.py
├── 📊 Models & Results
│   ├── runs/detect/        # Trained models
│   ├── models/            # ONNX models
│   └── Results/           # Output files
└── 📚 Documentation
    ├── README.md          # Original documentation
    ├── WEB_UI_README.md   # Web UI guide
    └── QUICK_START_GUIDE.md # This file
```

## 🚀 Getting Started (Step by Step)

### Step 1: Environment Setup
```bash
# Navigate to your project
cd "C:\Users\Vishal Kandakatla\PycharmProjects\weapons-and-knife-detection-system"

# Create virtual environment (if not already done)
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Choose Your Interface

#### For Web UI (Recommended):
```bash
python run_web_ui.py
```
Then open: http://localhost:5000

#### For Command Line:
```bash
python test_detection.py
```

### Step 3: Test Your System
1. **Web UI**: Upload the test image from `Results/teste.jpg`
2. **Command Line**: The test script will use it automatically

## 🎯 Usage Examples

### Web UI Examples

1. **Upload an Image**:
   - Drag and drop any image file
   - Watch real-time processing
   - View detection results with bounding boxes

2. **Upload a Video**:
   - Select a video file
   - Wait for processing (may take a while)
   - Download the processed video with detections

3. **Mobile Testing**:
   - Open the web UI on your phone
   - Take a photo and upload it
   - Get instant detection results

### Command Line Examples

1. **Process Specific Image**:
   ```python
   from detecting_images import detect_objects_in_photo
   result = detect_objects_in_photo("path/to/your/image.jpg")
   ```

2. **Process Video**:
   ```python
   from detecting_images import detect_objects_in_video
   result = detect_objects_in_video("path/to/your/video.mp4")
   ```

## 🔧 Configuration Options

### Model Selection
The system includes multiple trained models:
- **Normal_Compressed** (default)
- **Haar** (Haar wavelet preprocessing)
- **Symlet** (Symlet wavelet preprocessing)
- **Db** (Daubechies wavelet preprocessing)

To change models, edit the model path in `app.py` or `detecting-images.py`.

### Detection Sensitivity
Adjust the confidence threshold (currently 0.5):
```python
if conf[pos] >= 0.5:  # Change this value
```

## 🐛 Troubleshooting

### Common Issues

1. **"Model not found" Error**:
   - Ensure the model file exists at the specified path
   - Check if training was completed successfully

2. **Web UI Won't Start**:
   - Check if port 5000 is available
   - Try changing the port in `app.py`
   - Ensure all dependencies are installed

3. **Upload Fails**:
   - Check file size (max 16MB)
   - Verify file format is supported
   - Ensure upload directory has write permissions

4. **Processing Errors**:
   - Check if OpenCV is properly installed
   - Verify video codec support
   - Monitor system memory usage

### Getting Help

1. **Check Console Output**: Look for error messages
2. **Verify Dependencies**: Run `pip list` to check installed packages
3. **Test with Sample**: Use the provided test image first
4. **Check File Permissions**: Ensure write access to directories

## 📊 Performance Tips

1. **Image Optimization**: Resize large images before upload
2. **Video Compression**: Use compressed formats (MP4)
3. **Memory Management**: Monitor system resources
4. **Batch Processing**: Process files sequentially

## 🎉 What's Next?

### For Beginners:
1. Try the web UI with different images
2. Experiment with video uploads
3. Test on mobile devices
4. Explore the detection statistics

### For Advanced Users:
1. Modify detection thresholds
2. Switch between different models
3. Customize the web interface
4. Integrate with your own applications

### For Developers:
1. Add new preprocessing techniques
2. Implement real-time video streaming
3. Create API endpoints
4. Add user authentication

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section
2. Review console output for errors
3. Ensure all dependencies are installed
4. Verify the model file exists

## 🏆 Congratulations!

You now have a professional-grade weapons detection system with both command-line tools and a modern web interface. The system is ready for:

- **Security Applications**: Real-time surveillance
- **Research**: Academic and commercial research
- **Development**: Building custom applications
- **Testing**: Evaluating detection accuracy

**Happy Detecting! 🔫🛡️** 