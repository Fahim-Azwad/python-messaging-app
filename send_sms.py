from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio, my_sid

client = Client(account_sid, auth_token)

my_msg = ''.join(['Bad boi :)\n' for i in range(100)])

message = client.messages \
    .create(to=my_cell,
            body=my_msg,
            messaging_service_sid = my_sid
     )

print(message.sid)