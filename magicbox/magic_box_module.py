'''
Defines the requirements to be a magic_box module

Paul Lebel
2021
'''

from abc import ABC

# Methods
class MagicBoxModule(ABC):
    @abc.abstractmethod
    def __init__():
        pass

    @abc.abstractmethod
    def do_something(self, *args, **kwargs):
        pass

# Properties
