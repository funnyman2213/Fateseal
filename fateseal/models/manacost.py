from fateseal.models.card import MANACOLOR
from fateseal.models.abc import ScryfallObject
from typing import List

class ManaCost(ScryfallObject):
    cost: str
    cmc: float
    colors: List[MANACOLOR]
    colorless: bool
    monocolored: bool
    multicolored: bool