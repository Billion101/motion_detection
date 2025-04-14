import cv2
import numpy as np
import time
from datetime import datetime

def motion_detection():
    # Initialize webcam
    cap = cv2.VideoCapture(0)  # 0 is usually the default camera
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Give the camera sensor time to warm up
    time.sleep(2)
    
    # Read first frame
    ret, frame1 = cap.read()
    if not ret:
        print("Error: Can't receive frame from camera")
        return
        
    # Convert to grayscale
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise and improve accuracy
    gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
    
    print("Motion detection started. Press 'q' to quit.")
    
    # Variables for tracking
    motion_detected = False
    motion_start_time = None
    
    while True:
        # Read current frame
        ret, frame2 = cap.read()
        if not ret:
            print("Error: Can't receive frame from camera")
            break
            
        # Convert to grayscale and apply blur
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
        
        # Calculate difference between frames
        frame_delta = cv2.absdiff(gray1, gray2)
        
        # Apply threshold to highlight differences
        thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]
        
        # Dilate the thresholded image to fill in holes
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        # Find contours on thresholded image
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Initialize motion status
        current_motion = False
        
        # Loop over the contours
        for contour in contours:
            # If contour is too small, ignore it
            if cv2.contourArea(contour) < 1000:  # Adjust this value based on your needs
                continue
                
            # Mark motion detection by drawing a bounding box
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            current_motion = True
        
        # Display motion status
        if current_motion:
            status = "Motion Detected!"
            if not motion_detected:
                motion_detected = True
                motion_start_time = datetime.now()
                print(f"Person detected at {motion_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            status = "No Motion"
            if motion_detected:
                motion_detected = False
                duration = datetime.now() - motion_start_time
                print(f"Motion ended. Duration: {duration.total_seconds():.2f} seconds")
        
        # Put text on the frame
        cv2.putText(frame2, f"Status: {status}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame2, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), 
                   (10, frame2.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        
        # Display the frame
        cv2.imshow("Motion Detection", frame2)
        
        # Update frame1 to be the current frame
        gray1 = gray2
        
        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    motion_detection()