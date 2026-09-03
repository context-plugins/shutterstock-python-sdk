from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteImageCollectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteImageCollectionError:
    def map(self, response: HttpResponse) -> DeleteImageCollectionErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_image_collection_error_mapper: Final[ErrorMapper[DeleteImageCollectionErrorBody]] = _DeleteImageCollectionError()
