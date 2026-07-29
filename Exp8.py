import cv2

# Read the image
img = cv2.imread("image.png")

# Check if the image is loaded
if img is None:
    print("Error: Image not found.")
    exit()

# Scale the image to a bigger size (2x)
bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Scale the image to a smaller size (0.5x)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()