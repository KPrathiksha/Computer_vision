import cv2

img = cv2.imread("image.png")
template = cv2.imread("image.png")

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

_, max_val, _, max_loc = cv2.minMaxLoc(result)

h, w = template.shape[:2]

x, y = max_loc

cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.putText(img, "Watch", (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Watch Detection", img)

cv2.imwrite("watch_detected.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
