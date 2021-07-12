from Repository.groupingRepo import groupingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class groupingServices():
    __groupingRepo: groupingRepo
    
    def __init__(self, groupingTable: Table, context: Connection):
        self.__groupingRepo = groupingRepo(groupingTable, context=context)
        
    def AddManyGroupingWithCustomData(self, l: list):
        self.__groupingRepo.InsertManyWithCustomData(l)
        
    def FindGroupWithCondition(self, condition: BinaryExpression):
        rel = self.__groupingRepo.FindWithCondition(condition)
        return rel