import cv2,matplotlib,os
import numpy as np
from PIL import Image
path="hand_data"
Descriptor=[]
svm = cv2.ml.SVM_create()
# Set SVM type
svm.setType(cv2.ml.SVM_C_SVC)
# Set SVM Kernel to Radial Basis Function (RBF) 
svm.setKernel(cv2.ml.SVM_RBF)
# Set parameter C
svm.setC(100)
# Set parameter Gamma
svm.setGamma(20)
#######descriptor values
winSize = (20,20)
blockSize = (10,10)
blockStride = (5,5)
cellSize = (10,10)
nbins = 9
derivAperture = 1
winSigma = -1.
histogramNormType = 0
L2HysThreshold = 0.2
gammaCorrection = 1
nlevels = 64
signedGradients = True
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels,signedGradients)
## getting images from dataset
paths=[os.path.join(path,x) for x in os.listdir(path)]
for x in paths:
    if x=="hand_data\Thumbs.db":
        continue
    try:
        img=Image.open(x).convert('L')
        img=np.array(img,dtype='uint8')
        descriptor=hog.compute(img)
        svm.train(Descriptor, cv2.ml.ROW_SAMPLE,[1])
    except IOError:
        continue
# Save trained model 
svm.save("digits_svm_model.yml");
cv2.destroyAllWindows()
