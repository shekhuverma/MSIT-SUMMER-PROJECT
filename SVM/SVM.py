import cv2
import numpy as np
import matplotlib.pyplot as plt
cam = cv2.VideoCapture(0)
##aGest=cv2.CascadeClassifier('aGest.xml')
##Agest=aGest.detectMultiScale(mag, 1.3,1)
##print Agest
##for (x,y,w,h) in Agest:
##    cv2.rectangle(mag,(x,y),(x+w,y+h),(255,255,255),2)
while(True):
    ret, img = cam.read()
    img=np.float32(img)/255.0
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
    mag, angle = cv2.cartToPolar(gx, gy)
    bins = np.int32(16*angle/(2*np.pi))
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)
##    cv2.imshow('gx',gx)
##    cv2.imshow('gy',gy)
##    cv2.imshow("mag",mag)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
