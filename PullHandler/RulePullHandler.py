from Constract.Ipull import Ipull
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging
from Database.Db import Db

data = [
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "usedTimer": True,
    "startAt": "2021-07-10T09:20:08.539Z",
    "endAt": "2021-07-10T09:20:08.539Z",
    "useRepeater": True,
    "eachMonday": True,
    "eachTuesday": True,
    "eachWednesday": True,
    "eachThursday": True,
    "eachFriday": True,
    "eachSaturday": True,
    "eachSunday": True,
    "logicalOperatorId": 0,
    "useNotification": True,
    "dormitoryId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "ruleActions": [
      {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "ruleId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "ruleActionTypeId": 0,
        "deviceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "groupingId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "sceneId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "delayTime": "2021-07-10T09:20:08.539Z",
        "ruleActionDeviceSetupValues": [
          {
            "deviceAttributeId": 0,
            "deviceAttributeValue": 0
          }
        ],
        "ruleActionGroupingSetupValues": [
          {
            "deviceAttributeId": 0,
            "deviceAttributeValue": 0
          }
        ]
      }
    ],
    "ruleSceneMappings": [
      {
        "sceneId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "ruleId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ],
    "ruleTriggers": [
      {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "ruleId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "deviceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "deviceAttributeId": 0,
        "comparisonOperatorId": 0,
        "comparisonValue": 0
      }
    ],
    "createdAt": "2021-07-10T09:20:08.539Z",
    "updatedAt": "2021-07-10T09:20:08.539Z",
    "deletedAt": "2021-07-10T09:20:08.539Z"
  }
]

class RulePullHandler(Ipull):
   
    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)
    
    async def PullAndSave(self):
        await asyncio.sleep(1)
        # s = System(self._Ipull__logger)
        # data =await s.SendHttpRequestTotUrl(self._Ipull__http, "https://iot-dev.truesight.asia/rpc/iot-ebe/sync/list-rule", {})
        # if data == None:
        #     self._Ipull__logger.debug("have no data from cloud")
        #     print("have no data from cloud")
        #     return
        self.__saveToDb(data)
        
    def __saveToDb(self, l: list):
        db = Db()
        db.Services.EventTriggerServices.AddManyDeviceWithCustomData(l)