import requests

from twilio.rest import Client

OWM_Endpoint= "http://api.openweathermap.org/data/2.5/onecall"
api_key="9b8cd119d1919cc83fdb63111dc83aa2"

account_sid="AC60eff66308de9fd57e9aa831709166dc"
#account details
auth_token= "d7949e2dc9e684d0b6fa1efcdb79894a"

weather_params= {

    "lat": -0.949174,
    "lon": 21.971463,
    "appid": api_key,
    "exclude": "current,minute,daily"
    #coz we care about now hourly data and not past/future
}

response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
#if 200 dont come it will raise an exception
weather_data= response.json()
weather_slice=weather_data["hourly"][:12]

will_rain=False

for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True

if will_rain:
    #message sending format
    client = Client("AC60eff66308de9fd57e9aa831709166dc", "d7949e2dc9e684d0b6fa1efcdb79894a")
    message = client.messages.create(
        to="+919056253201", 
        from_="+19205261323",
        body="carry umbrella☔, it might rain today")
    print(message.status)



# from hourly(0) to 12 hours, going to find exact id at tat particular hour
# print(weather_data["hourly"][0]["weather"][0]["id"])

