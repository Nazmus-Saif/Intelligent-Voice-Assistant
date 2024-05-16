import requests
from speak import say
import main

city = "dhaka"

api_key = '30d4741c779ba94c470ca1f63045390a'  # taken from internet
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    say("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']  # weather condition is sunny, rainy, cloudy, hazy etc.
    temp = round(weather_data.json()['main']['temp'])  # weather condition in degree celsius
    # print(f"The weather in {city} is: {weather}")
    # print(f"The temperature in {city} is: {temp}ºC")
