<!-- Generated file — do not edit; regenerated with the SDK. -->

# EditorialImages — operations

Accessor: `client.editorial_images` · Source: `shutterstock_api_explorer/apis/editorial_images.py` · 18 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.editorial_images.get_editorial_categories

- **Route**: `GET /v2/editorial/categories`
- **Server**: `default`
- **Signature**: `def get_editorial_categories(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `EditorialCategoryResults`
- **Returns (raw)**: `ApiResult[EditorialCategoryResults, GetEditorialCategoriesErrorBody]`
- **Error**: `GetEditorialCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialCategoryResults` | `shutterstock_api_explorer/models/editorial_category_results.py` |
| `GetEditorialCategoriesErrorBody` | `shutterstock_api_explorer/errors/get_editorial_categories_error.py` |

### client.editorial_images.get_editorial_image

- **Route**: `GET /v2/editorial/images/{id}`
- **Server**: `default`
- **Signature**: `def get_editorial_image(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — path · `country` — query
- **Returns (parsed)**: `EditorialContent`
- **Returns (raw)**: `ApiResult[EditorialContent, GetEditorialImageErrorBody]`
- **Error**: `GetEditorialImageErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialContent` | `shutterstock_api_explorer/models/editorial_content.py` |
| `GetEditorialImageErrorBody` | `shutterstock_api_explorer/errors/get_editorial_image_error.py` |

### client.editorial_images.get_editorial_image2

- **Route**: `GET /v2/editorial/{id}`
- **Server**: `default`
- **Signature**: `def get_editorial_image2(id: str, country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — path · `country` — query · `search_id` — query
- **Returns (parsed)**: `EditorialContent`
- **Returns (raw)**: `ApiResult[EditorialContent, GetEditorialImage2ErrorBody]`
- **Error**: `GetEditorialImage2ErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialContent` | `shutterstock_api_explorer/models/editorial_content.py` |
| `GetEditorialImage2ErrorBody` | `shutterstock_api_explorer/errors/get_editorial_image2_error.py` |

### client.editorial_images.get_editorial_image_license_list

- **Route**: `GET /v2/editorial/images/licenses`
- **Server**: `default`
- **Signature**: `def get_editorial_image_license_list(*, image_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `image_id` — query · `license` — query · `page` — query · `per_page` — query · `sort` — query · `username` — query · `start_date` — query · `end_date` — query · `download_availability` — query · `team_history` — query
- **Returns (parsed)**: `DownloadHistoryDataList`
- **Returns (raw)**: `ApiResult[DownloadHistoryDataList, GetEditorialImageLicenseListErrorBody]`
- **Error**: `GetEditorialImageLicenseListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `DownloadAvailabilityOrStr` | `shutterstock_api_explorer/models/enums/download_availability.py` |
| `DownloadHistoryDataList` | `shutterstock_api_explorer/models/download_history_data_list.py` |
| `GetEditorialImageLicenseListErrorBody` | `shutterstock_api_explorer/errors/get_editorial_image_license_list_error.py` |

### client.editorial_images.get_editorial_image_livefeed

- **Route**: `GET /v2/editorial/images/livefeeds/{id}`
- **Server**: `default`
- **Signature**: `def get_editorial_image_livefeed(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — path · `country` — query
- **Returns (parsed)**: `EditorialImageLivefeed`
- **Returns (raw)**: `ApiResult[EditorialImageLivefeed, GetEditorialImageLivefeedErrorBody]`
- **Error**: `GetEditorialImageLivefeedErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialImageLivefeed` | `shutterstock_api_explorer/models/editorial_image_livefeed.py` |
| `GetEditorialImageLivefeedErrorBody` | `shutterstock_api_explorer/errors/get_editorial_image_livefeed_error.py` |

### client.editorial_images.get_editorial_image_livefeed_items

- **Route**: `GET /v2/editorial/images/livefeeds/{id}/items`
- **Server**: `default`
- **Signature**: `def get_editorial_image_livefeed_items(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — path · `country` — query
- **Returns (parsed)**: `EditorialContentDataList`
- **Returns (raw)**: `ApiResult[EditorialContentDataList, GetEditorialImageLivefeedItemsErrorBody]`
- **Error**: `GetEditorialImageLivefeedItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialContentDataList` | `shutterstock_api_explorer/models/editorial_content_data_list.py` |
| `GetEditorialImageLivefeedItemsErrorBody` | `shutterstock_api_explorer/errors/get_editorial_image_livefeed_items_error.py` |

### client.editorial_images.get_editorial_image_livefeed_list

- **Route**: `GET /v2/editorial/images/livefeeds`
- **Server**: `default`
- **Signature**: `def get_editorial_image_livefeed_list(country: str, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`
- **Params**: `country` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `EditorialImageLivefeedList`
- **Returns (raw)**: `ApiResult[EditorialImageLivefeedList, GetEditorialImageLivefeedListErrorBody]`
- **Error**: `GetEditorialImageLivefeedListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialImageLivefeedList` | `shutterstock_api_explorer/models/editorial_image_livefeed_list.py` |
| `GetEditorialImageLivefeedListErrorBody` | `shutterstock_api_explorer/errors/get_editorial_image_livefeed_list_error.py` |

### client.editorial_images.get_editorial_livefeed

- **Route**: `GET /v2/editorial/livefeeds/{id}`
- **Server**: `default`
- **Signature**: `def get_editorial_livefeed(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — path · `country` — query
- **Returns (parsed)**: `EditorialImageLivefeed`
- **Returns (raw)**: `ApiResult[EditorialImageLivefeed, GetEditorialLivefeedErrorBody]`
- **Error**: `GetEditorialLivefeedErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialImageLivefeed` | `shutterstock_api_explorer/models/editorial_image_livefeed.py` |
| `GetEditorialLivefeedErrorBody` | `shutterstock_api_explorer/errors/get_editorial_livefeed_error.py` |

### client.editorial_images.get_editorial_livefeed_items

- **Route**: `GET /v2/editorial/livefeeds/{id}/items`
- **Server**: `default`
- **Signature**: `def get_editorial_livefeed_items(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — path · `country` — query
- **Returns (parsed)**: `EditorialContentDataList`
- **Returns (raw)**: `ApiResult[EditorialContentDataList, GetEditorialLivefeedItemsErrorBody]`
- **Error**: `GetEditorialLivefeedItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialContentDataList` | `shutterstock_api_explorer/models/editorial_content_data_list.py` |
| `GetEditorialLivefeedItemsErrorBody` | `shutterstock_api_explorer/errors/get_editorial_livefeed_items_error.py` |

### client.editorial_images.get_editorial_livefeed_list

- **Route**: `GET /v2/editorial/livefeeds`
- **Server**: `default`
- **Signature**: `def get_editorial_livefeed_list(country: str, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`
- **Params**: `country` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `EditorialImageLivefeedList`
- **Returns (raw)**: `ApiResult[EditorialImageLivefeedList, GetEditorialLivefeedListErrorBody]`
- **Error**: `GetEditorialLivefeedListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialImageLivefeedList` | `shutterstock_api_explorer/models/editorial_image_livefeed_list.py` |
| `GetEditorialLivefeedListErrorBody` | `shutterstock_api_explorer/errors/get_editorial_livefeed_list_error.py` |

### client.editorial_images.get_updated_editorial_image

- **Route**: `GET /v2/editorial/updated`
- **Server**: `default`
- **Signature**: `def get_updated_editorial_image(type_: Type5OrStr, date_updated_start: RFC3339DateTime, date_updated_end: RFC3339DateTime, country: str, *, date_taken_start: Date | None = None, date_taken_end: Date | None = None, cursor: str | None = None, sort: Sort5OrStr | None = None, supplier_code: list[str] | None = None, per_page: int | None = 500, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `date_updated_start`, `date_updated_end`, `country`
- **Params**: `type_` — query `type` · `date_updated_start` — query · `date_updated_end` — query · `country` — query · `date_taken_start` — query · `date_taken_end` — query · `cursor` — query · `sort` — query · `supplier_code` — query · `per_page` — query
- **Returns (parsed)**: `EditorialUpdatedResults`
- **Returns (raw)**: `ApiResult[EditorialUpdatedResults, GetUpdatedEditorialImageErrorBody]`
- **Error**: `GetUpdatedEditorialImageErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `Type5OrStr` | `shutterstock_api_explorer/models/enums/type5.py` |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `EditorialUpdatedResults` | `shutterstock_api_explorer/models/editorial_updated_results.py` |
| `GetUpdatedEditorialImageErrorBody` | `shutterstock_api_explorer/errors/get_updated_editorial_image_error.py` |

### client.editorial_images.get_updated_editorial_images

- **Route**: `GET /v2/editorial/images/updated`
- **Server**: `default`
- **Signature**: `def get_updated_editorial_images(type_: Type5OrStr, date_updated_start: RFC3339DateTime, date_updated_end: RFC3339DateTime, country: str, *, date_taken_start: Date | None = None, date_taken_end: Date | None = None, cursor: str | None = None, sort: Sort5OrStr | None = None, supplier_code: list[str] | None = None, per_page: int | None = 500, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `date_updated_start`, `date_updated_end`, `country`
- **Params**: `type_` — query `type` · `date_updated_start` — query · `date_updated_end` — query · `country` — query · `date_taken_start` — query · `date_taken_end` — query · `cursor` — query · `sort` — query · `supplier_code` — query · `per_page` — query
- **Returns (parsed)**: `EditorialUpdatedResults`
- **Returns (raw)**: `ApiResult[EditorialUpdatedResults, GetUpdatedEditorialImagesErrorBody]`
- **Error**: `GetUpdatedEditorialImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `Type5OrStr` | `shutterstock_api_explorer/models/enums/type5.py` |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `EditorialUpdatedResults` | `shutterstock_api_explorer/models/editorial_updated_results.py` |
| `GetUpdatedEditorialImagesErrorBody` | `shutterstock_api_explorer/errors/get_updated_editorial_images_error.py` |

### client.editorial_images.license_editorial_image

- **Route**: `POST /v2/editorial/licenses`
- **Server**: `default`
- **Signature**: `def license_editorial_image(body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LicenseEditorialContentResults`
- **Returns (raw)**: `ApiResult[LicenseEditorialContentResults, LicenseEditorialImageErrorBody]`
- **Error**: `LicenseEditorialImageErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `LicenseEditorialContentRequest` | `shutterstock_api_explorer/models/license_editorial_content_request.py` |
| `LicenseEditorialContentRequestDict` | `shutterstock_api_explorer/models/license_editorial_content_request.py` |
| `LicenseEditorialContentResults` | `shutterstock_api_explorer/models/license_editorial_content_results.py` |
| `LicenseEditorialImageErrorBody` | `shutterstock_api_explorer/errors/license_editorial_image_error.py` |

### client.editorial_images.license_editorial_images

- **Route**: `POST /v2/editorial/images/licenses`
- **Server**: `default`
- **Signature**: `def license_editorial_images(body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LicenseEditorialContentResults`
- **Returns (raw)**: `ApiResult[LicenseEditorialContentResults, LicenseEditorialImagesErrorBody]`
- **Error**: `LicenseEditorialImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `LicenseEditorialContentRequest` | `shutterstock_api_explorer/models/license_editorial_content_request.py` |
| `LicenseEditorialContentRequestDict` | `shutterstock_api_explorer/models/license_editorial_content_request.py` |
| `LicenseEditorialContentResults` | `shutterstock_api_explorer/models/license_editorial_content_results.py` |
| `LicenseEditorialImagesErrorBody` | `shutterstock_api_explorer/errors/license_editorial_images_error.py` |

### client.editorial_images.list_editorial_image_categories

- **Route**: `GET /v2/editorial/images/categories`
- **Server**: `default`
- **Signature**: `def list_editorial_image_categories(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `EditorialImageCategoryResults`
- **Returns (raw)**: `ApiResult[EditorialImageCategoryResults, ListEditorialImageCategoriesErrorBody]`
- **Error**: `ListEditorialImageCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialImageCategoryResults` | `shutterstock_api_explorer/models/editorial_image_category_results.py` |
| `ListEditorialImageCategoriesErrorBody` | `shutterstock_api_explorer/errors/list_editorial_image_categories_error.py` |

### client.editorial_images.list_editorial_images

- **Route**: `GET /v2/editorial/images`
- **Server**: `default`
- **Signature**: `def list_editorial_images(id: list[str], country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `country`
- **Params**: `id` — query · `country` — query · `search_id` — query
- **Returns (parsed)**: `EditorialImageResults`
- **Returns (raw)**: `ApiResult[EditorialImageResults, ListEditorialImagesErrorBody]`
- **Error**: `ListEditorialImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `EditorialImageResults` | `shutterstock_api_explorer/models/editorial_image_results.py` |
| `ListEditorialImagesErrorBody` | `shutterstock_api_explorer/errors/list_editorial_images_error.py` |

### client.editorial_images.search_editorial

- **Route**: `GET /v2/editorial/search`
- **Server**: `default`
- **Signature**: `def search_editorial(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`
- **Params**: `country` — query · `query` — query · `sort` — query · `category` — query · `supplier_code` — query · `date_start` — query · `date_end` — query · `per_page` — query · `cursor` — query
- **Returns (parsed)**: `EditorialSearchResults`
- **Returns (raw)**: `ApiResult[EditorialSearchResults, SearchEditorialErrorBody]`
- **Error**: `SearchEditorialErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort17OrStr` | `shutterstock_api_explorer/models/enums/sort17.py` |
| `EditorialSearchResults` | `shutterstock_api_explorer/models/editorial_search_results.py` |
| `SearchEditorialErrorBody` | `shutterstock_api_explorer/errors/search_editorial_error.py` |

### client.editorial_images.search_editorial_images

- **Route**: `GET /v2/editorial/images/search`
- **Server**: `default`
- **Signature**: `def search_editorial_images(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`
- **Params**: `country` — query · `query` — query · `sort` — query · `category` — query · `supplier_code` — query · `date_start` — query · `date_end` — query · `per_page` — query · `cursor` — query
- **Returns (parsed)**: `EditorialSearchResults`
- **Returns (raw)**: `ApiResult[EditorialSearchResults, SearchEditorialImagesErrorBody]`
- **Error**: `SearchEditorialImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 406, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort17OrStr` | `shutterstock_api_explorer/models/enums/sort17.py` |
| `EditorialSearchResults` | `shutterstock_api_explorer/models/editorial_search_results.py` |
| `SearchEditorialImagesErrorBody` | `shutterstock_api_explorer/errors/search_editorial_images_error.py` |

