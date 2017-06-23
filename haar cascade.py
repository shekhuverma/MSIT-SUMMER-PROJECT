import cv2,time,matplotlib
import numpy as np
import sqlite3
open_palm = cv2.CascadeClassifier('open_palm.xml')
close_palm = cv2.CascadeClassifier('closed_palm.xml')
cam=cv2.VideoCapture(0)
last_time=time.time()
print "Open is red close is blue"
while True:
    ret,img=cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Open = open_palm.detectMultiScale(gray, 1.3, 1)
    Close = close_palm.detectMultiScale(gray, 1.3, 1)
    for (x,y,w,h) in Open:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    for (x,y,w,h) in Close:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    print "Frame rate == " ,1/(time.time()-last_time)
    last_time=time.time()
cam.release()
cv2.destroyAllWindows()
