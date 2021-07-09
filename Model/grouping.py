import asyncio
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import datetime
import time

class grouping():
    __groupingId: str
    __groupUnicastId: int
    __name: str
    __cagetoryId: int
    __createdAt: datetime
    __updatedAt: datetime
    __deletedAt: datetime
    
       