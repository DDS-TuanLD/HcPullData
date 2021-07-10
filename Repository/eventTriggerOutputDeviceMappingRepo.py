from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputDeviceMappingRepo():
    __eventTriggerOutputDeviceMappingTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputDeviceMappingTable: Table, context: Connection):
        self.__eventTriggerOutputDeviceMappingTable = eventTriggerOutputDeviceMappingTable
        self.__context = context
    