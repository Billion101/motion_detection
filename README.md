# Motion Detection using Image Processing

This project is a simple real-time motion detection system using Python and OpenCV. It captures video from the webcam, processes each frame, and detects motion by comparing differences between consecutive frames.

## 🔍 Features

- Real-time webcam feed.
- Motion detection using image processing.
- Contour detection and bounding box drawing.
- Displays motion status and timestamps.
- Logs motion start and end times in the console.

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV**
- **NumPy**
- **Datetime & Time modules**

## 📷 How It Works

1. Captures video from the webcam.
2. Converts video frames to grayscale and applies Gaussian blur to reduce noise.
3. Compares the current frame with the previous frame using absolute difference.
4. Applies thresholding and dilation to detect significant changes.
5. Uses contour detection to identify moving objects.
6. Displays bounding boxes around detected motion and logs events.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/motion-detection
cd motion-detection

```

### 2. Install dependencies

pip install opencv-python numpy

### 3. Run the program

python3 main.py