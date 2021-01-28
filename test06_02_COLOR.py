# 把numpy簡寫成np
import numpy as np
# opencv
import cv2

# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# 9.4_拆顏色通道


img = cv2.imread('ALL01.jpg',1)
b=cv2.imread('ALL01.jpg',1)
# b[:,:,0]=0
# b[:,:,1]=0
b[100:200,100:200,0]=0
b[300:500,600:800,1]=0
b[500:600,300:500,2]=0
print(b)


# cv2.namedWindow('test',cv2.WINDOW_NORMAL)
# cv2.imshow('test',img)
# cv2.imshow('b',b)


# cv2.waitKey(0)
# cv2.destroyAllWindows()



# plt.imshow(img)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
# plt.show()

# plt.imshow(b)
cv2.namedWindow('b', cv2.WINDOW_NORMAL)
cv2.imshow('b',b)

cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.namedWindow('image')





