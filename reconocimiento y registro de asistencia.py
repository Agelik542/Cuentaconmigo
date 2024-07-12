import cv2
import face_recognition
import pickle
import sqlite3
from datetime import datetime

# Cargar el modelo entrenado
with open('trained_model.pkl', 'rb') as f:
    known_faces, known_names = pickle.load(f)

# Conectar a la base de datos
conn = sqlite3.connect('attendance.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS attendance 
             (name TEXT, date TEXT, time TEXT)''')

def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    c.execute("INSERT INTO attendance (name, date, time) VALUES (?, ?, ?)", (name, date, time))
    conn.commit()

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen de BGR a RGB
    rgb_frame = frame[:, :, ::-1]

    # Encontrar todas las caras en el frame actual
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Desconocido"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
            mark_attendance(name)

        # Dibujar un rectángulo alrededor de la cara
        top, right, bottom, left = face_locations[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow('Reconocimiento Facial', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Presionar ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
