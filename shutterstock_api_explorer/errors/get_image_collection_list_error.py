from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetImageCollectionListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetImageCollectionListError:
    def map(self, response: HttpResponse) -> GetImageCollectionListErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_image_collection_list_error_mapper: Final[
    ErrorMapper[GetImageCollectionListErrorBody]
] = _GetImageCollectionListError()
