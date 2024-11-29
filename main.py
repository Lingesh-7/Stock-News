# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

# lingaweather@123,twilio=?DY2b!.4e!8G5Wp,recovery=XSGY8APJ8UYH1ZH8F5UZM2CD, num=+15188568535, LCJYVN9Z96ACDK9GYZ2FZ4N8

import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
num=os.environ.get("num")
tonum=os.environ.get("tonum")



openweathermap="https://api.openweathermap.org/data/2.5/forecast?"
api=os.environ.get("api")
lat=11.919550
lon=79.834505

parameter={
    'lat':lat,
    'lon':lon,
    'appid':api,
    'cnt':4
}

response=requests.get(url=openweathermap,params=parameter)
response.raise_for_status()
print(response)
data=response.json()
# print(data)
# weather_id1=data['list'][0]['weather'][0]['id']
# weather_desc1=data['list'][0]['weather'][0]['description']
# print(weather_id1,weather_desc1)
# weather_id2=data['list'][1]['weather'][0]['id']
# weather_desc2=data['list'][1]['weather'][0]['description']
# print(weather_id2,weather_desc2)

Umberala=False
for i in range(4):
    print(data['list'][i]['weather'][0]['id'])
    if data['list'][i]['weather'][0]['id']<700:
        Umberala=True

if Umberala:
    cilent=Client(account_sid,auth_token)
    message=cilent.messages.create(
        from_=f"{num}",
        to=f"{tonum}",
        body="It's going to rain today. Remember to carry a umberalla☔ with you"
        )
    print(message.status)


else:
    print("No rain")