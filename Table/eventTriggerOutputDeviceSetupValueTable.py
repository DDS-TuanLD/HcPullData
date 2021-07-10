from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime, Time
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class eventTriggerOutputDeviceSetupValueTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerOutputDeviceSetupValueTable = Table('EventTriggerOutputDeviceSetupValue', metadata,
                        Column('EventTriggerId', Integer, primary_key=True, nullable=True),
                        Column('DeviceId', String, primary_key=True, nullable=True),
                        Column('DeviceUnicastId', Integer),
                        Column('DeviceAttributeId', Integer, primary_key=True, nullable=True),
                        Column('DeviceAttributeValue', Integer),
                        Column('typerun', Integer,  primary_key=True, nullable=True),
                        Column('Time', Time),

                        ) 