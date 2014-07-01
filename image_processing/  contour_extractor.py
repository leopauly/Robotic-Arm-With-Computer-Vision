#-------------------------------------------------------------------------------
# Name:        contour extractor
# Purpose:     Extraction of contour from given image after background substraction
# email id:    meetleopauly@yahoo.com
# Author:      @leopauly
# Created:     19-06-2014
#-------------------------------------------------------------------------------

import numpy as np
import cv2
import scipy

wh=cv2.imread('whnew.jpg')
imgnew=cv2.imread('m25.jpg')
img1=imgnew
blur1= cv2.GaussianBlur(imgnew,(5,5),0)
cv2.imshow('image',blur1)

lower=np.array([100,100,100])
upper=np.array([180,255,255])
hsv=cv2.cvtColor(blur1,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv,lower,upper)
masked=cv2.bitwise_and(imgnew,imgnew,mask=mask)
roi=cv2.bitwise_not(mask)

kernel = np.ones((5,5),np.uint8)
roin = cv2.morphologyEx(roi, cv2.MORPH_OPEN, kernel)
conts,h=cv2.findContours(roin,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img1,conts,0,(0,255,0),2)
cv2.drawContours(masked,conts,0,(0,255,0),2)
cv2.imshow("roi",img1)
cv2.imshow("masked",masked)
cv2.drawContours(wh,conts,0,(0,255,0),2)
cv2.imwrite('cont7.jpg',wh)
shape=cv2.imread('cont7.jpg')
cv2.imshow("shape",shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
