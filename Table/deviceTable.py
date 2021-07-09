from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class deviceTable():
    def __init__(self, metadata: MetaData):
        self.deviceTable = Table('Device', metadata,
                        Column('DeviceId', Integer, primary_key=True, nullable=False),
                        Column('DeviceUnicastId', Integer),
                        Column('AppKey', String),
                        Column('NetKey', String),
                        Column('DeviceKey', String),
                        Column('DeviceTypeId', Integer),
                        Column('UpdateDay', Integer),
                        Column('UpdateTime', Integer),
                        Column('StatusId', Integer),
                        Column('Owner', Integer),
                        ) 