from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class groupIDTable():
    def __init__(self, metadata: MetaData):
        self.groupIDTable = Table('GROUPID', metadata,
                        Column('GroupUnicastId', Integer, primary_key=True, nullable=False),
                        Column('GroupingId', String),
                        Column('ValueCreate', Integer),
                        ) 