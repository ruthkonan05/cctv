import cv2 as cv
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import storage
from imutils import paths

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"databaseurl_firebase",
    "storageBucket":"prof-kim"
})
imagePaths = list(paths.list_images("images"))
# folderPath = "image"
# modepathlist=os.listdir(folderPath)
#print(modepathlist)
imagList = []
personIds= []

# for path in modepathlist:
for (i, path) in enumerate(imagePaths):
    print("[INFO] processing image {}/{}".format(i + 1,len(imagePaths)))
    name = path.split(os.path.sep)[-2]
    image = cv.imread(path)
    rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb,
		model="hog")

	# compute the facial embedding for the face
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
		# add each encoding + name to our set of known names and
		# encodings
        imagList.append(encoding)
        personIds.append(name)


    #print(path)
    #print(os.path.splitext(path))
print("[INFO] serializing encodings...")
data = {"encodings": imagList, "names": personIds}
f = open("encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()
    
print(len(imagList))



