import cv2,time,matplotlib
import numpy as np
import pyautogui
kernel=np.ones((5,5),np.uint8)
ORANGE_MIN = np.array([0, 0, 0],np.uint8)
ORANGE_MAX = np.loadtxt('config.txt')
ORANGE_MAX=np.array(ORANGE_MAX,dtype=np.uint8)
for a in range(len(ORANGE_MAX)):
    if ORANGE_MAX[a]==0:
        ORANGE_MAX[a]=255
    else:
        continue
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
aGest=cv2.CascadeClassifier('haar_cascades\\aGest.xml')
cam=cv2.VideoCapture(0)
last_time=time.time()
while True:
    ret,img=cam.read()
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)   #converting to hsv for bg filtering
    hsv_img = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
    res = cv2.bitwise_and(img,img, mask= hsv_img)   #masking image to remove bg
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    gray = clahe.apply(gray)        #histogram normalisation
    gray = cv2.medianBlur(gray,5)  #filtering to remove noise
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    Agest=aGest.detectMultiScale(gray, 1.3,1)
    for (x,y,w,h) in Agest:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,0),2)
####        x=x+w/2
####        y=y+h/2
####        x=(x*1920)/640
####        y=(y*1080)/480
####        pyautogui.moveTo(x,y)
    cv2.imshow("result",gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    print "Frame rate == " ,1/(time.time()-last_time)
    last_time=time.time()
cam.release()
cv2.destroyAllWindows()
