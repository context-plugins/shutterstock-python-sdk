from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SearchCatalogErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchCatalogError:
    def map(self, response: HttpResponse) -> SearchCatalogErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


search_catalog_error_mapper: Final[ErrorMapper[SearchCatalogErrorBody]] = _SearchCatalogError()
