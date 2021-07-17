from HcServices.Http import Http
import asyncio
from Database.Db import Db
import aiohttp
from Cache.GlobalVariables import GlobalVariables
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
from PullHandler.ScenePullHandler import ScenePullHandler
from Handler.MqttDataHandler import MqttDataHandler
from HcServices.Mqtt import Mqtt
from Constract.Itransport import Itransport
from HcServices.Led import Led
from Helper.System import System

class RdHc():
    __httpServices: Http
    __db: Db
    __globalVariables: GlobalVariables
    __lock: threading.Lock
    __logger: logging.Logger
    __mqttServices: Itransport
    __ledService: Led
    __mqttHandler: MqttDataHandler
    
    __devicePullHandler: Ipull
    __groupingPullHandler: Ipull
    __rulePullHandler: Ipull
    __scenePullHandler: Ipull
 
    def __init__(self, log: logging.Logger):
        self.__logger = log
        self.__httpServices = Http()
        self.__db = Db()
        self.__globalVariables = GlobalVariables()
        self.__lock = threading.Lock()
        self.__mqttServices = Mqtt(self.__logger)
        self.__ledService = Led()
        self.__mqttHandler = MqttDataHandler(self.__logger, self.__mqttServices)
        self.__devicePullHandler = DevicePullHandler(self.__logger, self.__httpServices)
        self.__groupingPullHandler = GroupingPullHandler(self.__logger, self.__httpServices)
        self.__rulePullHandler = RulePullHandler(self.__logger, self.__httpServices)
        self.__scenePullHandler = ScenePullHandler(self.__logger, self.__httpServices)
    
    def __HcCheckInternetConnection(self):
        s = System(self.__logger)
        if not s.PingGoogle():
            report_message = s.CreatePullStatusReportMessage(const.NO_NETWORK_CONNECTION)
            self.__mqttServices.Send(const.MQTT_RESPONSE_TOPIC, report_message, const.MQTT_QOS)
            time.sleep(2)
            exit()
        return
    
    async def __HcHandlerMqttData(self):
        """ This function handler data received in queue
        """
        while True:
            await asyncio.sleep(0.1)
            if not self.__mqttServices.mqttDataQueue.empty():
                with self.__lock:
                    item = self.__mqttServices.mqttDataQueue.get()
                    self.__mqttHandler.Handler(item)
                    self.__mqttServices.mqttDataQueue.task_done()
                if self.__globalVariables.EndUserId != "" and self.__globalVariables.RefreshToken != "":
                    return

    async def __HcReportPullCloudStatus(self):
        s = System(self.__logger)
        while True:
            await asyncio.sleep(2)
            if self.__globalVariables.NumberOfPullApiSuccess == 4:
                report_message = s.CreatePullStatusReportMessage(const.PULL_SUCCESS)
                self.__mqttServices.Send(const.MQTT_RESPONSE_TOPIC, report_message, const.MQTT_QOS)
                await asyncio.sleep(2)
                exit()
            if self.__globalVariables.PullCloudErrorState != 0:
                report_message = s.CreatePullStatusReportMessage(self.__globalVariables.PullCloudErrorState)
                self.__mqttServices.Send(const.MQTT_RESPONSE_TOPIC, report_message, const.MQTT_QOS)
                await asyncio.sleep(2)
                exit()

    async def __HcDevicePullHandler(self):
        while self.__globalVariables.EndUserId == "" or self.__globalVariables.RefreshToken == "":
            await asyncio.sleep(1)
        
        self.__ledService.ServiceLedControl.On()
        await self.__devicePullHandler.PullAndSave()
    
        self.__groupingPullHandler.DeExhibit()
        self.__scenePullHandler.DeExhibit()
    
    async def __HcGroupingPullHandler(self):
        while self.__groupingPullHandler.IsInExhibitState() != False:
            await asyncio.sleep(1)  
        await self.__groupingPullHandler.PullAndSave()
        
    async def __HcRulePullHandler(self):
        while self.__rulePullHandler.IsInExhibitState() != False:
            await asyncio.sleep(1)
        await self.__rulePullHandler.PullAndSave()
        
    async def __HcScenePullHandler(self):
        while self.__scenePullHandler.IsInExhibitState() != False:
            await asyncio.sleep(1)  
        await self.__scenePullHandler.PullAndSave()
        self.__rulePullHandler.DeExhibit()

    async def Run(self):
        
        s = System(self.__logger)
        #s.StopOthersPythonProgramAndCronjob()
        self.__mqttServices.Init()
        #self.__HcCheckInternetConnection()
        task1 = asyncio.create_task(self.__HcHandlerMqttData())
        task2 = asyncio.create_task(self.__HcDevicePullHandler())
        task3 = asyncio.create_task(self.__HcGroupingPullHandler())
        task4 = asyncio.create_task(self.__HcRulePullHandler())
        task5 = asyncio.create_task(self.__HcScenePullHandler())
        task6 = asyncio.create_task(self.__HcReportPullCloudStatus())
        tasks = [task1, task2, task3, task4, task5, task6]
        await asyncio.gather(*tasks)
        
        #self.__ledService.ServiceLedControl.Off()
        #s.StartCronjob()
        
        return

        
        
   