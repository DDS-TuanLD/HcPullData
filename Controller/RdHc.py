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
from PullHandler.GroupingPullHandler import GroupingPullHandler
from PullHandler.RulePullHandler import RulePullHandler
from Handler.MqttDataHandler import MqttDataHandler
from HcServices.Mqtt import Mqtt
from Constract.Itransport import Itransport

class RdHc():
    __httpServices: Http
    __db: Db
    __cache : Cache
    __lock: threading.Lock
    __logger: logging.Logger
    __mqttServices: Itransport
    __mqttHandler: MqttDataHandler
    __devicePullHandler: Ipull
    __groupingPullHandler: Ipull
    __rulePullHandler: Ipull
 
    def __init__(self, log: logging.Logger):
        self.__logger = log
        self.__httpServices = Http()
        self.__db = Db()
        self.__cache = Cache()
        self.__lock = threading.Lock()
        self.__mqttServices = Mqtt(self.__logger)
        self.__mqttHandler =  MqttDataHandler(self.__logger, self.__mqttServices)
        self.__devicePullHandler = DevicePullHandler(self.__logger, self.__httpServices)
        self.__groupingPullHandler = GroupingPullHandler(self.__logger, self.__httpServices)
        self.__rulePullHandler = RulePullHandler(self.__logger, self.__httpServices)
     
    async def __HcHandlerMqttData(self):
        """ This function handler data received in queue
        """
        while True:
            await asyncio.sleep(0.1)
            if self.__mqttServices.mqttDataQueue.empty() == False:
                with self.__lock:
                    item = self.__mqttServices.mqttDataQueue.get()
                    self.__mqttHandler.Handler(item)
                    self.__mqttServices.mqttDataQueue.task_done()
                if self.__cache.EndUserId != "" and self.__cache.RefreshToken != "":
                    return
         
    async def __HcDevicePullHandler(self):
        while self.__cache.EndUserId == "" or self.__cache.RefreshToken == "":
            await asyncio.sleep(1)
        await self.__devicePullHandler.PullAndSave()
        self.__groupingPullHandler.DeExhibit()
    
    async def __HcGroupingPullHandler(self):
        while self.__groupingPullHandler.ExhibitStatus() != False:
            await asyncio.sleep(1)  
        await self.__groupingPullHandler.PullAndSave()
        
    async def __HcRulePullHandler(self):
        # while self.__cache.EndUserId == "" or self.__cache.RefreshToken == "":
        #     await asyncio.sleep(1)
        await self.__rulePullHandler.PullAndSave()
                    
    async def Run(self):
        #await self.__mqttServices.Init()
        #task1 = asyncio.ensure_future(self.__HcHandlerMqttData())     
        # task2 = asyncio.ensure_future(self.__HcDevicePullHandler())
        # task3 = asyncio.ensure_future(self.__HcGroupingPullHandler())
        task4 = asyncio.ensure_future(self.__HcRulePullHandler())

        tasks = [task4]
        await asyncio.gather(*tasks)
        return

        
        
   