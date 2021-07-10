from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection


class eventTriggerInputDeviceMappingRepo():
    __eventTriggerInputDeviceMappingTable: Table
    __context: Connection
    
    def __init__(self, EventTriggerInputDeviceMappingTable: Table, context: Connection):
        self.__eventTriggerInputDeviceMappingTable = EventTriggerInputDeviceMappingTable
        self.__context = context
    