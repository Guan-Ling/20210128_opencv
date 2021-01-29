# 13_轉換顏色空間 講義p.59
# 識別藍色

# import cv2
# flags=[i for in dir(cv2) if i startswith('COLOR_')]
# print (flags)
# cv2.cvtColor(img,cv2.COLOR_RGB2HSV)  #RGB to HSV

import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    # BGR to HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # 設定藍色閥值 100~124 / 43~255 / 46~255 
    lower_blue=np.array([110,50,50])  #50,50,50
    upper_blue=np.array([130,255,255])

    # # 紅色閥值 0~10 / 43~255 / 46~255 
    # lower_red=np.array([0,50,50])
    # upper_red=np.array([10,255,255])

    # # 綠色閥值 35~77 / 43~255 / 46~255 
    # lower_green=np.array([35,50,50])
    # upper_green=np.array([77,255,255])


    # 根據閥值建構mask
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    # mask1=cv2.inRange(hsv,lower_blue,upper_blue)
    # mask2=cv2.inRange(hsv,lower_red,upper_red)
    # mask3=cv2.inRange(hsv,lower_green,upper_green)


    # 對原圖像和mask進行"and運算"
    res=cv2.bitwise_and(frame,frame,mask=mask)
    # res=cv2.bitwise_and(frame,frame,mask=mask1)
    # res2=cv2.bitwise_and(res,res,mask=mask2)
    # res3=cv2.bitwise_and(res2,res2,mask=mask3)

    # 顯示圖像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    # cv2.imshow('mask1',mask1)
    # cv2.imshow('mask2',mask2)
    # cv2.imshow('mask3',mask3)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    # 按ECS關閉
    if k==27:
        break
# 關閉視窗
cv2.destroyAllWindows()