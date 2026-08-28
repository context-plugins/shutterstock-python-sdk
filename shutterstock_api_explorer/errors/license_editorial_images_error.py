from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

LicenseEditorialImagesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LicenseEditorialImagesError:
    def map(self, response: HttpResponse) -> LicenseEditorialImagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


license_editorial_images_error_mapper: Final[
    ErrorMapper[LicenseEditorialImagesErrorBody]
] = _LicenseEditorialImagesError()
