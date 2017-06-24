import numpy as np
import cv2,matplotlib
import pyautogui
aGest=cv2.CascadeClassifier('aGest.xml')
fgbg = cv2.createBackgroundSubtractorMOG2()
cam=cv2.VideoCapture(0)
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    bg_gray=fgbg.apply(gray)
    ret,mask = cv2.threshold(bg_gray,40,255,cv2.THRESH_BINARY)
    bg_gray = cv2.GaussianBlur(bg_gray, (5, 5), 0)
    res = cv2.bitwise_and(bg_gray,gray,mask= mask)
    res = cv2.morphologyEx(res, cv2.MORPH_CLOSE,kernel=3)
    Agest=aGest.detectMultiScale(res,1.3,1,minSize=(20,20))
    for (x,y,w,h) in Agest:
        cv2.rectangle(res,(x,y),(x+w,y+h),(255,255,0),2)
    #finding contours in the b/w image
##    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    cv2.imshow("thresh",res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    
