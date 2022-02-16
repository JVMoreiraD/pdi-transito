import cv2 as cv
from cv2 import blur
import numpy as np
# import PIL
import sys

imgRGB = cv.imread(cv.samples.findFile("Dataset/25.jpg"))

# Checks if the image exist
if imgRGB is None:
    sys.exit("Could not read the image.")

# Resize in case of a image being too big.
imgRGBs = cv.resize(imgRGB, (940, 540))

#apply gaussian to remove the excess of red objects
blurred_img = cv.GaussianBlur(imgRGBs,(5,5),0)

# Convert to HSV
imgHSV = cv.cvtColor(blurred_img, cv.COLOR_BGR2HSV)

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



# discover image contours
contours, _= cv.findContours(image=full_mask, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
print("size:" + str(blurred_img.size))
print("size percentage:" + str((blurred_img.size * 10)/100.0))

# draw image contours
for contour in contours:
    contourn_area = cv.contourArea(contour)
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    # new value
    if contourn_area >= 1500:
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if len(approx) == 8:
            cv.drawContours(blurred_img,contour,-1,(0,255,0),2,cv.LINE_AA)
            cv.putText(blurred_img, "Placa", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
# Show images
# cv.imshow("Display window HSV", imgHSV)
# cv.imshow("Display window RGB", imgRGBs)
cv.imshow('full-mask',full_mask)
cv.imshow('blur',blurred_img)



 
cv.waitKey(0)
cv.destroyAllWindows()