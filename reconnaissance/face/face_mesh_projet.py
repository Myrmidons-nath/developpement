import mediapipe as mp
import cv2


mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils
face_mesh = mp_face.FaceMesh(max_num_faces=2)

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)

while True:
    lm, frame = cap.read()
    framrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(framrgb)
    if results.multi_face_landmarks:
        for f in results.multi_face_landmarks:
            mp_draw.draw_landmarks(frame, f, mp_face.FACE_CONNECTIONS, mp_draw.DrawingSpec(thickness=1, circle_radius=5))

            for id, lm in enumerate(f.landmark):
                #print (lm)
                ih, iw, ic = frame.shape
                x, y = int(lm.x*iw), int(lm. y*ih)
                print(id, x,y)


    cv2.imshow('video', frame)
    cv2.waitKey(int(100/fps))