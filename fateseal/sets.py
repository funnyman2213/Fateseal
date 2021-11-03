from fateseal.models.objlist import ObjList
from fateseal.models.set import CardSet
from uuid import UUID
from .abc import RequestType

class All(RequestType):
    """Returns all Sets"""

    return_type: ObjList[CardSet]

    def __init__(self) -> None:
        self.endpoint = "/sets"

class ByCode(RequestType):
    """Returns Set with specified code"""

    return_type: CardSet

    def __init__(self, code:str) -> None:
        self.endpoint = f"/sets/{code}"

class TCGPlayerID(RequestType):
    """Returns Set with TCGPlayer ID"""

    return_type: CardSet

    def __init__(self, id:int) -> None:
        self.endpoint = f"/sets/tcgplayer/{id}"


class ByID(RequestType):
    """Returns Set with Scryfall UUID"""

    return_type: CardSet 

    def __init__(self, id:UUID) -> None:
        self.endpoint = f"/sets/{id}"

        