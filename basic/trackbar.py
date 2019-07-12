import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar("B", "image", 255, 255, nothing)
cv2.createTrackbar("G", "image", 255, 255, nothing)
cv2.createTrackbar("R", "image", 255, 255, nothing)

while True:
    cv2.imshow('image', img)

    b = cv2.getTrackbarPos("B", "image")
    g = cv2.getTrackbarPos("G", "image")
    r = cv2.getTrackbarPos("R", "image")

    img[:] = [b, g, r]

    font = cv2.FONT_HERSHEY_COMPLEX

    cv2.putText(img, "B" + str(b), (0, 25), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, "G" + str(g), (0, 2*25), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, "R" + str(r), (0, 3*25), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()