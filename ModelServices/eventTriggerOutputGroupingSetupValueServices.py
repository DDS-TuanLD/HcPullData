from Repository.eventTriggerOutputGroupingSetupValueRepo import eventTriggerOutputGroupingSetupValueRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerOutputGroupingSetupValueServices():
    __eventTriggerOutputGroupingSetupValueRepo: eventTriggerOutputGroupingSetupValueRepo
    
    def __init__(self, eventTriggerOutputGroupingSetupValueTable: Table, context: Connection):
        self.__eventTriggerOutputGroupingSetupValueRepo = eventTriggerOutputGroupingSetupValueRepo(eventTriggerOutputGroupingSetupValueTable, context=context)
        
    def AddManyEventTriggerOutputGroupSetupValueWithCustomData(self, l:list):
        self.__eventTriggerOutputGroupingSetupValueRepo.InsertManyWithCustomData(l)