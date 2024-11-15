# AKSHADA AI-Enhanced Engagement Tracker for Young Learners (Infosys Internship - October 2024)

## Image Processing

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **NumPy**: For array manipulation

### Developed Logics:

#### A) `image_concatenation`
This function resizes two images to a specified pixel range and combines them both horizontally and vertically. The results are displayed in separate windows.

- **Input:**
<p>
  <img src="Image_processing/images/image.jpeg" alt="Image 1">&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="Image_processing/images/image2.jpeg" alt="Image 2" width="25%" height="194px">
</p>


- **Output:**

  ![Concatenated Image](Image_processing/images/image_concatenation_output.png)

#### B) `contour_detection`
This detects contours in a grayscale image using a binary threshold and `cv2.findContours()`. The contours are drawn onto the original image in green.

- **Input:**

  ![Image 1](Image_processing/images/image.jpeg)

- **Output:**

  ![Contoured Image](Image_processing/images/contour_detection_output.png)

#### C) `crop`
This function extracts a specific region of an image based on pixel range and displays the cropped section.

- **Input:**
 
    ![Image 1](Image_processing/images/image.jpeg)

- **Output:**
 
  ![Cropped Image](Image_processing/images/crop_output.png)

#### D) `dil_ero`
This function applies morphological operations, dilation and erosion, to enhance and reduce features in an image, respectively.

- **Input:**
 
   ![Image 1](Image_processing/images/image.jpeg)

- **Output:**

  ![Dilated and Eroded Image](Image_processing/images/dil_ero_output.png)

#### E) `edge`
This applies the Canny edge detection algorithm to detect edges in a grayscale image.

- **Input:**
 
    ![Image 1](Image_processing/images/image.jpeg)

- **Output:**
 
  ![Edge Detected Image](Image_processing/images/edge_output.png)

#### F) `hist_eq`
This enhances the contrast of a grayscale image using histogram equalization.

- **Input:**

     ![Image 1](Image_processing/images/image.jpeg)

- **Output:**
 
  ![Histogram Equalized Image](Image_processing/images/hist_eq_output.png)

#### G) `color_filtering`
This converts a color image from the BGR color space to HSV.

- **Input:**

     ![Image 1](Image_processing/images/image.jpeg)

- **Output:**
 
  ![HSV Image](Image_processing/images/color_filtering.png)

#### H) `morphological_transformation`
This applies opening and closing morphological operations to a grayscale image to remove noise and fill gaps.

- **Input:**

   ![Image 1](Image_processing/images/image.jpeg)

- **Output:**
 
  ![Morphologically Transformed Image](Image_processing/images/morphological_transformation_output.png)

#### I) `image_resize`
This resizes an image to specified dimensions.

- **Input:**
 
     ![Image 1](Image_processing/images/image.jpeg)

- **Output:**
 
  ![Resized Image](Image_processing/images/image_resize_output.png)

#### J) `rgbtogrey`
This converts a color image to grayscale.

- **Input:**

     ![Image 1](Image_processing/images/image.jpeg)

- **Output:**
 
  ![Grayscale Image](Image_processing/images/rgbtogrey_output.png)

#### K) `rotate`
This rotates an image by 90 degrees around its center.

- **Input:**

     ![Image 1](Image_processing/images/image.jpeg)

- **Output:**

  ![Rotated Image](Image_processing/images/rotate_output.png)

#### L) `blur_image`
This applies a Gaussian blur to an image to reduce noise and detail.

- **Input:**

  ![Image 1](Image_processing/images/image.jpeg)

- **Output:**
 
  ![Blurred Image](Image_processing/images/blur_image_output.png)

#### M) `template`
This function performs template matching to locate a template image within a larger image.

<p>
  <img src="Image_processing/images/image3.jpeg" alt="Image 1">&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="Image_processing/images/image2.jpeg" alt="Image 2" width="25%" height="194px">
</p>

- **Output:**

![Teplate Image](Image_processing/images/template_output.png)

## Video Processing

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84

### Developed Logics:

#### A) `fps`
This function captures video from the webcam, displays it in real-time, and calculates the FPS.

- **Input:**

  ![Video fps](Image_processing/images/image.jpeg)

- **Output:**
 
  ![Blurred Image](Image_processing/images/blur_image_output.png)
  
#### B) `Video_concatenation`
This function reads and resizes two video files, concatenating them horizontally.

#### C) `read_video`
This function reads video.

#### D) `read_save_video`
This function captures live video and saves it to a specified output file.

#### E) `capture_live_video`
This function captures live video from the webcam and displays it in real-time.

## Annotations

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6

### Developed Logics:

#### A) `data_segregate`
This function organizes images and their label files into matched and unmatched directories.

- **Input:**

![Screenshot 2024-11-13 174954](https://github.com/user-attachments/assets/828040b2-4b34-4355-b577-76b9beed0a9c)

- **Output:**

![Screenshot 2024-11-13 174816](https://github.com/user-attachments/assets/b46cc9cd-5c16-4df3-a950-4211bd1087e7)

#### B) `label`
This function draws bounding boxes on images based on annotations in the label files.

- **Input:**

![gun4](https://github.com/user-attachments/assets/ccba6a57-2506-4524-9c24-f384a5b248fa)

- **Output:**

![gun4](https://github.com/user-attachments/assets/71dba9a6-37ac-4bcd-aa4f-74e589bcfd09)

#### C) `label_manipulate`
This function updates class numbers in label files for object detection tasks.

- **Input:**

![Screenshot 2024-11-13 174620](https://github.com/user-attachments/assets/20cbc002-8864-42e5-9ad9-f64203421d26)

- **Output:**

![Screenshot 2024-11-13 174644](https://github.com/user-attachments/assets/1e71f3f6-cee9-45e7-bca6-eac2f35e6822)

## Face Recognition

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

### Developed Logics:

#### A) `Face_recognition`
This performs real-time face recognition to identify whether the person in live video frames a known image by comparing. His name is displayed if He/She is recognized; otherwise, "Not He/She" appears.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Screenshot 2024-11-13 175926](https://github.com/user-attachments/assets/df8d9bf1-4805-4b31-8b40-c8b8d251cbec)

#### B) `Attendence_save`
Using a live video stream, this performs real-time face recognition to identify He/She. When He/She's face is recognized, his/her name is displayed on the video feed, and the recognition event is logged with the date and time in an Excel file. After every 5 recognitions, the current log is saved to an Excel file, and the recognition counter and DataFrame are reset.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Screenshot 2024-11-13 175926](https://github.com/user-attachments/assets/df8d9bf1-4805-4b31-8b40-c8b8d251cbec)

![Screenshot 2024-11-13 180336](https://github.com/user-attachments/assets/e7a4fb5d-3d86-49b2-928e-6b6c65dbf1ba)

#### C) `test`
This performs real-time face recognition to identify He/She in a live video feed, logging each recognition event with the date and time into an Excel file every 30 seconds. It tracks recognition intervals to avoid duplicate entries and displays He/She or "Not He/She" based on identification.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Screenshot 2024-11-13 175926](https://github.com/user-attachments/assets/df8d9bf1-4805-4b31-8b40-c8b8d251cbec)

![Screenshot 2024-11-13 181026](https://github.com/user-attachments/assets/95c8a7ee-4008-426b-8869-0a978acda369)

#### D) `tools`
This performs real-time face recognition using the live camera feed to identify He/She. Each time a face is recognized, it records the name, date, and time in a data frame. Once a recognition count of 5 is reached, it saves the records to an Excel file, then resets the counter and DataFrame. It displays "He/She's name" or "Not He/She's name" over the video feed, and pressing 'q' exits the program with a final save of any remaining records.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Screenshot 2024-11-13 175926](https://github.com/user-attachments/assets/df8d9bf1-4805-4b31-8b40-c8b8d251cbec)

![Screenshot 2024-11-13 181459](https://github.com/user-attachments/assets/dcf0f639-e3a6-43fe-8ef0-e32741429a6c)


#### E) `excel_sc`
This is for face recognition with time-based logging looks well-structured and includes the logic to save screenshots and log attendance into an Excel file.

1. **Efficiency**: Resizing frames to 640x480 is good for speed. You can reduce the size further if needed.
2. **File Saving**: Screenshots are saved in `"Teja_screenshots(5)"`, and Excel is updated every 30 seconds.
3. **Recognition Timings**: Logs every 30 seconds for the same person and logs every 5 minutes to avoid multiple entries in short time frames.
4. **Error Handling**: Proper `try-except` block for handling errors.
5. **Termination**: Exits when the 'q' key is pressed.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Guru_Teja_2024-11-07_20-39-40](https://github.com/user-attachments/assets/ca7f31a4-4721-4de3-b346-7800de53c1c4)

![Screenshot 2024-11-13 183551](https://github.com/user-attachments/assets/846db4c7-d488-4e64-b6be-f5e6aab5209f)

#### F) `excel_sc_dt`
This uses OpenCV and `face_recognition` to detect and recognize a specific face (His/Her's) from a webcam feed. Upon recognition, a screenshot is saved, and the attendance (name, date, time, screenshot path) is logged into an Excel file. The script processes every second frame, saves data every 30 seconds, and ensures attendance is only logged every 5 minutes for the same person. The attendance data is stored in a DataFrame and periodically exported to an Excel file.

Key Features:
- Real-time face detection and recognition
- Saves screenshots with timestamp
- Logs attendance to Excel every 30 seconds
- Avoids multiple logs within a 5-minute interval for the same person

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Guru_Teja_2024-11-07_20-31-07](https://github.com/user-attachments/assets/967c8d9b-81f1-4ed1-bf0c-de2046ac778b)

![Screenshot 2024-11-13 183611](https://github.com/user-attachments/assets/96d0afcd-ad2b-4904-86ad-67d03cdac268)

#### G) `landmark`
This code is a face recognition and attentiveness tracking system that operates in real time. Key functions include:

1. **Face Recognition**: Detects and recognizes "His/Her's face" from the camera using a pre-loaded image.
2. **Attentiveness Detection**: Uses facial landmarks and head pose estimation to assess if the subject is attentive.
3. **Logging**: Records each recognition event with a timestamp, attentiveness status, and screenshot in an Excel file, saving every 30 seconds.
4. **Live Feedback**: Displays "Attentive" or "Not Attentive" on the video feed along with facial landmarks.

The system continues until you press 'q' to exit.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Guru Teja_2024-11-07_20-16-27](https://github.com/user-attachments/assets/20b1feef-0c90-4832-a128-45268391b394)

![Screenshot 2024-11-13 181911](https://github.com/user-attachments/assets/5de5e452-ba9d-4062-a23b-a02604d9ff3d)

#### H) `atten_score`
This script captures real-time webcam video to recognize "His/Her's face" and assess attentiveness based on head pose:

1. **Setup**: Loads His/Her's face data and initializes detectors.
2. **Face Recognition**: Compares detected faces with the known face, identifying if it's a match.
3. **Attentiveness Check**: Estimates head orientation (yaw/pitch) to compute an attentiveness score.
4. **Logging**: Logs details (name, date, time, attentiveness, screenshot) in an Excel file every 30 seconds if attentive.
5. **Display**: Shows video with face labels, attentiveness status, and facial landmarks. 

Exits on 'q' press, ensuring the final save to Excel.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Guru Teja_2024-11-07_21-34-50](https://github.com/user-attachments/assets/40f12cd5-c468-459c-a610-395366915ff8)

![Screenshot 2024-11-13 182336](https://github.com/user-attachments/assets/45034df8-9044-4850-b471-ba579c1a942a)

#### I) `avg_atten_score`
This captures webcam video, performs face recognition for "His/Her's face," calculates attentiveness based on the head pose, and logs the data into an Excel file every 30 seconds. Here is a summary of its key actions:

1. **Face Recognition**: Uses `face_recognition` to identify "His/Her's face" by comparing face encodings.
2. **Head Pose Detection**: Calculates the head pose (yaw, pitch) using `dlib`'s facial landmark predictor to assess attentiveness.
3. **Attentiveness Calculation**: Computes an attentiveness score based on yaw and pitch, with values between 0 (not attentive) and 1 (fully attentive).
4. **Logging**: Every 30 seconds, the script saves recognized face data (name, date, time, attentiveness, attention score, and screenshot) into an Excel file.
5. **Display and Feedback**: Shows real-time video with facial landmarks, attentiveness status, and face bounding boxes.

The final output includes an Excel file with logged details and an average attentiveness score at the end of the session. The user can stop the video stream by pressing 'q'.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Guru Teja_2024-11-07_22-10-43](https://github.com/user-attachments/assets/ace6a953-372a-4297-b598-3aa79f8ef4f3)

![Screenshot 2024-11-13 183057](https://github.com/user-attachments/assets/ad3ba39e-0b64-42f7-836a-2e0f3cacc442)
