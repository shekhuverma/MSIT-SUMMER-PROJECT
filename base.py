import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    ret,img2=cam.read()
    gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)
    #detecting motion by subtracitng frames
    frameDelta = cv2.absdiff(gray2, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=3)
    #finding contours in the b/w image
    img,cnts,_ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        if cv2.contourArea(c) < 100:
            continue
        (x,y, w, h) = cv2.boundingRect(c)
# compute the bounding box for the contour, draw it on the frame,
        cv2.rectangle(thresh, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("frameDelta",frameDelta)
    cv2.imshow("thresh",thresh)
    cv2.imshow("trial",gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    
