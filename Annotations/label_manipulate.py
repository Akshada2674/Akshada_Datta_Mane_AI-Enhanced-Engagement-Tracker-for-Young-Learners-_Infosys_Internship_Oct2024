import os

def change_class_number(label_dir, label_ext=".txt", old_class=0, new_class=19):
    for label_file in os.listdir(label_dir):
        if label_file.endswith(label_ext):
            label_path = os.path.join(label_dir, label_file)
            
            updated_lines = []
            with open(label_path, "r") as f:
                for line in f:
                    values = line.strip().split()
                    if len(values) < 5:
                        print(f"Skipping malformed label in {label_file}: {line}")
                        continue
                    
                    try:
                        class_id = int(values[0])
                        # Change class number if it matches old_class
                        if class_id == old_class:
                            class_id = new_class
                        
                        # Recreate the line with the updated class ID
                        updated_line = f"{class_id} " + " ".join(values[1:])
                        updated_lines.append(updated_line)
                    except ValueError as e:
                        print(f"Error parsing label in {label_file}: {line} - {e}")
                        continue

            # Write updated lines back to the file
            with open(label_path, "w") as f:
                f.write("\n".join(updated_lines) + "\n")

            print(f"Updated class numbers in: {label_file}")

# Set your label directory
label_dir = r"C:\Users\Akshada Mane\OneDrive\Desktop\Infosys Internship\Gun dataset\SasankYadati-Guns-Dataset-0eb7329\Labels"

change_class_number(label_dir)