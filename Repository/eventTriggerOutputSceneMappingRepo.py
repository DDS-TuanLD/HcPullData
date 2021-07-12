from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerOutputSceneMappingRepo():
    __eventTriggerOutputSceneMappingRepoTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerOutputSceneMappingRepoTable: Table, context: Connection):
        self.__eventTriggerOutputSceneMappingRepoTable = eventTriggerOutputSceneMappingRepoTable
        self.__context = context
    
    def InsertManyWithCustomData(self, l: list):
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
        if values == []:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)