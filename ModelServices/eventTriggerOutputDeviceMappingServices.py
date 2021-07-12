from Repository.eventTriggerOutputDeviceMappingRepo import eventTriggerOutputDeviceMappingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerOutputDeviceMappingServices():
    __eventTriggerOutputDeviceMappingRepo: eventTriggerOutputDeviceMappingRepo
    
    def __init__(self, eventTriggerOutputDeviceMappingTable: Table, context: Connection):
        self.__eventTriggerOutputDeviceMappingRepo = eventTriggerOutputDeviceMappingRepo(eventTriggerOutputDeviceMappingTable, context=context)
     
    def AddManyEventTriggerOutputDeviceMappingWithCustomData(self, l: list):
        self.__eventTriggerOutputDeviceMappingRepo.InsertManyWithCustomData(l)   