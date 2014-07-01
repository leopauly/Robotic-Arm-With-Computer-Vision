#-------------------------------------------------------------------------------
# Name:        mresizer
# Purpose:     resizing images to 700x525 resolution.
# Images to resized are named n1,n2....n31
# Resized images are saved with names m1,m2....m31
# Author:      @leopauly
# Created:     19-06-2014
#-------------------------------------------------------------------------------

import cv2
import numpy as np

for i in range(1,32,1):
 j=str(i)
 img1=cv2.imread('n'+j+'.jpg')
 v= cv2.resize(img1,(700,525))
 #cv2.imshow('img',v)
 cv2.imwrite('m'+j+'.jpg',v)

cv2.waitKey()

