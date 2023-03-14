# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC0e4ba82afcfdf6eb9c466c8c1bcbaaa5"
auth_token = "89414e09d7c542d1df66e1970a643949"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test",
                     from_='+15075015612',
                     to='+48739662231'
                 )

print(message.sid)