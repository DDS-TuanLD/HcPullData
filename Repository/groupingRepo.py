from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class groupingRepo():
    __groupingTable: Table
    __context: Connection
    
    def __init__(self, GroupingTable: Table, context: Connection):
        self.__groupingTable = GroupingTable
        self.__context = context
    
    def InsertManyWithCustomData(self, l: list):
        ins = self.__groupingTable.insert()
        values = []
        for i in range(len(l)):
            createdAt = l[i].get('createdAt')
            if createdAt != None:
                createdAt = datetime.datetime.strptime(createdAt, '%Y-%m-%dT%H:%M:%S.%fZ')
                
            updatedAt = l[i].get('updatedAt')
            if updatedAt != None:
                updatedAt = datetime.datetime.strptime(updatedAt, '%Y-%m-%dT%H:%M:%S.%fZ')
                
            deletedAt = l[i].get('deletedAt')
            if deletedAt != None:
                deletedAt = datetime.datetime.strptime(deletedAt, '%Y-%m-%dT%H:%M:%S.%fZ')
            
            groupingId = l[i].get('id', None)
            if groupingId == None:
                continue
            
            d = {
                'GroupingId': groupingId,
                'GroupUnicastId': l[i].get('unicastId', None),
                'Name': l[i].get('name', None),
                'CategoryId': l[i].get('categoryId', None),
                'CreatedAt': createdAt,
                'UpdatedAt': updatedAt,
                'DeletedAt': deletedAt
            }
            values.append(d)
        if values == []:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)
            
    def FindWithCondition(self, condition: BinaryExpression):
        ins = self.__groupingTable.select().where(condition)
        rel = self.__context.execute(ins)
        return rel   
    