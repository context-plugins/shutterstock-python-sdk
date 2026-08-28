<!-- Generated file — do not edit; regenerated with the SDK. -->

# Test — operations

Accessor: `client.test` · Source: `shutterstock/apis/test.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.test.echo

- **Route**: `GET /v2/test`
- **Server**: `default`
- **Signature**: `def echo(*, text: str | None = "ok", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `text` — query
- **Returns (parsed)**: `TestEcho`
- **Returns (raw)**: `ApiResult[TestEcho, EchoErrorBody]`
- **Error**: `EchoErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `TestEcho` | `shutterstock/models/test_echo.py` |
| `EchoErrorBody` | `shutterstock/errors/echo_error.py` |

### client.test.validate

- **Route**: `GET /v2/test/validate`
- **Server**: `default`
- **Signature**: `def validate(id: int, *, tag: list[str] | None = None, user_agent: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query · `tag` — query · `user_agent` — header `user-agent`
- **Returns (parsed)**: `TestValidate`
- **Returns (raw)**: `ApiResult[TestValidate, ValidateErrorBody]`
- **Error**: `ValidateErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `TestValidate` | `shutterstock/models/test_validate.py` |
| `ValidateErrorBody` | `shutterstock/errors/validate_error.py` |

