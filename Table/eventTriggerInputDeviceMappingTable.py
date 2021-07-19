from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


class eventTriggerInputDeviceMappingTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerInputDeviceMappingTable = Table('EventTriggerInputDeviceMapping', metadata,
                                                         Column('EventTriggerId', String, primary_key=True,
                                                                nullable=True),
                                                         Column('DeviceId', String, primary_key=True, nullable=True),
                                                         Column('DeviceUnicastId', Integer),
                                                         )
