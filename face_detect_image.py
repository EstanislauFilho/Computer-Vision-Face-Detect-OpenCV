import cv2

face_classifier = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")

image = cv2.imread("Imagens/scientists.jpg")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces_detect = face_classifier.detectMultiScale(image_gray)

while(True):
    for(x, y, width, height) in faces_detect:
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)