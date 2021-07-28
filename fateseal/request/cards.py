from fateseal.models.error import Error
from fateseal.models.objlist import ObjList
from fateseal.models.card import Card
from fateseal.models.catalog import Catalog
from typing import Optional, Union
from .abc import RequestType
from uuid import UUID

class Search(RequestType):
    """Returns a List of Cards based on the Query given"""

    _return_type: type = ObjList[Card]

    def __init__(
        self, 
        query: str, 
        unique: Optional[str] = None, 
        order: Optional[str] = None, 
        direction: Optional[str] = None, 
        extras: Optional[bool] = None,
        multilingual: Optional[bool] = None,
        variations: Optional[bool] = None,
        page: Optional[int] = None
        ) -> None:
        self.endpoint = "/cards/search"
        self._set_paramaters([
             ("q", query), 
             ('unique', unique), 
             ('order', order), 
             ('dir', direction), 
             ('include_extras', extras), 
             ('include_multilingual', multilingual),
             ('include_variations', variations),
             ('page', page)
             ])

    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class Named(RequestType):
    """Returns a single Card based on the input of either fuzzy or exact"""

    _return_type: type = Card

    def __init__(self, exact:Optional[str]=None, fuzzy:Optional[str]=None, set:Optional[str]=None) -> None:
        self.endpoint = "/cards/named"
        if bool(exact) != bool(fuzzy) :
            raise ValueError("Either Fuzzy or Exact must be set but not both.")
        self._set_paramaters([
            ('exact', exact),
            ('fuzzy', fuzzy),
            ('set', set)
            ])
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class Autocomplete(RequestType):
    """Returns a Catalog of up to 20 english autocompletions of the query"""

    _return_type: type = Catalog

    def __init__(self, query:str, extras:Optional[str]=None) -> None:
        self.endpoint = '/cards/autocomplete'
        self._set_paramaters([
            ('q', query),
            ('include_extras', extras)
        ])
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class Random(RequestType):
    """Returns a random Card"""

    _return_type: type = Card

    def __init__(self):
        self.endpoint = "/cards/random"
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class Collection(RequestType):
    #TODO: work on this. this one will be an interesting build
    def get(self) -> None:
        pass

    async def async_get(self) -> None:
        pass

class BySetCode(RequestType):
    """Returns a Card of specific collector number from the set code"""

    _return_type: type = Card

    def __init__(self, code:str, number:int, lang:Optional[str]=None) -> None:
        self.endpoint = f"/cards/{code}/{number}"
        if lang:
            self.endpoint += f"/{lang}"
        
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class Multiverse(RequestType):
    """Returns a Card of multivers ID"""

    _return_type: type = Card

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/multiverse/{id}"
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()
class Mtgo(RequestType):
    """Returns a Card of MTGO ID"""

    _return_type: type = Card

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/mtgo/{id}"
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class Arena(RequestType):
    """Returns a Card of Arena ID"""

    _return_type: type = Card

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/arena/{id}"
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class TCGPlayer(RequestType):
    """Returns a Card of TCGPlayer ID"""

    _return_type: type = Card

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/tcgplayer/{id}"
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class CardMarket(RequestType):
    """Returns a Card of CardMarket ID"""

    _return_type: type = Card

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/cardmarket/{id}"
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()

class ByID(RequestType):
    """Returns a Card of Scryfall UUID"""

    _return_type: type = Card

    def __init__(self, id:UUID) -> None:
        self.endpoint = f"/cards/{id}"
    
    def get(self) -> Union[_return_type, Error]:
        return super().get()

    async def async_get(self) -> Union[_return_type, Error]:
        return await super().async_get()