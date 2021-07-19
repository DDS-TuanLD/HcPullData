from Constract.IPull import IPull
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging
from Database.Db import Db
import Constant.Constant as const


class GroupingPullHandler(IPull):
   
    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)
    
    async def PullAndSave(self):
        s = System(self._IPull__logger)
        data = await s.SendHttpRequestTotUrl(self._IPull__http, const.SERVER_HOST+const.CLOUD_PULL_GROUPING_URL, {})
        if data is not None:
            self.__saveToDb(data)
            self.PullSuccess()

    def __saveToDb(self, data: list):
        db = Db()
        db.Services.GroupingServices.AddManyGroupingWithCustomData(data)
        device = []
        groupDeviceMappings = []
        for i in range(len(data)):
            gs = data[i].get("groupingDeviceMappings", [])
            for j in range(len(gs)):
                d = gs[j].get('deviceId')
                gDM = {
                    "GroupingId": gs[j].get('groupingId'),
                    "GroupUnicastId": data[j].get('unicastId'),
                    "DeviceId": gs[j].get('deviceId'),
                    "DeviceUnicastId": None
                }
                device.append(d)
                groupDeviceMappings.append(gDM)
        rel = db.Services.DeviceServices.FindDeviceWithCondition(db.Table.DeviceTable.c.DeviceId.in_(device))
        dt = rel.fetchall()
        for j in range(len(dt)):
            groupDeviceMappings[j]['DeviceUnicastId'] = dt[j]['DeviceUnicastId']
        db.Services.GroupingDeviceMappingServices.AddManyGroupingDeviceMappingWithCustomData(groupDeviceMappings)
