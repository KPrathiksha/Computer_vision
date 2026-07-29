import cv2
import numpy as np

# Read the image
img = cv2.imread("image.png")

# Check if the image is loaded
if img is None:
    print("Error: Image not found.")
    exit()

# Define Laplacian mask with negative center coefficient
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])

# Apply the Laplacian mask
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen the image
sharpened = cv2.subtract(img, laplacian)

# Display the original image
cv2.imshow("Original Image", img)

# Display the sharpened image
cv2.imshow("Sharpened Image", sharpened)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()