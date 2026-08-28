from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

LicensesSfxErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LicensesSfxError:
    def map(self, response: HttpResponse) -> LicensesSfxErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


licenses_sfx_error_mapper: Final[ErrorMapper[LicensesSfxErrorBody]] = _LicensesSfxError()
