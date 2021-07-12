from Repository.eventTriggerInputDeviceMappingRepo import eventTriggerInputDeviceMappingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerInputDeviceMappingServices():
    __eventTriggerInputDeviceMappingRepo: eventTriggerInputDeviceMappingRepo
    
    def __init__(self, eventTriggerInputDeviceMappingTable: Table, context: Connection):
        self.__eventTriggerInputDeviceMappingRepo = eventTriggerInputDeviceMappingRepo(eventTriggerInputDeviceMappingTable, context=context)
        
    def AddManyEventTriggerInputDeviceMappingWithCustomData(self, l : list):
        self.__eventTriggerInputDeviceMappingRepo.InsertManyWithCustomData(l)