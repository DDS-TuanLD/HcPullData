from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection


class eventTriggerOutputSceneMappingRepo:
    __eventTriggerOutputSceneMappingRepoTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputSceneMappingTable: Table, context: Connection):
        self.__eventTriggerOutputSceneMappingRepoTable = eventTriggerOutputSceneMappingTable
        self.__context = context
    
    def InsertManyWithCustomDataType1(self, l: list):
        ins = self.__eventTriggerOutputSceneMappingRepoTable.insert()
        values = []
        
        for i in range(len(l)):  
            d = {
                "EventTriggerId": l[i].get("id", None),
                "SceneId": l[i].get("id", None),
                "SceneUnicastID": l[i].get("unicastId", None),
                "typerun": l[i].get("typerun", None),
                "Time": l[i].get("time", None)
            }
            values.append(d)
        if not values:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)
            
    def InsertManyWithCustomDataType2(self, l: list):
        ins = self.__eventTriggerOutputSceneMappingRepoTable.insert()
        values = []
        
        for i in range(len(l)):  
            d = {
                "EventTriggerId": l[i].get("EventTriggerId"),
                "SceneId": l[i].get("SceneId"),
                "SceneUnicastID": l[i].get("SceneUnicastID"),
                "typerun": l[i].get("typerun"),
                "Time": l[i].get("time")
            }
            values.append(d)
        if not values:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)
