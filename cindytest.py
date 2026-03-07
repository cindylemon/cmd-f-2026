import cv2
import mediapipe as mp
import numpy as np

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='pose_landmarker.task'),
    running_mode=RunningMode.VIDEO
)

CONNECTIONS = [
    (11, 12), (11, 13), (13, 15),  # left arm
    (12, 14), (14, 16),             # right arm
    (11, 23), (12, 24),             # torso
    (23, 24), (23, 25), (24, 26),  # hips
    (25, 27), (26, 28)              # legs
]

cap = cv2.VideoCapture(0)
timestamp = 0

with PoseLandmarker.create_from_options(options) as landmarker:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        )

        timestamp += 1
        result = landmarker.detect_for_video(mp_image, timestamp)

        if result.pose_landmarks:
            landmarks = result.pose_landmarks[0]

            # draw dots on each landmark
            for lm in landmarks:
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            # draw lines between connected joints
            for a, b in CONNECTIONS:
                x1, y1 = int(landmarks[a].x * w), int(landmarks[a].y * h)
                x2, y2 = int(landmarks[b].x * w), int(landmarks[b].y * h)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)

        cv2.imshow("Badminton Coach", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()