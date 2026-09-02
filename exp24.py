import cv2

# Read image
img = cv2.imread("image.png")

# Check image
if img is None:
    print("Image not found!")
    exit()

# Blur the image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# High-boost filtering
A = 2
high_boost = cv2.addWeighted(img, A, blur, -(A - 1), 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("High Boost Sharpened", high_boost)

# Save result
cv2.imwrite("high_boost.jpg", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()
