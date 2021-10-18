from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from inky import InkyPHAT
from typing import List
from consts import *


class MagicBoxScreen():
    def __init__(self):
        self._inky = InkyPHAT("black")
        self._font = ImageFont.truetype(FredokaOne, 16)

    def displayMessage(self, message: str="No Message"):
        w, h = self._font.getsize(message)
        x = (self._inky.WIDTH / 2) - (w / 2)
        y = (self._inky.HEIGHT / 2) - (h / 2)
        img = Image.new("P", (self._inky.WIDTH, self._inky.HEIGHT))
        draw = ImageDraw.Draw(img)
        draw.text((x, y), message, self._inky.BLACK, self._font)
        self._inky.set_image(img)
        self._inky.show()

    def displayQuestion(self, \
        questionText: str="What is the speed of light?", \
        answerText: List[str] = \
        ['0 m/s', '100 m/s', '1 km/s', '3,000 km/s', '300,000 km/s']):


