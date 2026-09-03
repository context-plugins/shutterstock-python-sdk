from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListImageCategoriesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListImageCategoriesError:
    def map(self, response: HttpResponse) -> ListImageCategoriesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


list_image_categories_error_mapper: Final[ErrorMapper[ListImageCategoriesErrorBody]] = _ListImageCategoriesError()
