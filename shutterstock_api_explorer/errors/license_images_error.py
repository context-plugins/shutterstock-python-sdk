from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

LicenseImagesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LicenseImagesError:
    def map(self, response: HttpResponse) -> LicenseImagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


license_images_error_mapper: Final[ErrorMapper[LicenseImagesErrorBody]] = _LicenseImagesError()
