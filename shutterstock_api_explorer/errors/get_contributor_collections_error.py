from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetContributorCollectionsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetContributorCollectionsError:
    def map(self, response: HttpResponse) -> GetContributorCollectionsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_contributor_collections_error_mapper: Final[
    ErrorMapper[GetContributorCollectionsErrorBody]
] = _GetContributorCollectionsError()
