from fateseal.models.objlist import ObjList
from fateseal.models.ruling import Ruling
from uuid import UUID
from fateseal.abc import RequestType

class RulingsRequest(RequestType[ObjList[Ruling]]):
    return_type = ObjList[Ruling]

class Multiverse(RulingsRequest):
    """Returns a List of Rulings for a Card of Multiverse ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/multiverse/{id}/rulings"

class Mtgo(RulingsRequest):
    """Returns a List of Rulings for a Card of MTGO ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/mtgo/{id}/rulings"

class Arena(RulingsRequest):
    """Returns a List of Rulings for a Card of Arena ID"""
    def __init__(self, id:int) -> None:
        self.endpoint = f"/cards/arena/{id}/rulings"

class ByCode(RulingsRequest):
    """Returns a List of Rulings for a Card in set with collecter number"""
    def __init__(self, code:str, number:int) -> None:
        self.endpoint = f"/cards/{code}/{number}/rulings"

class ByID(RulingsRequest):
    """Returns a List of Rulings for a Card of Scryfall UUID"""
    def __init__(self, id:UUID) -> None:
        self.endpoint = f"/cards/{id}/rulings"