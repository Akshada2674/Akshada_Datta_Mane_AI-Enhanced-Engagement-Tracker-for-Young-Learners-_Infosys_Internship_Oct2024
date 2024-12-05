import wget
import bz2
import os

# Download the file if it doesn't exist
if not os.path.exists('shape_predictor_68_face_landmarks.dat'):
    print("Downloading facial landmark predictor...")
    wget.download('http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2')
    
    # Extract the .bz2 file
    with bz2.BZ2File('shape_predictor_68_face_landmarks.dat.bz2') as fr:
        with open('shape_predictor_68_face_landmarks.dat', 'wb') as fw:
            fw.write(fr.read())