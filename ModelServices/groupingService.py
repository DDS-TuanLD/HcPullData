from Repository.groupingRepo import groupingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection

class groupingServices():
    __groupingRepo: groupingRepo
    
    def __init__(self, groupingTable: Table, context: Connection):
        self.__groupingRepo = groupingRepo(groupingTable, context=context)
        
    def AddManyGroupingWithCustomData(self, l: list):
        self.__groupingRepo.InsertManyWithCustomData(l)