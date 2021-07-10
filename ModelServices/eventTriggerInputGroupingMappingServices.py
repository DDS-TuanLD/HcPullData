from Repository.eventTriggerInputGroupingMappingRepo import eventTriggerInputGroupingMappingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerInputGroupingMappingServices():
    __eventTriggerInputGroupingMappingRepo: eventTriggerInputGroupingMappingRepo
    
    def __init__(self, eventTriggerInputGroupingMappingTable: Table, context: Connection):
        self.__eventTriggerInputGroupingMappingRepo = eventTriggerInputGroupingMappingRepo(eventTriggerInputGroupingMappingTable, context=context)
        