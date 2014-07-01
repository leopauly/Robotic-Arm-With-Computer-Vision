#-------------------------------------------------------------------------------
# Name:        Shape Comparison
# Purpose:     For comparison of two different shapes
# All the 7 Hue Moments of two different shape(contours) are calculated and the
# difference between then is considered as a shape comparison parameter
# Author:      @leopauly
# created:     09-06-2014
#-------------------------------------------------------------------------------

import cv2
import numpy as np


img1=cv2.imread('cont7.jpg',0)
img2=cv2.imread('cont7.jpg',0)

kernel = np.ones((2, 2),np.uint8)
originalErosion = cv2.erode(img1, kernel, iterations = 1)
drawnErosion = cv2.erode(img2, kernel, iterations = 1)

thresh = 175
originalEdges = cv2.Canny(originalErosion, thresh, thresh*2)
drawnEdges = cv2.Canny(drawnErosion, thresh, thresh*2)

#extract contours
originalContours, Orighierarchy = cv2.findContours(originalEdges, cv2.cv.CV_RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
drawnContours, Drawnhierarchy = cv2.findContours(drawnEdges, cv2.cv.CV_RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

print len(originalContours)
print len(drawnContours)

d=drawnContours[3]
o=originalContours[3]

print len(o)
print len(d)

cv2.drawContours(img1,[o],0,(0,255,0),2)
cv2.drawContours(img2,[d],0,(0,255,0),2)


ret=cv2.matchShapes(d,o,cv2.cv.CV_CONTOURS_MATCH_I1, 0.0)
print ret

cv2.imshow('cont1',img1)
cv2.imshow('cont2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
