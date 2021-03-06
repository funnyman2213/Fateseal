from fateseal.models.manacost import ManaCost
from fateseal.models.objlist import ObjList
from fateseal.models.symbol import CardSymbol
from fateseal.abc import RequestType

class All(RequestType[ObjList[CardSymbol]]):
    """Returns all valid Symbols"""
    return_type = CardSymbol

    def __init__(self) -> None:
        self.endpoint = "/symbology"

class ParseMana(RequestType[ManaCost]):
    """Returns information about the requested mana string"""
    return_type = ManaCost

    def __init__(self, query:str) -> None:
        self.endpoint = "/symbology/parse-mana"
        self._set_paramaters([
            ('cost', query)
        ])
