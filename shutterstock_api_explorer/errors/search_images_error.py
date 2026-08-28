from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SearchImagesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchImagesError:
    def map(self, response: HttpResponse) -> SearchImagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


search_images_error_mapper: Final[ErrorMapper[SearchImagesErrorBody]] = _SearchImagesError()
