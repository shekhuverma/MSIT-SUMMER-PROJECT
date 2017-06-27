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
    center = None
    # only proceed if at least one contour was found
    if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    # only proceed if the radius meets a minimum size
            if radius > 10:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(thresh, (int(x), int(y)), int(radius),
                            (0, 255, 255), 2)
                    cv2.circle(thresh, center, 5, (0, 0, 255), -1)
    #width = 640 height 480
    if center==None:
        continue
    else:
        x=(center[0]*1920)/640
        y=(center[1]*1080)/480
        pyautogui.moveTo(x,y)
##    cv2.imshow("frameDelta",frameDelta)
    cv2.imshow("thresh",thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    
