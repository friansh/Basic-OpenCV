import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('./media/road2.jpg')
img_lane = np.copy(img)

gray = cv2.cvtColor(img_lane, cv2.COLOR_BGR2GRAY)
gblur = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(gblur, 220, 255)



plt.imshow(canny)
plt.show()

cv2.waitKey(0)