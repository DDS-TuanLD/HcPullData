from Repository.eventTriggerRepo import eventTriggerRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerServices():
    __eventTriggerRepo: eventTriggerRepo
    
    def __init__(self, eventTriggerTable: Table, context: Connection):
        self.__eventTriggerRepo = eventTriggerRepo(eventTriggerTable, context=context)
    
    def AddManyEventTriggerWithCustomData(self, l: list, type: int):
        self.__eventTriggerRepo.InsertManyWithCustomData(l, type)
        
    def FindEventTriggerWithCondition(self, condition: BinaryExpression):
       rel = self.__eventTriggerRepo.FindWithCondition(condition)
       return rel

    def FindAllEventTrigger(self):
        rel = self.__eventTriggerRepo.FindAll()
        return rel