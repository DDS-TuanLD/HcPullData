from Repository.deviceRepo import deviceRepo
from Model.device import device
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression
    
class deviceServices():
    __deviceRepo: deviceRepo
    
    def __init__(self, deviceTable: Table, context: Connection):
        self.__deviceRepo = deviceRepo(deviceTable, context=context)
        
    def AddManyDeviceWithCustomData(self, l: list):
        self.__deviceRepo.InsertManyWithCustomData(l=l)
        
    def FindDeviceWithCondition(self, condition: BinaryExpression):
        rel = self.__deviceRepo.FindWithCondition(condition)
        return rel