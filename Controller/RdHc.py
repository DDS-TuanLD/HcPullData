from HcServices.Http import Http

import asyncio
from Database.Db import Db
import aiohttp
from Cache.Cache import Cache
import Constant.Constant as const
import datetime
from Model.systemConfiguration import systemConfiguration
import time
from Model.userData import userData
import logging
import threading
import http
import json
from Constract.Ipull import Ipull
from PullHandler.DevicePullHandler import DevicePullHandler

class RdHc():
    __httpServices: Http
    __db: Db
    __cache : Cache
    __lock: threading.Lock
    __logger: logging.Logger
    __devicePullHandler: Ipull
 
    def __init__(self, log: logging.Logger):
        self.__logger = log
        self.__httpServices = Http()
        self.__db = Db()
        self.__cache = Cache()
        self.__lock = threading.Lock()
        self.__devicePullHandler = DevicePullHandler(self.__logger, self.__httpServices)
      
    #-----------load userdata from db----------------------------------------------------------
    def __HcLoadUserData(self):
        userData = self.__db.Services.UserdataServices.FindUserDataById(id=1)
        dt = userData.first()
        if dt != None:
            self.__cache.EndUserId = dt["EndUserProfileId"]
            self.__cache.RefreshToken = dt["RefreshToken"]  
      
    async def Run(self):
        self.__HcLoadUserData()
        task1 = asyncio.ensure_future(self.__devicePullHandler.PullAndSave())
        tasks = [task1]
        await asyncio.gather(*tasks)
        return

        
        
   