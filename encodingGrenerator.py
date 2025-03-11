import cv2 as cv
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://prof-kim-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket":"prof-kim.appspot.com"
})

folderPath = "image"
modepathlist=os.listdir(folderPath)
#print(modepathlist)
imagList = []
personIds= []

for path in modepathlist:
    imagList.append(cv.imread(os.path.join(folderPath,path)))
    #print(path)
    #print(os.path.splitext(path))
    personIds.append(os.path.splitext(path)[0])
    fileName=f"{folderPath}/{path}"
    bucket = storage.bucket()
    blob= bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    url = blob.generate_signed_url(expiration=3600)
    
print(len(imagList))

def findEncoding(imagesList):
    encodeList =[]
    
    for img in imagesList:
       
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print("Encoding Started ...")   
encodeListKnown = findEncoding(imagList)
encodeListKnownIds =[encodeListKnown,personIds]
print(encodeListKnownIds)
print("Encoding Complete")


file = open("encodeFile.p","wb")
pickle.dump(encodeListKnownIds,file)
file.close
print("File Saved")