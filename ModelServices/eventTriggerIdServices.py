from Repository.eventTriggerIdRepo import eventTriggerIdRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerIdServices():
    __eventTriggerIdRepo: eventTriggerIdRepo
    
    def __init__(self, eventTriggerIdTable: Table, context: Connection):
        self.__eventTriggerIdRepo = eventTriggerIdRepo(eventTriggerIdTable, context=context)
        