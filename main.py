from Controller.RdHc import RdHc
import asyncio
from Database.Db import Db
import logging
from logging.handlers import TimedRotatingFileHandler
from HcServices.Led import Led
from HcServices.Http import Http
from HcServices.Mqtt import Mqtt
from Handler.MqttDataHandler import MqttDataHandler
from PullHandler.DevicePullHandler import DevicePullHandler
from PullHandler.GroupingPullHandler import GroupingPullHandler
from PullHandler.RulePullHandler import RulePullHandler
from PullHandler.ScenePullHandler import ScenePullHandler
import os


d = os.path.dirname(__file__)

loghandler = logging.handlers.TimedRotatingFileHandler(filename=d + '/Logging/runtime.log', when="D", backupCount=4)
logfomatter = logging.Formatter(fmt=(
                                                    '%(asctime)s:\t'
                                                    '%(levelname)s:\t'
                                                    '%(filename)s:'
                                                    '%(funcName)s():'
                                                    '%(lineno)d\t'
                                                    '%(message)s'
                                                ))
logger = logging.getLogger("mylog")
loghandler.setFormatter(logfomatter)
logger.addHandler(loghandler)
logger.setLevel(logging.DEBUG)

mqtt = Mqtt(logger)
http = Http()
led = Led()
mqttDataHandler = MqttDataHandler(logger, mqtt)
devicePullHandler = DevicePullHandler(logger, http)
groupingPullHandler = GroupingPullHandler(logger, http)
rulePullHandler = RulePullHandler(logger, http)
scenePullHandler = ScenePullHandler(logger, http)

db = Db()
hc = RdHc(logger, http, mqtt, led, mqttDataHandler, devicePullHandler, groupingPullHandler, rulePullHandler,
          scenePullHandler)


async def main():
    db.Init()
    await hc.Run()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
