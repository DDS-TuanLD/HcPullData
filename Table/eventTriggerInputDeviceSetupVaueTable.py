from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


class eventTriggerInputDeviceSetupValueTable():
    def __init__(self, metadata: MetaData):
        self.eventTriggerInputDeviceSetupValueTable = Table('EventTriggerInputDeviceSetupValue', metadata,
                                                            Column('EventTriggerId', String, primary_key=True,
                                                                   nullable=True),
                                                            Column('DeviceId', String, primary_key=True, nullable=True),
                                                            Column('DeviceUnicastId', Integer),
                                                            Column('DeviceAttributeId', Integer, primary_key=True,
                                                                   nullable=True),
                                                            Column('ComparisonOperatorId', Integer),
                                                            Column('DeviceAttributeValue', Integer),
                                                            Column('DeviceAttributeValueMAX', Integer),
                                                            )
