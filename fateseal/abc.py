from fateseal.models.abc import ScryfallObject
from fateseal.models import Error, BulkData, Card, Catalog, ObjList, Ruling, CardSet, CardSymbol
from typing import Dict, Generic, List, Literal, Optional, Tuple, Any, TypeVar, Union

import aiohttp
import requests

T = TypeVar('T')

class StatusError(Exception):
    def __init__(self, status, message) -> None:
        self.status = status
        self.message = message

class RequestType(Generic[T]):
    _base_uri: str = "https://api.scryfall.com"
    endpoint: str
    return_type: ScryfallObject
    params: Optional[Dict[str, str]] = None
    data: Optional[Dict[str,str]] = None
    method: Literal["GET", "POST"] = "GET"

    def _set_paramaters(self, params:List[Tuple[str, Any]] ) -> None:
        self.params = {key:str(value) for (key, value) in params if value is not None}

    def get(self) -> Union[T, Error]:
        if self.method == "GET":
            r = requests.get(self._base_uri + self.endpoint, params=self.params)
        if self.method == "POST":
            r = requests.post(self._base_uri + self.endpoint, params=self.params, json=self.data)
        if r.status_code != 200:
            raise StatusError(r.status_code, r.text)
        if r.json['object'] == 'Error':
            return Error.parse_raw(r.text)
        return self.return_type.parse_raw(r.text)

    async def async_get(self) -> Union[T, Error]:
        async with aiohttp.ClientSession() as session:
            if self.method == 'GET':
                async with session.get(self._base_uri + self.endpoint, params=self.params) as response:   
                    responseJson = await response.json()['object']
                    if responseJson == 'Error':
                        return Error.parse_raw(await response.text())
                    else:
                        return self.return_type.parse_raw(await response.text())
            if self.method == 'POST':
                async with session.post(self._base_uri + self.endpoint, params=self.params, json=self.data) as response:
                    responseJson = await response.json()['object']
                    if responseJson == 'Error':
                        return Error.parse_raw(await response.text())
                    else:
                        return self.return_type.parse_raw(await response.text())