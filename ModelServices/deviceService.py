from Repository.deviceRepo import deviceRepo
from Model.device import device
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class MetaDeviceServices(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaDeviceServices, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class deviceServices(metaclass=MetaDeviceServices):
    __deviceRepo: deviceRepo
    
    def __init__(self, deviceTable: Table, context: Connection):
        self.__deviceRepo = deviceRepo(deviceTable, context=context)
        
    def AddManyDeviceWithCustomData(self, l: list):
        self.__deviceRepo.InsertManyWithCustomData(l=l)
        
    def FindDeviceWithCondition(self, condition: BinaryExpression):
        rel = self.__deviceRepo.FindWithCondition(condition)
        return rel