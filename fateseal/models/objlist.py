from fateseal.models.abc import ScryfallObject
from typing import Generic, Iterator, Optional, List, TypeVar

T = TypeVar('T')

class ObjList(ScryfallObject, Generic[T]):
    data: List[T]
    has_more: bool
    next_page: Optional[str]
    total_cards: Optional[int]
    warnings: Optional[List[str]]

    def __iter__(self) -> Iterator[T]:
        return iter(self.data)