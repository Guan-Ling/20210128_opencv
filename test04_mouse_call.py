import cv2
import numpy as np

# 7_把滑鼠當畫筆

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK: #左鍵按兩下
        cv2.circle(img,(x,y),100,(255,0,0),-1)
    elif event==cv2.EVENT_RBUTTONDBLCLK: #右鍵按兩下
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    elif event==cv2.EVENT_MBUTTONDOWN: #按下滾輪
        cv2.circle(img,(x,y),100,(0,0,255),-1)


        
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27: #按esc停止
        break
cv2.destroyAllWindows()