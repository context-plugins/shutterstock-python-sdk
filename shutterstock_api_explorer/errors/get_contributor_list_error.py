from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetContributorListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetContributorListError:
    def map(self, response: HttpResponse) -> GetContributorListErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_contributor_list_error_mapper: Final[ErrorMapper[GetContributorListErrorBody]] = _GetContributorListError()
