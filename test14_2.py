import dlib
import cv2
import imutils

img = cv2.imread('test14_00.jpg')

img = imutils.resize(img, width=1280)
detector = dlib.get_frontal_face_detector()

# 偵測人臉，輸出分數
# 第二個參數是指定反取樣（unsample）的次數，如果圖片太小的時候，將其設為 1 可讓程式偵較容易測出更多的人臉。
# 第三個參數是門檻值
face_rects, scores, idx = detector.run(img, 0, -1)

for i, d in enumerate(face_rects):
  x1 = d.left()
  y1 = d.top()
  x2 = d.right()
  y2 = d.bottom()
  text = "%2.2f(%d)" % (scores[i], idx[i])

  cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)

  # 標示分數
  cv2.putText(img, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,
          0.7, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow("Face Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()