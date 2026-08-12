import cv2
import numpy as np

# Read the image
image = cv2.imread("image.png")

if image is None:
    print("Image not found!")
else:
    # Define four points from the original image
    points1 = np.float32([
        [50, 50],
        [300, 50],
        [300, 300],
        [50, 300]
    ])

    # Define corresponding points in the output image
    points2 = np.float32([
        [20, 80],
        [320, 50],
        [280, 320],
        [50, 280]
    ])

    # Calculate Homography matrix
    matrix, status = cv2.findHomography(points1, points2)

    # Apply Homography transformation
    transformed = cv2.warpPerspective(
        image,
        matrix,
        (image.shape[1], image.shape[0])
    )

    # Display original and transformed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Homography Transformed Image", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
