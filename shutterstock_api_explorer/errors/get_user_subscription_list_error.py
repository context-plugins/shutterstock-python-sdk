from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetUserSubscriptionListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetUserSubscriptionListError:
    def map(self, response: HttpResponse) -> GetUserSubscriptionListErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_user_subscription_list_error_mapper: Final[
    ErrorMapper[GetUserSubscriptionListErrorBody]
] = _GetUserSubscriptionListError()
