from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class groupingDeviceMappingTable():
    def __init__(self, metadata: MetaData):
        self.groupingDeviceMappingTable = Table('GroupingDeviceMapping', metadata,
                        Column('GroupingId', String, primary_key=True, nullable=False),
                        Column('GroupUnicastId', Integer, nullable=False),
                        Column('DeviceId', String, primary_key=True, nullable=False),
                        Column('DeviceUnicastId', Integer, nullable=False),
                        ) 