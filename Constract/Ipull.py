from abc import ABCMeta, abstractmethod
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging

class Ipull(metaclass=ABCMeta):
    __http: Http
    __logger: logging.Logger
    
    def __init__(self, log: logging.Logger, http: Http):
        self.__http = http
        self.__logger = log
    
    @abstractmethod
    def PullAndSave(self):
        pass
  