import cv2

face_classifier = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")

image = cv2.imread("Imagens/scientists.jpg")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces_detect = face_classifier.detectMultiScale(image_gray)