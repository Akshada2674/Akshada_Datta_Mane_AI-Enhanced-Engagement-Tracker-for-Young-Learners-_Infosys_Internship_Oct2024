import cv2
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():                                                     # frames per second (FPS)
    print("Error: Could not open the video camera.")
    exit()

# Define the codec and create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_processing/output.avi', fourcc, 20.0, (640, 480))

# Initialize variables to calculate FPS
fps_start_time = 0
fps = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Calculate the FPS
    fps_end_time = time.time()
    time_diff = fps_end_time - fps_start_time
    fps = 1 / time_diff
    fps_start_time = fps_end_time

    # Put the FPS on the frame
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Write the frame to the output file
    out.write(frame)

    # Display the webcam frame with FPS
    cv2.imshow('Webcam', frame)

    # Press 'q' to quit the video display
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects, and close windows
cap.release()
out.release()
cv2.destroyAllWindows()



'''This code captures video from the default camera, 
displays the live video with an FPS (frames per second) overlay, 
and saves the video to a file named output.avi.'''