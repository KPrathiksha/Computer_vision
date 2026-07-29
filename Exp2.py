import cv2

# Read the image
img = cv2.imread("image.png")

# Check if the image is loaded
if img is None:
    print("Error: Image not found.")
    exit()

# Display original image
cv2.imshow("Original Image", img)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(img, (15, 15), 0)

# Display blurred image
cv2.imshow("Gaussian Blurred Image", blurred)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()