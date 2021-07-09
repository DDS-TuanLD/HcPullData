from sqlalchemy import Table, select
import sqlalchemy
from sqlalchemy.sql.expression import BinaryExpression
import asyncio
import datetime
from sqlalchemy.engine.base import Connection
from Model.device import device

class deviceRepo():
    __deviceTable: Table
    __context: Connection
    
    def __init__(self, DeviceTable: Table, context: Connection):
        self.__deviceTable = DeviceTable
        self.__context = context
        
    def CreateWithParams(self, d: device):
        ins = self.__deviceTable.insert()
        values = {
            'DeviceId': d.DeviceId,
            'DeviceUnicastId': d.DeviceUnicastId,
            'AppKey': d.AppKey,
            'NetKey': d.NetKey,
            'DeviceKey': d.DeviceKey,
            'DeviceTypeId': d.DeviceTypeId,
            'UpdateDay': d.UpdateDay,
            'UpdateTime': d.UpdateTime,
            'StatusId': d.StatusId,
            'Owner': d.Owner
        }
        self.__context.execute(ins, values)
        
    def InsertManyWithCustomData(self, l: list):
        ins = self.__deviceTable.insert()
        values = []
        for i in range(len(l)):
            t = self.__timeSplit(time=datetime.datetime.strptime(l[i].get('updatedAt'), '%Y-%m-%dT%H:%M:%S.%fZ'))
            updateDay = t[0]
            updateTime = t[1]                
            d = {
                'DeviceId': l[i].get('id', None),
                'DeviceUnicastId': l[i].get('unicastId', None),
                'AppKey': l[i].get('appKey', None),
                'NetKey': l[i].get('netKey', None),
                'DeviceKey': l[i].get('deviceKey', None),
                'DeviceTypeId': l[i].get('deviceTypeId', None),
                'UpdateDay': updateDay,
                'UpdateTime': updateTime,
                'StatusId': l[i].get('statusId', None),
                'Owner': l[i].get('Owner', None)
            }
            values.append(d)
        if values == []:
            return
        try:
            self.__context.execute(ins, values)
        except Exception as err:
            print(err)
            
    def FindWithCondition(self, condition: BinaryExpression):
        ins = self.__deviceTable.select().where(condition)
        rel = self.__context.execute(ins)
        return rel   
    
    def __timeSplit(self, time: datetime.datetime):
        m = str(time.month)
        if int(m) < 10:
            m = "0"+ m
            
        d = str(time.day)
        if int(d) < 10:
            d = "0" + d
            
        updateDay = int(str(time.year) + m + d)
        updateTime = 60*time.hour + time.minute
        return updateDay, updateTime