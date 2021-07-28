from fateseal.models.symbol import CardSymbol
from fateseal.models.set import CardSet
from fateseal.models.ruling import Ruling
from fateseal.models.objlist import ObjList
from fateseal.models.error import Error
from fateseal.models.catalog import Catalog
from fateseal.models.bulkdata import BulkData
from fateseal.models.card import Card
from fateseal.models.abc import ScryfallObject
from typing import Coroutine, Dict, List, Optional, Tuple, Any, Union

import requests
import aiohttp

class RequestType:
    _base_uri = "https://api.scryfall.com"
    endpoint: str
    params: Optional[Dict[str, str]] = None
    _return_type: type = ScryfallObject

    def _set_paramaters(self, params:List[Tuple[str, Any]] ) -> None:
        self.params = {key:str(value) for (key, value) in params if value is not None}

    def _interpret(self, object:str) -> ScryfallObject:
        objects = {
            "bulk_data": BulkData,
            "card": Card,
            "catalog": Catalog,
            "error": Error,
            "list": ObjList,
            "ruling": Ruling,
            "set": CardSet,
            "card_symbol": CardSymbol
        }
        if object in objects:
            return objects[object]

    def get(self) -> Union[_return_type, Error]:
        r = requests.get(self._base_uri + self.endpoint, params=self.params)
        return self._interpret(r.json()["object"]).parse_raw(r.text)

    async def async_get(self) -> Coroutine[None, None, Union[_return_type, Error]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self._base_uri + self.endpoint, params=self.params) as response:   
                responseJson = await response.json()
                objectType = self._interpret(responseJson['object'])
                return objectType.parse_raw(await response.text())

