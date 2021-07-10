from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputGroupingMappingRepo():
    __eventTriggerOutputGroupingMappingTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputGroupingMappingTable: Table, context: Connection):
        self.__eventTriggerOutputGroupingMappingTable = eventTriggerOutputGroupingMappingTable
        self.__context = context
    