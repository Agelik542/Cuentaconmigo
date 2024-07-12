import cv2
import os

def capture_images(nombre_estudiante):
    cap = cv2.VideoCapture(0)
    count = 0

    if not os.path.exists('dataset'):
        os.makedirs('dataset')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Capturing Images', frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:  # ESC pressed
            break
        elif k % 256 == 32:  # SPACE pressed
            img_name = f"dataset/{nombre_estudiante}_{count}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} Guardado!")
            count += 1

    cap.release()
    cv2.destroyAllWindows()

nombre_estudiante = input("Enter student's name: ")
capture_images(nombre_estudiante)
