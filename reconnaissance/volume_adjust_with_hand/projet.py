import mediapipe
import cv2
import time
import projet_principal_module  as hd
wCam, hCam = 1280, 720
detector = hd.hand_detector()
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
while True:
    fps = cap.get(cv2.CAP_PROP_FPS)

    lm, frame = cap.read()
    detector.find_hand(frame)
    lm_liste = detector.find_position(frame)
    if len(lm_liste)!=0:
        print(lm_liste[4], lm_liste[8])
        x1, y1 = lm_liste[4][1], lm_liste[4][2]
        x2, y2 = lm_liste[8][1], lm_liste[8][2]
        cv2.line(frame, (x1, y1), (x2, y2),(255, 255, 0), 5)
    cv2.putText(frame, f"fps : {str(int(fps))}", (40, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
    cv2.imshow('video', frame)
    cv2.waitKey(int(1000/fps))