from Constract.Ipull import Ipull
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging
from Database.Db import Db
import Constant.Constant as const

class ScenePullHandler(Ipull):
   
    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)
    
    async def PullAndSave(self):
        s = System(self._Ipull__logger)
        data =await s.SendHttpRequestTotUrl(self._Ipull__http, const.SERVER_HOST+const.CLOUD_PULL_SCENE_URL, {})
        if data == None:
            self._Ipull__logger.debug("have no data from cloud")
            print("have no data from cloud")
            return
        self.__saveToDb(data)
        
    def __saveToDb(self, l: list):
        db = Db()
        db.Services.EventTriggerServices.AddManyEventTriggerWithCustomData(l, 1)
        db.Services.EventTriggerOutputSceneMappingServices.AddManyEventTriggerOutputSceneMappingWithCustomData(l)
        sceneOutputDeviceMappings = []
        deviceForSceneOutputDeviceMapping = []
        
        sceneOutputDeviceSetupValue = []
        deviceForSceneOutputDeviceSetupValue = []
        
        for i in range(len(l)):
            sceneOutputDeviceMappingsReceivedList = l[i].get("sceneDeviceMappings", [])
            sceneOutputDeviceSetupValueReceivedList = l[i].get("sceneDeviceSetupValues", [])
            
            for j in range(len(sceneOutputDeviceMappingsReceivedList)):
                d = sceneOutputDeviceMappingsReceivedList[j].get('deviceId')
                sDM = {
                    "EventTriggerId": sceneOutputDeviceMappingsReceivedList[j].get('sceneId'),
                    "DeviceId": sceneOutputDeviceMappingsReceivedList[j].get('deviceId'),
                    "DeviceUnicastId": None,
                    "typerun": sceneOutputDeviceMappingsReceivedList[j].get('typerun', None)
                }
                deviceForSceneOutputDeviceMapping.append(d)
                sceneOutputDeviceMappings.append(sDM)
            
            for k in range(len(sceneOutputDeviceSetupValueReceivedList)):
                d = sceneOutputDeviceSetupValueReceivedList[k].get('deviceId')
                sDSV = {
                    "EventTriggerId": sceneOutputDeviceSetupValueReceivedList[k].get('sceneId'),
                    "DeviceId": sceneOutputDeviceSetupValueReceivedList[k].get('deviceId'),
                    "DeviceUnicastId": None,
                    "DeviceAttributeId": sceneOutputDeviceSetupValueReceivedList[k].get("deviceAttributeId"),
                    "DeviceAttributeValue": sceneOutputDeviceSetupValueReceivedList[k].get('deviceAttributeValue'),
                    "typerun": sceneOutputDeviceSetupValueReceivedList[k].get('typerun', None),
                    "Time": sceneOutputDeviceSetupValueReceivedList[k].get('Time', None)
                }
                deviceForSceneOutputDeviceSetupValue.append(d)
                sceneOutputDeviceSetupValue.append(sDSV) 
        rel = db.Services.DeviceServices.FindDeviceWithCondition(db.Table.DeviceTable.c.DeviceId.in_(deviceForSceneOutputDeviceMapping))
        dt = rel.fetchall()
        for m in range(len(dt)):
            sceneOutputDeviceMappings[m]['DeviceUnicastId'] = dt[m]['DeviceUnicastId']
        db.Services.EventTriggerOutputDeviceMappingServices.AddManyEventTriggerOutputDeviceMappingWithCustomData(sceneOutputDeviceMappings)
        
        rel2 = db.Services.DeviceServices.FindDeviceWithCondition(db.Table.DeviceTable.c.DeviceId.in_(deviceForSceneOutputDeviceSetupValue))
        dt2 = rel2.fetchall()
        for n in range(len(dt2)):
            sceneOutputDeviceSetupValue[n]['DeviceUnicastId'] = dt2[n]['DeviceUnicastId']
        db.Services.EventTriggerOutputDeviceSetupValueServices.AddManyEventTriggerOutputDeviceSetupValueWithCustomData(sceneOutputDeviceSetupValue)
           
    def Exhibit(self):
        return super().Exhibit()
    
    def DeExhibit(self):
        return super().DeExhibit()
    
    def IsInExhibitState(self):
        return super().IsInExhibitState()       
