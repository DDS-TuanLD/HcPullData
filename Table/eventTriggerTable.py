from sqlalchemy import Column, Integer, String, BigInteger, Time
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class eventTriggerTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerTable = Table('EventTrigger', metadata,
                        Column('EventTriggerId', String, primary_key=True, nullable=False),
                        Column('GroupId', Integer),
                        Column('EventTriggerTypeId', BigInteger),
                        Column('SceneUnicastID', Integer),
                        Column('Priority', BigInteger),
                        Column('Name', String),
                        Column('LogicalOperatorID', Integer),
                        Column('HasTimer', Integer),
                        Column('StartAt', Time),
                        Column('EndAt', Time),
                        Column('ValueCreate', Integer),
                        Column('StatusID', Integer),
                        Column('HasRepeater', Integer),
                        Column('EachMonday', Integer),
                        Column('EachTuesday', Integer),
                        Column('EachWednesday', Integer),
                        Column('EachThursday', Integer),
                        Column('EachFriday', Integer),
                        Column('EachSaturday', Integer),
                        Column('EachSunday', Integer),
                        Column('NotificationUser', Integer),
                        Column('FADE_IN', Integer),

                        ) 