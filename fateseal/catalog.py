from fateseal.abc import RequestType
from fateseal.models.catalog import Catalog


class CatalogRequest(RequestType[Catalog]):
    return_type = Catalog

class CardNames(CatalogRequest):
    """Returns a Catalog of all card names"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/card-names"

class ArtistNames(CatalogRequest):
    """Returns a Catalog of all artist names"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/artist-names"

class WordBank(CatalogRequest):
    """Returns a Catalog of the word bank """
    def __init__(self) -> None:
        self.endpoint = "/catalog/word-bank"

class CreatureTypes(CatalogRequest):
    """Returns a Catalog of all creature types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/creature-types"

class PlaneswalkerTypes(CatalogRequest):
    """Returns a Catalog of all planeswalker types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/planeswalker-types"

class LandTypes(CatalogRequest):
    """Returns a Catalog of all land types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/land-types"

class ArtifactTypes(CatalogRequest):
    """Returns a Catalog of all artifact types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/artifact-types"

class EnchantmentTypes(CatalogRequest):
    """Returns a Catalog of all enchantment types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/enchantment-types"

class SpellTypes(CatalogRequest):
    """Returns a Catalog of all spell types"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/spell-types"

class Powers(CatalogRequest):
    """Returns a Catalog of all valid powers"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/powers"

class Toughnesses(CatalogRequest):
    """Returns a Catalog of all valid toughnesses"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/toughnesses"

class Loyalties(CatalogRequest):
    """Returns a Catalog of all loyalties"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/loyalties"

class Watermarks(CatalogRequest):
    """Returns a Catalog of all watermarks"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/watermarks"

class KeywordAbilities(CatalogRequest):
    """Returns a Catalog of all keyword abilities"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/keyword-abilities"

class KeywordActions(CatalogRequest):
    """Returns a Catalog of all keyword actions"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/keyword-actions"

class AbilityWords(CatalogRequest):
    """Returns a Catalog of all ability words"""
    def __init__(self) -> None:
        self.endpoint = "/catalog/ability-words"
