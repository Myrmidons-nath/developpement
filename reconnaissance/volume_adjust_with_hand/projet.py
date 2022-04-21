import cv2
import math
import mediapipe as mp
import numpy as np
import projet_principal_module  as hd
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

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

class sound_detector:
    def __init__(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume. _iid_, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))

        self.vol = self.volume.GetVolumeRange()
        self.volume.SetMasterVolumeLevel(0, None)
        self.minVol = self.vol[0]
        self.maxVol = self.vol[1]

    def soud_detector_projet(self, frame, detector):
        detector.find_hand(frame)
        lm_liste = detector.find_position(frame)
        if len(lm_liste)!=0:
            # print(lm_liste[4], lm_liste[8])
            x1, y1 = lm_liste[4][1], lm_liste[4][2]
            x2, y2 = lm_liste[8][1], lm_liste[8][2]
            cx, cy= (x1+x2)//2, (y1+y2)//2
            cv2.line(frame, (x1, y1), (x2, y2),(255, 255, 0), 3)
            hyp = math.hypot(x2-x1, y2-y1)
            if hyp < 30:
                cv2.circle(frame, (cx, cy), 12, (0, 0, 255), cv2.FILLED)
            # print(hyp)
            sound = np.interp(hyp, [0, 300], [self.minVol, self.maxVol])
            self.volume.SetMasterVolumeLevel(sound, None)

            print(sound)
        



def main():
    wCam, hCam = 1280, 720
    detector = hand_detector()
    sound_classe = sound_detector()
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    while True:
        fps = cap.get(cv2.CAP_PROP_FPS)
        lm, frame = cap.read()
        sound_classe.soud_detector_projet(frame, detector)

        cv2.putText(frame, f"fps : {str(int(fps))}", (40, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        cv2.imshow('video', frame)
        cv2.waitKey(int(1000/fps))


if __name__ == '__main__':
    main()