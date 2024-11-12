import cv2 as cv
import face_recognition
import pandas as pd
from datetime import datetime, timedelta
import os

# Create a directory to save screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Load the known image of Barack Obama
known_image = face_recognition.load_image_file(r"C:\Users\Akshada Mane\OneDrive\Desktop\Infosys Internship\Face_Recognition_Codes\photo.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame to store recognized face information
columns = ['Name', 'Date', 'Time', 'Screenshot']
df = pd.DataFrame(columns=columns)

# Launch the live camera or video
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Camera not working")
    exit()

# Set thresholds and parameters
confidence_threshold = 0.6
frame_skip = 2  # Process every second frame to reduce CPU load
frame_count = 0
recognition_count = 0  # Counter for recognized faces
recognized_names = set()  # Track recognized individuals

# Time tracking variables
last_recognition_time = None
entry_time = None
entry_duration = timedelta(minutes=2)  # Log recognized face every 2 minutes
gap_time = timedelta(minutes=5)  # Time gap for logging the same person again

try:
    while True:
        ret, frame = cam.read()
        
        if not ret:
            print("Can't receive the frame")
            break

        frame = cv.resize(frame, (640, 480))  # Resize the frame for faster processing
        frame_count += 1
        if frame_count % frame_skip != 0:
            continue  # Skip frames for efficiency

        # Detect faces in the current frame
        face_locations = face_recognition.face_locations(frame)
        if not face_locations:
            continue  # If no faces are detected, move on

        # Encode faces for comparison
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        recognized = False

        for face_encoding in face_encodings:
            # Calculate the distance between the known face and detected faces
            distance = face_recognition.face_distance([known_faces], face_encoding)[0]

            if distance < confidence_threshold:
                recognized = True
                now = datetime.now()

                # Check if 2 minutes have passed since the last recognition
                if last_recognition_time is None or (now - last_recognition_time) >= entry_duration:
                    # Save screenshot
                    screenshot_filename = f"screenshots/Akshada_Mane_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                    cv.imwrite(screenshot_filename, frame)  # Save the screenshot

                    # Log a new entry for Akshada Mane with screenshot
                    new_entry = pd.DataFrame({
                        'Name': ['Akshada Mane'],
                        'Date': [now.strftime("%Y-%m-%d")],
                        'Time': [now.strftime("%H:%M:%S")],
                        'Screenshot': [screenshot_filename]  # Add screenshot path
                    })
                    df = pd.concat([df, new_entry], ignore_index=True)
                    last_recognition_time = now  # Update last recognition time
                    entry_time = now  # Update entry time

                elif (now - entry_time) >= gap_time:
                    # If 5 minutes have passed since the last entry, log again
                    screenshot_filename = f"screenshots/Akshada_Mane_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                    cv.imwrite(screenshot_filename, frame)  # Save the screenshot again

                    new_entry = pd.DataFrame({
                        'Name': ['Akshada Mane'],
                        'Date': [now.strftime("%Y-%m-%d")],
                        'Time': [now.strftime("%H:%M:%S")],
                        'Screenshot': [screenshot_filename]  # Add screenshot path
                    })
                    df = pd.concat([df, new_entry], ignore_index=True)
                    entry_time = now  # Update entry time

                # Draw a rectangle around the face and label it as Barack Obama
                for face_location in face_locations:
                    top, right, bottom, left = face_location
                    cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv.putText(frame, 'Akshada Mane', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                               (255, 0, 0), 2, cv.LINE_AA)

        if not recognized:
            # If the face is not recognized, label it as 'Not Akshada Mane'
            cv.putText(frame, 'Not Akshada Mane', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (255, 0, 0), 2, cv.LINE_AA)

        # Show the live video stream with the bounding boxes and labels
        cv.imshow('Video Stream', frame)

        if cv.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Final save of the DataFrame if recognitions were logged
    if not df.empty:
        df.to_excel(r'C:\Users\Akshada Mane\OneDrive\Desktop\Infosys Internship\Face_Recognition_Codes\Excel_Output\attendance_with_screenshots.xlsx', index=False)
        print("Attendance and screenshots saved to 'attendance_with_screenshots_1.xlsx'.")

    # Release the camera and close any OpenCV windows
    cam.release()
    cv.destroyAllWindows()