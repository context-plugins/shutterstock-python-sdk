from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DownloadImageErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DownloadImageError:
    def map(self, response: HttpResponse) -> DownloadImageErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


download_image_error_mapper: Final[ErrorMapper[DownloadImageErrorBody]] = _DownloadImageError()
