from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialImageLicenseListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialImageLicenseListError:
    def map(self, response: HttpResponse) -> GetEditorialImageLicenseListErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_image_license_list_error_mapper: Final[
    ErrorMapper[GetEditorialImageLicenseListErrorBody]
] = _GetEditorialImageLicenseListError()
