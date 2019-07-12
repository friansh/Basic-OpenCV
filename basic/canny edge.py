import cv2
#from matplotlib import pyplot as plt

def nothing(x):
    pass

cv2.namedWindow("image")
cv2.createTrackbar("l_t", "image", 100, 255, nothing)
cv2.createTrackbar("h_t", "image", 200, 255, nothing)

cap = cv2.VideoCapture(0)

while True:
    #img = cv2.imread('../media/city-walk.png', 1)
    #img = cv2.resize(img, (round(img.shape[1] / 3), round(img.shape[0] / 3)))
    _, frame = cap.read()

    img = frame

    l_t = cv2.getTrackbarPos("l_t", "image")
    h_t = cv2.getTrackbarPos("h_t", "image")

    canny = cv2.Canny(img, l_t, h_t)

    cv2.imshow("image", canny)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()

"""
titles = ["original image", "canny"]
images = [img, canny]

for i in range(len(images)):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
"""