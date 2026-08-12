import cv2
import numpy as np

# Read the image
image = cv2.imread("image.png")

if image is None:
    print("Image not found!")
else:
    # Get image dimensions
    height, width = image.shape[:2]

    # Four points from the original image
    points1 = np.float32([
        [50, 50],
        [width - 50, 50],
        [width - 50, height - 50],
        [50, height - 50]
    ])

    # Four points for perspective transformation
    points2 = np.float32([
        [0, 0],
        [width, 50],
        [width - 50, height],
        [50, height - 50]
    ])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(points1, points2)

    # Apply perspective transformation
    transformed = cv2.warpPerspective(
        image,
        matrix,
        (width, height)
    )

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
