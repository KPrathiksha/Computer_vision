import cv2

# Read the image
image = cv2.imread("image(4).png")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow("Grayscale Image", gray)

    # Save the grayscale image
    cv2.imwrite("grayscale_image.png", gray)

    print("Image converted to grayscale successfully.")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
