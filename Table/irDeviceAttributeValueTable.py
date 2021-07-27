from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


class irDeviceAttributeValueTable:
    def __init__(self, metadata: MetaData):
        self.irDeviceAttributeValueTable = Table('IrDeviceAttributeValue', metadata,
                                                 Column('IrDeviceId', Integer, primary_key=True, nullable=False),
                                                 Column('IrDeviceUnicastId', Integer),
                                                 Column('StandardControlld', DateTime),
                                                 Column('StandardControlValue', DateTime),
                                                 Column('IrDeviceAttributeValue', String),
                                                 Column('DeviceAttributeId', Integer, primary_key=True, nullable=False),
                                                 Column('DeviceAttributeValueExtention', DateTime),
                                                 Column('DeviceId', Integer),
                                                 Column('DeviceUnicastId', Integer),
                                                 )
