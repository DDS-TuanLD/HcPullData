from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection


class eventTriggerTypeRepo():
    __eventTriggerTypeTable: Table
    __context: Connection

    def __init__(self, eventTriggerTypeTable: Table, context: Connection):
        self.__eventTriggerTypeTable = eventTriggerTypeTable
        self.__context = context
