from Table.systemConfigurationTable import systemConfigurationTable
from Table.userDataTable import userDataTable
from Table.deviceAttributeValueTable import deviceAttributeValueTable
from Table.deviceTable import deviceTable
from Table.groupingTable import groupingTable
from Table.groupingDeviceMappingTable import groupingDeviceMappingTable
from Table.eventTriggerTable import eventTriggerTable
from Table.deviceAttributeTable import deviceAttributeTable
from Table.eventTriggerIDTable import eventTriggerIDTable
from Table.groupIdTable import groupIDTable
from Table.eventTriggerTypeTable import eventTriggerTypeTable
from Table.eventTriggerInputDeviceMappingTable import eventTriggerInputDeviceMappingTable
from Table.eventTriggerInputDeviceSetupVaueTable import eventTriggerInputDeviceSetupValueTable
from Table.eventTriggerInputGroupingMappingTable import eventTriggerInputGroupingMappingTable
from Table.eventTriggerOutputDeviceMappingTable import eventTriggerOutputDeviceMappingTable
from Table.eventTriggerOutputDeviceSetupValueTable import eventTriggerOutputDeviceSetupValueTable
from Table.eventTriggerOutputGroupingMappingTable import eventTriggerOutputGroupingMappingTable
from Table.eventTriggerOutputGroupingSetupValueTable import eventTriggerOutputGroupingSetupValueTable
from Table.eventTriggerOutputSceneMappingTable import eventTriggerOutputSceneMappingTable
from Table.irDeviceAttributeValueTable import irDeviceAttributeValueTable
from sqlalchemy import MetaData


class tableManager:
    __systemConfigurationTable: systemConfigurationTable
    __userDataTable: userDataTable
    __deviceAttributeTable: deviceAttributeValueTable
    __deviceTable: deviceTable
    __groupingTable: groupingTable
    __groupingDeviceMappingTable: groupingDeviceMappingTable
    __eventTriggerTable: eventTriggerTable
    __deviceAttributeTable: deviceAttributeTable
    __eventTriggerIDTable: eventTriggerIDTable
    __groupIdTable: groupIDTable
    __eventTriggerTypeTable: eventTriggerTypeTable
    __eventTriggerInputDeviceMappingTable: eventTriggerInputDeviceMappingTable
    __eventTriggerInputDeviceSetupValueTable: eventTriggerInputDeviceSetupValueTable
    __eventTriggerInputGroupingMappingTable: eventTriggerInputGroupingMappingTable
    __eventTriggerOutputDeviceMappingTable: eventTriggerOutputDeviceMappingTable
    __eventTriggerOutputDeviceSetupValueTable: eventTriggerOutputDeviceSetupValueTable
    __eventTriggerOutputGroupingMappingTable: eventTriggerOutputGroupingMappingTable
    __eventTriggerOutputGroupingSetupValueTable: eventTriggerOutputGroupingSetupValueTable
    __eventTriggerOutputSceneMappingTable: eventTriggerOutputSceneMappingTable
    __irDeviceAttributeValueTable: irDeviceAttributeValueTable

    def __init__(self, metadata: MetaData):
        self.__systemConfigurationTable = systemConfigurationTable(metadata)
        self.__userDataTable = userDataTable(metadata)
        self.__deviceAttributeValueTable = deviceAttributeValueTable(metadata)
        self.__deviceTable = deviceTable(metadata)
        self.__groupingTable = groupingTable(metadata)
        self.__groupingDeviceMappingTable = groupingDeviceMappingTable(metadata)
        self.__eventTriggerTable = eventTriggerTable(metadata)
        self.__deviceAttributeTable = deviceAttributeTable(metadata)
        self.__groupIdTable = groupIDTable(metadata)
        self.__eventTriggerTypeTable = eventTriggerTypeTable(metadata)
        self.__eventTriggerIDTable = eventTriggerIDTable(metadata)
        self.__eventTriggerInputDeviceMappingTable = eventTriggerInputDeviceMappingTable(metadata)
        self.__eventTriggerInputDeviceSetupValueTable = eventTriggerInputDeviceSetupValueTable(metadata)
        self.__eventTriggerInputGroupingMappingTable = eventTriggerInputGroupingMappingTable(metadata)
        self.__eventTriggerOutputDeviceMappingTable = eventTriggerOutputDeviceMappingTable(metadata)
        self.__eventTriggerOutputDeviceSetupValueTable = eventTriggerOutputDeviceSetupValueTable(metadata)
        self.__eventTriggerOutputGroupingMappingTable = eventTriggerOutputGroupingMappingTable(metadata)
        self.__eventTriggerOutputGroupingSetupValueTable = eventTriggerOutputGroupingSetupValueTable(metadata)
        self.__eventTriggerOutputSceneMappingTable = eventTriggerOutputSceneMappingTable(metadata)
        self.__irDeviceAttributeValueTable = irDeviceAttributeValueTable(metadata)

    @property
    def IrDeviceAttributeValueTable(self):
        return self.__irDeviceAttributeValueTable.irDeviceAttributeValueTable

    @property
    def EventTriggerInputDeviceMappingTable(self):
        return self.__eventTriggerInputDeviceMappingTable.eventTriggerInputDeviceMappingTable

    @property
    def EventTriggerInputDeviceSetupValueTable(self):
        return self.__eventTriggerInputDeviceSetupValueTable.eventTriggerInputDeviceSetupValueTable

    @property
    def EventTriggerInputGroupingMappingTable(self):
        return self.__eventTriggerInputGroupingMappingTable.eventTriggerInputGroupingMappingTable

    @property
    def EventTriggerOutputDeviceMappingTable(self):
        return self.__eventTriggerOutputDeviceMappingTable.eventTriggerOutputDeviceMappingTable

    @property
    def EventTriggerOutputDeviceSetupValueTable(self):
        return self.__eventTriggerOutputDeviceSetupValueTable.eventTriggerOutputDeviceSetupValueTable

    @property
    def EventTriggerOutputGroupingSetupValueTable(self):
        return self.__eventTriggerOutputGroupingSetupValueTable.eventTriggerOutputGroupingSetupValueTable

    @property
    def EventTriggerOutputGroupingMappingTable(self):
        return self.__eventTriggerOutputGroupingMappingTable.eventTriggerOutputGroupingMappingTable

    @property
    def EventTriggerOutputSceneMappingTable(self):
        return self.__eventTriggerOutputSceneMappingTable.eventTriggerOutputSceneMappingTable

    @property
    def EventTriggerIdTable(self):
        return self.__eventTriggerIDTable.eventTriggerIDTable

    @property
    def DeviceAttributeTable(self):
        return self.__deviceAttributeTable.deviceAttributeTable

    @property
    def GroupIdTable(self):
        return self.__groupIdTable.groupIDTable

    @property
    def EventTriggerTypeTable(self):
        return self.__eventTriggerTypeTable.eventTriggerTypeTable

    @property
    def EventTriggerTable(self):
        return self.__eventTriggerTable.eventTriggerTable

    @property
    def GroupingDeviceMappingTable(self):
        return self.__groupingDeviceMappingTable.groupingDeviceMappingTable

    @property
    def DeviceAttributeValueTable(self):
        return self.__deviceAttributeValueTable.deviceAttributeValueTable

    @property
    def SystemConfigurationTable(self):
        return self.__systemConfigurationTable.systemConfigurationTable

    @property
    def UserDataTable(self):
        return self.__userDataTable.userDataTable

    @property
    def DeviceTable(self):
        return self.__deviceTable.deviceTable

    @property
    def GroupingTable(self):
        return self.__groupingTable.groupingTable
