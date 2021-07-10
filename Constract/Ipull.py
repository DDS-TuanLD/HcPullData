from abc import ABCMeta, abstractmethod
import asyncio
from HcServices.Http import Http
from Helper.System import System
import logging

class Ipull(metaclass=ABCMeta):
    __http: Http
    __logger: logging.Logger
    __exhibitFlag: bool
    
    def __init__(self, log: logging.Logger, http: Http):
        self.__http = http
        self.__logger = log
        self.__exhibitFlag = None
    
    def Exhibit(self):
        self.__exhibitFlag = True
        
    def DeExhibit(self):
        self.__exhibitFlag = False
    
    def ExhibitStatus(self):
        return self.__exhibitFlag 
        
    @abstractmethod
    def PullAndSave(self):
        pass
  