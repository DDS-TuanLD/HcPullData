from ModelServices.systemConfigurationServices import systemConfigurationServices
from ModelServices.userDataService import userDataServices
from ModelServices.deviceAttributeValueServices import deviceAttributeValueServices
from ModelServices.deviceService import deviceServices
from ModelServices.groupingService import groupingServices
from ModelServices.groupingDeviceMappingServices import groupingDeviceMappingServices
from ModelServices.deviceAttributeServices import deviceAttributeServices
from ModelServices.groupIdServices import groupIdServices
from ModelServices.eventTriggerServices import eventTriggerServices
from ModelServices.eventTriggerIdServices import eventTriggerIdServices
from ModelServices.eventTriggerTypeServices import eventTriggerTypeServices
from ModelServices.eventTriggerInputDeviceMappingServices import eventTriggerInputDeviceMappingServices
from ModelServices.eventTriggerInputDeviceSetupValueServices import eventTriggerInputDeviceSetupValueServices
from ModelServices.eventTriggerInputGroupingMappingServices import eventTriggerInputGroupingMappingServices
from ModelServices.eventTriggerOutputDeviceMappingServices import eventTriggerOutputDeviceMappingServices
from ModelServices.eventTriggerOutputDeviceSetupValueServices import eventTriggerOutputDeviceSetupValueServices
from ModelServices.eventTriggerOutputGroupingMappingServices import eventTriggerOutputGroupingMappingServices
from ModelServices.eventTriggerOutputGroupingSetupValueServices import eventTriggerOutputGroupingSetupValueServices
from ModelServices.eventTriggerOutputSceneMappingServices import eventTriggerOutputSceneMappingServices
from ModelServices.irDeviceAttributeValueServices import irDeviceAttributeValueServices
from Table.tableManager import tableManager
from sqlalchemy.engine.base import Connection


class modelServicesManager:

    def __init__(self, table: tableManager, context: Connection):
        self.__systemConfigurationServices = systemConfigurationServices(table.SystemConfigurationTable, context)
        self.__userDataService = userDataServices(table.UserDataTable, context)
        self.__deviceAttributeValueService = deviceAttributeValueServices(table.DeviceAttributeValueTable, context)
        self.__deviceService = deviceServices(table.DeviceTable, context)
        self.__groupingService = groupingServices(table.GroupingTable, context)
        self.__groupingDeviceMappingService = groupingDeviceMappingServices(table.GroupingDeviceMappingTable, context)
        self.__deviceAttributeService = deviceAttributeServices(table.DeviceAttributeTable, context)
        self.__groupIdService = groupIdServices(table.GroupIdTable, context)
        self.__eventTriggerService = eventTriggerServices(table.EventTriggerTable, context)
        self.__eventTriggerIdService = eventTriggerIdServices(table.EventTriggerIdTable, context)
        self.__eventTriggerTypeService = eventTriggerTypeServices(table.EventTriggerTypeTable, context)
        self.__eventTriggerInputDeviceMappingService = \
            eventTriggerInputDeviceMappingServices(table.EventTriggerInputDeviceMappingTable, context)
        self.__eventTriggerInputDeviceSetupValueService = \
            eventTriggerInputDeviceSetupValueServices(table.EventTriggerInputDeviceSetupValueTable, context)
        self.__eventTriggerInputGroupingMappingService = \
            eventTriggerInputGroupingMappingServices(table.EventTriggerInputGroupingMappingTable, context)
        self.__eventTriggerOutputDeviceMappingService = \
            eventTriggerOutputDeviceMappingServices(table.EventTriggerOutputDeviceMappingTable, context)
        self.__eventTriggerOutputDeviceSetupValueService = \
            eventTriggerOutputDeviceSetupValueServices(table.EventTriggerOutputDeviceSetupValueTable, context)
        self.__eventTriggerOutputGroupingMappingServices = \
            eventTriggerOutputGroupingMappingServices(table.EventTriggerOutputGroupingMappingTable, context)
        self.__eventTriggerOutputGroupingSetupValueService = \
            eventTriggerOutputGroupingSetupValueServices(table.EventTriggerOutputGroupingSetupValueTable, context)
        self.__eventTriggerOutputSceneMappingService = \
            eventTriggerOutputSceneMappingServices(table.EventTriggerOutputSceneMappingTable, context)
        self.__irDeviceAttributeValueService = \
            irDeviceAttributeValueServices(table.IrDeviceAttributeValueTable, context)

    @property
    def IrDeviceAttributeValueServices(self):
        return self.__irDeviceAttributeValueService

    @property
    def EventTriggerInputDeviceMappingServices(self):
        return self.__eventTriggerInputDeviceMappingService
    
    @property
    def EventTriggerInputDeviceSetupValueServices(self):
        return self.__eventTriggerInputDeviceSetupValueService
    
    @property
    def EventTriggerInputGroupMappingServices(self):
        return self.__eventTriggerInputGroupingMappingService
    
    @property
    def EventTriggerOutputDeviceMappingServices(self):
        return self.__eventTriggerOutputDeviceMappingService
    
    @property
    def EventTriggerOutputDeviceSetupValueServices(self):
        return self.__eventTriggerOutputDeviceSetupValueService
    
    @property
    def EventTriggerOutputGroupingMappingServices(self):
        return self.__eventTriggerOutputGroupingMappingServices
    
    @property
    def EventTriggerOutputGroupingSetupValueServices(self):
        return self.__eventTriggerOutputGroupingSetupValueService
    
    @property
    def EventTriggerOutputSceneMappingServices(self):
        return self.__eventTriggerOutputSceneMappingService
    
    @property
    def DeviceAttributeServices(self):
        return self.__deviceAttributeService
    
    @property
    def GroupIdServices(self):
        return self.__groupIdService
    
    @property
    def EventTriggerServices(self):
        return self.__eventTriggerService
    
    @property
    def EventTriggerIdServices(self):
        return self.__eventTriggerIdService
    
    @property
    def EventTriggerTypeServices(self):
        return self.__eventTriggerTypeService
    
    @property
    def GroupingDeviceMappingServices(self):
        return self.__groupingDeviceMappingService
        
    @property
    def GroupingServices(self):
        return self.__groupingService
        
    @property
    def SystemConfigurationServices(self):
        return self.__systemConfigurationServices
    
    @property
    def UserdataServices(self):
        return self.__userDataService
    
    @property
    def DeviceAttributeValueServices(self):
        return self.__deviceAttributeValueService
    
    @property
    def DeviceServices(self):
        return self.__deviceService
    