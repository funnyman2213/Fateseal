from fateseal.models.objlist import ObjList
from fateseal.models.bulkdata import BulkData
from typing import Literal

from fateseal.abc import RequestType

class All(RequestType[ObjList[BulkData]]):
    """Returns a List of all Bulk Data entries"""
    return_type = ObjList[BulkData]

    def __init__(self) -> None:
        self.endpoint = "/bulk-data"

class ByID(RequestType[BulkData]):
    """Returns a Bulk Data entry based on ID"""
    return_type = BulkData

    def __init__(self, id: str) -> None:
        self.endpoint = "/bulk-data/{}".format(id)

class ByType(RequestType[BulkData]):
    """Returns a Bulk Data entry based on Type"""
    return_type = BulkData
    
    def __init__(self, type: Literal["oracle_cards", "unique_artwork", "default_cards", "all_cards", "rulings"]) -> None:
        self.endpoint = "/bulk-data/{}".format(type)