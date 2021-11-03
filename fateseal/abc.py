from fateseal.models.abc import ScryfallObject
from typing import Dict, List, Literal, Optional, Tuple, Any

class RequestType:
    endpoint: str
    return_type: type = ScryfallObject
    params: Optional[Dict[str, str]] = None
    data: Optional[Dict[str,str]] = None
    method: Literal["GET", "POST"] = "GET"

    def _set_paramaters(self, params:List[Tuple[str, Any]] ) -> None:
        self.params = {key:str(value) for (key, value) in params if value is not None}
