import cv2
import numpy as np

cap = cv2.VideoCapture(0) #用第幾個相機
if cap.isOpened() == False:
    print("Error in opening video stream or file")
#Define the codec for the Video
# fourcc = cv2.VideoWriter_fourcc("Fourcc Codec Eg-XVID")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Create Video Writer Object
writer = cv2.VideoWriter('test02_02.avi',fourcc,30, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow("Frame",frame)
        # Exit on pressing esc 按esc取消
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release() #關相機
writer.release() #關檔案
cv2.destroyAllWindows()

