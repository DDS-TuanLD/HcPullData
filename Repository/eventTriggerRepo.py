from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection

class eventTriggerRepo():
    __eventTriggerTable: Table
    __context: Connection
    
    def __init__(self, eventTriggerTable: Table, context: Connection):
        self.__eventTriggerTable = eventTriggerTable
        self.__context = context
        
    def InsertManyWithCustomData(self, l: list):
        ins = self.__eventTriggerTable.insert()
        values = []
        
        for i in range(len(l)):  
            eventTriggerId = l[i].get('id', None)
            if eventTriggerId == None:
                continue
            
            fade_in = l[i].get('fadeIn', None)
            if fade_in == None:
                fade_in = 0
                
            d = {
                "EventTriggerId": eventTriggerId,
                "GroupId": eventTriggerId,
                "EventTriggerTypeId": l[i].get('eventTriggerTypeId', None),
                "SceneUnicastID": l[i].get('unicastId', None),
                "Priority": l[i].get('priority', None),
                "Name": l[i].get('name', None),
                "LogicalOperatorID": l[i].get('logicalOperatorId', None),
                "HasTimer": l[i].get('userTimer', None),
                "StartAt": datetime.time(12, 13).isoformat(timespec='minutes'),
                "EndAt": datetime.time(12, 13).isoformat(timespec='minutes'),
                "ValueCreate": l[i].get('valueCreate', None),
                "StatusID": l[i].get('statusID', None),
                "HasRepeater": l[i].get('useRepeater', None),
                "EachMonday": l[i].get('eachMonday', None),
                "EachTuesday": l[i].get('eachTuesday', None),
                "EachWednesday": l[i].get('eachWednesday', None),
                "EachThursday": l[i].get('eachThursday', None),
                "EachFriday": l[i].get('eachFriday', None),
                "EachSaturday": l[i].get('eachSaturday', None),
                "EachSunday": l[i].get('eachSunday', None),
                "NotificationUser": l[i].get('useNotification', None),
                "FADE_IN": fade_in,
            }
            values.append(d)
        if values == []:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)
        