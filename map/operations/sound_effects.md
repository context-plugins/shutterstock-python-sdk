<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoundEffects — operations

Accessor: `client.sound_effects` · Source: `shutterstock_api_explorer/apis/sound_effects.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sound_effects.download_sfx

- **Route**: `POST /v2/sfx/licenses/{id}/downloads`
- **Server**: `default`
- **Signature**: `def download_sfx(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `SfxUrl`
- **Returns (raw)**: `ApiResult[SfxUrl, DownloadSfxErrorBody]`
- **Error**: `DownloadSfxErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `SfxUrl` | `shutterstock_api_explorer/models/sfx_url.py` |
| `DownloadSfxErrorBody` | `shutterstock_api_explorer/errors/download_sfx_error.py` |

### client.sound_effects.get_sfx_details

- **Route**: `GET /v2/sfx/{id}`
- **Server**: `default`
- **Signature**: `def get_sfx_details(id: int, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, library: Library2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `language` — query · `view` — query · `library` — query · `search_id` — query
- **Returns (parsed)**: `Sfx`
- **Returns (raw)**: `ApiResult[Sfx, GetSfxDetailsErrorBody]`
- **Error**: `GetSfxDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 503, anything unmapped]

| Type | Source |
| --- | --- |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `Library2OrStr` | `shutterstock_api_explorer/models/enums/library2.py` |
| `Sfx` | `shutterstock_api_explorer/models/sfx.py` |
| `GetSfxDetailsErrorBody` | `shutterstock_api_explorer/errors/get_sfx_details_error.py` |

### client.sound_effects.get_sfx_license_list

- **Route**: `GET /v2/sfx/licenses`
- **Server**: `default`
- **Signature**: `def get_sfx_license_list(*, sfx_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, license_id: str | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `sfx_id` — query · `license` — query · `page` — query · `per_page` — query · `sort` — query · `username` — query · `start_date` — query · `end_date` — query · `license_id` — query · `download_availability` — query · `team_history` — query
- **Returns (parsed)**: `DownloadHistoryDataList`
- **Returns (raw)**: `ApiResult[DownloadHistoryDataList, GetSfxLicenseListErrorBody]`
- **Error**: `GetSfxLicenseListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `DownloadAvailabilityOrStr` | `shutterstock_api_explorer/models/enums/download_availability.py` |
| `DownloadHistoryDataList` | `shutterstock_api_explorer/models/download_history_data_list.py` |
| `GetSfxLicenseListErrorBody` | `shutterstock_api_explorer/errors/get_sfx_license_list_error.py` |

### client.sound_effects.get_sfx_list_details

- **Route**: `GET /v2/sfx`
- **Server**: `default`
- **Signature**: `def get_sfx_list_details(id: list[str], *, view: View2OrStr | None = None, language: LanguageOrStr | None = None, library: Library2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query · `view` — query · `language` — query · `library` — query · `search_id` — query
- **Returns (parsed)**: `SfxdataList`
- **Returns (raw)**: `ApiResult[SfxdataList, GetSfxListDetailsErrorBody]`
- **Error**: `GetSfxListDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `Library2OrStr` | `shutterstock_api_explorer/models/enums/library2.py` |
| `SfxdataList` | `shutterstock_api_explorer/models/sfxdata_list.py` |
| `GetSfxListDetailsErrorBody` | `shutterstock_api_explorer/errors/get_sfx_list_details_error.py` |

### client.sound_effects.licenses_sfx

- **Route**: `POST /v2/sfx/licenses`
- **Server**: `default`
- **Signature**: `def licenses_sfx(body: LicenseSfxrequest | LicenseSfxrequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LicenseSfxresultDataList`
- **Returns (raw)**: `ApiResult[LicenseSfxresultDataList, LicensesSfxErrorBody]`
- **Error**: `LicensesSfxErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LicenseSfxrequest` | `shutterstock_api_explorer/models/license_sfxrequest.py` |
| `LicenseSfxrequestDict` | `shutterstock_api_explorer/models/license_sfxrequest.py` |
| `LicenseSfxresultDataList` | `shutterstock_api_explorer/models/license_sfxresult_data_list.py` |
| `LicensesSfxErrorBody` | `shutterstock_api_explorer/errors/licenses_sfx_error.py` |

### client.sound_effects.search_sfx

- **Route**: `GET /v2/sfx/search`
- **Server**: `default`
- **Signature**: `def search_sfx(*, added_date: Date | None = None, added_date_start: Date | None = None, added_date_end: Date | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, safe: bool | None = True, sort: Sort15OrStr | None = None, view: View2OrStr | None = None, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `added_date` — query · `added_date_start` — query · `added_date_end` — query · `duration` — query · `duration_from` — query · `duration_to` — query · `page` — query · `per_page` — query · `query` — query · `safe` — query · `sort` — query · `view` — query · `language` — query
- **Returns (parsed)**: `SfxsearchResults`
- **Returns (raw)**: `ApiResult[SfxsearchResults, SearchSfxErrorBody]`
- **Error**: `SearchSfxErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 503, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort15OrStr` | `shutterstock_api_explorer/models/enums/sort15.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `SfxsearchResults` | `shutterstock_api_explorer/models/sfxsearch_results.py` |
| `SearchSfxErrorBody` | `shutterstock_api_explorer/errors/search_sfx_error.py` |

