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
        
        deviceIdForGroupDeviceMapping = []
        groupDeviceMappingArray = []
        
        for i in range(len(data)):
            groupingDeviceMappingsList = data[i].get("groupingDeviceMappings", [])
            for j in range(len(groupingDeviceMappingsList)):
                deviceId = groupingDeviceMappingsList[j].get('deviceId')
                groupingObject = {
                    "GroupingId": groupingDeviceMappingsList[j].get('groupingId'),
                    "GroupUnicastId": data[j].get('unicastId'),
                    "DeviceId": groupingDeviceMappingsList[j].get('deviceId'),
                    "DeviceUnicastId": None
                }
                deviceIdForGroupDeviceMapping.append(deviceId)
                groupDeviceMappingArray.append(groupingObject)

        deviceRecords = db.Services.DeviceServices.FindAllDevice()
        deviceIdUnicastMapping = {}

        for deviceRecord in deviceRecords:
            deviceId = deviceRecord['DeviceId']
            deviceUnicastId = deviceRecord['DeviceUnicastId']
            deviceIdUnicastMapping[deviceId] = deviceUnicastId

        for i in range(len(deviceIdForGroupDeviceMapping)):
            deviceId = deviceIdForGroupDeviceMapping[i]
            groupDeviceMappingArray[i]['DeviceUnicastId'] = deviceIdUnicastMapping.get(deviceId)
        db.Services.GroupingDeviceMappingServices.AddManyGroupingDeviceMappingWithCustomData(groupDeviceMappingArray)
