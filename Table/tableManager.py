from Table.systemConfigurationTable import systemConfigurationTable
from Table.userDataTable import userDataTable
from Table.deviceAttributeValueTable import deviceAttributeValueTable
from Table.deviceTable import deviceTable
from Table.groupingTable import groupingTable
from Table.groupingDeviceMappingTable import groupingDeviceMappingTable

from sqlalchemy import MetaData

class tableManager():
    __systemConfigurationTable: systemConfigurationTable
    __userDataTable: userDataTable
    __deviceAttributeTable: deviceAttributeValueTable
    __deviceTable: deviceTable
    __groupingTable: groupingTable
    __groupingDeviceMapping: groupingDeviceMappingTable
    
    def __init__(self, metadata: MetaData):
        self.__systemConfigurationTable = systemConfigurationTable(metadata)
        self.__userDataTable = userDataTable(metadata)
        self.__deviceAttributeTable = deviceAttributeValueTable(metadata)
        self.__deviceTable = deviceTable(metadata)
        self.__groupingTable = groupingTable(metadata)
        self.__groupingDeviceMapping = groupingDeviceMappingTable(metadata)
    
    @property
    def GroupingDeviceMappingTable(self):
        return self.__groupingDeviceMapping.groupingDeviceMappingTable
        
    @property 
    def DeviceAttributeValueTable(self):
        return self.__deviceAttributeTable.deviceAttributeValueTable
        
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