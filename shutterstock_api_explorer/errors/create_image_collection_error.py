from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

CreateImageCollectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _CreateImageCollectionError:
    def map(self, response: HttpResponse) -> CreateImageCollectionErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


create_image_collection_error_mapper: Final[ErrorMapper[CreateImageCollectionErrorBody]] = _CreateImageCollectionError()
