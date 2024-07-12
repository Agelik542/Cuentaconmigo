import reconocimiento_facial
import os
import pickle

def train_model():
    known_faces = []
    known_names = []

    for filename in os.listdir('dataset'):
        if filename.endswith(".jpg"):
            img_path = os.path.join('dataset', filename)
            image = reconocimiento_facial.load_image_file(img_path)
            encoding = reconocimiento_facial.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(filename.split('_')[0])

    with open('trained_model.pkl', 'wb') as f:
        pickle.dump((known_faces, known_names), f)

train_model()
