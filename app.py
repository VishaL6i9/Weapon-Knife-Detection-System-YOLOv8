#!/usr/bin/env python3
"""
Weapons and Knife Detection System - Web UI
A modern Flask web application for real-time weapon detection
"""

import os
import cv2
import base64
import numpy as np
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import tempfile
import uuid
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'weapon-detection-secret-key-2024'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'static/results'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'mp4', 'avi', 'mov', 'mkv'}

# Global model variable
model = None

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_model():
    """Load the YOLO model"""
    global model
    if model is None:
        model_path = './runs/detect/Normal_Compressed/weights/best.pt'
        if os.path.exists(model_path):
            model = YOLO(model_path)
            print("✅ Model loaded successfully!")
        else:
            print("❌ Model file not found!")
            return False
    return True

def detect_objects(image):
    """Perform object detection on image"""
    if not load_model():
        return None, "Model not found"
    
    try:
        results = model(image)
        detections = []
        
        for result in results:
            classes = result.names
            cls = result.boxes.cls
            conf = result.boxes.conf
            boxes = result.boxes.xyxy
            
            for pos, box in enumerate(boxes):
                if conf[pos] >= 0.5:  # Confidence threshold
                    xmin, ymin, xmax, ymax = box
                    detection = {
                        'class': classes[int(cls[pos])],
                        'confidence': float(conf[pos]),
                        'bbox': [int(xmin), int(ymin), int(xmax), int(ymax)]
                    }
                    detections.append(detection)
        
        return detections, None
    except Exception as e:
        return None, str(e)

def process_image(image_path):
    """Process image and return detection results"""
    image = cv2.imread(image_path)
    if image is None:
        return None, "Could not load image"
    
    detections, error = detect_objects(image)
    if error:
        return None, error
    
    # Draw bounding boxes
    for detection in detections:
        xmin, ymin, xmax, ymax = detection['bbox']
        label = f"{detection['class']} {detection['confidence']:.2f}"
        color = (0, 255, 0) if detection['class'] == 'knife' else (0, 0, 255)
        
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
        cv2.putText(image, label, (xmin, ymin - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)
    
    # Save processed image
    result_filename = f"result_{uuid.uuid4().hex[:8]}.jpg"
    result_path = os.path.join(app.config['RESULTS_FOLDER'], result_filename)
    cv2.imwrite(result_path, image)
    
    return {
        'detections': detections,
        'result_image': f'/static/results/{result_filename}',
        'total_detections': len(detections)
    }, None

def process_video(video_path):
    """Process video and return detection results"""
    if not load_model():
        return None, "Model not found"
    
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            return None, "Could not open video file"
        
        # Get video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Create output video
        result_filename = f"result_{uuid.uuid4().hex[:8]}.mp4"
        result_path = os.path.join(app.config['RESULTS_FOLDER'], result_filename)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(result_path, fourcc, fps, (width, height))
        
        frame_count = 0
        total_detections = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Perform detection
            detections, error = detect_objects(frame)
            if detections:
                total_detections += len(detections)
                
                # Draw bounding boxes
                for detection in detections:
                    xmin, ymin, xmax, ymax = detection['bbox']
                    label = f"{detection['class']} {detection['confidence']:.2f}"
                    color = (0, 255, 0) if detection['class'] == 'knife' else (0, 0, 255)
                    
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
                    cv2.putText(frame, label, (xmin, ymin - 10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)
            
            out.write(frame)
            frame_count += 1
        
        cap.release()
        out.release()
        
        return {
            'result_video': f'/static/results/{result_filename}',
            'total_frames': frame_count,
            'total_detections': total_detections,
            'duration': frame_count / fps if fps > 0 else 0
        }, None
        
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and processing"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Determine file type and process
        file_ext = filename.rsplit('.', 1)[1].lower()
        
        if file_ext in ['mp4', 'avi', 'mov', 'mkv']:
            # Process video
            result, error = process_video(filepath)
        else:
            # Process image
            result, error = process_image(filepath)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        if error:
            return jsonify({'error': error}), 500
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    model_status = "loaded" if load_model() else "not found"
    return jsonify({
        'status': 'healthy',
        'model': model_status,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🔫 Starting Weapons Detection Web UI...")
    print("=" * 50)
    
    # Pre-load model
    if load_model():
        print("✅ Model loaded successfully!")
    else:
        print("⚠️  Model not found - some features may not work")
    
    print("🌐 Starting web server...")
    app.run(debug=True, host='0.0.0.0', port=5000) 