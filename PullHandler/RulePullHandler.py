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

        deviceForEventTriggerInputDeviceMappingRecords = db.Services.DeviceServices.FindDeviceWithCondition(
            db.Table.DeviceTable.c.DeviceId.in_(deviceIdForEventTriggerInputDeviceMappings))
        deviceForEventTriggerInputDeviceMappingArray = deviceForEventTriggerInputDeviceMappingRecords.fetchall()
        for device in range(len(deviceForEventTriggerInputDeviceMappingArray)):
            eventTriggerInputDeviceMappingArray[device]['DeviceUnicastId'] = \
                deviceForEventTriggerInputDeviceMappingArray[device]['DeviceUnicastId']
        db.Services.EventTriggerInputDeviceMappingServices.AddManyEventTriggerInputDeviceMappingWithCustomData(
            eventTriggerInputDeviceMappingArray)

        deviceForEventTriggerInputDeviceSetupValueRecords = db.Services.DeviceServices.FindDeviceWithCondition(
            db.Table.DeviceTable.c.DeviceId.in_(deviceIdForEventTriggerInputDeviceSetupValues))
        deviceForEventTriggerInputDeviceSetupValueArray = deviceForEventTriggerInputDeviceSetupValueRecords.fetchall()
        for device in range(len(deviceForEventTriggerInputDeviceSetupValueArray)):
            eventTriggerInputDeviceSetupValueArray[device]['DeviceUnicastId'] = \
                deviceForEventTriggerInputDeviceSetupValueArray[device]['DeviceUnicastId']
        db.Services.EventTriggerInputDeviceSetupValueServices.AddManyEventTriggerInputDeviceSetupValueWithCustomData(
            eventTriggerInputDeviceSetupValueArray)

        deviceForEventTriggerOutputDeviceMappingRecords = db.Services.DeviceServices.FindDeviceWithCondition(
            db.Table.DeviceTable.c.DeviceId.in_(deviceIdForEventTriggerOutputDeviceMappings))
        deviceForEventTriggerOutputDeviceMappingArray = deviceForEventTriggerOutputDeviceMappingRecords.fetchall()
        for device in range(len(deviceForEventTriggerOutputDeviceMappingArray)):
            eventTriggerOutputDeviceMappingArray[device]['DeviceUnicastId'] = \
                deviceForEventTriggerOutputDeviceMappingArray[device]['DeviceUnicastId']
        db.Services.EventTriggerOutputDeviceMappingServices.AddManyEventTriggerOutputDeviceMappingWithCustomData(
            eventTriggerOutputDeviceMappingArray)

        deviceForEventTriggerOutputDeviceSetupValueRecords = db.Services.DeviceServices.FindDeviceWithCondition(
            db.Table.DeviceTable.c.DeviceId.in_(deviceIdForEventTriggerOutputDeviceSetupValues))
        deviceForEventTriggerOutputDeviceSetupValueArray = deviceForEventTriggerOutputDeviceSetupValueRecords.fetchall()
        for device in range(len(deviceForEventTriggerOutputDeviceSetupValueArray)):
            eventTriggerOutputDeviceSetupValueArray[device]['DeviceUnicastId'] = \
                deviceForEventTriggerOutputDeviceSetupValueArray[device]['DeviceUnicastId']
        db.Services.EventTriggerOutputDeviceSetupValueServices.AddManyEventTriggerOutputDeviceSetupValueWithCustomData(
            eventTriggerOutputDeviceSetupValueArray)

        groupForEventTriggerOutputGroupingMappingRecords = db.Services.GroupingServices.FindGroupWithCondition(
            db.Table.GroupingTable.c.GroupingId.in_(groupIdForEventTriggerOutputGroupingMappings))
        groupForEventTriggerOutputGroupingMappingRecordArray = \
            groupForEventTriggerOutputGroupingMappingRecords.fetchall()
        for group in range(len(groupForEventTriggerOutputGroupingMappingRecordArray)):
            eventTriggerOutputGroupingMappingArray[group]['GroupUnicastId'] = \
                groupForEventTriggerOutputGroupingMappingRecordArray[group]['GroupUnicastId']
        db.Services.EventTriggerOutputGroupingMappingServices.AddManyEventTriggerOutputGroupMappingWithCustomData(
            eventTriggerOutputGroupingMappingArray)

        groupForEventTriggerOutputGroupingSetupValueRecords = db.Services.GroupingServices.FindGroupWithCondition(
            db.Table.GroupingTable.c.GroupingId.in_(groupIdForEventTriggerOutputGroupingSetupValues))
        groupForEventTriggerOutputGroupingSetupValueArray = \
            groupForEventTriggerOutputGroupingSetupValueRecords.fetchall()
        for group in range(len(groupForEventTriggerOutputGroupingSetupValueArray)):
            eventTriggerOutputGroupingSetupValueArray[group]['GroupUnicastId'] = \
                groupForEventTriggerOutputGroupingSetupValueArray[group]['GroupUnicastId']
        db.Services.EventTriggerOutputGroupingSetupValueServices.AddManyEventTriggerOutputGroupSetupValueWithCustomData(
            eventTriggerOutputGroupingSetupValueArray)

        sceneForEventTriggerOutputSceneMappingRecords = db.Services.EventTriggerServices.FindEventTriggerWithCondition(
            db.Table.EventTriggerTable.c.EventTriggerId.in_(sceneIdForEventTriggerOutputSceneMappings))
        sceneForEventTriggerOutputSceneMappingArray = sceneForEventTriggerOutputSceneMappingRecords.fetchall()
        for scene in range(len(sceneForEventTriggerOutputSceneMappingArray)):
            eventTriggerOutputSceneMappingArray[scene]['SceneUnicastID'] = \
                sceneForEventTriggerOutputSceneMappingArray[scene]['SceneUnicastID']
        db.Services.EventTriggerOutputSceneMappingServices.AddManyEventTriggerOutputSceneMappingWithCustomDataType2(
            eventTriggerOutputSceneMappingArray)
