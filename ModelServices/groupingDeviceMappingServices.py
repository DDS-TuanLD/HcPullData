from Repository.groupingDeviceMappingRepo import groupingDeviceMappingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class groupingDeviceMappingServices():
    __groupingDeviceMappingRepo: groupingDeviceMappingRepo
    
    def __init__(self, groupingDeviceMappingTable: Table, context: Connection):
        self.__groupingDeviceMappingRepo = groupingDeviceMappingRepo(groupingDeviceMappingTable, context=context)
        
    def AddManyDeviceWithCustomData(self, l: list):
        self.__groupingDeviceMappingRepo.InsertManyWithCustomData(l)