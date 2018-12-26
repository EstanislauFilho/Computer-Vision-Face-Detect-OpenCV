import cv2

face_detect = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while(True):
    conect, image_video = video.read()

    image_video_gray = cv2.cvtColor(image_video, cv2.COLOR_BGR2GRAY)

    facesDetectadas = face_detect.detectMultiScale(image_video_gray, scaleFactor=1.5, minSize=(100, 100))

    cv2.imshow("Captura Video funcionando", image_video)
    cv2.waitKey(1)
video.release()
cv2.destroyAllWindows()
