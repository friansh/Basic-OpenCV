import cv2
import numpy as np

def canny_edge(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gblur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(gblur, 50, 150)
    return canny

def region_of_interest(canny):
    mask = np.zeros_like(canny)
    height = mask.shape[0]
    trap = np.array([(180, height), (700, height), (530, 250), (250, 250)])
    cv2.fillPoly(mask, [trap], 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5, cv2.LINE_AA)
    return line_image


def make_coordinate(image, line_parameters):
    slope, intercept = line_parameters

    y1 = image.shape[0]
    y2 = int(round(y1*(3/5)))
    if slope != 0:
        x1 = int(round((y1 - intercept)/slope))
        x2 = int(round((y2 - intercept) / slope))
    else:
        x1 = 0
        x2 = 0


    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))

    if len(left_fit) != 0:
        left_fit_average = np.average(left_fit, axis=0)
    else:
        left_fit_average = np.array([0, 0])

    left_line = make_coordinate(image, left_fit_average)

    right_fit_average = np.average(right_fit, axis=0)
    right_line = make_coordinate(image, right_fit_average)
    return np.array([left_line, right_line])

#img = cv2.imread("../media/road.jpg")
#img = cv2.resize(img, (round(img.shape[1]*(2/3)), round(img.shape[0]*(2/3))))

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.resize(frame, (round(frame.shape[1]*(2/3)), round(frame.shape[0]*(2/3))))

    canny_image = canny_edge(frame)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=10, maxLineGap=100)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    cv2.imshow("asd", combo_image)


    k = cv2.waitKey(1)
    if k ==  ord("q"):
        break

cap.release()
cv2.destroyAllWindows()