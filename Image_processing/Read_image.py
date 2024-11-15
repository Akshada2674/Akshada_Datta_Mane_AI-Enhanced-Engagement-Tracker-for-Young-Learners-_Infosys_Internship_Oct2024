import cv2

# Read an image
image = cv2.imread('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/image.jpeg')

# Display the image using OpenCV
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To check dimensions of the image
print(image.shape)