import cv2
import numpy as np

# Read the image
img = cv2.imread("image.png")

# Check if the image is loaded
if img is None:
    print("Error: Image not found.")
    exit()

# Get image dimensions
rows, cols = img.shape[:2]

# Define three points from the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define their new positions after transformation
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute the affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply the affine transformation
affine = cv2.warpAffine(img, matrix, (cols, rows))

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()