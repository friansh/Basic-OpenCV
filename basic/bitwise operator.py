import cv2
import numpy as np

img1 = np.zeros((300, 512, 3), np.uint8)
img1 = cv2.rectangle(img1, (round(img1.shape[1]/2), 0), (img1.shape[1], img1.shape[0]), (255, 255, 255), -1)

img2 = np.zeros((300, 512, 3), np.uint8)
img2 = cv2.rectangle(img2, (round(img2.shape[1]/2)-100, 0), (round(img2.shape[1]/2)+100, 100), (255, 255, 255), -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)

while True:
    cv2.imshow("image1", img1)
    cv2.imshow("image2", img2)
    cv2.imshow("bitwise and", bitwise_and)
    cv2.imshow("bitwise or", bitwise_or)
    cv2.imshow("bitwise xor", bitwise_xor)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()