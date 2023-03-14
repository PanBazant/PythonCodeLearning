import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "f47a07bced830101bba597dcf2f7e4b5"
account_sid = "AC0e4ba82afcfdf6eb9c466c8c1bcbaaa5"
auth_token = "89414e09d7c542d1df66e1970a643949"
client = Client(account_sid, auth_token)


weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    message = client.messages \
                .create(
                     body="Bring and umbrella",
                     from_='+15075015612',
                     to='+48739662231'
                 )
    print(message.status)