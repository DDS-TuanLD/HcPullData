import asyncio
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import datetime
import time

class userData():
    __id: int
    __refreshToken: str
    __dormitoryId: str
    
    def __init__(self, refreshToken: str, dormitoryId: str):
       self.__refreshToken = refreshToken
       self.__dormitoryId = dormitoryId
       
    @property
    def RefreshToken(self):
        return self.__refreshToken
    
    @RefreshToken.setter
    def RefreshToken(self, refreshToken: str):
        self.__refreshToken = refreshToken
        
    @property
    def DormitoryId(self):
        return self.__dormitoryId
    
    @DormitoryId.setter
    def DormitoryId(self, dormitoryId: str):
        self.__dormitoryId = dormitoryId