# 🌐 Weapons Detection Web UI

A modern, professional web interface for the Weapons and Knife Detection System built with Flask and YOLOv8.

## ✨ Features

- **🎨 Modern UI**: Beautiful, responsive design with gradient backgrounds and smooth animations
- **📱 Mobile-Friendly**: Works perfectly on desktop, tablet, and mobile devices
- **🖼️ Image Processing**: Upload and detect weapons in images (JPG, PNG, GIF, BMP)
- **🎥 Video Processing**: Process videos with real-time detection (MP4, AVI, MOV, MKV)
- **⚡ Real-time Feedback**: Live progress tracking and status updates
- **📊 Detailed Results**: Comprehensive detection statistics and bounding box visualization
- **🔄 Drag & Drop**: Intuitive file upload with drag-and-drop support
- **🎯 Multiple Models**: Support for different preprocessing techniques
- **🔒 Secure**: File validation and size limits for security

## 🚀 Quick Start

### Option 1: Easy Startup (Recommended)
```bash
# Run the startup script
python run_web_ui.py
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

### Option 3: Direct Flask Run
```bash
# Set environment and run
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

## 🌐 Access the Web UI

Once started, open your browser and navigate to:
- **Local**: http://localhost:5000
- **Network**: http://your-ip-address:5000

## 📁 Project Structure

```
weapons-and-knife-detection-system/
├── app.py                 # Main Flask application
├── run_web_ui.py         # Startup script with dependency checks
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── style.css         # Additional custom styles
│   └── results/          # Processed images/videos
├── uploads/              # Temporary upload storage
└── requirements.txt      # Python dependencies
```

## 🎯 How to Use

### 1. Upload Media
- **Drag & Drop**: Simply drag your image or video file onto the upload area
- **Click to Browse**: Click the upload area to select files from your computer
- **Supported Formats**: 
  - Images: JPG, PNG, GIF, BMP
  - Videos: MP4, AVI, MOV, MKV
- **File Size Limit**: 16MB maximum

### 2. Processing
- The system automatically detects the file type
- Real-time progress bar shows processing status
- Processing time depends on file size and complexity

### 3. Results
- **Statistics**: Total detections, objects found, processing time
- **Detection List**: Detailed breakdown of each detected object
- **Visual Results**: Processed image/video with bounding boxes
- **Confidence Scores**: Accuracy percentage for each detection

## 🔧 Configuration

### Model Selection
To use a different trained model, modify the model path in `app.py`:

```python
# Change this line in the load_model() function
model_path = './runs/detect/Haar/weights/best.pt'  # Haar model
model_path = './runs/detect/Symlet/weights/best.pt'  # Symlet model
```

### Confidence Threshold
Adjust the detection sensitivity in `app.py`:

```python
# In the detect_objects() function
if conf[pos] >= 0.5:  # Change 0.5 to your desired threshold
```

### File Size Limits
Modify the maximum file size in `app.py`:

```python
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB
```

## 🎨 Customization

### Styling
- Edit `static/style.css` for custom styles
- Modify `templates/index.html` for layout changes
- The UI uses Bootstrap 5 and Font Awesome icons

### Colors
The UI uses CSS custom properties for easy color customization:

```css
:root {
    --primary-color: #2563eb;    /* Main blue */
    --secondary-color: #1e40af;  /* Darker blue */
    --success-color: #059669;    /* Green */
    --danger-color: #dc2626;     /* Red */
}
```

## 🔍 API Endpoints

### Health Check
```
GET /health
```
Returns system status and model information.

### File Upload
```
POST /upload
```
Accepts multipart form data with file upload.

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Change port in app.py
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Model Not Found**
   - Ensure the model file exists at the specified path
   - Check if training was completed successfully

3. **Upload Fails**
   - Check file size (max 16MB)
   - Verify file format is supported
   - Ensure upload directory has write permissions

4. **Processing Errors**
   - Check if OpenCV is properly installed
   - Verify video codec support
   - Monitor system memory usage

### Debug Mode
Enable debug mode for detailed error messages:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

## 📊 Performance Tips

1. **Image Optimization**: Resize large images before upload
2. **Video Compression**: Use compressed video formats (MP4)
3. **Batch Processing**: Process multiple files sequentially
4. **Memory Management**: Monitor system resources during processing

## 🔒 Security Considerations

- File upload validation prevents malicious uploads
- File size limits prevent DoS attacks
- Temporary files are automatically cleaned up
- Input sanitization prevents injection attacks

## 🌟 Advanced Features

### Multiple Model Support
The system can be extended to support multiple models:

```python
def load_model(model_type='normal'):
    model_paths = {
        'normal': './runs/detect/Normal_Compressed/weights/best.pt',
        'haar': './runs/detect/Haar/weights/best.pt',
        'symlet': './runs/detect/Symlet/weights/best.pt'
    }
    return YOLO(model_paths.get(model_type, model_paths['normal']))
```

### Real-time Processing
For real-time video processing, consider implementing WebSocket connections for live streaming.

## 📈 Monitoring

The web UI includes health monitoring:

```bash
# Check system health
curl http://localhost:5000/health
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the console output for error messages
3. Ensure all dependencies are properly installed
4. Verify the model file exists and is accessible

---

**Happy Detecting! 🔫🛡️** 