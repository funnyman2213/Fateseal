from fateseal.models.error import Error
from fateseal.models.objlist import ObjList
from fateseal.models.set import CardSet
from typing import Union
from uuid import UUID
from .abc import RequestType

class All(RequestType):
    """Returns all Sets"""

    _return_type: type = ObjList[CardSet]

    def __init__(self) -> None:
        self.endpoint = "/sets"

    def get(self) -> Union[_return_type, Error]:
        return super().get()
    
    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class ByCode(RequestType):
    """Returns Set with specified code"""

    _return_type: type = CardSet

    def __init__(self, code:str) -> None:
        self.endpoint = f"/sets/{code}"
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()
    
    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()
class TCGPlayerID(RequestType):
    """Returns Set with TCGPlayer ID"""

    _return_type: type = CardSet

    def __init__(self, id:int) -> None:
        self.endpoint = f"/sets/tcgplayer/{id}"

    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class ByID(RequestType):
    """Returns Set with Scryfall UUID"""

    _return_type: type = CardSet 

    def __init__(self, id:UUID) -> None:
        self.endpoint = f"/sets/{id}"

    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()
        