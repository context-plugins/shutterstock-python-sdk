<!-- Generated file — do not edit; regenerated with the SDK. -->

# Users — operations

Accessor: `client.users` · Source: `shutterstock_api_explorer/apis/users.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users.get_access_token

- **Route**: `GET /v2/user/access_token`
- **Server**: `default`
- **Signature**: `def get_access_token(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `AccessTokenDetails`
- **Returns (raw)**: `ApiResult[AccessTokenDetails, GetAccessTokenErrorBody]`
- **Error**: `GetAccessTokenErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `AccessTokenDetails` | `shutterstock_api_explorer/models/access_token_details.py` |
| `GetAccessTokenErrorBody` | `shutterstock_api_explorer/errors/get_access_token_error.py` |

### client.users.get_user

- **Route**: `GET /v2/user`
- **Server**: `default`
- **Signature**: `def get_user(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `UserDetails`
- **Returns (raw)**: `ApiResult[UserDetails, GetUserErrorBody]`
- **Error**: `GetUserErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `UserDetails` | `shutterstock_api_explorer/models/user_details.py` |
| `GetUserErrorBody` | `shutterstock_api_explorer/errors/get_user_error.py` |

### client.users.get_user_subscription_list

- **Route**: `GET /v2/user/subscriptions`
- **Server**: `default`
- **Signature**: `def get_user_subscription_list(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SubscriptionDataList`
- **Returns (raw)**: `ApiResult[SubscriptionDataList, GetUserSubscriptionListErrorBody]`
- **Error**: `GetUserSubscriptionListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `SubscriptionDataList` | `shutterstock_api_explorer/models/subscription_data_list.py` |
| `GetUserSubscriptionListErrorBody` | `shutterstock_api_explorer/errors/get_user_subscription_list_error.py` |

