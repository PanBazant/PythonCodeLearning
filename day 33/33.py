import time
import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = 0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) #przekazujemy dane do zapytania
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()
print(sunrise)
print(time_now)
