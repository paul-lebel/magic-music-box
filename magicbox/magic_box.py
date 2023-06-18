#! /usr/bin/env python3
""" MagicBox class definition

-- Important Links --


-- Application Notes --


"""

import RPi.GPIO as GPIO
from magicbox.box_constants import * 
from transitions.instrument import ThreadedInstrument
from transitions.decorators import lock_no_block
from box_sm import *

import threading, queue
import time
import enum
import sys



class MagicBox():
    def __init__(self):

        super().__init__(self, \
            states = States, \
            transitions=SM_TRANSITIONS, \
            initial=States.MAIN_MENU, \
            ignore_invalid_triggers = True, \
            after_state_change = self.print_state, \
            auto_transitions = False, \
            name='Magic Music Box')
        
        # Create threaded queues for operations that block execution
        self._queues = {'keyInput': {'q': queue.Queue(maxsize=3), 'func': self._parse_key_input}}
        
        self.get_graph().draw('magic_box_diagram.png', prog='dot')

        # Set gpio pin numbering to the gpio pin numbers on the raspberry pi
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self._buttonA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._buttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._buttonC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._buttonD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._buttonE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self._screen = MagicBoxScreen()
        self._screen.displayMessage("Welcome!")


    def start_key_input(self):
        self._queues['keyInput']['q'].put_nowait({'prompt': 'Enter an input:'})
        return


if __name__ == "__main__":
    mb = MagicBox()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

