from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputSceneMappingRepo():
    __eventTriggerOutputSceneMappingRepoTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputSceneMappingRepoTable: Table, context: Connection):
        self.__eventTriggerOutputSceneMappingRepoTable = eventTriggerOutputSceneMappingRepoTable
        self.__context = context
    