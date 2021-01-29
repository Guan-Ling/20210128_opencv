# 10.2_addweighted圖像混合
# 10_圖像加法 兩圖大小一樣
# 相加若超過255 取255
# 加-->越加越亮 減-->越減越暗

# 計算時間e1 e2

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('ALL01.jpg',1)
b=cv2.imread('ALL01.jpg',1)

# 開始計時
e1=cv2.getTickCount()

img1=b[600:700,100:300]
img2=b[100:200,700:900]
# print(img1)
# print(img2)


# 改透明度
dst=cv2.addWeighted(img1,0.3,img2,0.7,0)
b[100:200,700:900]=dst

# 結束計時
e2=cv2.getTickCount()
t=(e2-e1)/cv2.getTickFrequency()
print(t)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.namedWindow('b', cv2.WINDOW_NORMAL)
cv2.imshow('b',b)
cv2.waitKey(0)
cv2.destroyAllWindows()






