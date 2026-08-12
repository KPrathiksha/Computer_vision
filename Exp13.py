import cv2
import numpy as np

# Read the video
video = cv2.VideoCapture("demonslayer.mp4")

if not video.isOpened():
    print("Video not found!")
else:
    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Get frame dimensions
        height, width = frame.shape[:2]

        # Four points from the original frame
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
            frame,
            matrix,
            (width, height)
        )

        # Display original and transformed video
        cv2.imshow("Original Video", frame)
        cv2.imshow("Perspective Transformed Video", transformed)

        # Press q to stop
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
