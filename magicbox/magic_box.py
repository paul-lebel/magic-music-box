#! /usr/bin/env python3
""" MagicBox class definition

-- Important Links --

Inky phat
    

-- Application Notes --


"""

import RPi.GPIO as GPIO
from typing import List
from consts import *


# Set gpio pin numbering to the gpio pin numbers on the raspberry pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class MagicBox():
    def __init__(self):
        # BCM GPIO
        self._buttonA = 0
        self._buttonB = 5
        self._buttonC = 6
        self._buttonD = 23
        self._buttonE = 24

        # Raspberry Pi GPIO inputs are all either pull-up or pull-down. 
        GPIO.setup(self._buttonA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._buttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._buttonC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._buttonD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._buttonE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self._screen = MagicBoxScreen()
        self._screen.displayMessage("Welcome to magic box!")

    def importModules(self):
        pass



if __name__ == "__main__":
   
    mb = MagicBox()

    try:
        while True:
            
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

