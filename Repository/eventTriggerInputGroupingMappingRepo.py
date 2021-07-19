from sqlalchemy import Table
from sqlalchemy.engine.base import Connection


class eventTriggerInputGroupingMappingRepo:
    __eventTriggerInputGroupingMappingTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerInputGroupingMappingTable: Table, context: Connection):
        self.__eventTriggerInputGroupingMappingTable = eventTriggerInputGroupingMappingTable
        self.__context = context
