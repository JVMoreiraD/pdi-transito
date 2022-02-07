import cv2 as cv
import numpy as np
import sys

imgRGB = cv.imread(cv.samples.findFile("Dataset/1.jpg"))

if imgRGB is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window RGB", imgRGB)

imgHSV = cv.cvtColor(imgRGB, cv.COLOR_BGR2HSV)

result = imgHSV.copy()

# Convert to HSV

cv.imshow("Display window HSV", imgHSV)

k = cv.waitKey(0)

# lower boundary RED color range values; Hue (0 - 10)
lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])
 
# upper boundary RED color range values; Hue (160 - 180)
lower2 = np.array([160,100,20])
upper2 = np.array([179,255,255])
 
lower_mask = cv.inRange(imgHSV, lower1, upper1)
upper_mask = cv.inRange(imgHSV, lower2, upper2)

full_mask = lower_mask + upper_mask

cv.imshow('full-mask',full_mask)

 
cv.waitKey(0)
cv.destroyAllWindows()