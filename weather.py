import sys
import os
import requests
from win10toast import ToastNotifier

emojis = {
    "sunny": "\U0001F31E",
    "cloud": "\U00002601",
    "heavy_rainy": "\U000026C8",
    "cloud_rainy": "\U0001F327",
    "cloud_snow": "\U0001F328",
    "lighthing": "\U0001F329",
    "foggy": "\U0001F32B",
    "snow": "\U00002744",
    "moon": "\U0001F319",
    "moon_face": "\U0001F31B",
    "thermometer": "\U0001F321",
}
toaster = ToastNotifier()
toaster.show_toast("Weather Status",
                   "This notification is in it's own thread!" + emojis["thermometer"],
                   icon_path=None,
                   duration=5,
                   threaded=True)
