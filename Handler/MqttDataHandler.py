from Constract.Ihandler import Ihandler
import asyncio
import logging
from HcServices.Mqtt import Mqtt
from Constract.Itransport import Itransport
from Cache.Cache import Cache
import Constant.Constant as const
import json
from Database.Db import Db
from Model.systemConfiguration import systemConfiguration
from Model.userData import userData

class MqttDataHandler(Ihandler):
    __logger: logging.Logger
    __mqtt: Itransport
    __db: Db
    __cache : Cache
    
    def __init__(self, log: logging.Logger, mqtt: Itransport):
        self.__logger = log
        self.__mqtt = mqtt
        self.__db = Db()
        self.__cache = Cache()
        
    def Handler(self, item):
        switcher = {
            const.MQTT_CONTROL_TOPIC: self.__handlerTopicHcControl
        }
        func = switcher.get(item["topic"])
        func(item["msg"])
        return
       
    def __handlerTopicHcControl(self, data):
        print("data from topic HC.CONTROL: " + data)
        self.__logger.debug("data from topic HC.CONTROL: " + data)
        
        try:
            dt = json.loads(data)
            try:
                cmd = dt["CMD"]
                data = dt["DATA"]
                switcher = {
                    "HC_CONNECT_TO_CLOUD": self.__handlerCmdHcConnectToCloud
                }
                func = switcher.get(cmd)
                func(data)
            except:
                self.__logger.error("mqtt data receiver in topic HC.CONTROL invalid")
        except:
            self.__logger.error("mqtt data receiver in topic HC.CONTROL invalid")
          
    def __handlerCmdHcConnectToCloud(self, data):
        try:
            endUserProfileId = data["END_USER_PROFILE_ID"]
            refreshToken = data["REFRESH_TOKEN"]
            self.__cache.EndUserId = str(endUserProfileId)
            self.__cache.RefreshToken = refreshToken
            userDt = userData(refreshToken=refreshToken, endUserProfileId=str(endUserProfileId))
            rel = self.__db.Services.UserdataServices.FindUserDataById(id = 1)
            dt = rel.first()
            if dt != None:
                self.__db.Services.UserdataServices.UpdateUserDataById(id = 1, newUserData=userDt)
            if dt == None:
                self.__db.Services.UserdataServices.AddNewUserData(newUserData=userDt)
        except:
            self.__logger.error("data of cmd HcConnectToCLoud invalid")
            print("data of cmd HcConnectToCLoud invalid")