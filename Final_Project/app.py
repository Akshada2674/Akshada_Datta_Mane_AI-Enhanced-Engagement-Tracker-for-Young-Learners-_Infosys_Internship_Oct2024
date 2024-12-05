from flask import Flask, render_template, Response, jsonify, send_file, request
import cv2
from engagement_monitor import EngagementMonitor
from register_faces import register_known_faces
import json
from datetime import datetime
import os
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Initialize the engagement monitor
processor = register_known_faces()
monitor = EngagementMonitor(processor=processor)

def generate_frames():
    """Generate frames from webcam with engagement analysis"""
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process frame
        face_data, processed_frame = monitor.processor.extract_facial_features(frame)
        
        # Analyze each detected face
        for face in face_data:
            x, y, w, h = face['bbox']
            face_roi = frame[y:y+h, x:x+w]
            
            # Get all analysis data
            person_name = monitor.processor.identify_face(face_roi)
            engagement_data = monitor.analyze_face(face, face_roi)
            
            # Draw information on frame
            monitor._draw_face_info(processed_frame, face, 
                                  engagement_data['engagement_level'], 
                                  person_name)
            
            # Store data for the web interface
            app.engagement_data = {
                'name': person_name,
                'engagement': engagement_data['engagement_level'],
                'gaze': face['gaze'],
                'emotion': face['emotion'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        
        # Convert frame to jpg
        ret, buffer = cv2.imencode('.jpg', processed_frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route"""
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_data')
def get_data():
    """Get current engagement data"""
    if hasattr(app, 'engagement_data'):
        return jsonify(app.engagement_data)
    return jsonify({})

@app.route('/download_report')
def download_report():
    """Generate and download engagement report"""
    try:
        monitor.save_report()
        # Get the latest report
        report_dir = 'engagement_reports'
        if os.path.exists(report_dir):
            reports = sorted([f for f in os.listdir(report_dir) if f.endswith('.xlsx')])
            if reports:
                latest_report = os.path.join(report_dir, reports[-1])
                return send_file(
                    latest_report,
                    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    as_attachment=True,
                    download_name=f'engagement_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
                )
        return "No report available", 404
    except Exception as e:
        return str(e), 500

@app.route('/dashboard')
def dashboard():
    """Render dashboard page"""
    return render_template('dashboard.html')

@app.route('/upload_report', methods=['POST'])
def upload_report():
    """Handle report upload and generate visualization data"""
    try:
        file = request.files['file']
        if file:
            # Read Excel file
            xls = pd.ExcelFile(file)
            
            # Read each sheet
            detailed_data = pd.read_excel(xls, 'Detailed Data')
            summary_stats = pd.read_excel(xls, 'Summary Statistics')
            
            # Calculate person-wise statistics
            person_stats = detailed_data.groupby('name').agg({
                'engagement_level': lambda x: x.value_counts().index[0],
                'emotion': lambda x: x.value_counts().index[0],
                'gaze_direction': lambda x: (x == 'Looking Center').mean() * 100
            }).reset_index()
            
            # Prepare data for visualization
            visualization_data = {
                'person_data': person_stats.to_dict('records'),
                'average_engagement': float(summary_stats['average_engagement'].iloc[0]),
                'total_samples': int(summary_stats['total_samples'].iloc[0]),
                'dominant_emotion': str(summary_stats['dominant_emotion'].iloc[0]),
                'focus_time': 100 - float(summary_stats['looking_away_percentage'].iloc[0]),
                
                # Engagement distribution over time
                'timeline': {
                    'time': detailed_data['time'].astype(str).tolist(),
                    'engagement': detailed_data['engagement_level'].map({
                        'Highly Engaged': 4,
                        'Engaged': 3,
                        'Partially Engaged': 2,
                        'Not Engaged': 1
                    }).tolist()
                },
                
                # Emotion trends
                'emotion_trends': detailed_data['emotion'].value_counts().to_dict(),
                
                # Engagement distribution
                'engagement_distribution': detailed_data['engagement_level'].value_counts().to_dict()
            }
            
            return jsonify(visualization_data)
            
    except Exception as e:
        print(f"Error processing report: {str(e)}")  # Add this for debugging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 