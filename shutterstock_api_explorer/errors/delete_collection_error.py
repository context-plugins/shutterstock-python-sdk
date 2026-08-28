from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteCollectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteCollectionError:
    def map(self, response: HttpResponse) -> DeleteCollectionErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_collection_error_mapper: Final[ErrorMapper[DeleteCollectionErrorBody]] = _DeleteCollectionError()
