from fateseal.models.error import Error
from fateseal.models.manacost import ManaCost
from fateseal.models.objlist import ObjList
from fateseal.models.symbol import CardSymbol
from typing import Union
from .abc import RequestType

class All(RequestType):
    """Returns all valid Symbols"""

    _return_type: type = ObjList[CardSymbol]

    def __init__(self) -> None:
        self.endpoint = "/symbology"

    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class ParseMana(RequestType):
    """Returns information about the requested mana string"""

    _return_type: type = ManaCost

    def __init__(self, query:str) -> None:
        self.endpoint = "/symbology/parse-mana"
        self._set_paramaters([
            ('cost', query)
        ])
    
    def get(self) -> Union[_return_type, Error]:
        return super().get() 
    
    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()