import cv2
import numpy as np

# Read the image
img = cv2.imread("image.png")

# Check if the image is loaded
if img is None:
    print("Error: Image not found.")
    exit()

# Laplacian mask with diagonal neighbors (8-neighbour)
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

# Apply the Laplacian filter
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen the image
sharpened = cv2.subtract(img, laplacian)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Laplacian Image", laplacian)
cv2.imshow("Sharpened Image", sharpened)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()