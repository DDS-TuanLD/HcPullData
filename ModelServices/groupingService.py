from Repository.groupingRepo import groupingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection

class MetaGroupingServices(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaGroupingServices, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class groupingServices(metaclass=MetaGroupingServices):
    __groupingRepo: groupingRepo
    
    def __init__(self, groupingTable: Table, context: Connection):
        self.__groupingRepo = groupingRepo(groupingTable, context=context)
        
    def AddManyGroupingWithCustomData(self, l: list):
        self.__groupingRepo.InsertManyWithCustomData(l)