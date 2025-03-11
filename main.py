import cv2 as cv
import os
import pickle
import face_recognition
import numpy as np
import cvzone
import cv2 as cv
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials,firestore
from firebase_admin import storage
from datetime import datetime
import time

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://prof-kim-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket":"prof-kim.appspot.com"
})
bucket = storage.bucket()
cam = cv.VideoCapture(0)
# cam = cv.VideoCapture("rtsp://admin:TYIZXA@192.168.222.8/h264/ch1/main/av_stream")
if not cam.isOpened():
    print("Erreur: Impossible d'ouvrir le flux vidéo.")
    

width = 512
height = 384
cam.set(3, width)  # Définir la largeur
cam.set(4, height) 
imgBackground  = cv.imread("ressources/back1.png")
folderPath = "ressources/modes"
modepathlist=os.listdir(folderPath)
imageModeList = []
modeType=0
counter =0
id=-1
for path in modepathlist:
    imageModeList.append(cv.imread(os.path.join(folderPath,path)))
   # print(imageModeList)




#iport the encoding file
file = open("encodeFile.p","rb")
encodeListKnownIds =pickle.load(file)
file.close()
encodeListKnown,personIds = encodeListKnownIds
imgPerson=[]
#print(personIds)
# Référence à votre collection d'utilisateurs

# Référence à votre base de données Firestore
# db2 = firestore.client()
# users_ref = db2.collection('personinfo')

# # La nouvelle valeur que vous souhaitez attribuer à la clé "state"
# new_state_value = "0"

# # Fonction pour mettre à jour la valeur "state" pour tous les utilisateurs
# def update_state_for_all_users():
#     users = users_ref.stream()
#     for user in users:
#         # Mise à jour de la valeur "state" pour cet utilisateur
#         user_ref = users_ref.document(user.id)
#         user_ref.update({"state": new_state_value})
#     print("Toutes les valeurs 'state' ont été mises à jour avec succès.")

# Appel de la fonction pour mettre à jour les valeurs "state" pour tous les utilisateurs

while True:
    success , img = cam.read()
    if not success:
            print("Erreur: Impossible de lire l'image de la caméra.")
            break
    # img = cv.resize(img, (width, height))

    imgS = cv.resize(img,(0,0),None ,0.25,0.25)


    # imgS = cv.resize(img,(width, height),None ,0.25,0.25)




    imgS = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encoFaceCurframe = face_recognition.face_encodings(imgS,faceCurFrame)

   

    imgBackground[90:90+384, 63:63+512] = img
    imgBackground[49:49+477, 696:696+538] = imageModeList[modeType]
    if faceCurFrame:
        for encoFace,faceLoc in zip(encoFaceCurframe,faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encoFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encoFace)
            # print("matches",matches)
            # print("faceDis",faceDis)
        
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                #personIds[matchIndex]
                # print(personIds[matchIndex])

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox =  x1, y1 , x2 - x1 , y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id= personIds[matchIndex]
                if counter==0:
                    counter=1
                    modeType= 1
            else:
                modeType= 4


    
        if counter != 0:
            if counter == 1:
                print(f"1ier etape j affiche le counterwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
                studentinfo = db.reference(f"personinfo/{id}").get()
                #print(bucket.get_blob(f"image/12345.jpeg"))
                blob = bucket.get_blob(f"image/{id}.jpeg")
            
                #print(blob)
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgPerson = cv.imdecode(array, cv.COLOR_BGRA2BGR)

                dateTimeObject = datetime.strptime(studentinfo["lastRegister"],"%Y-%m-%d %H:%M:%S")
                temps_mis=(datetime.now()-dateTimeObject).total_seconds()
                if temps_mis > 30:
                    ref = db.reference(f'personinfo/{id}')
                    studentinfo['state'] = "1"
                    studentinfo['entry'] += 1
                    print(f"state {studentinfo['state']}")
                    print(f"state {studentinfo['entry']}")
                  
                    ref.child('entry').set(studentinfo['entry'])
                    ref.child('lastRegister').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    ref.child('state').set(studentinfo['state'])
                else:
                    print(f"le else etape j affiche le counter{counter}")
                    modeType = 3
                    counter = 0
                    imgBackground[49:49+477, 696:696+538] = imageModeList[modeType]
            if modeType != 3:

                if 10<counter <20: 
                    modeType=2
                imgBackground[49:49+477, 696:696+538] = imageModeList[modeType]
                if counter <=10: 
                    print(f"2ieme etape j affiche le counter{counter}")
                    cv.putText(imgBackground,str(studentinfo["entry"]),(740,95),cv.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)
                
                    cv.putText(imgBackground,str(studentinfo["status"]),(840,400),cv.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)
                    cv.putText(imgBackground,str(studentinfo["major"]),(830,435),cv.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),1)
                    cv.putText(imgBackground,str(studentinfo["lastRegister"]),(850,472),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
                    #pour center le nom
                    # (w,h),_ =cv.getTextSize(studentinfo["name"],cv.FONT_HERSHEY_COMPLEX,1,1)
                    # offset =(310-w)//2
                    # cv.putText(imgBackground,str(studentinfo["name"]),(840+offset,310),cv.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)
                    cv.putText(imgBackground,str(studentinfo["name"]),(840,360),cv.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)
                    imgBackground[84:84+225, 851:851+225] = imgPerson
                counter+=1
                print(f"voyons la valeur du conpter ici{counter}")
                if counter >= 20:
                    print(f"voyons la valeur du conpter ici aussi{counter}")
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[49:49+477, 696:696+538] = imageModeList[modeType]
            # else:
            #     print("qui cest")
                # print(" match index",matchIndex)
    else:
        print("on est dans la fin")
        modeType = 0
        counter = 0
        studentinfo_u = db.reference(f"personinfo/").get()
        for doc in studentinfo_u:
            ref_1 = db.reference(f'personinfo/{doc}')
            studentinfo_u_i = db.reference(f"personinfo/{doc}").get()
            
            
            
        # for doc in studentinfo_u:
        #     ref_1 = db.reference(f'personinfo/{doc}')
        #     studentinfo_u_i = db.reference(f"personinfo/{doc}").get()
        #     studentinfo_u_i['state'] = "0"
            
        #     ref_1.child('state').set(studentinfo_u_i['state'])
        #     ref_1.child('lastRegister').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #studentinfo_u.child('lastRegister').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            dateTimeObject_u = datetime.strptime(studentinfo_u_i["lastRegister"],"%Y-%m-%d %H:%M:%S")
            temps_mis_u=(datetime.now()-dateTimeObject_u).total_seconds()
            if temps_mis_u > 45:
                print("on est dans la fin  rrrrrrrr")
        
                studentinfo_u_i['state'] = "0"
            
                ref_1.child('state').set(studentinfo_u_i['state'])
                ref_1.child('lastRegister').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        # print("Mise à jour terminée avec succès.")
    cv.imshow("imge Background",imgBackground)
    cv.waitKey(1)
    #time.sleep(30)
    # qSpN-k33XsBtbNI
    # TYIZXA
    # qSpN-k33XsBtbNI
    # 12345#PAFFTYIZXA