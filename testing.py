import cv2
import numpy as np
import matplotlib.pyplot as plt
cam = cv2.VideoCapture(0)
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceNp=np.array(gray)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    x=cv2.calcHist(hsv,[0],None,[256],[0,256])
    cv2.normalize(x,x,0,255,cv2.NORM_MINMAX)
    cv2.imshow("hsv",hsv)
    cv2.imshow('Normal gray',gray)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
