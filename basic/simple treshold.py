import cv2

def nothing(x):
    pass

cv2.namedWindow("img")
cv2.createTrackbar("threshold", "img", 0, 255, nothing)

while True:
    img = cv2.imread("gradient.jpg")
    thres = cv2.getTrackbarPos("threshold", "img")
    _, img_thres = cv2.threshold(img, thres, 255, cv2.THRESH_TRUNC)

    cv2.imshow("img", img)
    cv2.imshow("img_thres", img_thres)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()

