import cv2,matplotlib
import numpy as np
import pyautogui
import functions as f
HIST=[]
HOG=[]
np.array(HIST)
np.array(HOG)
img=cv2.imread("test.jpg")
print img.shape[0]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for a in range(0,len(img),8):#column
    for b in range(0,len(img),8):#row
        temp=img[b:b+8,a:a+8]
        np.array(temp)
        hist=cv2.calcHist([temp],[0],None,[256],[0,256])
        print hist
        break
        HIST.append(temp)
cv2.destroyAllWindows()
