from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class groupingDeviceMappingRepo():
    __groupingDeviceMappingTable: Table
    __context: Connection
    
    def __init__(self, groupingDeviceMappingTable: Table, context: Connection):
        self.__groupingDeviceMappingTable = groupingDeviceMappingTable
        self.__context = context
    
    def InsertManyWithCustomData(self, l: list):
        ins = self.__groupingDeviceMappingTable.insert()
        values = []
        
        for i in range(len(l)):  
            groupingId = l[i].get('GroupingId', None)
            if groupingId == None:
                continue   
            
            groupingUnicastId = l[i].get('GroupUnicastId', None)
            if groupingUnicastId == None:
                continue
            
            deviceId = l[i].get('DeviceId', None)
            if deviceId == None:
                continue
            
            deviceUnicastId = l[i].get('DeviceUnicastId', None)
            if deviceUnicastId == None:
                continue
            
            d = {
                "GroupingId": groupingId,
                "GroupUnicastId": groupingUnicastId,
                "DeviceId": deviceId,
                "DeviceUnicastId":  deviceUnicastId,
            }
            values.append(d)
        if values == []:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)    