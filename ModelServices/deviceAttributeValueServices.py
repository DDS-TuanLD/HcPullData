from Repository.deviceAttributeValueRepo import deviceAttributeValueRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression
    
class deviceAttributeValueServices():
    __deviceAttributeValueRepo: deviceAttributeValueRepo
    
    def __init__(self, deviceAttributeValueTable: Table, context: Connection):
        self.__deviceAttributeValueRepo = deviceAttributeValueRepo(DeviceAttributeValueTable=deviceAttributeValueTable, context=context)
        
    def FindDeviceAttributeValueWithCondition(self, condition: BinaryExpression):
        rel = self.__deviceAttributeValueRepo.FindWithCondition(condition)
        return rel