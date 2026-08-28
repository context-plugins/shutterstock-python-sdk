from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetImageListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetImageListError:
    def map(self, response: HttpResponse) -> GetImageListErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_image_list_error_mapper: Final[ErrorMapper[GetImageListErrorBody]] = _GetImageListError()
