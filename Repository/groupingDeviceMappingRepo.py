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
            d = {
                "GroupingId": l[i].get('GroupingId'),
                "GroupUnicastId": l[i].get('GroupUnicastId'),
                "DeviceId": l[i].get('DeviceId'),
                "DeviceUnicastId":  l[i].get('DeviceUnicastId'),
            }
            values.append(d)
        if values == []:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)    