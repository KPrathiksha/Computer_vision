import cv2

# Read the video
video = cv2.VideoCapture("demonslayer.mp4")

if not video.isOpened():
    print("Video not found!")

else:
    print("1 - Normal Speed")
    print("2 - Slow Motion")
    print("3 - Fast Motion")

    choice = input("Enter your choice: ")

    if choice == "1":
        delay = 30
    elif choice == "2":
        delay = 100
    elif choice == "3":
        delay = 10
    else:
        print("Invalid choice")
        delay = 30

    while True:
        ret, frame = video.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
