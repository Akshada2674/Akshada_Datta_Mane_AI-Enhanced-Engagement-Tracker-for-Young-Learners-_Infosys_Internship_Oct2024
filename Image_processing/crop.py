import cv2

img = cv2.imread('image.jpeg')
cropped = img[50:200, 100:300]                   #cropped = img[start_y:end_y, start_x:end_x]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()