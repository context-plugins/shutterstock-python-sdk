from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListSimilarImagesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListSimilarImagesError:
    def map(self, response: HttpResponse) -> ListSimilarImagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


list_similar_images_error_mapper: Final[ErrorMapper[ListSimilarImagesErrorBody]] = _ListSimilarImagesError()
