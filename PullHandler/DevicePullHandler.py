from Constract.Ipull import Ipull
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging
from Database.Db import Db

class DevicePullHandler(Ipull):
   
    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)
    
    async def PullAndSave(self):
        s = System(self._Ipull__logger)
        data =await s.SendHttpRequestTotUrl(self._Ipull__http, "https://iot-dev.truesight.asia/rpc/iot-ebe/sync/list-device", {})
        if data == None:
            self._Ipull__logger.debug("have no data from cloud")
            print("have no data from cloud")
            return
        self.__saveToDb(data)
        
    def __saveToDb(self, data: list):
        db = Db()
        db.Services.DeviceServices.AddManyDeviceWithCustomData(data)
