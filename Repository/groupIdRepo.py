from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class groupIdRepo():
    __groupIdTable: Table
    __context: Connection
    
    def __init__(self, groupIdTable: Table, context: Connection):
        self.__groupIdTable = groupIdTable
        self.__context = context