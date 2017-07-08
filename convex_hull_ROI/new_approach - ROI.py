import cv2,time,pyautogui
import numpy as np
print "Press Q to quit the program at any time......."
print "Move the hand within the rectangle....."
kernelopen=np.ones((5,5),np.uint8)
kernelclose=np.ones((10,10),np.uint8)
cap = cv2.VideoCapture(0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
#reding from config file and applying settings
ORANGE_MIN = np.array([0, 0, 0],np.uint8)
ORANGE_MAX = np.loadtxt('config.txt')
ORANGE_MAX=np.array(ORANGE_MAX,dtype=np.uint8)
print ORANGE_MAX

while(cap.isOpened()) :
    last_time=time.time()
    ret,img = cap.read() #capturing frame
    img=cv2.flip(img,1)
    cv2.rectangle(img,(0,0),(320,300),(0,255,0),2)
    img2=img[:320,:300]
########### pre processing #################
    hsv_img = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)   #converting to hsv for bg filtering
    hsv_img = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
    res = cv2.bitwise_and(img2,img2, mask= hsv_img)   #masking image to remove bg
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)   #converting to grayscale
    gray = clahe.apply(gray)        #histogram normalisation
    ret,thresh1 = cv2.threshold(gray,10,255,cv2.THRESH_BINARY_INV)
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernelopen)
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernelclose)
    
##################################
    _,contours,heirachy= cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros(img2.shape,np.uint8)
    max_area=0
##### finding the biggest contour ##############
    try:
        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area 
                ci=i
        cnt=contours[ci]
    except:
        continue
    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)
    if moments['m00']!=0:
        cx = int(moments['m10']/moments['m00']) # cx = M10/M00
        cy = int(moments['m01']/moments['m00']) # cy = M01/M00
    centr=(cx,cy)       
    cv2.circle(img,centr,5,[0,0,255],2)       
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2) 
    cv2.drawContours(drawing,[hull],0,(0,0,255),2) 
    cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    hull = cv2.convexHull(cnt,returnPoints = False)
    if True:
        defects = cv2.convexityDefects(cnt,hull)
        mind=0
        maxd=0
        try:
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                dist = cv2.pointPolygonTest(cnt,centr,True)
                cv2.line(img,start,end,[0,255,0],2)
                cv2.circle(img,far,5,[0,0,255],-1)
        except:
            continue
##        print i 
        if i in range(4,6):
            x=(cx*1920)/320
            y=(cy*1080)/300
            pyautogui.moveTo(x,y)
        i=0
    cv2.imshow('result',img)
    cv2.imshow("output",drawing)
##    cv2.imshow("thresh1",thresh1)
    print "FPS==",1.0/(time.time()-last_time)
    last_time=time.time()
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
