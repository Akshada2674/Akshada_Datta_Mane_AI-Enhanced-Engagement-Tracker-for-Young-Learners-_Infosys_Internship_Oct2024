import cv2
import numpy as np
from data_processor import EngagementDataProcessor
from engagement_cnn_model import create_engagement_cnn
import time
from datetime import datetime
import pandas as pd
import os

class EngagementMonitor:
    def __init__(self, processor=None):
        try:
            self.model = create_engagement_cnn()
            if self.model is None:
                raise Exception("Failed to create CNN model")
                
            self.processor = processor if processor else EngagementDataProcessor()
            self.engagement_levels = [
                'Highly Engaged',
                'Engaged',
                'Partially Engaged',
                'Not Engaged'
            ]
            self.engagement_data = []
            
        except Exception as e:
            print(f"Error initializing EngagementMonitor: {str(e)}")
            raise

    def start_monitoring(self, video_source=0, person_name="Unknown"):
        """
        Start real-time engagement monitoring
        Args:
            video_source: Camera index or video file path
            person_name: Name of the person being monitored
        """
        try:
            cap = cv2.VideoCapture(video_source)
            if not cap.isOpened():
                raise Exception("Failed to open video source")

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                    
                # Process frame
                face_data, processed_frame = self.processor.extract_facial_features(frame)
                
                # Analyze each detected face
                for face in face_data:
                    x, y, w, h = face['bbox']
                    face_roi = frame[y:y+h, x:x+w]
                    
                    # Identify person
                    person_name = self.processor.identify_face(face_roi)
                    
                    # Preprocess for model
                    processed_face = self.processor.preprocess_image(face_roi)
                    processed_face = np.expand_dims(processed_face, axis=0)
                    
                    # Improved engagement detection
                    predictions = self.model.predict(processed_face, verbose=0)
                    confidence = float(np.max(predictions[0]))
                    
                    # Adjust engagement thresholds with more lenient conditions
                    if face['gaze'] == "Looking Center":
                        if face['emotion'] in ['happy', 'neutral', 'surprise']:
                            engagement_level = 'Highly Engaged'
                        else:
                            engagement_level = 'Engaged'
                    elif face['gaze'] in ["Looking Left", "Looking Right"]:
                        if face['emotion'] in ['happy', 'neutral', 'surprise']:
                            engagement_level = 'Engaged'
                        else:
                            engagement_level = 'Partially Engaged'
                    elif face['gaze'] == "Eyes Closed":
                        engagement_level = 'Partially Engaged'
                    else:
                        engagement_level = 'Not Engaged'
                    
                    # Override with CNN prediction if confidence is very high
                    if confidence > 0.9:  # Only override if very confident
                        cnn_prediction = self.engagement_levels[np.argmax(predictions[0])]
                        if cnn_prediction in ['Highly Engaged', 'Engaged']:
                            engagement_level = cnn_prediction
                    
                    # Store engagement data
                    self.engagement_data.append({
                        'name': person_name,
                        'timestamp': face['timestamp'],
                        'engagement_level': engagement_level,
                        'gaze_direction': face['gaze'],
                        'emotion': face['emotion'],
                        'confidence': confidence
                    })
                    
                    # Draw information
                    self._draw_face_info(processed_frame, face, engagement_level, person_name)
                
                cv2.imshow('Student Engagement Monitor', processed_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            self.save_report()
            cap.release()
            cv2.destroyAllWindows()
            
        except Exception as e:
            print(f"Error during monitoring: {str(e)}")
            if 'cap' in locals():
                cap.release()
            cv2.destroyAllWindows()

    def _draw_face_info(self, frame, face, engagement_level, person_name):
        """Helper method to draw face information on frame"""
        x, y, w, h = face['bbox']
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Define colors for different engagement levels
        colors = {
            'Highly Engaged': (0, 255, 0),    # Green
            'Engaged': (0, 255, 255),         # Yellow
            'Partially Engaged': (0, 165, 255),# Orange
            'Not Engaged': (0, 0, 255)        # Red
        }
        
        color = colors.get(engagement_level, (0, 255, 0))
        
        y_offset = y - 10
        for text, text_color in [
            (f"Person: {person_name}", (255, 255, 255)),  # White
            (f"Engagement: {engagement_level}", color),
            (f"Gaze: {face['gaze']}", (255, 255, 0)),    # Yellow
            (f"Emotion: {face['emotion']}", (0, 255, 255))# Cyan
        ]:
            cv2.putText(
                frame,
                text,
                (x, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                text_color,
                2
            )
            y_offset -= 20

    def save_report(self):
        """
        Save engagement data to Excel file
        """
        if not self.engagement_data:
            print("No engagement data to save")
            return
            
        # Create DataFrame
        df = pd.DataFrame(self.engagement_data)
        
        # Add date and time columns
        df['date'] = df['timestamp'].dt.date
        df['time'] = df['timestamp'].dt.time
        
        # Calculate statistics
        stats = {
            'total_samples': len(df),
            'average_engagement': df['engagement_level'].map({
                'Highly Engaged': 4,
                'Engaged': 3,
                'Partially Engaged': 2,
                'Not Engaged': 1
            }).mean(),
            'looking_away_percentage': (df['gaze_direction'] != 'Looking Center').mean() * 100,
            'dominant_emotion': df['emotion'].mode()[0]
        }
        
        # Create report directory if it doesn't exist
        os.makedirs('engagement_reports', exist_ok=True)
        
        # Save detailed report
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'engagement_reports/engagement_report_{timestamp}.xlsx'
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Save raw data
            df.to_excel(writer, sheet_name='Detailed Data', index=False)
            
            # Save statistics
            pd.DataFrame([stats]).to_excel(writer, sheet_name='Summary Statistics', index=False)
            
            # Create engagement distribution sheet
            engagement_dist = df['engagement_level'].value_counts()
            engagement_dist.to_excel(writer, sheet_name='Engagement Distribution')
            
            # Create emotion distribution sheet
            emotion_dist = df['emotion'].value_counts()
            emotion_dist.to_excel(writer, sheet_name='Emotion Distribution')
        
        print(f"Report saved as: {filename}")

    def analyze_face(self, face, face_roi):
        """Analyze a single face and return engagement data"""
        processed_face = self.processor.preprocess_image(face_roi)
        processed_face = np.expand_dims(processed_face, axis=0)
        
        predictions = self.model.predict(processed_face, verbose=0)
        confidence = float(np.max(predictions[0]))
        
        # Determine engagement level
        if face['gaze'] == "Looking Center":
            if face['emotion'] in ['happy', 'neutral', 'surprise']:
                engagement_level = 'Highly Engaged'
            else:
                engagement_level = 'Engaged'
        elif face['gaze'] in ["Looking Left", "Looking Right"]:
            if face['emotion'] in ['happy', 'neutral', 'surprise']:
                engagement_level = 'Engaged'
            else:
                engagement_level = 'Partially Engaged'
        else:
            engagement_level = 'Not Engaged'
        
        return {
            'engagement_level': engagement_level,
            'confidence': confidence
        }

if __name__ == "__main__":
    # Initialize and start the engagement monitor
    monitor = EngagementMonitor()
    monitor.start_monitoring() 