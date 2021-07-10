from Repository.eventTriggerTypeRepo import eventTriggerTypeRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerTypeServices():
    __eventTriggerTypeRepo: eventTriggerTypeRepo
    
    def __init__(self, eventTriggerTypeTable: Table, context: Connection):
        self.__eventTriggerTypeRepo = eventTriggerTypeRepo(eventTriggerTypeTable, context=context)
        