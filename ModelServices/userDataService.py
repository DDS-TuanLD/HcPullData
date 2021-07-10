from Repository.userDataRepo import userDataRepo
from Model.userData import userData
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
    
class userDataServices():
    __userDataRepo: userDataRepo
    
    def __init__(self, UserDataTable: Table, context: Connection):
        self.__userDataRepo = userDataRepo(UserDataTable, context=context)
        
    def AddNewUserData(self, newUserData: userData):
        self.__userDataRepo.CreateWithParams(newUserData)
        
    def UpdateUserDataById(self, id: int, newUserData: userData):
        self.__userDataRepo.UpdateById(id, newUserData)
        
    def FindUserDataById(self, id:int):
        rel = self.__userDataRepo.FindwithId(id)
        return rel