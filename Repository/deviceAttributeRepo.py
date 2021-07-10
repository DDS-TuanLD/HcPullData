from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class deviceAttributeRepo():
    __deviceAttributeTable: Table
    __context: Connection
    
    def __init__(self, DeviceAttributeTable: Table, context: Connection):
        self.__deviceAttributeTable = DeviceAttributeTable
        self.__context = context
    
    def FindWithCondition(self, condition: BinaryExpression):
        ins = self.__deviceAttributeTable.select().where(condition)
        rel = self.__context.execute(ins)
        return rel