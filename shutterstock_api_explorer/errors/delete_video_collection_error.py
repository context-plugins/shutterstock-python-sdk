from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteVideoCollectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteVideoCollectionError:
    def map(self, response: HttpResponse) -> DeleteVideoCollectionErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_video_collection_error_mapper: Final[ErrorMapper[DeleteVideoCollectionErrorBody]] = _DeleteVideoCollectionError()
