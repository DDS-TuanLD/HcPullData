from Repository.irDeviceAttibuteValueRepo import irDeviceAttributeValueRepo
from Model.systemConfiguration import systemConfiguration
from sqlalchemy import Table
from sqlalchemy.engine.base import Connection


class irDeviceAttributeValueServices:
    __irDeviceAttributeValueRepo: irDeviceAttributeValueRepo

    def __init__(self, irDeviceAttributeValueTable: Table, context: Connection):
        self.__irDeviceAttributeValueRepo = irDeviceAttributeValueRepo(irDeviceAttributeValueTable, context)
