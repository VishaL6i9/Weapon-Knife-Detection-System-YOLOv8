# 🚀 Weapons and Knife Detection System - Setup Guide

## Quick Start

### 1. Environment Setup

```bash
# Navigate to your project directory
cd "weapons-and-knife-detection-system"

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Test the System

```bash
# Run the test script to verify everything works
python test_detection.py
```

### 3. Run the Main Application

```bash
# Run the interactive detection system
python detecting-images.py
```

## 📋 Requirements

- **Python 3.7+**
- **OpenCV** (for image/video processing)
- **Ultralytics** (YOLOv8 framework)
- **NumPy** (numerical computations)
- **PyWavelets** (wavelet transforms)
- **Matplotlib** (plotting)
- **Pandas** (data manipulation)

## 🎯 Available Models

The project includes several trained models with different preprocessing techniques:

- **Normal_Compressed**: Standard model (currently used)
- **Haar**: Haar wavelet preprocessing
- **Symlet**: Symlet wavelet preprocessing
- **Db**: Daubechies wavelet preprocessing
- **Normal**: Standard preprocessing

## 🔧 Usage Options

### Option 1: Quick Test
```bash
python test_detection.py
```
- Uses the existing test image in `Results/teste.jpg`
- Displays results in a window
- Saves output to `Results/test_result.jpg`

### Option 2: Interactive Mode
```bash
python detecting-images.py
```
- Choose from 4 options:
  1. **Image Detection**: Process any image file
  2. **Video Detection**: Process video files
  3. **Real-time Display**: Show results in window
  4. **Exit**: Close the application

### Option 3: Direct Function Calls
You can also import and use the functions directly:

```python
from detecting_images import detect_objects_in_photo, detect_objects_in_video

# Detect in image
result_path = detect_objects_in_photo("path/to/your/image.jpg")

# Detect in video
result_path = detect_objects_in_video("path/to/your/video.mp4")
```

## 📁 Project Structure

```
weapons-and-knife-detection-system/
├── detecting-images.py      # Main detection script
├── test_detection.py        # Test script
├── preprocessing-images.py  # Image preprocessing utilities
├── requirements.txt         # Python dependencies
├── models/                  # ONNX model files
├── runs/detect/            # Trained YOLO models
│   ├── Normal_Compressed/
│   ├── Haar/
│   ├── Symlet/
│   └── ...
└── Results/                # Output files
    ├── teste.jpg           # Test image
    └── detected_objects_video.mp4
```

## 🐛 Troubleshooting

### Common Issues:

1. **Model not found error**:
   - Ensure the model file exists at `./runs/detect/Normal_Compressed/weights/best.pt`
   - Check if the training was completed successfully

2. **OpenCV installation issues**:
   ```bash
   pip uninstall opencv-python opencv-contrib-python
   pip install opencv-contrib-python
   ```

3. **CUDA/GPU issues**:
   - The system works on CPU by default
   - For GPU acceleration, ensure CUDA is properly installed

4. **Memory issues**:
   - Reduce image/video resolution
   - Process smaller batches

## 🎨 Customization

### Changing the Model
To use a different trained model, modify the model path in the scripts:

```python
# Instead of:
yolo_model = YOLO('./runs/detect/Normal_Compressed/weights/best.pt')

# Use:
yolo_model = YOLO('./runs/detect/Haar/weights/best.pt')  # Haar model
yolo_model = YOLO('./runs/detect/Symlet/weights/best.pt')  # Symlet model
```

### Adjusting Detection Threshold
Change the confidence threshold (currently 0.5):

```python
if conf[pos] >= 0.5:  # Change 0.5 to your desired threshold
```

## 📊 Performance Notes

- **Detection Speed**: Varies based on image size and hardware
- **Accuracy**: Models are trained on weapon detection datasets
- **Supported Formats**: JPG, PNG, MP4, AVI, etc.
- **Output**: Bounding boxes with confidence scores

## 🔗 Additional Resources

- **Dataset**: https://www.kaggle.com/datasets/jubaerad/weapons-in-images-segmented-videos
- **YOLOv11 Documentation**: https://docs.ultralytics.com/
- **OpenCV Documentation**: https://docs.opencv.org/

## 📝 License

This project is distributed under the MIT license. See LICENSE file for details. 