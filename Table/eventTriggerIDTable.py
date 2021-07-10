from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class eventTriggerIDTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerIDTable = Table('EventTriggerID', metadata,
                        Column('SceneUnicastID', Integer, primary_key=True, nullable=False),
                        Column('EventTriggerId', String),
                        Column('ValueCreate', Integer),
                        ) 