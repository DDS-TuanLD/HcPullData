from Repository.deviceAttributeRepo import deviceAttributeRepo
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.expression import BinaryExpression

class deviceAttributeServices():
    __deviceAtrributeRepo: deviceAttributeRepo
    
    def __init__(self, deviceAttributeTable: Table, context: Connection):
        self.__deviceAtrributeRepo = deviceAttributeRepo(deviceAttributeTable, context=context)
        