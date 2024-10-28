#Capture , display frames live , save in output.avi

import cv2

# Capture, display frames live, and save in output.avi
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit()

# Define the codec and create VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_processing/output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Write the frame to the output file
    out.write(frame)

    # Display the frame on screen
    cv2.imshow('Webcam', frame)

    # Press 'q' to quit the video display
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and file writer, and close all OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()
