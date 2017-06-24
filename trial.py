import numpy as np
import cv2,time,matplotlib
import pyautogui
aGest=cv2.CascadeClassifier('aGest.xml')
cam=cv2.VideoCapture(0)
last_time=time.time()
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (11, 11), 0)
    Agest=aGest.detectMultiScale(gray,1.3,1,minSize=(20,20))
    for (x,y,w,h) in Agest:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    #finding contours in the b/w image
##    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    cv2.imshow("thresh",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    
