from Repository.eventTriggerInputDeviceSetupValueRepo import eventTriggerInputDeviceSetupValueRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class eventTriggerInputDeviceSetupValueServices():
    __eventTriggerInputDeviceSetupValueRepo: eventTriggerInputDeviceSetupValueRepo
    
    def __init__(self, eventTriggerInputDeviceSetupValueTable: Table, context: Connection):
        self.__eventTriggerInputDeviceSetupValueRepo = eventTriggerInputDeviceSetupValueRepo(eventTriggerInputDeviceSetupValueTable, context=context)
        
    def AddManyEventTriggerInputDeviceSetupValueWithCustomData(self, l: list):
        self.__eventTriggerInputDeviceSetupValueRepo.InsertManyWithCustomData(l)