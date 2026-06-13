import cv2
import numpy as np
import serial
import time


# CAMERA

url = "http://10.45.60.18:8080/video"
cap = cv2.VideoCapture(url)


# SERIAL

arduino = serial.Serial('COM3', 115200)
time.sleep(2)


# CLICK SERVO

servo_angle = 75

def mouse_click(event, x, y, flags, param):
    global servo_angle

    if event == cv2.EVENT_LBUTTONDOWN:

        servo_angle = 0 if servo_angle == 75 else 75

        arduino.write(f"{servo_angle}\n".encode())

        print(f"Clicked at ({x}, {y})")
        print(f"Click Servo -> {servo_angle}")
 

# SETTINGS

fgbg = cv2.createBackgroundSubtractorMOG2(
    history=120,
    varThreshold=35
)

prev_x, prev_y = 320, 240
alpha = 0.3
Kp = 0.15

locked = False
lock_pos = (0, 0)


# WINDOW

cv2.namedWindow("LOCK + PREDICTION")
cv2.setMouseCallback("LOCK + PREDICTION", mouse_click)


# MAIN LOOP

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    frame = cv2.resize(frame, (640, 480))

    h, w, _ = frame.shape
    center_x = w // 2
    center_y = h // 2

    fgmask = fgbg.apply(frame)

    kernel = np.ones((5, 5), np.uint8)

    fgmask = cv2.morphologyEx(
        fgmask,
        cv2.MORPH_OPEN,
        kernel
    )

    fgmask = cv2.morphologyEx(
        fgmask,
        cv2.MORPH_DILATE,
        kernel
    )

    contours, _ = cv2.findContours(
        fgmask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    target_found = False

    if contours:

        contours = sorted(
            contours,
            key=cv2.contourArea,
            reverse=True
        )

        for c in contours:

            if cv2.contourArea(c) < 500:
                continue

            x, y, w_box, h_box = cv2.boundingRect(c)

            cx = int(x + w_box / 2)
            cy = int(y + h_box / 2)

            if not locked:
                lock_pos = (cx, cy)
                locked = True

            dist = np.linalg.norm(
                np.array(lock_pos) -
                np.array((cx, cy))
            )

            if dist < 80:
                lock_pos = (cx, cy)
                target_found = True
                break

    if locked and target_found:

        cx, cy = lock_pos

        vx = cx - prev_x
        vy = cy - prev_y

        cx = int(cx + vx * 0.5)
        cy = int(cy + vy * 0.5)

        cx = int(prev_x + alpha * (cx - prev_x))
        cy = int(prev_y + alpha * (cy - prev_y))

        prev_x, prev_y = cx, cy

        error_x = cx - center_x
        error_y = cy - center_y

        if abs(error_x) < 20:
            error_x = 0

        if abs(error_y) < 20:
            error_y = 0

        servo_x = 90 - int(Kp * error_x)
        servo_y = 90 - int(Kp * error_y)

        servo_x = max(10, min(170, servo_x))
        servo_y = max(20, min(160, servo_y))

        arduino.write(
            f"{servo_x},{servo_y}\n".encode()
        )

        cv2.rectangle(
            frame,
            (cx - 20, cy - 20),
            (cx + 20, cy + 20),
            (0, 0, 255),
            2
        )

        cv2.putText(
            frame,
            "LOCKED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    else:
        locked = False

    cv2.circle(
        frame,
        (center_x, center_y),
        5,
        (255, 255, 255),
        -1
    )

    cv2.imshow("LOCK + PREDICTION", frame)

    key = cv2.waitKey(1)

    if key == ord('r'):
        locked = False

    if key == 27:
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
