from Constract.IPull import IPull
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging
from Database.Db import Db
import Constant.Constant as const


class ScenePullHandler(IPull):

    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)

    async def PullAndSave(self):
        s = System(self._IPull__logger)
        data = await s.SendHttpRequestTotUrl(self._IPull__http, const.SERVER_HOST + const.CLOUD_PULL_SCENE_URL, {})
        if data is not None:
            self.__saveToDb(data)
            self.PullSuccess()

    def __saveToDb(self, data: list):
        db = Db()
        db.Services.EventTriggerServices.AddManyEventTriggerWithCustomData(data, 1)
        db.Services.EventTriggerOutputSceneMappingServices. \
            AddManyEventTriggerOutputSceneMappingWithCustomDataType1(data)
        sceneOutputDeviceMappingArray = []
        deviceIdForSceneOutputDeviceMappingList = []

        sceneOutputDeviceSetupValueArray = []
        deviceIdForSceneOutputDeviceSetupValueList = []

        for i in range(len(data)):
            sceneOutputDeviceMappingReceivedList = data[i].get("sceneDeviceMappings", [])
            sceneOutputDeviceSetupValueReceivedList = data[i].get("sceneDeviceSetupValues", [])

            for j in range(len(sceneOutputDeviceMappingReceivedList)):
                deviceId = sceneOutputDeviceMappingReceivedList[j].get('deviceId')
                sceneOutputDeviceMappingObject = {
                    "EventTriggerId": sceneOutputDeviceMappingReceivedList[j].get('sceneId'),
                    "DeviceId": sceneOutputDeviceMappingReceivedList[j].get('deviceId'),
                    "DeviceUnicastId": None,
                    "typerun": sceneOutputDeviceMappingReceivedList[j].get('typerun', None)
                }
                deviceIdForSceneOutputDeviceMappingList.append(deviceId)
                sceneOutputDeviceMappingArray.append(sceneOutputDeviceMappingObject)

            for j in range(len(sceneOutputDeviceSetupValueReceivedList)):
                deviceId = sceneOutputDeviceSetupValueReceivedList[j].get('deviceId')
                sceneOutputDeviceSetupValueObject = {
                    "EventTriggerId": sceneOutputDeviceSetupValueReceivedList[j].get('sceneId'),
                    "DeviceId": sceneOutputDeviceSetupValueReceivedList[j].get('deviceId'),
                    "DeviceUnicastId": None,
                    "DeviceAttributeId": sceneOutputDeviceSetupValueReceivedList[j].get("deviceAttributeId"),
                    "DeviceAttributeValue": sceneOutputDeviceSetupValueReceivedList[j].get('deviceAttributeValue'),
                    "typerun": sceneOutputDeviceSetupValueReceivedList[j].get('typerun', None),
                    "Time": sceneOutputDeviceSetupValueReceivedList[j].get('Time', None)
                }
                deviceIdForSceneOutputDeviceSetupValueList.append(deviceId)
                sceneOutputDeviceSetupValueArray.append(sceneOutputDeviceSetupValueObject)

        deviceRecords = db.Services.DeviceServices.FindAllDevice()
        deviceIdUnicastMapping = {}

        for deviceRecord in deviceRecords:
            deviceId = deviceRecord['DeviceId']
            deviceUnicastId = deviceRecord['DeviceUnicastId']
            deviceIdUnicastMapping[deviceId] = deviceUnicastId

        for i in range(len(deviceIdForSceneOutputDeviceMappingList)):
            deviceId = deviceIdForSceneOutputDeviceMappingList[i]
            sceneOutputDeviceMappingArray[i]['DeviceUnicastId'] = deviceIdUnicastMapping.get(deviceId)
        db.Services.EventTriggerOutputDeviceMappingServices.AddManyEventTriggerOutputDeviceMappingWithCustomData(
            sceneOutputDeviceMappingArray)

        for i in range(len(deviceIdForSceneOutputDeviceSetupValueList)):
            deviceId = deviceIdForSceneOutputDeviceSetupValueList[i]
            sceneOutputDeviceSetupValueArray[i]['DeviceUnicastId'] = deviceIdUnicastMapping.get(deviceId)
        db.Services.EventTriggerOutputDeviceSetupValueServices.AddManyEventTriggerOutputDeviceSetupValueWithCustomData(
            sceneOutputDeviceSetupValueArray)
