import cv2
import numpy as np

# Read image
img = cv2.imread("image.png")

# Check image
if img is None:
    print("ERROR: image.jpg not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilation = cv2.dilate(gray, kernel, iterations=1)

# Display
cv2.imshow("Original Image", gray)
cv2.imshow("Dilation", dilation)

# Save result
cv2.imwrite("dilation.jpg", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
