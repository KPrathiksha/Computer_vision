import cv2
import numpy as np

# Read image
img = cv2.imread("image.png")

# Check image
if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find gradients
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculate gradient magnitude
gradient = cv2.magnitude(gx.astype(np.float32), gy.astype(np.float32))

# Normalize gradient
gradient = cv2.normalize(gradient, None, 0, 255, cv2.NORM_MINMAX)
gradient = gradient.astype(np.uint8)

# Sharpen using gradient mask
sharpened = cv2.add(gray, gradient)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Gradient Mask", gradient)
cv2.imshow("Sharpened Image", sharpened)

# Save result
cv2.imwrite("gradient_sharpened.jpg", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
