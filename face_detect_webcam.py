import cv2

face_detect = cv2.CascadeClassifier("Classificador/haarcascade_frontal_default.xml")

video = cv2.VideoCapture(0)

while(True):
    conect, image_video = video.read()

    image_video_gray = cv2.cvtColor(image_video, cv2.COLOR_BGR2GRAY)

    faces_video = detectMultiScale(image_video_gray)

    