from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListEditorialVideoCategoriesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListEditorialVideoCategoriesError:
    def map(self, response: HttpResponse) -> ListEditorialVideoCategoriesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


list_editorial_video_categories_error_mapper: Final[
    ErrorMapper[ListEditorialVideoCategoriesErrorBody]
] = _ListEditorialVideoCategoriesError()
