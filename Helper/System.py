from Database.Db import Db
from Model.systemConfiguration import systemConfiguration
from Cache.Cache import Cache
import datetime
from HcServices.Http import Http
from sqlalchemy import and_, or_
from HcServices.Http import Http
import aiohttp
import asyncio
import Constant.Constant as const
import http
import json
import logging

class System():
    __db=Db()
    __cache=Cache()
    __logger = logging.Logger
    
    def __init__(self, logger: logging.Logger):
        self.__logger = logger
        
    async def SendHttpRequestTotUrl(self, h: Http, url: str, body: dict):
        endUser = self.__cache.EndUserId
        token = await self.__getToken(h) 
        cookie = f"Token={token}"
        header = h.CreateNewHttpHeader(cookie = cookie, endProfileId=self.__cache.EndUserId)
        req = h.CreateNewHttpRequest(url=url, header=header)
        session = aiohttp.ClientSession()
        res = await h.Post(session, req)
        await session.close()
        if res == "":
            return None
        if (res != "") and (res.status == http.HTTPStatus.OK):
            print(res)
            try:
                data = await res.json()
                return data
            except:
                return None
        
    async def __getToken(self, http: Http):
        refreshToken = self.__cache.RefreshToken
        if refreshToken == "":
            return ""
        tokenUrl = const.SERVER_HOST + const.TOKEN_URL
        cookie = f"RefreshToken={refreshToken}"
        header = http.CreateNewHttpHeader(cookie = cookie, endProfileId=self.__cache.EndUserId)
        req = http.CreateNewHttpRequest(url=tokenUrl, header=header)
        session = aiohttp.ClientSession()
        res = await http.Post(session, req)  
        token = ""
        if res != "":
            try:
                data = await res.json()
                token = data['token']
            except:
                return ""
        await session.close()
        return token 