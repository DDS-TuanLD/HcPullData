from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection


class irDeviceAttributeValueRepo:
    __irDeviceAttributeValueTable: Table
    __context: Connection

    def __init__(self, irDeviceAttributeValueTable: Table, context: Connection):
        self.__irDeviceAttributeValueTable = irDeviceAttributeValueTable
        self.__context = context
