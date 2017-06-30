import cv2,time,matplotlib
import numpy as np
import pyautogui
import functions as f
aGest=cv2.CascadeClassifier('haar_cascades\\aGest.xml')
print aGest
cam=cv2.VideoCapture(0)
last_time=time.time()
print "Open is red close is blue"
while True:
    ret,img=cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    Open = open_palm.detectMultiScale(gray, 1.05, 6,minSize=(30,30),maxSize=(50,50))
##    Close = close_palm.detectMultiScale(gray, 1.3, 1,)
    Agest=aGest.detectMultiScale(gray, 1.3,1)
    for (x,y,w,h) in Agest:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
##        x=x+w/2
##        y=y+h/2
##        x=(x*1920)/640
##        y=(y*1080)/480
##        pyautogui.moveTo(x,y)
    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    print "Frame rate == " ,1/(time.time()-last_time)
    last_time=time.time()
cam.release()
cv2.destroyAllWindows()
