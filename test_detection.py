#!/usr/bin/env python3
"""
Simple test script for the Weapons and Knife Detection System
This script demonstrates the detection capabilities using the existing test image.
"""

import cv2
from ultralytics import YOLO
import os

def test_detection():
    print("🔫 Testing Weapons and Knife Detection System")
    print("=" * 50)
    
    # Check if model exists
    model_path = './runs/detect/Normal_Compressed/weights/best.pt'
    if not os.path.exists(model_path):
        print(f"❌ Error: Model file not found at {model_path}")
        print("Please ensure the trained model is available.")
        return False
    
    # Check if test image exists
    test_image_path = './Results/teste.jpg'
    if not os.path.exists(test_image_path):
        print(f"❌ Error: Test image not found at {test_image_path}")
        print("Please ensure the test image is available.")
        return False
    
    print("✅ Model and test image found!")
    print("🔍 Loading YOLO model...")
    
    try:
        # Load the model
        yolo_model = YOLO(model_path)
        print("✅ Model loaded successfully!")
        
        # Load the test image
        print("📸 Loading test image...")
        image = cv2.imread(test_image_path)
        
        if image is None:
            print("❌ Error: Could not load the test image")
            return False
        
        print(f"✅ Image loaded! Size: {image.shape}")
        
        # Perform detection
        print("🔍 Performing detection...")
        results = yolo_model(image)
        
        # Process results
        detection_count = 0
        for result in results:
            classes = result.names
            cls = result.boxes.cls
            conf = result.boxes.conf
            detections = result.boxes.xyxy
            
            for pos, detection in enumerate(detections):
                if conf[pos] >= 0.5:
                    detection_count += 1
                    xmin, ymin, xmax, ymax = detection
                    label = f"{classes[int(cls[pos])]} {conf[pos]:.2f}"
                    color = (0, int(cls[pos]), 255)
                    
                    # Draw bounding box
                    cv2.rectangle(image, (int(xmin), int(ymin)), (int(xmax), int(ymax)), color, 2)
                    cv2.putText(image, label, (int(xmin), int(ymin) - 10), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)
        
        print(f"✅ Detection complete! Found {detection_count} objects")
        
        # Save result
        output_path = "./Results/test_result.jpg"
        cv2.imwrite(output_path, image)
        print(f"💾 Result saved to: {output_path}")
        
        # Display the result
        print("🖥️  Displaying result (press any key to close)...")
        cv2.imshow("Weapon Detection Result", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return True
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return False

if __name__ == "__main__":
    success = test_detection()
    if success:
        print("\n🎉 Test completed successfully!")
    else:
        print("\n❌ Test failed!") 