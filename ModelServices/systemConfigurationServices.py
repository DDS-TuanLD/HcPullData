from Repository.systemConfigurationRepo import systemConfigurationRepo
from Model.systemConfiguration import systemConfiguration
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection

class systemConfigurationServices():
    __systemConfigurationRepo: systemConfigurationRepo
    
    def __init__(self, SystemConfigurationTable: Table, context: Connection):
        self.__systemConfigurationRepo = systemConfigurationRepo(SystemConfigurationTable=SystemConfigurationTable, context=context)
        
    def AddNewSysConfiguration(self, sysConfig: systemConfiguration):
        self.__systemConfigurationRepo.CreateWithParams(sysConfig)
        
    def FindSysConfigurationById(self, id:int):
        rel = self.__systemConfigurationRepo.FindwithId(id=id)
        return rel
    
    def UpdateSysConfigurationById(self, id:int, sysConfig: systemConfiguration):
        self.__systemConfigurationRepo.UpdateById(id=id, newSysConfig=sysConfig)
        
    def FindAllSysConfiguration(self):
        rel = self.__systemConfigurationRepo.FindAll()
        return rel
    
    def RomoveSysConfigurationById(self, id:int):
        self.__systemConfigurationRepo.RemoveById(id)