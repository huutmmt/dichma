import cv2
import os
import numpy as np
from PIL import Image

# huu cap nhat 

# tung cap nhat

# Create LBPH Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer.create()
path = 'dataSet'

def getImagesAndLabels(path):
    # Get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)] 
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        # Split to get ID of the image
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow("training", faceNp)
        cv2.waitKey(10)
    return IDs, faces

Ids, faces = getImagesAndLabels(path)

# Training
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
