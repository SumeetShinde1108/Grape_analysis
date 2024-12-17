import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "1733819666475.jpeg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Failed to load image at {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(
    blurred, 
    cv2.HOUGH_GRADIENT, 
    dp=1.2, 
    minDist=15, 
    param1=50, 
    param2=30, 
    minRadius=5, 
    maxRadius=50
)

output = image.copy()
grape_count = 0
sizes = []

if circles is not None:
    circles = np.uint16(np.around(circles))
    grape_count = len(circles[0, :])
    for circle in circles[0, :]:
        x, y, radius = circle
        sizes.append(radius)
        cv2.circle(output, (x, y), radius, (0, 255, 0), 2)  
        cv2.circle(output, (x, y), 2, (0, 0, 255), 3)      

plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title(f"Grapes Detected: {grape_count}")
plt.axis("off")
plt.show()

print(f"Total Grapes Detected: {grape_count}")
print(f"Grape Sizes (Radius): {sizes}")
