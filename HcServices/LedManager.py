from Helper.Terminal import Terminal
from Constract.Iled import Iled
import time
import Constant.Constant as const
from Led.ServiceLed import ServiceLed

class LedManager():
    
    __serviceLed: ServiceLed
    
    def __init__(self):
       self.__serviceLed = ServiceLed()
       
    @property
    def ServiceLedControl(self):
        return self.__serviceLed