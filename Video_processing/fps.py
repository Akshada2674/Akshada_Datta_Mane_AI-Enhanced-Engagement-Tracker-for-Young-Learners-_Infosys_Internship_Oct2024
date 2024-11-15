import cv2
import time
import os

video_path = "C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/video.mp4"  
if not os.path.isfile(video_path):
    print("Error: Video file not found.")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit()

# Define the codec and create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_size = (640, 360)  # Resize the output video to 640x360
out = cv2.VideoWriter('video_processing/output.avi', fourcc, 20.0, output_size)

# Initialize variables to calculate FPS
fps_start_time = 0
fps = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Resize the frame to the desired output size
    resized_frame = cv2.resize(frame, output_size)

    # Calculate the FPS
    fps_end_time = time.time()
    time_diff = fps_end_time - fps_start_time
    fps = 1 / time_diff
    fps_start_time = fps_end_time

    # Put the FPS on the resized frame
    cv2.putText(resized_frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Write the resized frame to the output file
    out.write(resized_frame)

    # Display the resized frame with FPS
    cv2.imshow('Webcam', resized_frame)

    # Press 'q' to quit the video display
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects, and close windows
cap.release()
out.release()
cv2.destroyAllWindows()
