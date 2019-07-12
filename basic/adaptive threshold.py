import cv2

def nothing(x):
    pass

cv2.namedWindow("img")
cv2.createTrackbar("threshold", "img", 0, 255, nothing)

while True:
    img = cv2.imread("../media/gradient.jpg", 0)

    thres = cv2.getTrackbarPos("threshold", "img")
    th2 = cv2.adaptiveThreshold(img, thres, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2);

    cv2.imshow("img", img)
    cv2.imshow("img_thres", th2)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()

