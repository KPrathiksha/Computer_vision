import cv2

# Read image
img = cv2.imread("image.png")

# Check image
if img is None:
    print("Image not found!")
    exit()

# Watermark text
text = "PRATHIKSHA"

# Position of watermark
position = (50, 50)

# Font
font = cv2.FONT_HERSHEY_SIMPLEX

# Add watermark
cv2.putText(img, text, position, font, 1, (255, 255, 255), 2)

# Display image
cv2.imshow("Watermarked Image", img)

# Save image
cv2.imwrite("watermarked.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
