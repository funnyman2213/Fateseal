from fateseal.abc import RequestType
from typing import Coroutine, Generic, TypeVar, Union
from fateseal.models.abc import ScryfallObject
from fateseal.models.bulkdata import BulkData
from fateseal.models.card import Card
from fateseal.models.catalog import Catalog
from fateseal.models.error import Error
from fateseal.models.objlist import ObjList
from fateseal.models.ruling import Ruling
from fateseal.models.set import CardSet
from fateseal.models.symbol import CardSymbol

import aiohttp
import requests

T = TypeVar('T', bound=ScryfallObject)

class StatusError(Exception):
    def __init__(self, status, message) -> None:
        self.status = status
        self.message = message

class Request(Generic[T]):
    _base_uri = "https://api.scryfall.com"

    def __init__(self, request: RequestType) -> None:
        self.request = request

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

    def get(self) -> Union[T, Error]:
        if self.request.method == "GET":
            r = requests.get(self._base_uri + self.request.endpoint, params=self.request.params)
        if self.request.method == "POST":
            r = requests.post(self._base_uri + self.request.endpoint, params=self.request.params, json=self.request.data)
        if r.status_code != 200:
            raise StatusError(r.status_code, r.text)
        return self._interpret(r.json()["object"]).parse_raw(r.text)

    async def async_get(self) -> Coroutine[None, None, Union[T, Error]]:
        async with aiohttp.ClientSession() as session:
            if self.request.method == 'GET':
                async with session.get(self._base_uri + self.request.endpoint, params=self.request.params) as response:   
                    responseJson = await response.json()
                    objectType = self._interpret(responseJson['object'])
                    return objectType.parse_raw(await response.text())
            if self.request.method == 'POST':
                async with session.post(self._base_uri + self.request.endpoint, params=self.request.params, json=self.request.data) as response:
                    responseJson = await response.json()
                    objectType = self._interpret(responseJson['object'])
                    return objectType.parse_raw(await response.text())