import cv2,matplotlib,os
import numpy as np
from PIL import Image
from skimage.feature import hog
from sklearn.svm import SVC
from sklearn.externals import joblib   
pos_path="hand_data"
neg_path="neg_data"
Features=[]
Features=np.array(Features)
Labels=[]
classifier=SVC(kernel='rbf',random_state=0)
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
        joblib.dump(fd,"features.dat")
        Features=np.append(Features,fd)
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
        joblib.dump(fd,"features.dat")
        Features=np.append(Features,fd)
        Labels.append(0)
    except IOError:
        continue
classifier.fit(Features,Labels)
# Save trained model 
svm.save("digits_svm_model.yml");
cv2.destroyAllWindows()
