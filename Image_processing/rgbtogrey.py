import cv2

# Read the original image
image = cv2.imread("C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/image.jpeg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image as a new file
cv2.imwrite("C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Akshada_Datta_Mane_AI-Enhanced-Engagement-Tracker-for-Young-Learners-_Infosys_Internship_Oct2024/Image_processing/images/image_gray.png", gray_image)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close the display window
cv2.waitKey(0)
cv2.destroyAllWindows()
