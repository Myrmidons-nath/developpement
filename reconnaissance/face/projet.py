import mediapipe as mp
import cv2


mp_face = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
face_detection = mp_face.FaceDetection()


cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)




while True:
    lm, frame = cap.read()
    framrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(framrgb)
    print(results)
    if results.detections:
        for id, detection in enumerate(results.detections):
            # mp_draw.draw_detection(frame, detection)
            box = detection.location_data.relative_bounding_box
            a, b, c= frame.shape
            bbox = int(box.xmin * b), int(box.ymin * a), int(box.width * b), int(box.height * a)
            cv2.rectangle(frame, bbox, (255, 0, 255), 2)


    cv2.imshow('video', frame)
    cv2.waitKey(int(1000/fps))