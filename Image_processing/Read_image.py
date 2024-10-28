import cv2

# Read an image
image = cv2.imread('image.jpeg')

# Display the image using OpenCV
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To check dimensions of the image
print(image.shape)