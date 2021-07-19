from Led.ServiceLedControl import serviceLedControl


class Led:
    __serviceLedControl: serviceLedControl
    
    def __init__(self):
       self.__serviceLedControl = serviceLedControl()
       
    @property
    def ServiceLedControl(self):
        return self.__serviceLedControl
