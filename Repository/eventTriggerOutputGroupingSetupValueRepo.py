from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputGroupingSetupValueRepo():
    __eventTriggerOutputGroupingSetupValueTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputGroupingSetupValueTable: Table, context: Connection):
        self.__eventTriggerOutputGroupingSetupValueTable = eventTriggerOutputGroupingSetupValueTable
        self.__context = context
    