from HcServices.Http import Http
import asyncio
from Cache.GlobalVariables import GlobalVariables
import Constant.Constant as const
import time
import logging
import threading
from Constract.IPull import IPull
from Constract.IHandler import IHandler
from HcServices.Mqtt import Mqtt
from Constract.ITransport import ITransport
from HcServices.Led import Led
from Helper.System import System


class RdHc:
    __httpServices: Http
    __globalVariables: GlobalVariables
    __lock: threading.Lock
    __logger: logging.Logger
    __mqttServices: ITransport
    __ledService: Led
    __mqttHandler: IHandler
    
    __devicePullHandler: IPull
    __groupingPullHandler: IPull
    __rulePullHandler: IPull
    __scenePullHandler: IPull
 
    def __init__(self, log: logging.Logger, http: Http, mqtt: Mqtt, led: Led, mqttDataHandler: IHandler,
                 devicePullHandler: IPull, groupPullHandler: IPull, rulePullHandler: IPull, scenePullHandler: IPull):
        self.__logger = log
        self.__httpServices = http
        self.__globalVariables = GlobalVariables()
        self.__lock = threading.Lock()
        self.__mqttServices = mqtt
        self.__ledService = led
        self.__mqttHandler = mqttDataHandler
        self.__devicePullHandler = devicePullHandler
        self.__groupingPullHandler = groupPullHandler
        self.__rulePullHandler = rulePullHandler
        self.__scenePullHandler = scenePullHandler
    
    def __HcCheckInternetConnection(self):
        s = System(self.__logger)
        if not s.PingGoogle():
            report_message = s.CreatePullStatusReportMessage(const.NO_NETWORK_CONNECTION)
            self.__mqttServices.send(const.MQTT_RESPONSE_TOPIC, report_message)
            time.sleep(2)
            exit()
        return
    
    async def __HcHandlerMqttData(self):
        while True:
            await asyncio.sleep(0.1)
            if not self.__mqttServices.receive_data_queue.empty():
                with self.__lock:
                    item = self.__mqttServices.receive_data_queue.get()
                    self.__mqttHandler.handler(item)
                    self.__mqttServices.receive_data_queue.task_done()
                if self.__globalVariables.EndUserId != "" and self.__globalVariables.RefreshToken != "":
                    return

    async def __HcReportPullCloudStatus(self):
        s = System(self.__logger)
        while True:
            await asyncio.sleep(2)
            if self.__globalVariables.NumberOfPullApiSuccess == 4:
                report_message = s.CreatePullStatusReportMessage(const.PULL_SUCCESS)
                self.__mqttServices.send(const.MQTT_RESPONSE_TOPIC, report_message)
                await asyncio.sleep(2)
                exit()
            if self.__globalVariables.PullCloudErrorState != 0:
                report_message = s.CreatePullStatusReportMessage(self.__globalVariables.PullCloudErrorState)
                self.__mqttServices.send(const.MQTT_RESPONSE_TOPIC, report_message)
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
        while self.__groupingPullHandler.IsInExhibitState():
            await asyncio.sleep(1)  
        await self.__groupingPullHandler.PullAndSave()
        
    async def __HcRulePullHandler(self):
        while self.__rulePullHandler.IsInExhibitState():
            await asyncio.sleep(1)
        await self.__rulePullHandler.PullAndSave()
        
    async def __HcScenePullHandler(self):
        while self.__scenePullHandler.IsInExhibitState():
            await asyncio.sleep(1)  
        await self.__scenePullHandler.PullAndSave()
        self.__rulePullHandler.DeExhibit()

    async def Run(self):
        
        s = System(self.__logger)
        #s.StopOthersPythonProgramAndCronjob()
        self.__mqttServices.connect()
        self.__HcCheckInternetConnection()
        task1 = asyncio.create_task(self.__HcHandlerMqttData())
        task2 = asyncio.create_task(self.__HcDevicePullHandler())
        task3 = asyncio.create_task(self.__HcGroupingPullHandler())
        task4 = asyncio.create_task(self.__HcRulePullHandler())
        task5 = asyncio.create_task(self.__HcScenePullHandler())
        task6 = asyncio.create_task(self.__HcReportPullCloudStatus())
        tasks = [task1, task2, task3, task4, task5, task6]
        await asyncio.gather(*tasks)
        
        self.__ledService.ServiceLedControl.Off()
        #s.StartCronjob()
        
        return

        
        
   