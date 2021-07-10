from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class deviceAttributeTable():
    def __init__(self, metadata: MetaData):
        self.deviceAttributeTable = Table('DeviceAttribute', metadata,
                        Column('DeviceAttributeId', Integer, primary_key=True, nullable=False),
                        Column('Code', String),
                        Column('Name', String),
                        ) 