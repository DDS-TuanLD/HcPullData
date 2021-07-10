from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class eventTriggerInputGroupingMappingTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerInputGroupingMappingTable = Table('EventTriggerInputGroupingMapping', metadata,
                        Column('EventTriggerId', Integer, primary_key=True, nullable=True),
                        Column('GroupingId', String,  primary_key=True, nullable=True),
                        Column('GroupingUnicastId', Integer),
                        ) 