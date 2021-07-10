from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime, Time
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class eventTriggerOutputGroupingSetupValueTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerOutputGroupingSetupValueTable = Table('EventTriggerOutputGroupingSetupValue', metadata,
                        Column('EventTriggerId', Integer, primary_key=True, nullable=True),
                        Column('GroupingId', String, primary_key=True, nullable=True),
                        Column('GroupUnicastId', Integer),
                        Column('DeviceAttributeId', Integer, primary_key=True, nullable=True),
                        Column('DeviceAttributeValue', Integer),
                        Column('typerun', Integer,  primary_key=True, nullable=True),
                        Column('Time', Time),

                        ) 