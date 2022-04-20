import mediapipe as mp
import cv2




class detections_face:
    def __init__(self):
        self.mp_face = mp.solutions.face_detection
        self.mp_draw = mp.solutions.drawing_utils
        self.face_detection = self.mp_face.FaceDetection()
    def detect(self, frame):
        framrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(framrgb)
        if results.detections:
            for id, detection in enumerate(results.detections):
                # mp_draw.draw_detection(frame, detection)
                box = detection.location_data.relative_bounding_box
                a, b, c= frame.shape
                bbox = int(box.xmin * b), int(box.ymin * a), int(box.width * b), int(box.height * a)
                cv2.rectangle(frame, bbox, (0, 255, 0), 2)

def main():
        
    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        lm, frame = cap.read()
        detections_face().detect(frame)
        cv2.imshow('video', frame)
        cv2.waitKey(int(1000/fps))

if __name__ == '__main__':
    main()