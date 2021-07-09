import asyncio
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import datetime
import time

class device():
    __deviceId: int
    __deviceUnicastId: int
    __appKey: str
    __netKey: str
    __deviceKey: str
    __deviceTypeId: int
    __updateDay: int
    __updateTime: int
    __statusId: int
    __owner: int
    
    def __init__(self, deviceId: int, deviceUnicastId: int, appKey: str, netKey: str, deviceKey: str, deviceTypeId: int, 
                 updateDay: int, updateTime: int, statusId: int, owner: int):
        self.__deviceId: deviceId
        self.__deviceUnicastId: deviceUnicastId
        self.__appKey: appKey
        self.__netKey: netKey
        self.__deviceKey: deviceKey
        self.__deviceTypeId: deviceTypeId
        self.__updateDay: updateDay
        self.__updateTime: updateTime
        self.__statusId: statusId
        self.__owner: owner
        
    @property
    def DeviceId(self):
        return self.__deviceId
    
    @DeviceId.setter
    def DeviceId(self, deviceId: int):
        self.__deviceId = deviceId
        
    @property
    def DeviceUnicastId(self):
        return self.__deviceUnicastId
    
    @DeviceUnicastId.setter
    def DeviceUnicastId(self, deviceUnicastId: int):
        self.__deviceUnicastId = deviceUnicastId
        
    @property
    def AppKey(self):
        return self.__appKey
    
    @AppKey.setter
    def AppKey(self, apppKey: str):
        self.__appKey = apppKey
        
    @property
    def NetKey(self):
        return self.__netKey
    
    @NetKey.setter
    def NetKey(self, netKey: str):
        self.__netKey = netKey
        
    @property
    def DeviceKey(self):
        return self.__deviceKey
    
    @DeviceKey.setter
    def DeviceKey(self, deviceKey: str):
        self.__deviceKey = deviceKey
        
    @property
    def DeviceTypeId(self):
        return self.__deviceTypeId
    
    @DeviceTypeId.setter
    def DeviceTypeId(self, deviceTypeId: int):
        self.__deviceTypeId = deviceTypeId
        
    @property
    def UpdateDay(self):
        return self.__updateDay
    
    @UpdateDay.setter
    def UpdateDay(self, updateDay: int):
        self.__updateDay = updateDay
        
    @property
    def UpdateTime(self):
        return self.__updateTime
    
    @UpdateTime.setter
    def UpdateTime(self, updateTime: int):
        self.__updateTime = updateTime
        
    @property
    def StatusId(self):
        return self.__statusId
    
    @StatusId.setter
    def StatusId(self, statusId: int):
        self.__statusId = statusId
        
    @property
    def Owner(self):
        return self.__owner
    
    @Owner.setter
    def Owner(self, owner: int):
        self.__owner = owner
        


      