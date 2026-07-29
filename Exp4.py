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

# Dilate the image
dilated = cv2.dilate(img, kernel, iterations=1)

# Display the original image
cv2.imshow("Original Image", img)

# Display the dilated image
cv2.imshow("Dilated Image", dilated)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()