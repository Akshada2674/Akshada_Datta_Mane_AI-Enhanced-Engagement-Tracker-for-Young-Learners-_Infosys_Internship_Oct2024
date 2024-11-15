import cv2
import numpy as np

# Read images
img1 = cv2.imread('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/image.jpeg')
img2 = cv2.imread('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/image2.jpeg')



# Resize images to smaller dimensions
img1 = cv2.resize(img1, (300, 300))  # Reduced size
img2 = cv2.resize(img2, (300, 300))  # Reduced size

# Concatenate images
h_concat = np.hstack((img1, img2))  # Horizontal concatenation
v_concat = np.vstack((img1, img2))  # Vertical concatenation

# Resize concatenated images to fit within a single page
h_concat_resized = cv2.resize(h_concat, (600, 300))  # Width and height
v_concat_resized = cv2.resize(v_concat, (300, 600))

# Display the concatenated images
cv2.imshow('Horizontal Concatenation', h_concat_resized)
cv2.imshow('Vertical Concatenation', v_concat_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
