from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetImageSuggestionsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetImageSuggestionsError:
    def map(self, response: HttpResponse) -> GetImageSuggestionsErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_image_suggestions_error_mapper: Final[ErrorMapper[GetImageSuggestionsErrorBody]] = _GetImageSuggestionsError()
