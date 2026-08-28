from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetContributorErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetContributorError:
    def map(self, response: HttpResponse) -> GetContributorErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_contributor_error_mapper: Final[ErrorMapper[GetContributorErrorBody]] = _GetContributorError()
