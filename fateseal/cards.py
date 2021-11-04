from fateseal.models.objlist import ObjList
from fateseal.models.card import Card
from fateseal.models.catalog import Catalog
from typing import Dict, List, Literal, Optional
from fateseal.abc import RequestType
from uuid import UUID

class Search(RequestType[ObjList[Card]]):
    """Returns a List of Cards based on the Query given"""

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

class Named(RequestType[Card]):
    """Returns a single Card based on the input of either fuzzy or exact"""

    def __init__(self, exact:Optional[str]=None, fuzzy:Optional[str]=None, set:Optional[str]=None) -> None:
        self.endpoint = "/cards/named"
        if bool(exact) == bool(fuzzy) :
            raise ValueError("Either Fuzzy or Exact must be set but not both.")
        self._set_paramaters([
            ('exact', exact),
            ('fuzzy', fuzzy),
            ('set', set)
            ])

class Autocomplete(RequestType[Catalog]):
    """Returns a Catalog of up to 20 english autocompletions of the query"""

    def __init__(self, query:str, extras:Optional[str]=None) -> None:
        self.endpoint = '/cards/autocomplete'
        self._set_paramaters([
            ('q', query),
            ('include_extras', extras)
        ])

class Random(RequestType[Card]):
    """Returns a random Card"""

    def __init__(self):
        self.endpoint = "/cards/random"

class Collection(RequestType[ObjList[Card]]):
    """Returns a list of cards based on the passed in identifiers"""
    method: Literal["GET", "POST"] = "POST"

    def __init__(self, identifiers:List[Dict[str,str]]) -> None:
        self.data = {"identifiers":identifiers}
        self.endpoint = "/cards/collection"

class BySetCode(RequestType[Card]):
    """Returns a Card of specific collector number from the set code"""

    def __init__(self, code:str, number:int, lang:Optional[str]=None) -> None:
        self.endpoint = f"/cards/{code}/{number}"
        if lang:
            self.endpoint += f"/{lang}"

class Multiverse(RequestType[Card]):
    """Returns a Card of multivers ID"""

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/multiverse/{id}"
 
class Mtgo(RequestType[Card]):
    """Returns a Card of MTGO ID"""

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/mtgo/{id}"

class Arena(RequestType[Card]):
    """Returns a Card of Arena ID"""

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/arena/{id}"

class TCGPlayer(RequestType[Card]):
    """Returns a Card of TCGPlayer ID"""

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/tcgplayer/{id}"

class CardMarket(RequestType[Card]):
    """Returns a Card of CardMarket ID"""

    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/cardmarket/{id}"

class ByID(RequestType[Card]):
    """Returns a Card of Scryfall UUID"""

    def __init__(self, id:UUID) -> None:
        self.endpoint = f"/cards/{id}"