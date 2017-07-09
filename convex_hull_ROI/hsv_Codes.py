import cv2
import numpy as np
import pickle
print "Adjust the sliders so that background will be become black (Choose the best possible combination)"
print "Move the switch (Last slider) to one if your are darkening the subject otherwise dont change it"
cap = cv2.VideoCapture(0)
# Creating a window for later use
cv2.namedWindow('result')
def nothing(x):
    pass

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('h1', 'result',1,170,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)
cv2.createTrackbar('switch', 'result',0,1,nothing)
while(1):
    _, frame = cap.read()
    frame=cv2.flip(frame,1)
    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # get info from track bar and appy to result
    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')
    h1 = cv2.getTrackbarPos('h1','result')
    s1 = cv2.getTrackbarPos('switch','result')
    arr=[h,s,v]
##    if arr[0]==0:
##        arr[0]=180
##    for a in range(1,len(arr)):
##        if arr[a]==0:
##            arr[a]=255
    arr=np.array(arr,dtype=np.uint8)
    print arr
    np.savetxt("config.txt",arr,delimiter="'")
    # Normal masking algorithm
    lower_blue = np.array([h,s,v])
    upper_blue = np.array([180-h1,255,255])
    np.savetxt("config1.txt",upper_blue,delimiter="'")
    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    result = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('result',result)
    np.savetxt("config3.txt",[s1],delimiter="'")
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
