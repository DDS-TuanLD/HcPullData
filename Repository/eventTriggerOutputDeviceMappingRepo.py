from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputDeviceMappingRepo():
    __eventTriggerOutputDeviceMappingTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputDeviceMappingTable: Table, context: Connection):
        self.__eventTriggerOutputDeviceMappingTable = eventTriggerOutputDeviceMappingTable
        self.__context = context
    
    def InsertManyWithCustomData(self, l: list):
        ins = self.__eventTriggerOutputDeviceMappingTable.insert()
        values = []
        for i in range(len(l)):
            d = {
                    "EventTriggerId": l[i].get("EventTriggerId"),
                    "DeviceId": l[i].get("DeviceId"),
                    "DeviceUnicastId": l[i].get("DeviceUnicastId"),
                    "typerun": l[i].get("typerun")
                }  
            values.append(d)
            
        if not values:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)