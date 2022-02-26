import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint= "http://api.openweathermap.org/data/2.5/onecall"
api_key=os.environ.get("API_KEY")

account_sid=os.environ.get("ACCOUNT_SID")
#account details
auth_token= os.environ.get("AUTH_TOKEN")

weather_params= {

    "lat": 30.884729,
    "lon": 76.684692,
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
    proxy_client=TwilioHttpClient()
    proxy_client.session.proxies={'https': os.environ['https_proxy']}
    #message sending format
    client = Client(account_sid,auth_token,http_client=proxy_client)
    message = client.messages.create(
        to=os.environ.get("MY_NO"),
        from_="+19205261323",
        body="carry umbrella☔, it might rain today")
    print(message.status)



# from hourly(0) to 12 hours, going to find exact id at tat particular hour
# print(weather_data["hourly"][0]["weather"][0]["id"])

