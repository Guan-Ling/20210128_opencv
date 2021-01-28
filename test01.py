# 把numpy簡寫成np
import numpy as np
# opencv
import cv2

# 讀照片 檔名(或是貼絕對路徑(不建議)D:\\2021\\20210128_opencv\\ALL01.jpg)-->右鍵圖片 copy path要用兩個反斜線
# cv2.IMREAD_COLOR(彩色)-->1/cv2.IMREAD_GRAYSCALE(灰階)-->0
img = cv2.imread('ALL01.jpg',0)

# BGR 0-255
print(img)

# cv2.WINDOW_NORMAL就可調整視窗大小，但無法等比例調整
cv2.namedWindow('title_test', cv2.WINDOW_NORMAL)

# show 圖片title---->test
cv2.imshow("title_test",img)

# 存成檔名為ALL02_gray.jpg的檔案
cv2.imwrite('ALL02_gray.jpg',img)

# 等輸入任一按鍵照片才消失
cv2.waitKey(0)
cv2.destroyAllWindows()

