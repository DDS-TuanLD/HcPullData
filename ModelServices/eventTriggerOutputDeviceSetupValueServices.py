from Repository.eventTriggerOutputDeviceSetupValueRepo import eventTriggerOutputDeviceSetupValueRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerOutputDeviceSetupValueServices():
    __eventTriggerOutputDeviceSetupValueRepo: eventTriggerOutputDeviceSetupValueRepo
    
    def __init__(self, eventTriggerOutputDeviceSetupValueTable: Table, context: Connection):
        self.__eventTriggerOutputDeviceSetupValueRepo = eventTriggerOutputDeviceSetupValueRepo(eventTriggerOutputDeviceSetupValueTable, context=context)
        
    def AddManyDeviceWithCustomData(self, l: list):
        self.__eventTriggerOutputDeviceSetupValueRepo.InsertManyWithCustomData(l)