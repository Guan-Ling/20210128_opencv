import numpy as np
import cv2

# 6_畫圖

# 產生空白圖 unint8-->0~255
img=np.zeros((512,512,3), np.uint8)

# 直線
# cv2.line(image,(startCoor),(EndCoor),(B,G,R),thickness)                   #Color is by default black
cv2.line(img,(0,0),(500,500),(255,0,0),5)
# cv2.line(img,(0,500),(500,0),(0,255,0),5)
# cv2.line(img,(0,250),(500,250),(0,0,255),5)

# 矩形
# cv2.rectangle(image,(topLeftCoor),(bottomRightCoor),(0,0,0),thickness)                   #Color is by default black
cv2.rectangle(img,(100,100),(300,300),(0,255,0),3)

# 圓形
# cv2.circle(image,(CenterCoordinates), radius, (0, 0, 0) ,thickness)                     #Color is by default black
cv2.circle(img,(200,200),150,(0,0,255),1)

# 橢圓形
# cv2.ellipse(image,(CenterCoordinates),(height,width), RotationAngle,startingAngle,finalangle,(0, 0, 0),thickness)                        #Color is by default black
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.ellipse(img,(400,400),(100,50),0,0,360,(0,255,0),-1)

# 多邊形
pts=np.array([[200,200],[300,100],[400,200],[400,400],[200,400]], np.int32)
print(pts)
# 照著點的順序畫
# cv2.polylines(image,[coordinates],Boolean(True if closed polygon),(0,0,0))                   #Color is by default black
cv2.polylines(img,[pts],1,(120,120,120),2)

# 輸入字otex
# font = cv2.fontstyle
# cv2.putText(image, "text", (Coordinates),font, fontsize, (0, 0, 0),thickness, cv2.LineType)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "text", (100,100),font, 2, (255, 255, 255),5) #無法寫中文





# for i in range(100):
#     cv2.rectangle(img,(100+i-1,100),(300+i-1,300),(0,0,0),3)
#     cv2.rectangle(img,(100+i,100),(300+i,300),(0,255,0),3)
    


cv2.imshow("Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()









