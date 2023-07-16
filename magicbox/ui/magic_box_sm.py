import enum
from transitions.extensions.nesting import NestedState
import threading

NestedState.separator = '=>'

LOCK = dict()
LOCK["SCREEN_LOCK"] = threading.Lock()

class States(enum.Enum):
    MAIN_MENU = enum.auto()
    

# For readability, organize state transitions by the source state
leaving = dict()
leaving["MAIN_MENU"] = [
    { 'trigger': 'encoder_up', 'source': States.MAIN_MENU, 'dest': States.CALENDAR}
    ]


leaving["CALENDAR"] = [
    { 'trigger': 'encoder_down', 'source': States.CALENDAR, 'dest': States.MAIN_MENU}
    ]


# Construct one single list of transitions that defines them
SM_TRANSITIONS = []

for val in leaving.values():
    SM_TRANSITIONS += val

del leaving

