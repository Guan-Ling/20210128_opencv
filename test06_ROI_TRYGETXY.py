# TRY 用滑鼠標點
# 標原兩點 第三下點新圖左上 之後按ESC

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('ALL01.jpg',1)
print(img.shape)

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)



# roi=img1[0:200,0:1024]
# img1[567:767,0:1024]=roi

xx=[]
yy=[]

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: #按左鍵
        xx.append(x)
        yy.append(y)



cv2.namedWindow('three points and esc')
cv2.setMouseCallback('three points and esc',draw_circle)
while(1):
    cv2.imshow('three points and esc',img)
    if cv2.waitKey(20)&0xFF==27: #按esc停止
        break




print(xx,yy)

roi=img1[yy[0]:yy[1],xx[0]:xx[1]]
xx.append(xx[1]-xx[0]+xx[2])
yy.append(yy[1]-yy[0]+yy[2])
print(xx,yy)
img1[yy[2]:yy[3],xx[2]:xx[3]]=roi

# cv2.namedWindow('final', cv2.WINDOW_NORMAL)
# cv2.imshow('final',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



plt.imshow(img1)
plt.xticks([]), plt.yticks([])  # 顯示座標
plt.show()






