from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import datetime

class groupingTable():
    def __init__(self, metadata: MetaData):
        self.groupingTable = Table('GROUPING', metadata,
                        Column('GroupingId', String, primary_key=True, nullable=False),
                        Column('GroupingUnicastId', Integer),
                        Column('Name', String),
                        Column('CategoryId', Integer),
                        Column('CreatedAt', DateTime),
                        Column('UpdatedAt', DateTime),
                        Column('DeleteAt', DateTime),
                        ) 
        
  