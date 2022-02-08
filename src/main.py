import cv2 as cv
import numpy as np
# import PIL
import sys

imgRGB = cv.imread(cv.samples.findFile("Dataset/3.jpg"))

# Checks if the image exist
if imgRGB is None:
    sys.exit("Could not read the image.")

# Resize in case of a image being too big.
imgRGBs = cv.resize(imgRGB, (940, 540))

# Convert to HSV
imgHSV = cv.cvtColor(imgRGBs, cv.COLOR_BGR2HSV)

# Lower boundary RED color range values; Hue (0 - 10)
lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])
 
# Upper boundary RED color range values; Hue (160 - 180)
lower2 = np.array([160,100,20]) 
upper2 = np.array([179,255,255])
 
 # Apply masks in imageHSV
lower_mask = cv.inRange(imgHSV, lower1, upper1)
upper_mask = cv.inRange(imgHSV, lower2, upper2) 

full_mask = lower_mask + upper_mask

# Show images
cv.imshow("Display window HSV", imgHSV)
cv.imshow("Display window RGB", imgRGBs)
cv.imshow('full-mask',full_mask)

 
cv.waitKey(0)
cv.destroyAllWindows()