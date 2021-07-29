from Database.Db import Db
from Cache.GlobalVariables import GlobalVariables
from HcServices.Http import Http
import aiohttp
import asyncio
import Constant.Constant as const
import http
import json
import logging
from Helper.Terminal import Terminal


def noServerResponseErrorMessageCreate():
    data = {
        "CMD": "HC_PULL_DATA_STATUS",
        "DATA": {
            "STATUS": "FAIL"
        }
    }
    return json.dumps(data)


def noNetWorkConnectionErrorMessageCreate():
    data = {
        "CMD": "HC_PULL_DATA_STATUS",
        "DATA": {
            "STATUS": "FAIL"
        }
    }
    return json.dumps(data)


def pullSuccessMessageCreate():
    data = {
        "CMD": "HC_PULL_DATA_STATUS",
        "DATA": {
            "STATUS": "SUCCESS"
        }
    }
    return json.dumps(data)


class System:
    __db = Db()
    __globalVariables = GlobalVariables()
    __logger = logging.Logger
    
    def __init__(self, logger: logging.Logger):
        self.__logger = logger
        
    def StopOthersPythonProgramAndCronjob(self):
        t = Terminal()
        
        s = t.ExecuteWithResult(f'ps | grep python3 RDhcPy/main.py')
        dt = s[1].split(" ")
        otherPythonProgramPort = ""
        for i in range(len(dt)):
            if dt[i] != "":
                otherPythonProgramPort = dt[i]
                break
        s = t.Execute(f'kill -9 {otherPythonProgramPort}')

        s2 = t.Execute("/etc/init.d/cron stop")
        
    def StartCronjob(self):
        t = Terminal()
        t.Execute("/etc/init.d/cron start")

    def PingGoogle(self):
        t = Terminal()
        rel = t.ExecuteWithResult("ping -c3 www.google.com|grep packet")[1]
        try:
            rel2 = rel.split(", ")
            rel3 = rel2[2].split(" ")
            r = rel3[0] == "0%"
        except:
            r = False
        return r

    async def SendHttpRequestTotUrl(self, h: Http, url: str, body: dict):
        token = await self.__getToken(h)
        if token == "":
            self.__globalVariables.PullCloudErrorState = const.NO_SERVER_RESPONSE
            return None
        cookie = f"Token={token}"
        header = h.CreateNewHttpHeader(cookie = cookie, dormitoryId=self.__globalVariables.DormitoryId)
        req = h.CreateNewHttpRequest(url=url, header=header)
        session = aiohttp.ClientSession()
        res = await h.Post(session, req)
        await session.close()
        if res == "":
            self.__globalVariables.PullCloudErrorState = const.NO_SERVER_RESPONSE
            return None
        if (res != "") and (res.status == http.HTTPStatus.OK):
            print(res)
            try:
                data = await res.json()
                return data
            except:
                self.__globalVariables.PullCloudErrorState = const.NO_SERVER_RESPONSE
                return None
        
    async def __getToken(self, http: Http):
        refreshToken = self.__globalVariables.RefreshToken
        if refreshToken == "":
            return ""

        tokenUrl = const.SERVER_HOST + const.TOKEN_URL
        cookie = f"RefreshToken={refreshToken}"
        header = http.CreateNewHttpHeader(cookie = cookie, dormitoryId=self.__globalVariables.DormitoryId)
        req = http.CreateNewHttpRequest(url=tokenUrl, header=header)

        session = aiohttp.ClientSession()
        res = await http.Post(session, req)  
        token = ""
        if res != "":
            try:
                data = await res.json()
                token = data['token']
            except:
                self.__globalVariables.PullCloudErrorState = const.NO_SERVER_RESPONSE
                return ""
        await session.close()
        return token 
    
    def CreatePullStatusReportMessage(self, pullState: int):
        switcher = {
            const.NO_SERVER_RESPONSE: noServerResponseErrorMessageCreate,
            const.NO_NETWORK_CONNECTION: noNetWorkConnectionErrorMessageCreate,
            const.PULL_SUCCESS: pullSuccessMessageCreate
        }
        func = switcher.get(pullState)
        report_message = func()
        return report_message
