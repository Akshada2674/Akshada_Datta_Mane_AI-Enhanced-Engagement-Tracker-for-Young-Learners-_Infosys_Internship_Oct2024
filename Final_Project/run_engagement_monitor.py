from engagement_monitor import EngagementMonitor
from register_faces import register_known_faces
import cv2

def main():
    # Create instance of EngagementMonitor with registered faces
    print("Initializing Engagement Monitor...")
    processor = register_known_faces()
    monitor = EngagementMonitor(processor=processor)
    
    print("Starting monitoring... Press 'q' to quit")
    monitor.start_monitoring(video_source=0)

if __name__ == "__main__":
    main() 