from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListVideoCategoriesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListVideoCategoriesError:
    def map(self, response: HttpResponse) -> ListVideoCategoriesErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


list_video_categories_error_mapper: Final[ErrorMapper[ListVideoCategoriesErrorBody]] = _ListVideoCategoriesError()
