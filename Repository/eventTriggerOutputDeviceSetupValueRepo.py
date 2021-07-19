from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputDeviceSetupValueRepo():
    __eventTriggerOutputDeviceSetupValueTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputDeviceSetupValueTable: Table, context: Connection):
        self.__eventTriggerOutputDeviceSetupValueTable = eventTriggerOutputDeviceSetupValueTable
        self.__context = context

    def InsertManyWithCustomData(self, l: list):
        ins = self.__eventTriggerOutputDeviceSetupValueTable.insert()
        values = []
        for i in range(len(l)):
            d = {
                    "EventTriggerId": l[i].get("EventTriggerId"),
                    "DeviceId": l[i].get("DeviceId"),
                    "DeviceUnicastId": l[i].get("DeviceUnicastId"),
                    "DeviceAttributeId": l[i].get("DeviceAttributeId"),
                    "DeviceAttributeValue": l[i].get("DeviceAttributeValue"),
                    "typerun": l[i].get('typerun'),
                    "Time": l[i].get('Time')
                }  
            values.append(d)
            
        if not values:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)