from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DownloadSfxErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DownloadSfxError:
    def map(self, response: HttpResponse) -> DownloadSfxErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


download_sfx_error_mapper: Final[ErrorMapper[DownloadSfxErrorBody]] = _DownloadSfxError()
