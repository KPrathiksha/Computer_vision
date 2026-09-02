import cv2

# Read image
img = cv2.imread("image.png")

# Blur the image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Unsharp masking
sharpened = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

# Save result
cv2.imwrite("sharpened.jpg", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
