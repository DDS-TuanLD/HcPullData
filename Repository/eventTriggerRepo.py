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

    def InsertManyWithCustomData(self, l: list, type: int):
        ins = self.__eventTriggerTable.insert()
        values = []

        for i in range(len(l)):
            eventTriggerId = l[i].get('id', None)
            if eventTriggerId is None:
                continue

            startAt = ""
            s = l[i].get('startAt', None)
            if s is not None:
                t = datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%fZ')
                startAt = datetime.time(t.hour, t.minute).strftime("%H:%M")

            endAt = ""
            e = l[i].get('endAt', None)
            if e is not None:
                t = datetime.datetime.strptime(e, '%Y-%m-%dT%H:%M:%S.%fZ')
                endAt = datetime.time(t.hour, t.minute).strftime("%H:%M")
            fade_in = l[i].get('fadeIn', None)
            if fade_in is None:
                fade_in = 0

            d = {
                "EventTriggerId": eventTriggerId,
                "GroupId": eventTriggerId,
                "EventTriggerTypeId": l[i].get('eventTriggerTypeId', type),
                "SceneUnicastID": l[i].get('unicastId', None),
                "Priority": l[i].get('priority', None),
                "Name": l[i].get('name', None),
                "LogicalOperatorID": l[i].get('logicalOperatorId', None),
                "HasTimer": l[i].get('hasTimer', None),
                "StartAt": startAt,
                "EndAt": endAt,
                "ValueCreate": l[i].get('valueCreate', None),
                "StatusID": l[i].get('statusID', None),
                "HasRepeater": l[i].get('hasRepeater', None),
                "EachMonday": l[i].get('eachMonday', None),
                "EachTuesday": l[i].get('eachTuesday', None),
                "EachWednesday": l[i].get('eachWednesday', None),
                "EachThursday": l[i].get('eachThursday', None),
                "EachFriday": l[i].get('eachFriday', None),
                "EachSaturday": l[i].get('eachSaturday', None),
                "EachSunday": l[i].get('eachSunday', None),
                "NotificationUser": l[i].get('hasNotification', None),
                "FADE_IN": fade_in,
            }
            values.append(d)
        if not values:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)

    def FindWithCondition(self, condition: BinaryExpression):
        ins = self.__eventTriggerTable.select().where(condition)
        rel = self.__context.execute(ins)
        return rel

    def FindAll(self):
        ins = self.__eventTriggerTable.select()
        rel = self.__context.execute(ins)
        return rel
