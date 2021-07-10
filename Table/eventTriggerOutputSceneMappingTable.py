from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime, Time
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class eventTriggerOutputSceneMappingTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerOutputSceneMappingTable = Table('EventTriggerOutputSceneMapping', metadata,
                        Column('EventTriggerId', String, primary_key=True, nullable=True),
                        Column('SceneId', String, primary_key=True, nullable=True),
                        Column('SceneUnicastId', Integer),
                        Column('typerun', Integer,  primary_key=True, nullable=True),
                        Column('Time', Time),
                        ) 