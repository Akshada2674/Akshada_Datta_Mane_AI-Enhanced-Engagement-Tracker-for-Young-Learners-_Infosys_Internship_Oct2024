import cv2
import os

def draw_bbox(image_dir, label_dir, output_dir, img_ext=".jpg", label_ext=".txt"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for label_file in os.listdir(label_dir):
        if label_file.endswith(label_ext):
            img_file = label_file.replace(label_ext, img_ext)
            img_path = os.path.join(image_dir, img_file)
            label_path = os.path.join(label_dir, label_file)
            
            img = cv2.imread(img_path)
            if img is None:
                print(f"Image not found: {img_path}")
                continue

            height, width, _ = img.shape

            with open(label_path, "r") as f:
                for line in f.readlines():
                    values = line.strip().split()
                    class_id = int(values[0])
                    x_center, y_center, bbox_width, bbox_height = map(float, values[1:])

                    x1 = int((x_center - bbox_width / 2) * width)
                    y1 = int((y_center - bbox_height / 2) * height)
                    x2 = int((x_center + bbox_width / 2) * width)
                    y2 = int((y_center + bbox_height / 2) * height)

                    color = (0, 255, 0)
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

                    label = f"Class {class_id}"
                    cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            output_img_path = os.path.join(output_dir, img_file)
            cv2.imwrite(output_img_path, img)

            print(f"Processed: {output_img_path}")

image_dir = 'C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Codes/Annotations/images'
label_dir = 'C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Codes/Annotations/labels'
output_dir = 'C:/Users/Akshada Mane/OneDrive/Desktop/Infosys Internship/Codes/Annotations/output'

draw_bbox(image_dir, label_dir, output_dir)

