import cv2,time,matplotlib
import numpy as np
import pyautogui
aGest=cv2.CascadeClassifier('aGest.xml')
cam=cv2.VideoCapture(0)
last_time=time.time()
print "Open is red close is blue"
while True:
    ret,img=cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Agest=aGest.detectMultiScale(gray, 1.3,1)
    for (x,y,w,h) in Agest:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    print "Frame rate == " ,1/(time.time()-last_time)
    last_time=time.time()
cam.release()
cv2.destroyAllWindows()
