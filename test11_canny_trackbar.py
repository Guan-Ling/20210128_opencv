# canny邊緣偵測 & trackbar
# 數值沒有一定大或小比較好，要根據圖片特性去調整
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ALL01.jpg', 0)
cv2.imshow("images",img)
edges = cv2.Canny(img, 50, 150)

def nothing(x):
    pass
cv2.namedWindow('image')
cv2.createTrackbar('minval','image',0,255,nothing)
cv2.createTrackbar('maxval','image',0,255,nothing)

while(1):
    cv2.imshow('image',edges)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    minval=cv2.getTrackbarPos('minval','image')
    maxval=cv2.getTrackbarPos('maxval','image')
    edges = cv2.Canny(img, minval, maxval)



cv2.destroyAllWindows()