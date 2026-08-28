from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

UploadImageErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UploadImageError:
    def map(self, response: HttpResponse) -> UploadImageErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 413 | 415:
                return RawError(response)
            case _:
                return RawError(response)


upload_image_error_mapper: Final[ErrorMapper[UploadImageErrorBody]] = _UploadImageError()
