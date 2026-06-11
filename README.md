# Computer Vision Based Coin Counter and Detection System

This project is an automated image processing pipeline built using OpenCV to detect, isolate, and count coins within an image. By utilizing classical computer vision techniques, the system bypasses the need for heavy machine learning models to perform real-time object segmentation and counting based on geometry and contrast.

---

## Key Performance Capabilities
* **Background Isolation:** Successfully segments overlapping or high-contrast coins from varied background surfaces using adaptive thresholding.
* **Shape Optimization:** Utilizes morphological operations to cleanly close gaps in object contours, preventing dual-counting of single coins.
* **Automated Counting:** Accurately counts distinct coin boundaries and outputs the total tally directly onto the processed frame.

---

## Tech Stack and Libraries
* **Language:** Python
* **Computer Vision Library:** OpenCV (cv2)
* **Matrix Operations:** NumPy
* **Visualization:** Matplotlib

---

## Computer Vision Pipeline and Execution Steps

### 1. Image Preprocessing and Noise Reduction
* **Grayscale Conversion:** Converts the source BGR image to grayscale to remove color noise and focus strictly on pixel intensity variations.
* **Gaussian Blurring:** Applies a Gaussian blur filter to smooth out surface textures, scratches, or minor text details on the coins that could cause false edge detection.

### 2. Image Segmentation and Thresholding
* **Otsu's / Adaptive Thresholding:** Binarizes the image into absolute black and white pixels to separate the coins from the background foreground.
* **Morphological Transformations:** Executes erosion and dilation steps to eliminate small background noise artifacts and fill structural holes inside the detected coin shapes.

### 3. Contour Detection and Counting Logic
* **Edge Detection:** Implements the Canny edge detection algorithm to track the sharp boundaries of the circular objects.
* **Contour Extraction:** Utilizes `cv2.findContours` to map individual closed shapes and determine spatial coordinates.
* **Bounding & Tallying:** Loops through valid contours, draws bounding circles around each identified coin, and increments the global count variable.

---

## Summary and Takeaway
This project demonstrates the strength of foundational image processing algorithms. By combining blurring, thresholding, and contour mapping, the system achieves highly accurate object counting performance, serving as a rock-solid baseline for manufacturing sorting automation or digital currency verification systems.

---
Maintained and documented by Gayatri
