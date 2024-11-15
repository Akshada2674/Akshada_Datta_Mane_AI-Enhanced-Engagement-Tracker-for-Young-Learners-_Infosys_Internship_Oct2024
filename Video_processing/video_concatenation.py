import cv2
import numpy as np

cap1 = cv2.VideoCapture('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/video.mp4')
cap2 = cv2.VideoCapture('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/video.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    # Resize individual frames
    frame1 = cv2.resize(frame1, (640, 360))
    frame2 = cv2.resize(frame2, (640, 360))

    # Concatenate the two resized frames horizontally
    h_concat = np.hstack((frame1, frame2))

    # Resize the concatenated result to further reduce size (optional)
    final_output = cv2.resize(h_concat, (480, 270))  # New size, change as needed

    # Display the resized concatenated frame
    cv2.imshow('Concatenated Video', final_output)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
