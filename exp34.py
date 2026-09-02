import cv2
import numpy as np

img = cv2.imread("image.png", 0)

kernel = np.ones((5, 5), np.uint8)

top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original", img)
cv2.imshow("Top Hat", top_hat)

cv2.imwrite("top_hat.jpg", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
