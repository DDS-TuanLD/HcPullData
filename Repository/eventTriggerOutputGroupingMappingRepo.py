from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputGroupingMappingRepo():
    __eventTriggerOutputGroupingMappingTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputGroupingMappingTable: Table, context: Connection):
        self.__eventTriggerOutputGroupingMappingTable = eventTriggerOutputGroupingMappingTable
        self.__context = context
    
    def InsertManyWithCustomData(self, l: list):
        ins = self.__eventTriggerOutputGroupingMappingTable.insert()
        values = []
        for i in range(len(l)):
            d = {
                    "EventTriggerId": l[i].get("EventTriggerId"),
                    "GroupingId": l[i].get("GroupingId"),
                    "GroupUnicastId": l[i].get("GroupUnicastId"),
                    "typerun": l[i].get("typerun")
                }  
            values.append(d)
            
        if not values:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)