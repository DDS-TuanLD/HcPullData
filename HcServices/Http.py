import Constant.Constant as const
from requests.exceptions import HTTPError
from requests.structures import CaseInsensitiveDict
import asyncio
import aiohttp
import logging
class HttpRequest():
    __header: CaseInsensitiveDict
    __body: dict
    __url: str
    __cookie: dict
    
    @property
    def Body(self):
        return self.__body
    
    @property
    def Header(self):
        return self.__header
    
    @property 
    def Url(self):
        return self.__url

    @Header.setter
    def Header(self, header: CaseInsensitiveDict):
        self.__header = header
        return self
    
    @Body.setter
    def Body(self, body: dict):
        self.__body = body
        return self
    
    @Url.setter
    def Url(self, url: str):
        self.__url = url
        return self
class Http():
    
    def CreateNewHttpHeader(self, token: str = "", dormitoryId: str = "", cookie: str = ""):
        newHttpHeader = CaseInsensitiveDict()
        newHttpHeader["Accept"] = "application/json"
        newHttpHeader["Authorization"] = "Bearer " + token
        newHttpHeader["X-DormitoryId"] = dormitoryId
        newHttpHeader["Cookie"] = cookie
        return newHttpHeader
    
    def CreateNewHttpRequest(
        self, url: str = None, body_data: dict = {}, header: CaseInsensitiveDict = {}):

        newHttpRequest = HttpRequest()
        newHttpRequest.Body = body_data
        newHttpRequest.Header = header
        newHttpRequest.Url = url
        
        return newHttpRequest

    async def Get(
        self, session: aiohttp.ClientSession, req: HttpRequest):
        resp = None
        try:
            async with session.get(req.Url, headers=req.Header, json=req.Body) as resp:
                resp.raise_for_status()
                await resp.json()
        except HTTPError as err:  
            return ""
        except Exception as err:
            return ""
        return resp

    async def Post(
        self, session: aiohttp.ClientSession, req: HttpRequest):
        try:
            async with session.post(req.Url, headers=req.Header, json=req.Body) as resp:
                resp.raise_for_status()
                await resp.json()
                return resp
        except HTTPError as err:  
            return ""
        except Exception as err:
            return ""
    
    async def Put(
        self, session: aiohttp.ClientSession, req: HttpRequest):
        resp = None
        try:
            async with session.put(req.Url, headers=req.Header, json=req.Body) as resp:
                resp.raise_for_status()
                await resp.json()
        except HTTPError as err:  
            return ""
        except Exception as err:
            return ""
        return resp

    async def Delete(
        self, session: aiohttp.ClientSession, req: HttpRequest):
        resp = None
        try:
            async with session.delete(req.Url, headers=req.Header, json=req.Body) as resp:
                resp.raise_for_status()
                await resp.json()
        except HTTPError as err:  
            return ""
        except Exception as err:
            return ""
        return resp
