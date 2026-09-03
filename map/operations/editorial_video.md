<!-- Generated file — do not edit; regenerated with the SDK. -->

# EditorialVideo — operations

Accessor: `client.editorial_video` · Source: `shutterstock_api_explorer/apis/editorial_video.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.editorial_video.get_editorial_video

- **Route**: `GET /v2/editorial/videos/{id}`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_editorial_video(id: str, country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — path · `country` — query · `search_id` — query
- **Returns (parsed)**: `EditorialVideoContent`
- **Returns (raw)**: `ApiResult[EditorialVideoContent, GetEditorialVideoErrorBody]`
- **Error**: `GetEditorialVideoErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialVideoContent` | `shutterstock_api_explorer/models/editorial_video_content.py` |
| `GetEditorialVideoErrorBody` | `shutterstock_api_explorer/errors/get_editorial_video_error.py` |

### client.editorial_video.get_editorial_video_license_list

- **Route**: `GET /v2/editorial/videos/licenses`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_editorial_video_license_list(*, video_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `video_id` — query · `license` — query · `page` — query · `per_page` — query · `sort` — query · `username` — query · `start_date` — query · `end_date` — query · `download_availability` — query · `team_history` — query
- **Returns (parsed)**: `DownloadHistoryDataList`
- **Returns (raw)**: `ApiResult[DownloadHistoryDataList, GetEditorialVideoLicenseListErrorBody]`
- **Error**: `GetEditorialVideoLicenseListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `DownloadAvailabilityOrStr` | `shutterstock_api_explorer/models/enums/download_availability.py` |
| `DownloadHistoryDataList` | `shutterstock_api_explorer/models/download_history_data_list.py` |
| `GetEditorialVideoLicenseListErrorBody` | `shutterstock_api_explorer/errors/get_editorial_video_license_list_error.py` |

### client.editorial_video.license_editorial_video

- **Route**: `POST /v2/editorial/videos/licenses`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def license_editorial_video(body: LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LicenseEditorialContentResults`
- **Returns (raw)**: `ApiResult[LicenseEditorialContentResults, LicenseEditorialVideoErrorBody]`
- **Error**: `LicenseEditorialVideoErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LicenseEditorialVideoContentRequest` | `shutterstock_api_explorer/models/license_editorial_video_content_request.py` |
| `LicenseEditorialVideoContentRequestDict` | `shutterstock_api_explorer/models/license_editorial_video_content_request.py` |
| `LicenseEditorialContentResults` | `shutterstock_api_explorer/models/license_editorial_content_results.py` |
| `LicenseEditorialVideoErrorBody` | `shutterstock_api_explorer/errors/license_editorial_video_error.py` |

### client.editorial_video.list_editorial_video_categories

- **Route**: `GET /v2/editorial/videos/categories`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def list_editorial_video_categories(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `EditorialVideoCategoryResults`
- **Returns (raw)**: `ApiResult[EditorialVideoCategoryResults, ListEditorialVideoCategoriesErrorBody]`
- **Error**: `ListEditorialVideoCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialVideoCategoryResults` | `shutterstock_api_explorer/models/editorial_video_category_results.py` |
| `ListEditorialVideoCategoriesErrorBody` | `shutterstock_api_explorer/errors/list_editorial_video_categories_error.py` |

### client.editorial_video.list_editorial_videos

- **Route**: `GET /v2/editorial/videos`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def list_editorial_videos(id: list[str], country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — query · `country` — query · `search_id` — query
- **Returns (parsed)**: `EditorialVideoResults`
- **Returns (raw)**: `ApiResult[EditorialVideoResults, ListEditorialVideosErrorBody]`
- **Error**: `ListEditorialVideosErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialVideoResults` | `shutterstock_api_explorer/models/editorial_video_results.py` |
| `ListEditorialVideosErrorBody` | `shutterstock_api_explorer/errors/list_editorial_videos_error.py` |

### client.editorial_video.search_editorial_videos

- **Route**: `GET /v2/editorial/videos/search`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def search_editorial_videos(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, resolution: ResolutionOrStr | None = None, fps: float | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`
- **Params**: `country` — query · `query` — query · `sort` — query · `category` — query · `supplier_code` — query · `date_start` — query · `date_end` — query · `resolution` — query · `fps` — query · `per_page` — query · `cursor` — query
- **Returns (parsed)**: `EditorialVideoSearchResults`
- **Returns (raw)**: `ApiResult[EditorialVideoSearchResults, SearchEditorialVideosErrorBody]`
- **Error**: `SearchEditorialVideosErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort17OrStr` | `shutterstock_api_explorer/models/enums/sort17.py` |
| `ResolutionOrStr` | `shutterstock_api_explorer/models/enums/resolution.py` |
| `EditorialVideoSearchResults` | `shutterstock_api_explorer/models/editorial_video_search_results.py` |
| `SearchEditorialVideosErrorBody` | `shutterstock_api_explorer/errors/search_editorial_videos_error.py` |

