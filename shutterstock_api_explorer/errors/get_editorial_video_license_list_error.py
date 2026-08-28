from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetEditorialVideoLicenseListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetEditorialVideoLicenseListError:
    def map(self, response: HttpResponse) -> GetEditorialVideoLicenseListErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_editorial_video_license_list_error_mapper: Final[
    ErrorMapper[GetEditorialVideoLicenseListErrorBody]
] = _GetEditorialVideoLicenseListError()
