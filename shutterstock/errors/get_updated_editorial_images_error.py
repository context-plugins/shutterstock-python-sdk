from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetUpdatedEditorialImagesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetUpdatedEditorialImagesError:
    def map(self, response: HttpResponse) -> GetUpdatedEditorialImagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


get_updated_editorial_images_error_mapper: Final[
    ErrorMapper[GetUpdatedEditorialImagesErrorBody]
] = _GetUpdatedEditorialImagesError()
