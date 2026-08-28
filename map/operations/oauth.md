<!-- Generated file — do not edit; regenerated with the SDK. -->

# Oauth — operations

Accessor: `client.oauth` · Source: `shutterstock/apis/oauth.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.oauth.authorize

- **Route**: `GET /v2/oauth/authorize`
- **Server**: `default`
- **Signature**: `def authorize(client_id: str, redirect_uri: str, response_type: ResponseTypeOrStr, state: str, *, realm: Realm2OrStr | None = None, scope: str | None = "user.view", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`, `redirect_uri`, `response_type`, `state`
- **Params**: `client_id` — query · `redirect_uri` — query · `response_type` — query · `state` — query · `realm` — query · `scope` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AuthorizeErrorBody]`
- **Error**: `AuthorizeErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `ResponseTypeOrStr` | `shutterstock/models/enums/response_type.py` |
| `Realm2OrStr` | `shutterstock/models/enums/realm2.py` |
| `AuthorizeErrorBody` | `shutterstock/errors/authorize_error.py` |

### client.oauth.create_access_token

- **Route**: `POST /v2/oauth/access_token`
- **Server**: `default`
- **Signature**: `def create_access_token(client_id: str, grant_type: GrantTypeOrStr, *, client_secret: str | None = None, code: str | None = None, realm: Realm3OrStr | None = None, expires: ExpiresOrStr | None = None, refresh_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`, `grant_type`
- **Params**: `client_id` — form field · `grant_type` — form field · `client_secret` — form field · `code` — form field · `realm` — form field · `expires` — form field · `refresh_token` — form field
- **Returns (parsed)**: `OauthAccessTokenResponse`
- **Returns (raw)**: `ApiResult[OauthAccessTokenResponse, CreateAccessTokenErrorBody]`
- **Error**: `CreateAccessTokenErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `GrantTypeOrStr` | `shutterstock/models/enums/grant_type.py` |
| `Realm3OrStr` | `shutterstock/models/enums/realm3.py` |
| `ExpiresOrStr` | `shutterstock/models/enums/expires.py` |
| `OauthAccessTokenResponse` | `shutterstock/models/oauth_access_token_response.py` |
| `CreateAccessTokenErrorBody` | `shutterstock/errors/create_access_token_error.py` |

