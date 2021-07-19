from abc import ABCMeta, abstractmethod


class IController(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass
