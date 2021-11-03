from fateseal.models.abc import ScryfallObject
from typing import Iterator, List

class Catalog(ScryfallObject):
    uri: str #URI
    total_values: int
    data: List[str]
    
    def __iter__(self) -> Iterator[str]:
        return iter(self.data)

    def __getitem__(self, i) -> str:
        return self.data[i]