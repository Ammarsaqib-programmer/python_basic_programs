import cv2
import numpy as np
import math as m

# pixels -> cm scale factor (set from your calibration)
DISTANCE_PER_PIXEL_CM = 0.06912

# open the camera (try 0 first; change if you truly have multiple cameras)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open camera (index 0). Check device index / permissions / that no other app is using it.")

while True:
    ret, img = cap.read()
    if not ret or img is None:
        print("Can't receive frame (stream end? camera disconnected?). Exiting ...")
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # threshold for yellow (tune as needed; HSV hue range in OpenCV is 0-179)
    lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
    upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    result = cv2.bitwise_and(img, img, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    centers = []
    label_ord = 65  # 'A'

    for c in contours:
        if cv2.contourArea(c) > 500:
            x, y, w, h = cv2.boundingRect(c)
            cx = x + w // 2
            cy = y + h // 2
            centers.append((cx, cy))

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)
            cv2.putText(img, chr(label_ord), (cx - 50, cy + 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            label_ord += 1

    # draw distances between successive centers (A->B, B->C, ...)
    for i in range(len(centers) - 1):
        (x1, y1), (x2, y2) = centers[i], centers[i + 1]
        pixels = m.hypot(x2 - x1, y2 - y1)
        dist_cm = pixels * DISTANCE_PER_PIXEL_CM
        tx, ty = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, f"{dist_cm:.2f} cm", (tx, ty),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    cv2.imshow("final output", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cleanup
cap.release()
cv2.destroyAllWindows()
