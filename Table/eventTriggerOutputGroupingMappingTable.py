from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class eventTriggerOutputGroupingMappingTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerOutputGroupingMappingTable = Table('EventTriggerOutputGroupingMapping', metadata,
                        Column('EventTriggerId', Integer, primary_key=True, nullable=True),
                        Column('GroupingId', String, primary_key=True, nullable=True),
                        Column('GroupUnicastId', Integer),
                        Column('typerun', Integer,  primary_key=True, nullable=True),
                        ) 