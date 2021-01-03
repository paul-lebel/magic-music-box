from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from inky import InkyPHAT


class MagicBoxScreen():
    def __init__(self):
        self._inky = InkyPHAT("black")
        self._font = ImageFont.truetype(FredokaOne, 22)

    def displayMessage(self, message: str="No Message")
        w, h = self._font.getsize(message)
        x = (self._inky.WIDTH / 2) - (w / 2)
        y = (self._inky.HEIGHT / 2) - (h / 2)
        img = Image.new("P", (self._inky.WIDTH, self._inky.HEIGHT))
        draw = ImageDraw.Draw(img)
        draw.text((x, y), message, self._inky.BLACK, font)
        self._inky.set_image(img)
        self._inky.show()