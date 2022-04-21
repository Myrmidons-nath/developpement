import mediapipe as mp
import cv2
import time
from projet_principal_module import hand_detector
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://youtu.be/6a-FnIqM0rI")

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

while True:
    rep, frame = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    detector = hand_detector()
    frame = detector.find_hand(frame, draw=True)
    lm_liste = detector.find_position(frame, draw=False)
    if len(lm_liste)!=0:
        if lm_liste[8][2]>lm_liste[6][2]:
            sb = driver.find_element_by_class_name("ytp-play-button ytp-button").click()
    cv2.imshow("video", frame)
    cv2.waitKey(1)