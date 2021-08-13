from Constract.IPull import IPull
from HcServices.Http import Http
import logging
from Database.Db import Db

test_data = [
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "hasTimer": True,
    "startAt": "2021-07-19T06:50:26.470Z",
    "endAt": "2021-07-19T06:50:26.470Z",
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
    "createdAt": "2021-07-19T06:50:26.470Z",
    "updatedAt": "2021-07-19T06:50:26.470Z",
    "deletedAt": "2021-07-19T06:50:26.470Z",
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


class RulePullHandler(IPull):

    def __init__(self, log: logging.Logger, http: Http):
        super().__init__(log, http)

    async def PullAndSave(self):
        # await asyncio.sleep(1)
        # s = System(self._IPull__logger)
        # data = await s.SendHttpRequestTotUrl(self._IPull__http, const.SERVER_HOST + const.CLOUD_PULL_RULE_URL, {})
        data = test_data
        if data is not None:
            self.__saveToDb(data)
            self.PullSuccess()

    def __saveToDb(self, data: list):
        db = Db()
        db.Services.EventTriggerServices.AddManyEventTriggerWithCustomData(data, 2)

        eventTriggerInputDeviceMappingArray = []
        deviceIdForEventTriggerInputDeviceMappings = []

        eventTriggerInputDeviceSetupValueArray = []
        deviceIdForEventTriggerInputDeviceSetupValues = []

        eventTriggerOutputDeviceMappingArray = []
        deviceIdForEventTriggerOutputDeviceMappings = []

        eventTriggerOutputDeviceSetupValueArray = []
        deviceIdForEventTriggerOutputDeviceSetupValues = []

        eventTriggerOutputGroupingMappingArray = []
        groupIdForEventTriggerOutputGroupingMappings = []

        eventTriggerOutputGroupingSetupValueArray = []
        groupIdForEventTriggerOutputGroupingSetupValues = []

        eventTriggerOutputSceneMappingArray = []
        sceneIdForEventTriggerOutputSceneMappings = []

        for i in range(len(data)):
            eventTriggerInputDeviceMappingsList = data[i].get("eventTriggerInputDeviceMappings", [])
            eventTriggerInputDeviceSetupValuesList = data[i].get("eventTriggerInputDeviceSetupValues", [])
            eventTriggerOutputDeviceMappingsList = data[i].get("eventTriggerOutputDeviceMappings", [])
            eventTriggerOutputDeviceSetupValuesList = data[i].get("eventTriggerOutputDeviceSetupValues", [])
            eventTriggerOutputGroupingMappingsList = data[i].get("eventTriggerOutputGroupingMappings", [])
            eventTriggerOutputGroupingSetupValuesList = data[i].get("eventTriggerOutputGroupingSetupValues", [])
            eventTriggerOutputSceneMappingsList = data[i].get("eventTriggerOutputSceneMappings", [])

            for s in range(len(eventTriggerInputDeviceMappingsList)):
                deviceId = eventTriggerInputDeviceMappingsList[s].get('inputDeviceId')
                eventTriggerInputDeviceMappingObject = {
                    "EventTriggerId": eventTriggerInputDeviceMappingsList[s].get('eventTriggerId'),
                    "DeviceId": eventTriggerInputDeviceMappingsList[s].get('inputDeviceId'),
                    "DeviceUnicastId": None,
                }
                deviceIdForEventTriggerInputDeviceMappings.append(deviceId)
                eventTriggerInputDeviceMappingArray.append(eventTriggerInputDeviceMappingObject)

            for s in range(len(eventTriggerInputDeviceSetupValuesList)):
                deviceId = eventTriggerInputDeviceSetupValuesList[s].get('inputDeviceId')
                eventTriggerInputDeviceSetupValueObject = {
                    "EventTriggerId": eventTriggerInputDeviceSetupValuesList[s].get('eventTriggerId'),
                    "DeviceId": eventTriggerInputDeviceSetupValuesList[s].get('inputDeviceId'),
                    "DeviceUnicastId": None,
                    "DeviceAttributeId": eventTriggerInputDeviceSetupValuesList[s].get('deviceAttributeId'),
                    "ComparisonOperatorId": eventTriggerInputDeviceSetupValuesList[s].get('comparisonOperatorId'),
                    "DeviceAttributeValue": eventTriggerInputDeviceSetupValuesList[s].get('deviceAttributeValue'),
                    "DeviceAttributeValueMAX": eventTriggerInputDeviceSetupValuesList[s].get('deviceAttributeValueMAX',
                                                                                             -1000)
                }
                deviceIdForEventTriggerInputDeviceSetupValues.append(deviceId)
                eventTriggerInputDeviceSetupValueArray.append(eventTriggerInputDeviceSetupValueObject)

            for s in range(len(eventTriggerOutputDeviceMappingsList)):
                deviceId = eventTriggerOutputDeviceMappingsList[s].get('outputDeviceId')
                eventTriggerOutputDeviceMappingObject = {
                    "EventTriggerId": eventTriggerOutputDeviceMappingsList[s].get('eventTriggerId'),
                    "DeviceId": eventTriggerOutputDeviceMappingsList[s].get('outputDeviceId'),
                    "DeviceUnicastId": None,
                }
                deviceIdForEventTriggerOutputDeviceMappings.append(deviceId)
                eventTriggerOutputDeviceMappingArray.append(eventTriggerOutputDeviceMappingObject)

            for s in range(len(eventTriggerOutputDeviceSetupValuesList)):
                deviceId = eventTriggerOutputDeviceSetupValuesList[s].get('outputDeviceId')
                eventTriggerOutputDeviceSetupValueObject = {
                    "EventTriggerId": eventTriggerOutputDeviceSetupValuesList[s].get('eventTriggerId'),
                    "DeviceId": eventTriggerOutputDeviceSetupValuesList[s].get('outputDeviceId'),
                    "DeviceUnicastId": None,
                    "DeviceAttributeId": eventTriggerOutputDeviceSetupValuesList[s].get('deviceAttributeId'),
                    "DeviceAttributeValue": eventTriggerOutputDeviceSetupValuesList[s].get('deviceAttributeValue')
                }
                deviceIdForEventTriggerOutputDeviceSetupValues.append(deviceId)
                eventTriggerOutputDeviceSetupValueArray.append(eventTriggerOutputDeviceSetupValueObject)

            for s in range(len(eventTriggerOutputGroupingMappingsList)):
                groupId = eventTriggerOutputGroupingMappingsList[s].get('outputGroupingId')
                eventTriggerOutputGroupingMappingObject = {
                    "EventTriggerId": eventTriggerOutputGroupingMappingsList[s].get('eventTriggerId'),
                    "GroupingId": eventTriggerOutputGroupingMappingsList[s].get('outputGroupingId'),
                    "GroupUnicastId": None,
                }
                groupIdForEventTriggerOutputGroupingMappings.append(groupId)
                eventTriggerOutputGroupingMappingArray.append(eventTriggerOutputGroupingMappingObject)

            for s in range(len(eventTriggerOutputGroupingSetupValuesList)):
                groupId = eventTriggerOutputGroupingSetupValuesList[s].get('outputGroupingId')
                eventTriggerOutputGroupingSetupValueObject = {
                    "EventTriggerId": eventTriggerOutputGroupingSetupValuesList[s].get('eventTriggerId'),
                    "GroupingId": eventTriggerOutputGroupingSetupValuesList[s].get('outputGroupingId'),
                    "GroupUnicastId": None,
                    "DeviceAttributeId": eventTriggerOutputGroupingSetupValuesList[s].get('deviceAttributeId'),
                    "DeviceAttributeValue": eventTriggerOutputGroupingSetupValuesList[s].get('deviceAttributeValue')
                }
                groupIdForEventTriggerOutputGroupingSetupValues.append(groupId)
                eventTriggerOutputGroupingSetupValueArray.append(eventTriggerOutputGroupingSetupValueObject)

            for s in range(len(eventTriggerOutputSceneMappingsList)):
                sceneId = eventTriggerOutputSceneMappingsList[s].get('outputSceneId')
                eventTriggerOutputSceneMappingObject = {
                    "EventTriggerId": eventTriggerOutputSceneMappingsList[s].get('eventTriggerId'),
                    "SceneId": eventTriggerOutputSceneMappingsList[s].get('outputSceneId'),
                    "SceneUnicastID": None,
                }
                sceneIdForEventTriggerOutputSceneMappings.append(sceneId)
                eventTriggerOutputSceneMappingArray.append(eventTriggerOutputSceneMappingObject)

        deviceRecords = db.Services.DeviceServices.FindAllDevice()
        deviceIdUnicastMapping = {}

        for deviceRecord in deviceRecords:
            deviceId = deviceRecord['DeviceId']
            deviceUnicastId = deviceRecord['DeviceUnicastId']
            deviceIdUnicastMapping[deviceId] = deviceUnicastId

        for i in range(len(deviceIdForEventTriggerInputDeviceMappings)):
            deviceId = deviceIdForEventTriggerInputDeviceMappings[i]
            eventTriggerInputDeviceMappingArray[i]['DeviceUnicastId'] = deviceIdUnicastMapping.get(deviceId)
        db.Services.EventTriggerInputDeviceMappingServices.AddManyEventTriggerInputDeviceMappingWithCustomData(
            eventTriggerInputDeviceMappingArray)

        for i in range(len(deviceIdForEventTriggerInputDeviceSetupValues)):
            deviceId = deviceIdForEventTriggerInputDeviceSetupValues[i]
            eventTriggerInputDeviceSetupValueArray[i]['DeviceUnicastId'] = deviceIdUnicastMapping.get(deviceId)
        db.Services.EventTriggerInputDeviceSetupValueServices.AddManyEventTriggerInputDeviceSetupValueWithCustomData(
            eventTriggerInputDeviceSetupValueArray)

        for i in range(len(deviceIdForEventTriggerOutputDeviceMappings)):
            deviceId = deviceIdForEventTriggerOutputDeviceMappings[i]
            eventTriggerOutputDeviceMappingArray[i]['DeviceUnicastId'] = deviceIdUnicastMapping.get(deviceId)
        db.Services.EventTriggerOutputDeviceMappingServices.AddManyEventTriggerOutputDeviceMappingWithCustomData(
            eventTriggerOutputDeviceMappingArray)

        for i in range(len(deviceIdForEventTriggerOutputDeviceSetupValues)):
            deviceId = deviceIdForEventTriggerOutputDeviceSetupValues[i]
            eventTriggerOutputDeviceSetupValueArray[i]['DeviceUnicastId'] = deviceIdUnicastMapping.get(deviceId)
        db.Services.EventTriggerOutputDeviceSetupValueServices.AddManyEventTriggerOutputDeviceSetupValueWithCustomData(
            eventTriggerOutputDeviceSetupValueArray)

        groupRecords = db.Services.GroupingServices.FindAllGroup()
        groupIdUnicastMapping = {}

        for groupRecord in groupRecords:
            groupId = groupRecord['GroupingId']
            groupUnicastId = groupRecord['GroupingUnicastId']
            groupIdUnicastMapping[groupId] = groupUnicastId

        for i in range(len(groupIdForEventTriggerOutputGroupingMappings)):
            groupId = groupIdForEventTriggerOutputGroupingMappings[i]
            eventTriggerOutputGroupingMappingArray[i]['GroupUnicastId'] = groupIdUnicastMapping.get(groupId)
        db.Services.EventTriggerOutputGroupingMappingServices.AddManyEventTriggerOutputGroupMappingWithCustomData(
            eventTriggerOutputGroupingMappingArray)

        for i in range(len(groupIdForEventTriggerOutputGroupingSetupValues)):
            groupId = groupIdForEventTriggerOutputGroupingSetupValues[i]
            eventTriggerOutputGroupingSetupValueArray[i]['GroupUnicastId'] = groupIdUnicastMapping.get(groupId)
        db.Services.EventTriggerOutputGroupingSetupValueServices.AddManyEventTriggerOutputGroupSetupValueWithCustomData(
            eventTriggerOutputGroupingSetupValueArray)

        sceneRecords = db.Services.EventTriggerServices.FindAllEventTrigger()
        sceneIdUnicastMapping = {}

        for sceneRecord in sceneRecords:
            sceneId = sceneRecord['EventTriggerId']
            sceneUnicastId = sceneRecord['SceneUnicastID']
            sceneIdUnicastMapping[sceneId] = sceneUnicastId

        for i in range(len(sceneIdForEventTriggerOutputSceneMappings)):
            sceneId = sceneIdForEventTriggerOutputSceneMappings[i]
            eventTriggerOutputSceneMappingArray[i]['SceneUnicastID'] = sceneIdUnicastMapping.get(sceneId)
        db.Services.EventTriggerOutputSceneMappingServices.AddManyEventTriggerOutputSceneMappingWithCustomDataType2(
            eventTriggerOutputSceneMappingArray)
