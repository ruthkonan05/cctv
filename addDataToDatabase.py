import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"databaseurl_firebase"
})
ref = db.reference("personinfo")
data={
    "12345":{
        "name":"Beyonce",
        "status":"artist",
        "major":"Singer",
        "entry":8,
        "lastRegister":"2024-04-23 01:05:05",
        "state":"0",

    },
    "12346":{
        "name":"IU",
        "status":"artist",
        "major":"Singer",
        "entry":9,
        "lastRegister":"2024-04-23 01:06:05",
        "state":"0",
        "imageURL": "prof-kim.appspot.com/",

    },
    "12348":{
        "name":"Ruth",
        "status":"Master Student",
        "major":"Computer Engeeniring",
        "entry":5,
        "lastRegister":"2024-04-23 01:07:05",
        "state":"0",
        "imageURL": "/prof-kim.",

    },
    "12459":{
        "name":"Obama",
        "status":"President",
        "major":"President",
        "entry":1,
        "lastRegister":"2024-04-23 01:08:05",
        "state":"0",
        "imageURL": "gs://prof-kim.a",

    },
    "12349":{
        "name":"KIM Jong-Deok",
        "status":"Profesor",
        "major":"Computer Engeeniring",
        "entry":1,
        "lastRegister":"2024-04-23 01:08:05",
        "state":"0",
        "imageURL": "rof-kim.appsp",

    },
}
for key,value in data.items():
    ref.child(key).set(value)
