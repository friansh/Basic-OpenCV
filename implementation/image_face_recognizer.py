import cv2
import pickle
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/face-trainer.yml")

face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')

labels = {"person-name", 0}

with open("lables.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k, v in og_labels.items()}

img = cv2.imread("../media/test-faces/test4.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (41, 163, 41), 2, cv2.LINE_AA)
    roi = gray[x:x + w, y:y + h]
    if len(roi) != 0:
        cv2.imwrite("asd.jpg", roi)
        id_, conf = recognizer.predict(roi)

        if conf <= 85:
            pad = 2
            text_scale = 0.7

            t_w, t_h = cv2.getTextSize(labels[id_] + " " + str(round(conf)), cv2.FONT_HERSHEY_SIMPLEX, text_scale, 1)[0]
            cv2.rectangle(img, (x, y + h), (x + t_w + 2 * pad, y + h + t_h + 2 * pad), (41, 163, 41), -1)
            cv2.putText(img, labels[id_] + " " + str(round(conf)), (x + pad, y + h + t_h + pad),
                        cv2.FONT_HERSHEY_SIMPLEX, text_scale,
                        (255, 255, 255), 1, cv2.LINE_AA)


while img.shape[0] > 720:
    img = cv2.resize(img, (int(round(img.shape[1]/2)), int(round(img.shape[0]/2))))

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()