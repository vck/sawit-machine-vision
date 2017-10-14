import os
import cv2



img = cv2.imread('data/raw/F0S1 ( L ).jpg')
img = img[10:300 , 10:440]
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('test', img)
cv2.waitKey(0)


