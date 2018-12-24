import cv2

face_classifier = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")

image = cv2.imread("Imagens/scientists.jpg")