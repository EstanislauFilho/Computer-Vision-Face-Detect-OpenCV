import cv2

face_detect = cv2.CascadeClassifier("Classificador/haarcascade_frontal_default.xml")

video = cv2.VideoCapture(0)