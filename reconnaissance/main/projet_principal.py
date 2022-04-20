from unittest import result
import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraws = mp.solutions.drawing_utils

while True:
    rep, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handsnumber in results.multi_hand_landmarks:
            mpDraws.draw_landmarks(frame, handsnumber, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handsnumber.landmark):
                h, w, C = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                                        
                print(id, cx, cy)
                if id == 4 or id == 8 or id == 12 or id == 16 or id == 20:
                    cv2.circle(frame, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
    cv2.imshow("video", frame)
    cv2.waitKey(1)


