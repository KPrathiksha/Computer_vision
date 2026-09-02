import cv2

# Read image
img = cv2.imread("image.png")

if img is None:
    print("Image not found!")
    exit()

# Get image size
h, w = img.shape[:2]

# Crop a portion
crop = img[0:h//2, 0:w//2]

# Get crop size
ch, cw = crop.shape[:2]

# Paste crop at bottom-right
img[h-ch:h, w-cw:w] = crop

# Display result
cv2.imshow("Cropped, Copied and Pasted", img)

# Save result
cv2.imwrite("crop_paste.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
