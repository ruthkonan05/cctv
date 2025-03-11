import firebase_admin
from firebase_admin import credentials,messaging

cred = credentials.Certificate("serviceAccountKey.json")

default_app = firebase_admin.initialize_app(cred)
registration_token = 'fRUE3jhfSKiyIwVhbhvVkm:APA91bGzwsvqF5OuUoVA7OrNc-S0LQKCmTEHoIk5_JPn8CI_d9LWdpf7bXi8olvXhH7FB4xVndPmUqQBypOxViXjBRa0BU3AO-73z1-cug465SCzL57KCOivH5pdQ_mRLYEyxoHpEIM4'

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
