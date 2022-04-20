import mediapipe as mp
import cv2
# from projet_principal_module import hand_detector

class body_detector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose()
    def find_body(self, img):
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgrgb)
        if results.pose_landmarks:
            self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

def main():
    # detector_h = hand_detector()
    detector = body_detector()
    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        sucess, img = cap.read()
        detector.find_body(img)     
        # detector_h.find_hand(img) 
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow('video', img)
        cv2.waitKey(int(100/int(fps)))

if __name__ == '__main__':
    main()
