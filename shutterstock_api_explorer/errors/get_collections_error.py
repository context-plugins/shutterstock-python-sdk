from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetCollectionsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetCollectionsError:
    def map(self, response: HttpResponse) -> GetCollectionsErrorBody:
        match response.status_code:
            case 400:
                return RawError(response)
            case _:
                return RawError(response)


get_collections_error_mapper: Final[ErrorMapper[GetCollectionsErrorBody]] = _GetCollectionsError()
