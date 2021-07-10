from Repository.groupIdRepo import groupIdRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection

class groupIdServices():
    __groupingIdRepo: groupIdRepo
    
    def __init__(self, groupIdTable: Table, context: Connection):
        self.__groupingIdRepo = groupIdRepo(groupIdTable, context=context)
   