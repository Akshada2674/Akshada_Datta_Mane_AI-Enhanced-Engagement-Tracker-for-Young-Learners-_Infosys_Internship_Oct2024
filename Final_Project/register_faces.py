from data_processor import EngagementDataProcessor
import os

def register_known_faces():
    processor = EngagementDataProcessor()
    
    # Path to known_faces directory
    faces_dir = "known_faces"
    
    # Add known people
    if os.path.exists(os.path.join(faces_dir, "barack_obama.jpg")):
        processor.add_known_person(os.path.join(faces_dir, "barack_obama.jpg"), "Mr.Barack Obama")
    if os.path.exists(os.path.join(faces_dir, "akshada.jpg")):
        processor.add_known_person(os.path.join(faces_dir, "akshada.jpg"), "Akshada Mane")
    
    return processor

if __name__ == "__main__":
    register_known_faces() 