from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetContributorCollectionsListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetContributorCollectionsListError:
    def map(self, response: HttpResponse) -> GetContributorCollectionsListErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_contributor_collections_list_error_mapper: Final[
    ErrorMapper[GetContributorCollectionsListErrorBody]
] = _GetContributorCollectionsListError()
