import cv2
import pyautogui
import numpy as np
cam=cv2.VideoCapture(0)
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (11, 11), 0)
    ret,img2=cam.read()
    gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (11, 11), 0)
    #detecting motion by subtracitng frames
    frameDelta = cv2.absdiff(gray2,gray)
    thresh = cv2.threshold(frameDelta, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=3)
    #finding contours in the b/w image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    cv2.drawContours(thresh, cnts, -1, (0,255,0), 3)
    cv2.imshow("thresh",thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    
