from Repository.groupingDeviceMappingRepo import groupingDeviceMappingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class MetaGroupingDeviceMappingServices(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaGroupingDeviceMappingServices, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class groupingDeviceMappingServices(metaclass=MetaGroupingDeviceMappingServices):
    __groupingDeviceMappingRepo: groupingDeviceMappingRepo
    
    def __init__(self, groupingDeviceMappingTable: Table, context: Connection):
        self.__groupingDeviceMappingRepo = groupingDeviceMappingRepo(groupingDeviceMappingTable, context=context)
        
    def AddManyDeviceWithCustomData(self, l: list):
        self.__groupingDeviceMappingRepo.InsertManyWithCustomData(l)