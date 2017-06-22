import cv2
import numpy as np
cam=cv2.VideoCapture(0)
firstframe=None
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    if firstframe==None:
        firstframe=gray
        continue
    frameDelta = cv2.absdiff(firstframe, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cv2.imshow("frameDelta",frameDelta)
    cv2.imshow("thresh",thresh)
    cv2.imshow("trial",gray)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    
