from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputDeviceSetupValueRepo():
    __eventTriggerOutputDeviceSetupValueTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputDeviceSetupValueTable: Table, context: Connection):
        self.__eventTriggerOutputDeviceSetupValueTable = eventTriggerOutputDeviceSetupValueTable
        self.__context = context
    