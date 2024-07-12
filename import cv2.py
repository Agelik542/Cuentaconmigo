import cv2
import os

def capture_images(Ingrese_nombre_del_estudiante):
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
            img_name = f"dataset/{student_name}_{count}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} saved!")
            count += 1

    cap.release()
    cv2.destroyAllWindows()

student_name = input("Ingrese el nombre de los estudiantes")
capture_images(student_name)
