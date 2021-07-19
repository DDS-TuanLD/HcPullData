from Constract.IPull import IPull
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging
from Database.Db import Db
import Constant.Constant as const


class DevicePullHandler(IPull):
   
    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)
    
    async def PullAndSave(self):
        s = System(self._IPull__logger)
        data = await s.SendHttpRequestTotUrl(self._IPull__http, const.SERVER_HOST+const.CLOUD_PULL_DEVICE_URL, {})
        if data is not None:
            self.__saveToDb(data)
            self.PullSuccess()
        
    def __saveToDb(self, data: list):
        db = Db()
        db.Services.DeviceServices.AddManyDeviceWithCustomData(data)
