import mediapipe as mp
import cv2
import time



class hand_detector:
    def __init__(self, mode=False, maxHands=1, detectionCon=0.75, trackCon=0.75):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraws = mp.solutions.drawing_utils     



    def find_hand(self, frame, draw=True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handsnumber in self.results.multi_hand_landmarks:
                
                if draw:
                    self.mpDraws.draw_landmarks(frame, handsnumber, self.mpHands.HAND_CONNECTIONS)
        return frame
    def find_position(self, frame, handno=0, draw=True):
        lm_list = []
        if self.results.multi_hand_landmarks:
            myhands = self.results.multi_hand_landmarks[handno]

            for id, lm in enumerate(myhands.landmark):
                h, w, C = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])                           
                if draw:
                    if id == 4 or id == 8:
                        cv2.circle(frame, (cx, cy), 7, (255, 255, 0), cv2.FILLED)
        return lm_list
def main(input_list_choice, choice):
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector=hand_detector()
    while True:
        
        rep, frame = cap.read()
        frame = detector.find_hand(frame)
        lm_list = detector.find_position(frame, draw=choice)
        if len(lm_list) !=0:
            print(lm_list[input_list_choice])
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("video", frame)
        cv2.flip(frame, 0)
        cv2.waitKey(1)
if __name__ == '__main__':
    a = True
    while a:
        input_list_choice = int(input("number : "))
        if input_list_choice<20 and input_list_choice>0:
            a=False

    while True:
        choice = input("draw : ")
        try:
            bool(choice)
            break
        except:
            continue
    main(input_list_choice, choice)