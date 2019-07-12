import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel = np.ones((5, 5), np.float32)/25
img = cv2.imread("../media/noised1.jpg")

dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
mblur = cv2.medianBlur(img, 5)
gblur = cv2.GaussianBlur(img, (5, 5), 0)
bil = cv2.bilateralFilter(img, 9, 75, 75)

titles = ["original image", "2d conv", "blur", "median blur", "gaussian blur", "bilateral filter"]
images = [img, dst, blur, mblur, gblur, bil]

for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()