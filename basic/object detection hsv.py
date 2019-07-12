import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("tracking")
cv2.createTrackbar("l_h", "tracking", 0, 255, nothing)
cv2.createTrackbar("l_s", "tracking", 0, 255, nothing)
cv2.createTrackbar("l_v", "tracking", 0, 255, nothing)
cv2.createTrackbar("h_h", "tracking", 255, 255, nothing)
cv2.createTrackbar("h_s", "tracking", 255, 255, nothing)
cv2.createTrackbar("h_v", "tracking", 255, 255, nothing)

cap = cv2.VideoCapture(0)


while True:
    #img = cv2.imread("balls.jpg")

    ret, img = cap.read()

    l_h = cv2.getTrackbarPos("l_h", "tracking")
    l_s = cv2.getTrackbarPos("l_s", "tracking")
    l_v = cv2.getTrackbarPos("l_v", "tracking")

    h_h = cv2.getTrackbarPos("h_h", "tracking")
    h_s = cv2.getTrackbarPos("h_s", "tracking")
    h_v = cv2.getTrackbarPos("h_v", "tracking")

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, "l_h" + str(l_h), (0, 18), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, "l_s" + str(l_s), (0, 2*18), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, "l_v" + str(l_v), (0, 3*18), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, "h_h" + str(h_h), (0, 4*18), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, "h_s" + str(h_s), (0, 5*18), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, "h_v" + str(h_v), (0, 6*18), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([h_h, h_s, h_v])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(img, l_b, u_b)
    mask_hsv = cv2.inRange(hsv, l_b, u_b)

    #mask_hsv = cv2.bitwise_not(mask_hsv)

    res = cv2.bitwise_and(img, img, mask=mask)
    res_hsv = cv2.bitwise_and(img, img, mask=mask_hsv)


    #cv2.imshow('frame', img)
    #cv2.imshow('hsv', hsv)
    #cv2.imshow('mask', mask)
    cv2.imshow('mask hsv', mask_hsv)
    #cv2.imshow('res', res)
    cv2.imshow('res hsv', res_hsv)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()

