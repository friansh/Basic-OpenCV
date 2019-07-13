import cv2
import datetime
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/face-trainer.yml")

face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')

labels = {"person_name": 1}

with open("lables.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v: k for k, v in og_labels.items()}


cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.7, 2)

	for x, y, w, h in faces:
		cv2.rectangle(frame, (x,y),(x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
		roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)

		id_, conf = recognizer.predict(roi_gray)

		if conf <= 100:
			cv2.putText(frame, labels[id_] + " " + str(round(conf)), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA)

	frame = cv2.putText(frame, str(datetime.datetime.now()), (0, frame.shape[0] - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
	frame = cv2.putText(frame, "friansh.2k19", (0, 25), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
	frame = cv2.putText(frame, "Press s to screenshot, q to exit", (0, 2 * 25), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)

	cv2.imshow("frame", frame)

	k = cv2.waitKey(1)
	if k == ord("q"):
		break
	elif k == ord("s"):
		cv2.imwrite("ss.jpg", frame)

cap.release()
cv2.destroyAllWindows()