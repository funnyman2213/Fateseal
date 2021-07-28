from fateseal.models.error import Error
from fateseal.models.objlist import ObjList
from fateseal.models.bulkdata import BulkData
from typing import Literal, Type, Union

from .abc import RequestType

class All(RequestType):
    """Returns a List of all Bulk Data entries"""
    _return_type: type = ObjList[BulkData]

    def __init__(self) -> None:
        self.endpoint = "/bulk-data"

    def get(self) -> Union[_return_type, Error]:
        return super().get()
    
    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class ByID(RequestType):
    """Returns a Bulk Data entry based on ID"""
    _return_type: type = BulkData
    def __init__(self, id: str) -> None:
        self.endpoint = "/bulk-data/{}".format(id)
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()
    
    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()
    

class ByType(RequestType):
    """Returns a Bulk Data entry based on Type"""
    _return_type: type = BulkData

    def __init__(self, type: Literal["oracle_cards", "unique_artwork", "default_cards", "all_cards", "rulings"]) -> None:
        self.endpoint = "/bulk-data/{}".format(type)

    def get(self) -> Union[_return_type, Error]:
        return super().get()
    
    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()