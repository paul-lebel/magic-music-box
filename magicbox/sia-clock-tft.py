#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import time
import json
from sys import exit
import requests

from font_fredoka_one import FredokaOne
from PIL import Image, ImageDraw, ImageFont

import geocoder
import digitalio
import board

from adafruit_rgb_display.rgb import color565
from adafruit_rgb_display import st7789


# Get the current path
PATH = os.path.dirname(__file__)

# Details to customise the weather display
CITY = "Redwood City"
COUNTRYCODE = "US"
WARNING_TEMP = 30.0
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
BAUDRATE = 64000000  # The pi can be very fast!
FONT = ImageFont.truetype(FredokaOne, 22)


class Display(st7789.ST7789):
# Subclass to wrap buttons and backlight into same object

    def __init__(self):

        # Configuration for CS and DC pins for Raspberry Pi
        cs_pin = digitalio.DigitalInOut(board.CE0)
        dc_pin = digitalio.DigitalInOut(board.D25)
        reset_pin = None

        super().__init__(
        board.SPI(),
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
        width=240,
        height=240,
        x_offset=0,
        y_offset=80,
        )

        self.backlight = digitalio.DigitalInOut(board.D22)
        self.backlight.switch_to_output()
        self.backlight.value = True
        self.buttonA = digitalio.DigitalInOut(board.D23)
        self.buttonB = digitalio.DigitalInOut(board.D24)
        self.buttonA.switch_to_input()
        self.buttonB.switch_to_input()


# Convert a city name and country code to latitude and longitude
def get_coords(address):
    g = geocoder.arcgis(address)
    coords = g.latlng
    return coords


# Query OpenMeteo (https://open-meteo.com) to get current weather data
def get_weather(address):
    coords = get_coords(address)
    weather = {}
    res = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + str(coords[0]) + "&longitude=" + str(coords[1]) + "&current_weather=true")
    if res.status_code == 200:
        j = json.loads(res.text)
        current = j["current_weather"]
        weather["temperature"] = current["temperature"]
        weather["windspeed"] = current["windspeed"]
        weather["weathercode"] = current["weathercode"]
        return weather
    else:
        return weather

def C_to_F(temp_C):
    return -40 + (temp_C + 40)*1.8 

def kmh_to_mph(speed_kmh):
    return speed_kmh*1.6
    

def main():

    display = Display()

    # Dictionaries to store our icons and icon masks in
    icons = {}
    masks = {}

    # Get the weather data for the given location
    location_string = "{city}, {countrycode}".format(city=CITY, countrycode=COUNTRYCODE)
    weather = get_weather(location_string)

    # This maps the weather code from Open Meteo
    # to the appropriate weather icons
    # Weather codes from https://open-meteo.com/en/docs
    icon_map = {
        "snow": [71, 73, 75, 77, 85, 86],
        "rain": [51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82],
        "cloud": [1, 2, 3, 45, 48],
        "sun": [0],
        "storm": [95, 96, 99],
        "wind": []
    } 

    if weather:
        temperature = weather["temperature"]
        windspeed = weather["windspeed"]
        weathercode = weather["weathercode"]

        for icon in icon_map:
            if weathercode in icon_map[icon]:
                weather_icon = icon
                break
    else:
        print("Warning, no weather information found!")
        windspeed = 0.0
        temperature = 0.0
        weather_icon = None

    # Create a new canvas to draw on
    image = Image.new('RGB', (display.width, display.height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, display.width, display.height), outline=0, fill=(0, 0, 0))
    display.image(image)

    # Write text with weather values to the canvas
    datetime = time.strftime("%m/%d %I:%M %p")
    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    day = time.strftime("%A")

    if day in WEEKDAYS:
        # Night time is 7:30pm to 6:45am
        time_color = (255,255,255) if ( (hour > 6.75)  and ((hour + minute/60) < 19.5) ) else (255,0,0) 

    else:
        # Night time is 7:30pm to 7am
        time_color = (255,255,255) if ( (hour > 7)  and ((hour + minute/60) < 19.5) ) else (255,0,0) 

    draw.text((41, 12), datetime, time_color, font=FONT)
    draw.text((72, 34), "T", (255,255,255) , font=FONT)
    draw.text((92, 34), "{0:.1f}°F".format(C_to_F(temperature)), (255,255,255)  if temperature < WARNING_TEMP else (255,0,0) , font=FONT)

    draw.text((72, 58), "W", (255,255,255), font=FONT)
    draw.text((92, 58), "{}km/h".format(kmh_to_mph(windspeed)), (255,255,255) , font=FONT)

    display.image(image)

    # # Draw the current weather icon over the backdrop
    # if weather_icon is not None:
    #     img.paste(icons[weather_icon], (28, 36), masks[weather_icon])

    # else:
    #     draw.text((28, 36), "?", inky_display.RED, font=font)

  

if __name__ == "__main__":
    main()
