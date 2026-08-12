import cv2

# Read the image
image = cv2.imread("image.png")

if image is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sobel edge detection along Y-axis
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Convert result to 8-bit image
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Sobel Y Edge Image", sobel_y)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
