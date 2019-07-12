import cv2
import numpy as np
import datetime

def nothing(x):
    pass

cv2.namedWindow("track")
cv2.createTrackbar("l_t", "track", 160, 255, nothing)
cv2.createTrackbar("h_t", "track", 255, 255, nothing)
cv2.createTrackbar("mll", "track", 30, 50, nothing)
cv2.createTrackbar("mlg", "track", 180, 200, nothing)
cv2.createTrackbar("r_th", "track", 30, 120, nothing)

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("../media/road2.mp4")

while True:
    _, frame = cap.read()
    img_lane = np.copy(frame)

    gray = cv2.cvtColor(img_lane, cv2.COLOR_BGR2GRAY)
    gblur = cv2.GaussianBlur(gray, (5, 5), 0)

    l_t = cv2.getTrackbarPos("l_t", "track")
    h_t = cv2.getTrackbarPos("h_t", "track")

    canny = cv2.Canny(gblur, l_t, h_t)

    mask = np.zeros_like(canny)

    height = canny.shape[0]
    width = canny.shape[1]
    #trap = np.array([(120, height), (240, 245), (423, 245), (580, height)])

    p1 = [int(round(width*(1/5))), height]
    p2 = [int(round(width*(1.5/5))), int(round(height*(5/7)))]
    p3 = [int(round(width*(3.5/5))), int(round(height*(5/7)))]
    p4 = [int(round(width*(4/5))), height]

    #p4 = [int(round(width * (4 / 5))), height]

    trap = np.array([p1, p2, p3, p4])

    cv2.fillPoly(mask, [trap], 255)
    roi = cv2.bitwise_and(mask, canny)

    mll = cv2.getTrackbarPos("mll", "track")
    mlg = cv2.getTrackbarPos("mlg", "track")

    r_th = cv2.getTrackbarPos("r_th", "track")
    lines = cv2.HoughLinesP(roi, 2, np.pi/180, r_th, np.array([]), minLineLength=mll, maxLineGap=mlg)

    final_mask = np.zeros_like(img_lane)

    if lines is not None:
        left_line = []
        right_line = []
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            slope, intercept = np.polyfit((x1, x2), (y1, y2), 1)
            if slope < 0:
                left_line.append([slope, intercept])
            else:
                right_line.append([slope, intercept])

        left_line_average = []
        right_line_average = []

        if len(left_line) != 0:
            left_line_average = np.average(left_line, axis=0)
        else:
            left_line_average = [0, 0]

        if len(right_line) != 0:
            right_line_average = np.average(right_line, axis=0)
        else:
            right_line_average = [0, 0]

        print(left_line_average)
        l_slope, l_intercept = left_line_average
        r_slope, r_intercept = right_line_average

        p1_trap = []
        p2_trap = []
        p3_trap = []
        p4_trap = []

        if l_slope != 0 and l_intercept != 0:
            try:
                y1 = roi.shape[0]
                y2 = int(round(y1 * (5/7)))
                x1 = int(round((y1 - l_intercept) / l_slope))
                x2 = int(round((y2 - l_intercept) / l_slope))

                p1_trap = np.array([x1, y1])
                p2_trap = np.array([x2, y2])

                cv2.line(final_mask, (x1, y1), (x2, y2), (255, 0, 0), 5)
            except:
                pass

        if r_slope != 0 and r_intercept != 0:
            try:
                y1 = roi.shape[0]
                y2 = int(round(y1*(5/7)))
                x1 = int(round((y1-r_intercept)/r_slope))
                x2 = int(round((y2-r_intercept)/r_slope))

                p3_trap = np.array([x2, y2])
                p4_trap = np.array([x1, y1])

                cv2.line(final_mask, (x1, y1), (x2, y2), (255, 0, 0), 5)
            except:
                pass

        if len(p1_trap) == 2 and len(p2_trap) == 2 and len(p3_trap) == 2 and len(p4_trap) == 2:
            trap_lane = np.array([p1_trap, p2_trap, p3_trap, p4_trap])
            cv2.fillPoly(final_mask, [trap_lane], (0, 255, 0))
            cv2.putText(img_lane, "OK!", (final_mask.shape[1]-86, 43), cv2.FONT_HERSHEY_COMPLEX, 1.3, (0, 255, 0), 1,
                        cv2.LINE_AA)
        else:
            cv2.putText(img_lane, "ERROR", (final_mask.shape[1] - 158, 43), cv2.FONT_HERSHEY_COMPLEX, 1.3, (0, 0, 255),
                        1, cv2.LINE_AA)

    cv2.putText(img_lane, "friansh.2k18", (5, 21), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img_lane, "press s to screenshot, q to exit", (5, 2*21), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                (255, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(img_lane, str(datetime.datetime.now()), (5, final_mask.shape[0] - 8), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                (255, 255, 255), 1, cv2.LINE_AA)

    final_output = cv2.addWeighted(img_lane, 1, final_mask, 0.3, 1)

    roi_w = cv2.addWeighted(roi, 1, mask, 0.1, 1)
    gray_w = cv2.addWeighted(gray, 0.5, roi_w, 1, 1)

    cv2.imshow("roi", gray_w)
    cv2.imshow("image", final_output)

    k = cv2.waitKey(20)
    if k == ord("q"):
        break

cv2.destroyAllWindows()