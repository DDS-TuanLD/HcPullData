from Repository.eventTriggerOutputSceneMappingRepo import eventTriggerOutputSceneMappingRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerOutputSceneMappingServices():
    __eventTriggerOutputSceneMappingRepo: eventTriggerOutputSceneMappingRepo
    
    def __init__(self, eventTriggerOutputSceneMappingTable: Table, context: Connection):
        self.__eventTriggerOutputSceneMappingRepo = eventTriggerOutputSceneMappingRepo(eventTriggerOutputSceneMappingTable, context=context)
        
    def AddManyEventTriggerOutputSceneMappingWithCustomDataType1(self, l: list):
        self.__eventTriggerOutputSceneMappingRepo.InsertManyWithCustomDataType1(l)
        
    def AddManyEventTriggerOutputSceneMappingWithCustomDataType2(self, l: list):
        self.__eventTriggerOutputSceneMappingRepo.InsertManyWithCustomDataType2(l)