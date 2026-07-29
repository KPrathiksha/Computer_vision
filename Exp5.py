import cv2
import numpy as np

# Read the image
img = cv2.imread("image.png")

# Check if the image is loaded
if img is None:
    print("Error: Image not found.")
    exit()

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Erode the image
eroded = cv2.erode(img, kernel, iterations=1)

# Display the original image
cv2.imshow("Original Image", img)

# Display the eroded image
cv2.imshow("Eroded Image", eroded)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()