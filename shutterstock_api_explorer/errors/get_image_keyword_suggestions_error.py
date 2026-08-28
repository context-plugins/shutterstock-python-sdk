from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetImageKeywordSuggestionsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetImageKeywordSuggestionsError:
    def map(self, response: HttpResponse) -> GetImageKeywordSuggestionsErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_image_keyword_suggestions_error_mapper: Final[
    ErrorMapper[GetImageKeywordSuggestionsErrorBody]
] = _GetImageKeywordSuggestionsError()
