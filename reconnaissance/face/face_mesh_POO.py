import mediapipe as mp
import cv2

class detector:
    def __init__(self):
        self.mp_face = mp.solutions.face_mesh
        self.mp_draw = mp.solutions.drawing_utils
        self.face_mesh = self.mp_face.FaceMesh(max_num_faces=2)

    def action(self, frame, print_position):
        framrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(framrgb)
        if results.multi_face_landmarks:
            for f in results.multi_face_landmarks:
                self.mp_draw.draw_landmarks(frame, f, self.mp_face.FACE_CONNECTIONS, self.mp_draw.DrawingSpec(thickness=1, circle_radius=2))
                if print_position=="True":
                    for id, lm in enumerate(f.landmark):
                        ih, iw, ic = frame.shape
                        x, y = int(lm.x*iw), int(lm. y*ih)
                        print(id, x,y)


def main():
    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        print_position = input("see position : ")
        
        if print_position in ["True", "False"]:
            break
        else:
            print("False or True ?")
            continue
        
        

    while True:
        lm, frame = cap.read()

        detector_ = detector().action(frame, print_position)
        cv2.imshow('video', frame)
        cv2.waitKey(int(1000/fps))


if __name__ == '__main__':
    main()

