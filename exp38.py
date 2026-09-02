import cv2

# Read image
img = cv2.imread("image.png")

# Check if image is loaded
if img is None:
    print("ERROR: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

# Draw rectangle around faces
for x, y, w, h in faces:
    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Display result
cv2.imshow("Face Detection", img)

# Save result
cv2.imwrite("face_detected.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
