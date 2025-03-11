import cv2 as cv
import numpy as np
import face_recognition

# URL de la caméra IP
url = "rtsp://admin:TYIZXA@192.168.222.10/h264/ch1/main/av_stream"

# Ouvrir le flux vidéo de la caméra IP
cam = cv.VideoCapture(url)

if not cam.isOpened():
    print("Erreur: Impossible d'ouvrir le flux vidéo.")
    exit()

while True:
    # Lire une image du flux vidéo
    ret, frame = cam.read()

    if not ret:
        print("Erreur: Impossible de lire l'image de la caméra.")
        break

    # Effectuer le traitement de l'image ici (détection de visage, reconnaissance faciale, etc.)

    # Enregistrer l'image sur le disque
    cv.imwrite("frame_capturee.jpg", frame)

    # Attendre 1 milliseconde entre chaque image
    # Si une touche est pressée, sortir de la boucle
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo
cam.release()
