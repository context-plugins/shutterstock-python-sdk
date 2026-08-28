from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetImageRecommendationsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetImageRecommendationsError:
    def map(self, response: HttpResponse) -> GetImageRecommendationsErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_image_recommendations_error_mapper: Final[
    ErrorMapper[GetImageRecommendationsErrorBody]
] = _GetImageRecommendationsError()
