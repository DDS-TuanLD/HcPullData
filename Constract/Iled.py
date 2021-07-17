from abc import ABCMeta, abstractmethod


class Iled(metaclass=ABCMeta):
    @abstractmethod
    def On(self):
        pass
    
    @abstractmethod
    def Off(self):
        pass
    
    @abstractmethod
    def Delay(self, delay: int):
        pass
    
    @abstractmethod
    def Toggle(self, delay: int):
        pass