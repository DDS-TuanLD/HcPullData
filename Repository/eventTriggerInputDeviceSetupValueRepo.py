from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerInputDeviceSetupValueRepo():
    __eventTriggerInputDeviceSetupValueTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerInputDeviceSetupValueTable: Table, context: Connection):
        self.__eventTriggerInputDeviceSetupValueTable = eventTriggerInputDeviceSetupValueTable
        self.__context = context
    