import cv2
from matplotlib import pyplot as plt

img = cv2.imread("gradient.jpg")

_, th1 = cv2.threshold(img, 137, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 137, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 137, 255, cv2.THRESH_TOZERO)
_, th4 = cv2.threshold(img, 137, 255, cv2.THRESH_TOZERO_INV)
_, th5 = cv2.threshold(img, 137, 255, cv2.THRESH_TRUNC)

titles = ["original image", "binary", "binary inv", "to zero", "to zero inv", "trunc"]
images = [img, th1, th2, th3, th4, th5]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
