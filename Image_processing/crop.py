import cv2

img = cv2.imread('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/image.jpeg')
cropped = img[50:200, 100:300]                   #cropped = img[start_y:end_y, start_x:end_x]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()