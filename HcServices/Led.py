from Helper.Terminal import Terminal
from Constract.Iled import Iled
import time
import Constant.Constant as const
from Led.ServiceLedControl import serviceLedControl

class Led():
    __serviceLedControl: serviceLedControl
    
    def __init__(self):
       self.__serviceLedControl = serviceLedControl()
       
    @property
    def ServiceLedControl(self):
        return self.__serviceLedControl