from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

AddImageCollectionItemsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _AddImageCollectionItemsError:
    def map(self, response: HttpResponse) -> AddImageCollectionItemsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


add_image_collection_items_error_mapper: Final[
    ErrorMapper[AddImageCollectionItemsErrorBody]
] = _AddImageCollectionItemsError()
