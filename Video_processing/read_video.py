import cv2
import os

# Path to the video file, with a check to make sure the file exists
video_path = "C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/video.mp4"  
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

    # Resize the frame to decrease its size (50% of the original size in this case)
    width = int(frame.shape[1] * 0.5)  # 50% of original width
    height = int(frame.shape[0] * 0.5)  # 50% of original height
    resized_frame = cv2.resize(frame, (width, height))

    # Display the resized frame
    cv2.imshow('Video', resized_frame)

    # Press 'q' to quit the video display
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
