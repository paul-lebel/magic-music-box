import abc


class MagicBoxModule(abc.ABC):
    @abc.abstractmethod
    def __init__():
        pass

    @abc.abstractmethod
    def do_something(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def do_something_else(self):
        pass
