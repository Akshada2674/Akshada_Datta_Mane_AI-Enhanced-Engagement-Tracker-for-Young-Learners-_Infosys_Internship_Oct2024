import cv2

img = cv2.imread('image.jpeg',0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()