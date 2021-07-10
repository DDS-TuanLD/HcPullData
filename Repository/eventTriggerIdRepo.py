from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerIdRepo():
    __eventTriggerIdTable: Table
    __context: Connection
    
    def __init__(self, EventTriggerIdTable: Table, context: Connection):
        self.__eventTriggerIdTable = EventTriggerIdTable
        self.__context = context
    