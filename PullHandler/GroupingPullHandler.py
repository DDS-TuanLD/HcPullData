from Constract.Ipull import Ipull
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging
from Database.Db import Db

class GroupingPullHandler(Ipull):
   
    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)
    
    async def PullAndSave(self):
        s = System(self._Ipull__logger)
        data =await s.SendHttpRequestTotUrl(self._Ipull__http, "https://iot-dev.truesight.asia/rpc/iot-ebe/sync/list-grouping", {})
        if data == None:
            self._Ipull__logger.debug("have no data from cloud")
            print("have no data from cloud")
            return
        self.__saveToDb(data)
        
    def __saveToDb(self, data: list):
        db = Db()
        #db.Services.GroupingServices.AddManyGroupingWithCustomData(data)
        device = []
        groupDeviceMappings = []
        for i in range(len(data)):
            gs = data[i].get("groupingDeviceMappings")
            # print(gs)
            # print(type(gs))
            for j in range(len(gs)):
                d = gs[j].get('deviceId')
                gDM = {
                    "GroupingId": gs[j].get('groupingId'),
                    "GroupUnicastId": data[i].get('unicastId'),
                    "DeviceId": gs[j].get('deviceId'),
                    "DeviceUnicastId": None
                }
                device.append(d)
                groupDeviceMappings.append(gDM)
        
        rel = db.Services.DeviceServices.FindDeviceWithCondition(db.Table.DeviceTable.c.DeviceId.in_(device))
        dt = rel.fetchall()
        for j in range(len(dt)):
            groupDeviceMappings[i]['DeviceUnicastId'] = dt[j]['DeviceUnicastId']
        db.Services.GroupingDeviceMappingServices.AddManyDeviceWithCustomData(groupDeviceMappings)
            
