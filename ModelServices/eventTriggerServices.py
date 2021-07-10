from Repository.eventTriggerRepo import eventTriggerRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerServices():
    __eventTriggerRepo: eventTriggerRepo
    
    def __init__(self, eventTriggerTable: Table, context: Connection):
        self.__eventTriggerRepo = eventTriggerRepo(eventTriggerTable, context=context)
    
    def AddManyDeviceWithCustomData(self, l: list):
        self.__eventTriggerRepo.InsertManyWithCustomData(l)