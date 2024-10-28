import cv2
import os

# List to store image paths
image_paths = ['image.jpeg','image.jpeg', 'image.jpeg', 'image.jpeg', 
               'image.jpeg','image.jpeg','image.jpeg', 'image.jpeg', 'image.jpeg', 
               'image.jpeg']

# Loop through and read 10 images
for i, image_path in enumerate(image_paths):
    if os.path.exists(image_path):  # Check if the file exists
        image = cv2.imread(image_path)  # Read image

        # Display the image
        cv2.imshow(f'Image {i+1}', image)

        # To check dimensions of the image
        print(f'Image {i+1} dimensions: {image.shape}')

        # Wait for a key press to close the image
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f'File {image_path} does not exist.')
