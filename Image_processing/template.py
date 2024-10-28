import cv2

# Load the main image and the template image
img = cv2.imread('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Images/image1.jpeg')
template = cv2.imread('C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Images/images2.jpeg', 0)

# Check if images were loaded correctly
if img is None or template is None:
    print("Could not open one of the images. Check file paths.")
    exit()

# Convert the main image to grayscale for template matching
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Get the location with the highest match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

# Draw a rectangle around the detected template
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

# Display the result
cv2.imshow('Detected Template', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
