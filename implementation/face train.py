import os
import numpy as np
import cv2
import pickle
from shutil import rmtree
from PIL import Image

base_dir = "../media"
image_dir = os.path.join(base_dir, "train")

face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
crt_img = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("JPG") or file.endswith("jpeg"):
            path = os.path.join(root, "faces")
            if os.path.exists(path):
                rmtree(path)

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("JPG") or file.endswith("jpeg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()

            if label not in label_ids:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image, np.uint8)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi = image_array[y:y + h, x:x + w]
                x_train.append(roi)
                y_labels.append(id_)
                if not os.path.exists(os.path.join(root, "faces")):
                    os.makedirs(os.path.join(root, "faces"))
                cv2.imwrite(os.path.join(root, "faces") + "\\fcs" + str(crt_img) + ".png", roi)
                print(label + " " + file + " Face detected, saving...")
                crt_img += 1



with open("lables.pickle", "wb") as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("./recognizers/face-trainer.yml")

print("COMPLETED!!!")