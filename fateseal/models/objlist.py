from fateseal.models.abc import ScryfallObject
from typing import Dict, Generic, Iterator, Optional, List, TypeVar

T = TypeVar('T')

class ObjList(ScryfallObject, Generic[T]):
    data: List[T]
    has_more: bool
    not_found: Optional[List[Dict[str,str]]]
    next_page: Optional[str]
    total_cards: Optional[int]
    warnings: Optional[List[str]]

    def __iter__(self) -> Iterator[T]:
        return iter(self.data)

    def __getitem__(self, i) -> T:
        return self.data[i]