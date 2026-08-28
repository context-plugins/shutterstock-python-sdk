from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

BulkSearchImagesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _BulkSearchImagesError:
    def map(self, response: HttpResponse) -> BulkSearchImagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


bulk_search_images_error_mapper: Final[ErrorMapper[BulkSearchImagesErrorBody]] = _BulkSearchImagesError()
