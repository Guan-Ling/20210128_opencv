# 用test0012.jpg 找contours!
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test27.jpg')
# img = cv2.imread('test0012.jpg')
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (11, 11), 0)  #高斯濾波平滑處理
edges = cv2.Canny(blurred,60,160)   #用canny找edge  可調60 160 可改track bar
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #找contours
print(len(contours)) #共幾個
draw = cv2.drawContours(img1, contours, -1, (0, 255, 0), 5) #框綠色


ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours2, hierarchy2 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours2))
# cnt2=contours2[2]

def nothing(x):
    pass
cv2.namedWindow('image')
cv2.createTrackbar('minval','image',0,255,nothing)
cv2.createTrackbar('maxval','image',0,255,nothing)

WindowName = 'Approx'  # 視窗名字
cv2.namedWindow(WindowName, cv2.WINDOW_AUTOSIZE)  # 建立空視窗
cv2.createTrackbar('epsilon', WindowName, 0, 10, nothing)  # 兩張圖像間轉換

while(1):
    cv2.imshow('image',edges)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    minval=cv2.getTrackbarPos('minval','image')
    maxval=cv2.getTrackbarPos('maxval','image')
    edges = cv2.Canny(blurred, minval, maxval)

    img3 = img.copy()
    n = 10 - cv2.getTrackbarPos('epsilon', WindowName)  # 獲取a1滑動bar值

    for i in contours2:
        length = cv2.arcLength(i, True) #算周長

        epsilon = (n/100)*length  #輪廓近似epsilon 用少少的點去組成輪廓形狀
        approx = cv2.approxPolyDP(i, epsilon, False) #true閉合 false開著

        cv2.drawContours(img3, approx, -1, (0, 255, 0), 3)
        cv2.polylines(img3, [approx], True, (0, 255, 0), 3) #[approx]剩下的點
        cv2.imshow(WindowName, img3)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break




cnt2=[]
for i in contours2:
    cnt2.append(cv2.boundingRect(i))

# bounding_boxes = [cv2.boundingRect(cnt2) for cnt2 in contours2]
img2 = img.copy()
for i in cnt2:
     [x , y, w, h] = i
     cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),5)











# img2 = img.copy()
# for i in range(0,len(contours2),100):
#     x,y,w,h = cv2.boundingRect(contours2[i])
#     img22 = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

# # 最小矩形
# img2 = img.copy()
# rect = cv2.minAreaRect(contours2)
# box = cv2.boxPoints(rect)
# box = np.int0(box)  # 獲得矩形頂點
# area = cv2.contourArea(box)
# width = rect[1][0]
# height = rect[1][1]
# cv2.polylines(img2, [box], True, (0, 255, 0), 3) #畫線 點在box裡
# # text1 = 'Width: ' + str(int(width)) + ' Height: ' + str(int(height))
# # text2 = 'Rect Area: ' + str(area)
# # cv2.putText(img2, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
# # cv2.putText(img2, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
# draw2 = cv2.drawContours(img2, contours2, -1, (0, 255, 0), 10)





plt.subplot(151), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('Original Image')

plt.subplot(152), plt.imshow(edges,cmap='gray'), plt.title('Edge Image')
plt.subplot(153), plt.imshow(cv2.cvtColor(draw,cv2.COLOR_BGR2RGB)), plt.title('contour Image')
plt.subplot(154), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)), plt.title('Rectangle')
plt.subplot(155), plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)), plt.title('epsilon')
plt.show()



# 自動取canny
# def auto_canny(image, sigma=0.33):
# # compute the median of the single channel pixel intensities
# v = np.median(image)
# # apply automatic Canny edge detection using the computed median
# lower = int(max(0, (1.0 – sigma) * v))
# upper = int(min(255, (1.0 + sigma) * v))
# edged = cv2.Canny(image, lower, upper)
# # return the edged image
# return edged