import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mp_pose.Pose()


cap = cv2.VideoCapture(r'C:\Users\Nathan\Documents\github\git\reconnaissance\face\video.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
while True:
    sucess, img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgrgb)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow('video', img)
    cv2.waitKey(int(100/int(fps)))

        

