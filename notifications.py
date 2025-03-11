import firebase_admin
from firebase_admin import credentials,messaging

cred = credentials.Certificate("serviceAccountKey.json")

default_app = firebase_admin.initialize_app(cred)
registration_token = 'token'

    # See documentation on defining a message payload.
message = messaging.Message(
    notification=messaging.Notification(
        title='test',
        body='python push test',
        image='https://icnu.kr/coupang/logo.png'
    ),
    data = {
        'title':'test',
        'message':'python fcm test',
        'mode':'test',
        'data':'12345'
    },
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
# [END send_to_token]
