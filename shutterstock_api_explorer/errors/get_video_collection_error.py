from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetVideoCollectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetVideoCollectionError:
    def map(self, response: HttpResponse) -> GetVideoCollectionErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_video_collection_error_mapper: Final[ErrorMapper[GetVideoCollectionErrorBody]] = _GetVideoCollectionError()
