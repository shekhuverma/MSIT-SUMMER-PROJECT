import cv2
import numpy as np
import pickle
print "Change the slider so that your hand will be coloured black (Choose the bes tpossible combination)"
cap = cv2.VideoCapture(0)
# Creating a window for later use
cv2.namedWindow('result')
def nothing():
    pass
# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)
while(1):
    _, frame = cap.read()
    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # get info from track bar and appy to result
    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')
    arr=[h,s,v]
    arr=np.array(arr,dtype=np.uint8)
    np.savetxt("config.txt",arr,delimiter="'")
    # Normal masking algorithm
    lower_blue = np.array([h,s,v])
    upper_blue = np.array([180,255,255])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

cap.release()

cv2.destroyAllWindows()
