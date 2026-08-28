<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoundEffects — operations

Accessor: `client.sound_effects` · Source: `shutterstock/apis/sound_effects.py` · 6 operations

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
| `SfxUrl` | `shutterstock/models/sfx_url.py` |
| `DownloadSfxErrorBody` | `shutterstock/errors/download_sfx_error.py` |

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
| `LanguageOrStr` | `shutterstock/models/enums/language.py` |
| `View2OrStr` | `shutterstock/models/enums/view2.py` |
| `Library2OrStr` | `shutterstock/models/enums/library2.py` |
| `Sfx` | `shutterstock/models/sfx.py` |
| `GetSfxDetailsErrorBody` | `shutterstock/errors/get_sfx_details_error.py` |

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
| `Sort5OrStr` | `shutterstock/models/enums/sort5.py` |
| `DownloadAvailabilityOrStr` | `shutterstock/models/enums/download_availability.py` |
| `DownloadHistoryDataList` | `shutterstock/models/download_history_data_list.py` |
| `GetSfxLicenseListErrorBody` | `shutterstock/errors/get_sfx_license_list_error.py` |

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
| `View2OrStr` | `shutterstock/models/enums/view2.py` |
| `LanguageOrStr` | `shutterstock/models/enums/language.py` |
| `Library2OrStr` | `shutterstock/models/enums/library2.py` |
| `SfxdataList` | `shutterstock/models/sfxdata_list.py` |
| `GetSfxListDetailsErrorBody` | `shutterstock/errors/get_sfx_list_details_error.py` |

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
| `LicenseSfxrequest` | `shutterstock/models/license_sfxrequest.py` |
| `LicenseSfxrequestDict` | `shutterstock/models/license_sfxrequest.py` |
| `LicenseSfxresultDataList` | `shutterstock/models/license_sfxresult_data_list.py` |
| `LicensesSfxErrorBody` | `shutterstock/errors/licenses_sfx_error.py` |

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
| `Sort15OrStr` | `shutterstock/models/enums/sort15.py` |
| `View2OrStr` | `shutterstock/models/enums/view2.py` |
| `LanguageOrStr` | `shutterstock/models/enums/language.py` |
| `SfxsearchResults` | `shutterstock/models/sfxsearch_results.py` |
| `SearchSfxErrorBody` | `shutterstock/errors/search_sfx_error.py` |

