import cv2,matplotlib,os
import numpy as np
from PIL import Image
from skimage.feature import hog
from sklearn.svm import LinearSVC
from sklearn.externals import joblib  
import pandas as pd 
pos_path="hand_data"
neg_path="neg_data"
Features=[]
Labels=[]
classifier=LinearSVC()
## getting positive images from dataset
pos_paths=[os.path.join(pos_path,x) for x in os.listdir(pos_path)]
for x in pos_paths:
    if x=="hand_data\Thumbs.db":
        continue
    try:    
        img=Image.open(x).convert('L')
        img=np.array(img)
        fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualise=True)
        Features.append(fd)
        Labels.append(1)
    except IOError:
        continue
##Getting negative images from dataset
neg_paths=[os.path.join(neg_path,x) for x in os.listdir(neg_path)]
for x in neg_paths:
    if x=="hand_data\Thumbs.db":
        continue
    try:    
        img=Image.open(x).convert('L')
        img=np.array(img)
        fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualise=True)
        Features.append(fd)
        Labels.append(0)
    except IOError:
        continue
#saving files for future use
joblib.dump(Features,"features.pkl")
joblib.dump(Labels,"labels.pkl")
#loading files
Labels=joblib.load("labels.pkl")
Features=joblib.load("features.pkl")
#data processing
data=pd.DataFrame.from_records(Features,columns=None)
temp=temp[:,:1152]
temp=np.array(data)
classifier.fit(temp,Labels)
#saving the model
joblib.dump(classifier,"model1.pkl")
cv2.destroyAllWindows()
