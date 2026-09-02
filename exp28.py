import cv2
import numpy as np

img = cv2.imread("image.png", 0)

# Boundary kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Apply convolution
boundary = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Boundary", boundary)

cv2.imwrite("boundary.jpg", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
