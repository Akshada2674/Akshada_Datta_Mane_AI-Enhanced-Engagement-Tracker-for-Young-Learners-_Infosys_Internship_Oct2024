import cv2

img = cv2.imread('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/image.jpeg')
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()