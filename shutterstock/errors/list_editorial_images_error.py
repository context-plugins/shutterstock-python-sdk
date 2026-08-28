from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListEditorialImagesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListEditorialImagesError:
    def map(self, response: HttpResponse) -> ListEditorialImagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


list_editorial_images_error_mapper: Final[ErrorMapper[ListEditorialImagesErrorBody]] = _ListEditorialImagesError()
