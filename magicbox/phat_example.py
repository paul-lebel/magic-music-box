#! /usr/bin/env python3

from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from inky import InkyPHAT
from time import sleep

if __name__ == "__main__":

    inkyphat = InkyPHAT("black")
    font = ImageFont.truetype(FredokaOne, 22)
    count = 0
    try:
        while True:
            count += 1
            message = f"Hi! Count = {count}"
            print(message)
            w, h = font.getsize(message)
            x = (inkyphat.WIDTH / 2) - (w / 2)
            y = (inkyphat.HEIGHT / 2) - (h / 2)
            img = Image.new("P", (inkyphat.WIDTH, inkyphat.HEIGHT))
            draw = ImageDraw.Draw(img)
            draw.text((x, y), message, inkyphat.BLACK, font)
            inkyphat.set_image(img)
            inkyphat.show()
            sleep(1)

    except KeyboardInterrupt:
        pass
