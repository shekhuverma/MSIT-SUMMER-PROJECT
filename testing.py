import cv2,matplotlib,os
import numpy as np
from PIL import Image
from sklearn.svm import SVC
path="hand_data"
classifier=SVC(kernel='rbf',random_state=0)
#######descriptor values
winSize = (100,100)
blockSize = (25,25)
blockStride = (5,5)
cellSize = (5,5)
nbins = 9
derivAperture = 1
winSigma = -1.
histogramNormType = 0
L2HysThreshold = 0.2
gammaCorrection = 1
nlevels = 64
signedGradients = True
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels, signedGradients)
## getting images from dataset
paths=[os.path.join(path,x) for x in os.listdir(path)]
for x in paths:
    if x=="hand_data\Thumbs.db":
        continue
    try:
        img=Image.open(x).convert('L')
        img=np.array(img)
        descriptor=hog.compute(img)
        classifier.fit(descriptor,[1])
    except IOError:
        continue
# Save trained model 
svm.save("digits_svm_model.yml");
cv2.destroyAllWindows()
