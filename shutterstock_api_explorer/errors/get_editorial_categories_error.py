from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialCategoriesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialCategoriesError:
    def map(self, response: HttpResponse) -> GetEditorialCategoriesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_categories_error_mapper: Final[
    ErrorMapper[GetEditorialCategoriesErrorBody]
] = _GetEditorialCategoriesError()
