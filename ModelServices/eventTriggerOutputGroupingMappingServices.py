from Repository.eventTriggerOutputGroupingMappingRepo import eventTriggerOutputGroupingMappingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerOutputGroupingMappingServices():
    __eventTriggerOutputGroupingMappingRepo: eventTriggerOutputGroupingMappingRepo
    
    def __init__(self, eventTriggerOutputGroupingMappingTable: Table, context: Connection):
        self.__eventTriggerOutputGroupingMappingRepo = eventTriggerOutputGroupingMappingRepo(eventTriggerOutputGroupingMappingTable, context=context)
        
    def AddManyEventTriggerOutputGroupMappingWithCustomData(self, l: list):
        self.__eventTriggerOutputGroupingMappingRepo.InsertManyWithCustomData(l)