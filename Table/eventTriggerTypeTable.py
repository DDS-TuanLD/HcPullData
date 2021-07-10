from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class eventTriggerTypeTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerTypeTable = Table('EventTriggerType', metadata,
                        Column('EventTriggerTypeId', Integer, primary_key=True, nullable=False),
                        Column('Code', String),
                        Column('Name', String),
                        ) 