## Goal of this project, is to simply use the devices webcam, detect the users face, and bluring only the detected face
import cv2
import mediapipe as mp

def main():

    # Init MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils


    # # Load a pre-trained face detection model from OpenCV
    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open webcam
    cap = cv2.VideoCapture(0)
    
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(rgb_frame)

            if results.detections:
                for detection in results.detections:
                    # Extract bounding box relative coordinates
                    bboxC = detection.location_data.relative_bounding_box
                    h, w, _ = frame.shape
                    x = int(bboxC.xmin * w)
                    y = int(bboxC.ymin * h)
                    width = int(bboxC.width * w)
                    height = int(bboxC.height * h)

                    # Validate values are in frame
                    x, y = max(0, x), max(0, y)
                    width = min(width, w - x)
                    height = min(height, h - y)

                    face_region = frame[y:y+height, x:x+width]
                    blurred_face = cv2.GaussianBlur(face_region, (51, 51), 30)
                    frame[y:y+height, x:x+width] = blurred_face
        

            cv2.imshow('Blurred Face Detected', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
