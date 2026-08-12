import cv2

# Read the image
image = cv2.imread("image.png")

if image is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Image", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
