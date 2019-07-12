print("Belajar citra opencv2")
print("v 0.1 alpha friansh.2k19\n")

x = 1
y = 0

import cv2

img = cv2.imread('city-walk.png', 1)

print("Image size: " + str(img.shape[x]) + "x" + str(img.shape[y]))

img = cv2.resize(img, (round(img.shape[x]/2), round(img.shape[y]/2)))


img = cv2.line(img, (round(img.shape[x]/2), 0), (round(img.shape[x]/2), img.shape[y]), (255, 0, 0), 4)
img = cv2.line(img, (0, round(img.shape[y]/2)), (img.shape[x], round(img.shape[y]/2)), (255, 0, 0), 4)
img = cv2.circle(img, (round(img.shape[x]/2), round(img.shape[y]/2)), 100, (0, 255, 0), 10)

cv2.imshow("NIH!", img)


cv2.waitKey(0)


