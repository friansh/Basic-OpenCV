import cv2
import numpy as np


img = cv2.imread('./media/road2.jpg')
img_lane = np.copy(img)

hsv = cv2.cvtColor(img_lane, cv2.COLOR_BGR2HSV)

gblur = cv2.GaussianBlur(hsv, (5, 5), 0)
canny = cv2.Canny(gblur, 220, 255)



cv2.imshow("img lane", img_lane)
cv2.imshow("canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()