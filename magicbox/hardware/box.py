# Encapsulation of all hardware control

from magicbox.hardware.pico import Pico

class Box():
    def __init__(self):

    	self.pico = Pico()
    	self._btnA = BTN_A
    	self._btnB = BTN_B
    	self._btnC = BTN_C
    	self._btnD = BTN_D
    	self._btnE = BTN_E
