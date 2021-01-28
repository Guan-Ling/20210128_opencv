# 把numpy簡寫成np
import numpy as np
# opencv
import cv2

# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# orimg

# 讀照片 檔名(或是貼絕對路徑(不建議)D:\\2021\\20210128_opencv\\ALL01.jpg)-->右鍵圖片 copy path要用兩個反斜線
# cv2.IMREAD_COLOR(彩色)-->1/cv2.IMREAD_GRAYSCALE(灰階)-->0
img = cv2.imread('ALL01.jpg',1)

# BGR 0-255
# print(img)
px=img[100,100]
print(px)
pxb=img[100,100,0] #抓B的值
print(pxb)

# 把[100,100]改黑色
img[100,100]=[0,0,0]
print(img[100,100])


# 把[100,100]的B值(0)改黑色   G值(1) R值(2) 
# img[100,100,0]=[0,0,0]
# print(img[100,100,0])

# 圖像屬性 x,y值和color(灰階就只回傳x,y值)
print(img.shape)


img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# ROI 先y再x
# roi=img1[77:122,640:788]  #45 148 另一格也要大小一致
# img1[149:194,460:608]=roi  #45 148

# roi=img1[200:400,200:400]
# img1[300:500,300:500]=roi

# roi=img1[0:1020,0:200]
# img1[0:1020,600:800]=roi

roi=img1[0:200,0:1024]
img1[567:767,0:1024]=roi



plt.imshow(img1)
plt.xticks([]), plt.yticks([])  # 顯示座標
plt.show()






