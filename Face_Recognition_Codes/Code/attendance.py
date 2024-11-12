import cv2 as cv
import face_recognition
import pandas as pd
from datetime import datetime

# Load the known image of Barack Obama
known_image = face_recognition.load_image_file(r"C:\Users\Akshada Mane\OneDrive\Desktop\Infosys Internship\Face_Recognition_Codes\photo.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame to store recognized face information
columns = ['Name', 'Date', 'Time']
df = pd.DataFrame(columns=columns)

# Launch the live camera
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Camera not working")
    exit()

confidence_threshold = 0.6  # Adjust this value as needed
frame_skip = 2  # Process every 2nd frame
frame_count = 0
recognition_count = 0  # Counter for recognized faces

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("Can't receive the frame")
        break

    # Resize frame to speed up processing
    frame = cv.resize(frame, (640, 480))  # Adjust resolution as needed

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue  # Skip processing for this frame

    # Face detection in the frame
    face_locations = face_recognition.face_locations(frame)
    if not face_locations:
        continue  # Skip if no faces detected

    face_encodings = face_recognition.face_encodings(frame, face_locations)

    recognized = False

    for face_encoding in face_encodings:
        distance = face_recognition.face_distance([known_faces], face_encoding)[0]

        if distance < confidence_threshold:
            recognized = True
            recognition_count += 1  # Increment recognition counter
            for face_location in face_locations:
                top, right, bottom, left = face_location
                cv.rectangle(frame, (left, top), (right, bottom), color=(0, 255, 0), thickness=2)
                cv.putText(frame, 'Akshada Mane', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                           (255, 0, 0), 2, cv.LINE_AA)

            # Save recognition info to DataFrame
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")
            
            new_entry = pd.DataFrame({'Name': ['Akshada Mane'], 'Date': [date_str], 'Time': [time_str]})
            df = pd.concat([df, new_entry], ignore_index=True)

    if not recognized:
        cv.putText(frame, 'Not Akshada Mane', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1,
                   (255, 0, 0), 2, cv.LINE_AA)

    # Check if recognized count has reached 5
    if recognition_count >= 5:
        # Save the DataFrame to an Excel file
        df.to_excel(r'C:\Users\Akshada Mane\OneDrive\Desktop\Infosys Internship\Face_Recognition_Codes\Excel_Output\recognized_faces.xlsx', index=False)
        recognition_count = 0  # Reset the counter
        df = pd.DataFrame(columns=columns)  # Reset the DataFrame

    cv.imshow('Video Stream', frame)

    if cv.waitKey(1) == ord('q'):
        break

# Final save if any recognitions were made before exiting
if not df.empty:
    df.to_excel(r'C:\Users\Akshada Mane\OneDrive\Desktop\Infosys Internship\Face_Recognition_Codes\Excel_Output\attendance.xlsx', index=False)

# Release the capture
cam.release()
cv.destroyAllWindows()