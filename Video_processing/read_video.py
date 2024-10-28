import cv2
import os

# Path to the video file, with a check to make sure the file exists
video_path = "video_processing/video1.mp4"  
if not os.path.isfile(video_path):
    print("Error: Video file not found.")
    exit()

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open the video file.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video or error: Failed to capture frame.")
        break

    cv2.imshow('Video', frame)

    # Press 'q' to quit the video display
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
