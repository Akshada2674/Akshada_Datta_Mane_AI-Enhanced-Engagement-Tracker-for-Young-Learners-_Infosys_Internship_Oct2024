import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
import dlib
from datetime import datetime
import pandas as pd
from deepface import DeepFace
import face_recognition

class EngagementDataProcessor:
    def __init__(self, target_size=(224, 224)):
        self.target_size = target_size
        # Initialize dlib's face detector and facial landmark predictor
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        # Add known faces storage
        self.known_face_encodings = []
        self.known_face_names = []
        
    def add_known_person(self, image_path, person_name):
        """
        Add a known person to the face recognition system
        Args:
            image_path: Path to the person's image
            person_name: Name of the person
        """
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        self.known_face_encodings.append(encoding)
        self.known_face_names.append(person_name)
        
    def identify_face(self, face_image):
        """
        Identify a face using face_recognition
        Returns: Name of the person or "Unknown"
        """
        # Get face encoding
        rgb_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_image)
        
        if not encodings:
            return "Unknown"
        
        encoding = encodings[0]
        
        # Compare with known faces
        matches = face_recognition.compare_faces(self.known_face_encodings, encoding)
        if True in matches:
            match_index = matches.index(True)
            return self.known_face_names[match_index]
        
        return "Unknown"
    
    def _eye_aspect_ratio(self, eye):
        """Calculate eye aspect ratio"""
        vertical_dist = np.linalg.norm(eye[1] - eye[5]) + np.linalg.norm(eye[2] - eye[4])
        horizontal_dist = np.linalg.norm(eye[0] - eye[3]) * 2
        return vertical_dist / horizontal_dist if horizontal_dist != 0 else 0
        
    def analyze_emotion(self, face_roi):
        """
        Analyze facial emotion using DeepFace
        Returns: Dominant emotion
        """
        try:
            analysis = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            return analysis[0]['dominant_emotion']
        except:
            return "Unknown"

    def extract_facial_features(self, image):
        """
        Extract facial features from the image
        Returns: Faces, landmarks, emotions, and processed image
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
        
        face_data = []
        for (x, y, w, h) in faces:
            face_roi = image[y:y+h, x:x+w]
            rect = dlib.rectangle(x, y, x+w, y+h)
            
            # Get facial landmarks
            landmarks = self.predictor(gray, rect)
            landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])
            
            # Get gaze direction
            gaze = self.get_gaze_direction(landmarks, face_roi)
            
            # Get emotion
            emotion = self.analyze_emotion(face_roi)
            
            face_data.append({
                'bbox': (x, y, w, h),
                'landmarks': landmarks,
                'gaze': gaze,
                'emotion': emotion,
                'timestamp': datetime.now()
            })
            
        return face_data, image
    
    def preprocess_image(self, image):
        """
        Preprocess a single image for the CNN model
        Args:
            image: Input image (BGR format from OpenCV)
        Returns:
            Preprocessed image array
        """
        # Resize image
        image = cv2.resize(image, self.target_size)
        
        # Convert BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Convert to array and normalize
        image = img_to_array(image)
        image = image / 255.0
        
        return image
    
    def get_gaze_direction(self, landmarks, face_roi):
        """
        Determine gaze direction using eye landmarks with improved thresholds
        """
        try:
            # Get eye landmarks
            left_eye = landmarks[36:42]
            right_eye = landmarks[42:48]
            nose_bridge = landmarks[27:31]
            
            # Calculate eye aspect ratio
            left_ear = self._eye_aspect_ratio(left_eye)
            right_ear = self._eye_aspect_ratio(right_eye)
            
            if left_ear < 0.17 and right_ear < 0.17:  # Adjusted threshold
                return "Eyes Closed"
            
            # Calculate center points
            left_eye_center = np.mean(left_eye, axis=0)
            right_eye_center = np.mean(right_eye, axis=0)
            nose_center = np.mean(nose_bridge, axis=0)
            
            # Calculate the angle between eyes and nose
            eye_line = right_eye_center - left_eye_center
            nose_line = nose_center - np.mean([left_eye_center, right_eye_center], axis=0)
            
            # Normalize vectors
            eye_line = eye_line / np.linalg.norm(eye_line)
            nose_line = nose_line / np.linalg.norm(nose_line)
            
            # Calculate angle
            angle = np.arccos(np.clip(np.dot(eye_line, nose_line), -1.0, 1.0))
            angle_degrees = np.degrees(angle)
            
            # More accurate thresholds for gaze detection
            if abs(angle_degrees - 90) < 15:  # Looking straight ahead
                return "Looking Center"
            elif angle_degrees > 100:  # Head turned right
                return "Looking Right"
            elif angle_degrees < 80:  # Head turned left
                return "Looking Left"
            else:
                return "Looking Center"
            
        except Exception as e:
            print(f"Gaze detection error: {str(e)}")
            return "Looking Center"  # Default to center if detection fails