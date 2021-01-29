import cv2
import numpy as np
from matplotlib import pyplot as plt
pts1 = np.float32([[0,0],[0,0],[0,0],[0,0]])
i=0
def savexy(event,x,y,flags,param):
    global pts1
    global i
    if event==cv2.EVENT_LBUTTONDBLCLK:
        # 把點標記綠色圈圈
        cv2.circle(img,(x,y),3,(0,255,0),3)
        print(x,y)
        pts1[i]=[x,y]
        i+=1
# img=cv2.imread('test10.jpg')
img=cv2.imread('test_09_number.jpg')
rows,cols,ch=img.shape
# pts2 = np.float32([[0,0],[300,0],[300,300],[0,300]])
pts2 = np.float32([[0,0],[400,0],[400,200],[0,200]]) #左上開始 順時針點
cv2.namedWindow('image')
cv2.setMouseCallback('image',savexy)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27 or i>3:  #四個點點完就關掉 可以不用按ESC
        break
cv2.destroyAllWindows()
M=cv2.getPerspectiveTransform(pts1,pts2)
# dst=cv2.warpPerspective(img,M,(300,300))
dst=cv2.warpPerspective(img,M,(400,200))
dst1 = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
plt.subplot(211), plt.imshow(img), plt.title('Input')
plt.subplot(212), plt.imshow(dst1), plt.title('Output')
plt.show()