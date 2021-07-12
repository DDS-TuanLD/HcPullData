from Constract.Ipull import Ipull
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging
from Database.Db import Db
import Constant.Constant as const

data = [
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "hasTimer": True,
    "startAt": "2021-07-12T08:49:53.803Z",
    "endAt": "2021-07-12T08:49:53.803Z",
    "hasRepeater": True,
    "eachMonday": True,
    "eachTuesday": True,
    "eachWednesday": True,
    "eachThursday": True,
    "eachFriday": True,
    "eachSaturday": True,
    "eachSunday": True,
    "hasNotification": True,
    "notificationDelayTime": 0,
    "logicalOperatorId": 0,
    "createdAt": "2021-07-12T08:49:53.803Z",
    "updatedAt": "2021-07-12T08:49:53.803Z",
    "deletedAt": "2021-07-12T08:49:53.803Z",
    "eventTriggerInputDeviceMappings": [
      {
        "eventTriggerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "inputDeviceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ],
    "eventTriggerInputDeviceSetupValues": [
      {
        "eventTriggerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "inputDeviceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "deviceAttributeId": 0,
        "comparisonOperatorId": 0,
        "deviceAttributeValue": 0
      }
    ],
    "eventTriggerOutputDeviceMappings": [
      {
        "eventTriggerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "outputDeviceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ],
    "eventTriggerOutputDeviceSetupValues": [
      {
        "eventTriggerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "outputDeviceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "deviceAttributeId": 0,
        "deviceAttributeValue": 0
      }
    ],
    "eventTriggerOutputGroupingMappings": [
      {
        "eventTriggerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "outputGroupingId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ],
    "eventTriggerOutputGroupingSetupValues": [
      {
        "eventTriggerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "outputGroupingId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "deviceAttributeId": 0,
        "deviceAttributeValue": 0
      }
    ],
    "eventTriggerOutputSceneMappings": [
      {
        "eventTriggerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "outputSceneId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  }
]

class RulePullHandler(Ipull):
   
    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)
    
    async def PullAndSave(self):
        await asyncio.sleep(1)
        # s = System(self._Ipull__logger)
        # data =await s.SendHttpRequestTotUrl(self._Ipull__http, const.SERVER_HOST+const.CLOUD_PULL_RULE_URL, {})
        # if data == None:
        #     self._Ipull__logger.debug("have no data from cloud")
        #     print("have no data from cloud")
        #     return
        self.__saveToDb(data)
        
    def __saveToDb(self, l: list):
        db = Db()
        db.Services.EventTriggerServices.AddManyEventTriggerWithCustomData(l, 2)
        
        eventTriggerInputDeviceMappings = []
        deviceForEventTriggerInputDeviceMappings = []
        
        eventTriggerInputDeviceSetupValues = []
        deviceForEventTriggerInputDeviceSetupValues = []
        
        eventTriggerOutputDeviceMappings = []
        deviceForEventTriggerOutputDeviceMappings = []
        
        eventTriggerOutputDeviceSetupValues = []
        deviceForEventTriggerOutputDeviceSetupValues = []
        
        eventTriggerOutputGroupingMappings = []
        groupForEventTriggerOutputGroupingMappings = []
        
        eventTriggerOutputGroupingSetupValues = []
        groupForEventTriggerOutputGroupingSetupValues = []
        
        eventTriggerOutputSceneMappings = []
        sceneForEventTriggerOutputSceneMappings = []
        
        for i in range(len(l)):
            eventTriggerInputDeviceMappingsList = l[i].get("eventTriggerInputDeviceMappings", [])
            eventTriggerInputDeviceSetupValuesList = l[i].get("eventTriggerInputDeviceSetupValues", [])
            eventTriggerOutputDeviceMappingsList = l[i].get("eventTriggerOutputDeviceMappings", [])
            eventTriggerOutputDeviceSetupValuesList = l[i].get("eventTriggerOutputDeviceSetupValues", [])
            eventTriggerOutputGroupingMappingsList = l[i].get("eventTriggerOutputGroupingMappings", [])
            eventTriggerOutputGroupingSetupValuesList = l[i].get("eventTriggerOutputGroupingSetupValues", [])
            eventTriggerOutputSceneMappingsList = l[i].get("eventTriggerOutputSceneMappings", [])
            
            for s in range(len(eventTriggerInputDeviceMappingsList)):
                d = eventTriggerInputDeviceMappingsList[s].get('inputDeviceId')
                e = {
                    "EventTriggerId": eventTriggerInputDeviceMappingsList[s].get('eventTriggerId'),
                    "DeviceId": eventTriggerInputDeviceMappingsList[s].get('inputDeviceId'),
                    "DeviceUnicastId": None,
                }
                deviceForEventTriggerInputDeviceMappings.append(d)
                eventTriggerInputDeviceMappings.append(e) 
                
            for s1 in range(len(eventTriggerInputDeviceSetupValuesList)):
                d = eventTriggerInputDeviceSetupValuesList[s1].get('inputDeviceId')
                e = {
                    "EventTriggerId": eventTriggerInputDeviceSetupValuesList[s1].get('eventTriggerId'),
                    "DeviceId": eventTriggerInputDeviceSetupValuesList[s1].get('inputDeviceId'),
                    "DeviceUnicastId": None,
                    "DeviceAttributeId": eventTriggerInputDeviceSetupValuesList[s1].get('deviceAttributeId'),
                    "ComparisonOperatorId": eventTriggerInputDeviceSetupValuesList[s1].get('comparisonOperatorId'),
                    "DeviceAttributeValue": eventTriggerInputDeviceSetupValuesList[s1].get('deviceAttributeValue'),
                    "DeviceAttributeValueMAX": eventTriggerInputDeviceSetupValuesList[s1].get('deviceAttributeValueMAX', -1000)
                }
                deviceForEventTriggerInputDeviceSetupValues.append(d)
                eventTriggerInputDeviceSetupValues.append(e)  
                
            for s2 in range(len(eventTriggerOutputDeviceMappingsList)):
                d = eventTriggerOutputDeviceMappingsList[s2].get('outputDeviceId')
                e = {
                    "EventTriggerId": eventTriggerOutputDeviceMappingsList[s2].get('eventTriggerId'),
                    "DeviceId": eventTriggerOutputDeviceMappingsList[s2].get('outputDeviceId'),
                    "DeviceUnicastId": None,
                }
                deviceForEventTriggerOutputDeviceMappings.append(d)
                eventTriggerOutputDeviceMappings.append(e) 
                
            for s3 in range(len(eventTriggerOutputDeviceSetupValuesList)):
                d = eventTriggerOutputDeviceSetupValuesList[s3].get('outputDeviceId')
                e = {
                    "EventTriggerId": eventTriggerOutputDeviceSetupValuesList[s3].get('eventTriggerId'),
                    "DeviceId": eventTriggerOutputDeviceSetupValuesList[s3].get('outputDeviceId'),
                    "DeviceUnicastId": None,
                    "DeviceAttributeId": eventTriggerOutputDeviceSetupValuesList[s3].get('deviceAttributeId'),
                    "DeviceAttributeValue": eventTriggerOutputDeviceSetupValuesList[s3].get('deviceAttributeValue')
                }
                deviceForEventTriggerOutputDeviceSetupValues.append(d)
                eventTriggerOutputDeviceSetupValues.append(e) 
                
            for s4 in range(len(eventTriggerOutputGroupingMappingsList)):
                g = eventTriggerOutputGroupingMappingsList[s4].get('outputGroupingId')
                e = {
                    "EventTriggerId": eventTriggerOutputGroupingMappingsList[s4].get('eventTriggerId'),
                    "GroupingId": eventTriggerOutputGroupingMappingsList[s4].get('outputGroupingId'),
                    "GroupUnicastId": None,
                }
                groupForEventTriggerOutputGroupingMappings.append(g)
                eventTriggerOutputGroupingMappings.append(e) 
                
            for s5 in range(len(eventTriggerOutputGroupingSetupValuesList)):
                g = eventTriggerOutputGroupingSetupValuesList[s5].get('outputGroupingId')
                e = {
                    "EventTriggerId": eventTriggerInputDeviceMappingsList[s5].get('eventTriggerId'),
                    "GroupingId": eventTriggerInputDeviceMappingsList[s5].get('outputGroupingId'),
                    "GroupUnicastId": None,
                    "DeviceAttributeId": eventTriggerOutputGroupingSetupValuesList[s5].get('deviceAttributeId'),
                    "DeviceAttributeValue": eventTriggerOutputGroupingSetupValuesList[s5].get('deviceAttributeValue')
                }
                groupForEventTriggerOutputGroupingSetupValues.append(g)
                eventTriggerOutputGroupingSetupValuesList.append(e) 
                
            for s6 in range(len(eventTriggerOutputSceneMappingsList)):
                c = eventTriggerOutputSceneMappingsList[s6].get('outputSceneId')
                e = {
                    "EventTriggerId": eventTriggerInputDeviceMappingsList[s6].get('eventTriggerId'),
                    "SceneId": eventTriggerInputDeviceMappingsList[s6].get('outputSceneId'),
                    "SceneUnicastID": None,
                }
                sceneForEventTriggerOutputSceneMappings.append(c)
                eventTriggerOutputSceneMappings.append(e) 
        
        rel1 = db.Services.DeviceServices.FindDeviceWithCondition(db.Table.DeviceTable.c.DeviceId.in_(deviceForEventTriggerInputDeviceMappings))
        dt1 = rel1.fetchall()
        for m1 in range(len(dt1)):
            eventTriggerInputDeviceMappings[m1]['DeviceUnicastId'] = dt1[m1]['DeviceUnicastId']
        db.Services.EventTriggerInputDeviceMappingServices.AddManyEventTriggerInputDeviceMappingWithCustomData(eventTriggerInputDeviceMappings)
        
        rel2 = db.Services.DeviceServices.FindDeviceWithCondition(db.Table.DeviceTable.c.DeviceId.in_(deviceForEventTriggerInputDeviceSetupValues))
        dt2 = rel2.fetchall()
        for m2 in range(len(dt2)):
            eventTriggerInputDeviceSetupValues[m2]['DeviceUnicastId'] = dt2[m2]['DeviceUnicastId']
        db.Services.EventTriggerInputDeviceSetupValueServices.AddManyEventTriggerInputDeviceSetupValueWithCustomData(eventTriggerInputDeviceSetupValues)
        
        rel3 = db.Services.DeviceServices.FindDeviceWithCondition(db.Table.DeviceTable.c.DeviceId.in_(deviceForEventTriggerOutputDeviceMappings))
        dt3 = rel3.fetchall()
        for m3 in range(len(dt3)):
            eventTriggerOutputDeviceMappings[m3]['DeviceUnicastId'] = dt3[m3]['DeviceUnicastId']
        db.Services.EventTriggerOutputDeviceMappingServices.AddManyEventTriggerOutputDeviceMappingWithCustomData(eventTriggerOutputDeviceMappings)
        
        rel4 = db.Services.DeviceServices.FindDeviceWithCondition(db.Table.DeviceTable.c.DeviceId.in_(deviceForEventTriggerOutputDeviceSetupValues))
        dt4 = rel4.fetchall()
        for m4 in range(len(dt4)):
            eventTriggerOutputGroupingSetupValues[m4]['DeviceUnicastId'] = dt4[m4]['DeviceUnicastId']
        db.Services.EventTriggerOutputDeviceSetupValueServices.AddManyEventTriggerOutputDeviceSetupValueWithCustomData(eventTriggerOutputGroupingSetupValues)
        
        rel5 = db.Services.GroupingServices.FindGroupWithCondition(db.Table.GroupingTable.c.GroupingId.in_(groupForEventTriggerOutputGroupingMappings))
        dt5 = rel5.fetchall()
        for m5 in range(len(dt5)):
              eventTriggerOutputGroupingMappings[m5]['GroupUnicastId'] = dt5[m5]['GroupUnicastId']
        db.Services.EventTriggerOutputGroupingMappingServices.AddManyEventTriggerOutputGroupMappingWithCustomData(eventTriggerOutputGroupingMappings)
        
        rel6 = db.Services.GroupingServices.FindGroupWithCondition(db.Table.GroupingTable.c.GroupingId.in_(groupForEventTriggerOutputGroupingSetupValues))
        dt6 = rel6.fetchall()
        for m6 in range(len(dt6)):
              eventTriggerOutputGroupingMappings[m6]['GroupUnicastId'] = dt6[m6]['GroupUnicastId']
        db.Services.EventTriggerOutputGroupingSetupValueServices.AddManyEventTriggerOutputGroupSetupValueWithCustomData(eventTriggerOutputGroupingSetupValues)
        
        rel7 = db.Services.EventTriggerServices.FindEventTriggerWithCondition(db.Table.EventTriggerTable.c.EventTriggerId.in_(sceneForEventTriggerOutputSceneMappings))
        dt7 = rel7.fetchall()
        for m7 in range(len(dt7)):
              eventTriggerOutputGroupingMappings[m7]['SceneUnicastID'] = dt7[m7]['SceneUnicastID']
        db.Services.EventTriggerOutputSceneMappingServices.AddManyEventTriggerOutputSceneMappingWithCustomData(eventTriggerOutputSceneMappings)
                
    def Exhibit(self):
        return super().Exhibit()

    
    def DeExhibit(self):
        return super().DeExhibit()
    
    def IsInExhibitState(self):
        return super().IsInExhibitState()       
