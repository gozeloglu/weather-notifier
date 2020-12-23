import sys
import os
import requests
from win10toast import ToastNotifier
from datetime import datetime
from enum import Enum


WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
CITY = "Antalya"

class TimeSlot(Enum):
    MORNING = "\U0001F305"
    EVENING = "\U0001F319"

class Weather(Enum):
    SUNNY = "\U0001F31E"
    CLOUD = "\U00002601"
    HEAVY_RAINY = "\U000026C8"
    CLOUD_RAINY = "\U0001F327"
    CLOUD_SNOW = "\U0001F328"
    LIGHTHING = "\U0001F329"
    FOGGY = "\U0001F32B"
    SNOW = "\U00002744"
    MOON_FACE = "\U0001F31B"
    THERMOMETER = "\U0001F321"
    

def get_current_time_slot(sunrise, sunset, timezone):
    now = datetime.now().strftime("%H:%M")
    sunrise = datetime.fromtimestamp(sunrise).strftime("%A, %B %d, %Y %H:%M:%S")
    sunset = datetime.fromtimestamp(sunset).strftime("%A, %B %d, %Y %H:%M:%S")

    sunrise_utc = sunrise.split(" ")[-1].split(":")[:2]
    sunset_utc = sunset.split(" ")[-1].split(":")[:2]

    # Morning 
    if int(now.split(":")[0]) >= int(sunrise_utc[0]) and int(now.split(":")[0]) < int(sunset_utc[0]):
        return TimeSlot.MORNING.value
    # Evening
    elif int(now.split(":")[0]) < int(sunrise_utc[0]) or int(now.split(":")[0]) >= int(sunset_utc[0]):
        return TimeSlot.EVENING.value
    else:
        return TimeSlot.EVENING.value
    
def get_weather_emoji(weather_id):
    
    if weather_id < 300:
        return Weather.LIGHTHING.value
    elif weather_id < 400:
        return Weather.CLOUD_RAINY.value
    elif weather_id < 600:
        return Weather.HEAVY_RAINY.value
    elif weather_id < 700:
        return Weather.SNOW.value
    elif weather_id < 800:
        return Weather.FOGGY.value
    elif weather_id == 800:
        return Weather.SUNNY.value
    elif weather_id < 900:
        return Weather.CLOUD.value
    return Weather.SUNNY.value

def send_notification(weather_emoji, time_slot_emoji, weather_description, tempature):
    now = datetime.now().strftime("%H:%M")
    toaster = ToastNotifier()
    city = "City: " + CITY + "\n"
    time = "Time: " + now + time_slot_emoji + "\n"
    description = "Description: " + weather_description + "  " + weather_emoji + "\n"
    temp = "Tempature: " + tempature + "°C " + Weather.THERMOMETER.value
    message = city + time + description + temp 
    toaster.show_toast("Weather Forecast", message,
                   icon_path=None,
                   duration=10,
                   threaded=True)

def parse_json(data):
    
    weather = data["weather"][0]["description"]
    weather_id = int(data["weather"][0]["id"])
    tempature = str(data["main"]["temp"])
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]
    timezone = data["timezone"]

    time_slot = get_current_time_slot(sunrise, sunset, timezone)
    emoji = get_weather_emoji(weather_id)
    send_notification(emoji, time_slot, weather, tempature)


def get_weather_information():
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "&APPID=" + WEATHER_API_KEY + "&units=metric"
    res = requests.get(url)
    data = res.json()
    parse_json(data)


get_weather_information()