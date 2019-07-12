import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)

    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()