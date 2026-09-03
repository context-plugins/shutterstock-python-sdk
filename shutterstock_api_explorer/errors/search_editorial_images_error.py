from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SearchEditorialImagesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchEditorialImagesError:
    def map(self, response: HttpResponse) -> SearchEditorialImagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


search_editorial_images_error_mapper: Final[ErrorMapper[SearchEditorialImagesErrorBody]] = _SearchEditorialImagesError()
