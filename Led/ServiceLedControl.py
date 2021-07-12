from Helper.Terminal import Terminal
from Constract.Iled import Iled
import time
import Constant.Constant as const

class serviceLedControl():
    __terminal: Terminal
    
    def __init__(self):
        self.__terminal = Terminal()
    
    def On(self):
        self.__terminal.Execute(const.LED_SERVICE_PIN_ON)
    
    def Off(self):
        self.__terminal.Execute(const.LED_SERVICE_PIN_OFF)
    
    def Delay(self, delay_s: int):
        time.sleep(delay_s)
    
    def Toggle(self, delay_s: int):
        self.On()
        self.Delay(delay_s)
        self.Off()