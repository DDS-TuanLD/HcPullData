from abc import ABCMeta, abstractmethod
from HcServices.Http import Http
import logging
from Cache.GlobalVariables import GlobalVariables


class IPull(metaclass=ABCMeta):
    __http: Http
    __logger: logging.Logger
    __exhibitFlag: bool
    __globalVariables: GlobalVariables

    def __init__(self, log: logging.Logger, http: Http):
        self.__http = http
        self.__logger = log
        self.__exhibitFlag = True
        self.__globalVariables = GlobalVariables()

    def PullSuccess(self):
        self.__globalVariables.NumberOfPullApiSuccess = self.__globalVariables.NumberOfPullApiSuccess + 1

    def Exhibit(self):
        self.__exhibitFlag = True

    def DeExhibit(self):
        self.__exhibitFlag = False

    def IsInExhibitState(self):
        return self.__exhibitFlag

    @abstractmethod
    def PullAndSave(self):
        pass
