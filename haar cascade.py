import cv2,time,matplotlib
import numpy as np
import pyautogui
def non_max_suppression_fast(boxes, overlapThresh):
    # if there are no boxes, return an empty list
    if len(boxes) == 0:
            return []
    # if the bounding boxes integers, convert them to floats --
    # this is important since we'll be doing a bunch of divisions
    if boxes.dtype.kind == "i":
            boxes = boxes.astype("float")
    # initialize the list of picked indexes	
    pick = []
    # grab the coordinates of the bounding boxes
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]
    # compute the area of the bounding boxes and sort the bounding
    # boxes by the bottom-right y-coordinate of the bounding box
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)
    # keep looping while some indexes still remain in the indexes
    # list
    while len(idxs) > 0:
            # grab the last index in the indexes list and add the
            # index value to the list of picked indexes
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)
            # find the largest (x, y) coordinates for the start of
            # the bounding box and the smallest (x, y) coordinates
            # for the end of the bounding box
            xx1 = np.maximum(x1[i], x1[idxs[:last]])
            yy1 = np.maximum(y1[i], y1[idxs[:last]])
            xx2 = np.minimum(x2[i], x2[idxs[:last]])
            yy2 = np.minimum(y2[i], y2[idxs[:last]])
            # compute the width and height of the bounding box
            w = np.maximum(0, xx2 - xx1 + 1)
            h = np.maximum(0, yy2 - yy1 + 1)
            # compute the ratio of overlap
            overlap = (w * h) / area[idxs[:last]]
            # delete all indexes from the index list that have
            idxs = np.delete(idxs, np.concatenate(([last],
                    np.where(overlap > overlapThresh)[0])))
    # return only the bounding boxes that were picked using the
    # integer data type
    return boxes[pick].astype("int")
##open_palm = cv2.CascadeClassifier('open_palm.xml')
##close_palm = cv2.CascadeClassifier('closed_palm.xml')
aGest=cv2.CascadeClassifier('aGest.xml')
cam=cv2.VideoCapture(0)
last_time=time.time()
print "Open is red close is blue"
while True:
    ret,img=cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    Open = open_palm.detectMultiScale(gray, 1.05, 6,minSize=(30,30),maxSize=(50,50))
##    Close = close_palm.detectMultiScale(gray, 1.3, 1,)
    Agest=aGest.detectMultiScale(gray, 1.3,1,winstride=(2,2))
    Agest=non_max_suppression_fast(Agest, 3)
    for (x,y,w,h) in Agest:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
##        x=x+w/2
##        y=y+h/2
##        x=(x*1920)/640
##        y=(y*1080)/480
##        pyautogui.moveTo(x,y)
    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    print "Frame rate == " ,1/(time.time()-last_time)
    last_time=time.time()
cam.release()
cv2.destroyAllWindows()
