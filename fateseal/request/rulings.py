from fateseal.models.error import Error
from fateseal.models.objlist import ObjList
from fateseal.models.ruling import Ruling
from typing import Union
from uuid import UUID
from .abc import RequestType

class RulingsRequest(RequestType):
    _return_type: type = ObjList[Ruling]

    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()
class Multiverse(RequestType):
    """Returns a List of Rulings for a Card of Multiverse ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/multiverse/{id}/rulings"

class Mtgo(RequestType):
    """Returns a List of Rulings for a Card of MTGO ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/mtgo/{id}/rulings"

class Arena(RequestType):
    """Returns a List of Rulings for a Card of Arena ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/arena/{id}/rulings"

class ByCode(RequestType):
    """Returns a List of Rulings for a Card in set with collecter number"""
    def __init__(self, code:str, number:int) -> None:
        self.endpoint = f"/cards/{code}/{number}/rulings"

class ByID(RequestType):
    """Returns a List of Rulings for a Card of Scryfall UUID"""
    def __init__(self, id:UUID) -> None:
        self.endpoint = f"/cards/{id}/rulings"