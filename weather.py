import sys
import os
import requests
from win10toast import ToastNotifier
from datetime import datetime
from enum import Enum


WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
CITY = "Antalya"

class TimeSlot(Enum):
    MORNING = 1
    EVENING = 2

class Weather(Enum):
    SUNNY = "\U0001F31E"
    CLOUD = "\U00002601"
    HEAVY_RAINY = "\U000026C8"
    CLOUD_RAINY = "\U0001F327"
    CLOUD_SNOW = "\U0001F328"
    LIGHTHING = "\U0001F329"
    FOGGY = "\U0001F32B"
    SNOW = "\U00002744"
    MOON = "\U0001F319"
    MOON_FACE = "\U0001F31B"
    THERMOMETER = "\U0001F321"

def get_current_time_slot(sunrise, sunset, timezone):
    now = datetime.now().strftime("%H:%M")
    sunrise = datetime.fromtimestamp(sunrise).strftime("%A, %B %d, %Y %H:%M:%S")
    sunset = datetime.fromtimestamp(sunset).strftime("%A, %B %d, %Y %H:%M:%S")

    """sunrise_utc = (":".join(sunrise.split(" ")[-1].split(":")[:2]))
    sunset_utc = (":".join(sunset.split(" ")[-1].split(":")[:2]))"""

    sunrise_utc = sunrise.split(" ")[-1].split(":")[:2]
    sunset_utc = sunset.split(" ")[-1].split(":")[:2]

    if int(now.split(":")[0]) >= int(sunrise_utc[0]) and int(now.split(":")[0]) < int(sunset_utc[0]):
        return TimeSlot.MORNING
    elif int(now.split(":")[0]) < int(sunrise_utc[0]) and int(now.split(":")[0]) >= int(sunset_utc[0]):
        return TimeSlot.EVENING
    else:
        return TimeSlot.MORNING
    
def get_weather_emoji(time_slot, weather_id):
    emoji = ""
    if weather_id < 300:
        emoji = Weather.LIGHTHING.value
    elif weather_id < 400:
        emoji = Weather.CLOUD_RAINY.value
    elif weather_id < 600:
        emoji = Weather.HEAVY_RAINY.value
    elif weather_id < 700:
        emoji = Weather.SNOW.value
    elif weather_id < 800:
        emoji = Weather.FOGGY.value
    elif weather_id == 800:
        emoji = Weather.SUNNY.value
    elif weather_id < 900:
        emoji = Weather.CLOUD.value
    
    if time_slot.EVENING == TimeSlot.EVENING:
        emoji += Weather.MOON.value
    else:
        emoji += Weather.SUNNY.value
    return emoji

def send_notification(weather_emoji, weather_description, tempature):
    now = datetime.now().strftime("%H:%M")
    toaster = ToastNotifier()
    message = "City: " + CITY + "\nTime: " + now + "\nDescription: " + weather_description + "\nTempature: " + tempature + Weather.THERMOMETER.value + "  " + weather_emoji
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
    emoji = get_weather_emoji(time_slot, weather_id)
    send_notification(emoji, weather, tempature)


def get_weather_information():
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "&APPID=" + WEATHER_API_KEY + "&units=metric"
    res = requests.get(url)
    data = res.json()
    parse_json(data)


get_weather_information()