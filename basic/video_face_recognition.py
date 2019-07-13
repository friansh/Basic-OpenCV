print("Belajar face recog opencv2")
print("v 0.1 alpha friansh.2k19")

import cv2
import datetime

face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    font = cv2.FONT_HERSHEY_COMPLEX
    datet = str(datetime.datetime.now())

    upper1_text = "friansh.2k19"
    upper2_text = "Press s to screenshot, q to exit"

    frame = cv2.putText(frame, datet, (0, frame.shape[0]-10), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    frame = cv2.putText(frame, upper1_text, (0, 25), font, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
    frame = cv2.putText(frame, upper2_text, (0, 2*25), font, 0.7, (255, 255, 255), 1, cv2.LINE_AA)

    faces = face_cascade.detectMultiScale(frame_bw)
    for (x, y, w, h) in faces:
        if faces is not None:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("video", frame)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break
    elif k == ord("s"):
        cv2.imwrite("webcam_out.jpg", frame)

cap.release()
cv2.destroyAllWindows()
