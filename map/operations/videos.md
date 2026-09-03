<!-- Generated file — do not edit; regenerated with the SDK. -->

# Videos — operations

Accessor: `client.videos` · Source: `shutterstock_api_explorer/apis/videos.py` · 18 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos.add_video_collection_items

- **Route**: `POST /v2/videos/collections/{id}/items`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def add_video_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoCollectionItemsErrorBody]`
- **Error**: `AddVideoCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionItemRequest` | `shutterstock_api_explorer/models/collection_item_request.py` |
| `CollectionItemRequestDict` | `shutterstock_api_explorer/models/collection_item_request.py` |
| `AddVideoCollectionItemsErrorBody` | `shutterstock_api_explorer/errors/add_video_collection_items_error.py` |

### client.videos.create_video_collection

- **Route**: `POST /v2/videos/collections`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def create_video_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CollectionCreateResponse`
- **Returns (raw)**: `ApiResult[CollectionCreateResponse, CreateVideoCollectionErrorBody]`
- **Error**: `CreateVideoCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionCreateRequest` | `shutterstock_api_explorer/models/collection_create_request.py` |
| `CollectionCreateRequestDict` | `shutterstock_api_explorer/models/collection_create_request.py` |
| `CollectionCreateResponse` | `shutterstock_api_explorer/models/collection_create_response.py` |
| `CreateVideoCollectionErrorBody` | `shutterstock_api_explorer/errors/create_video_collection_error.py` |

### client.videos.delete_video_collection

- **Route**: `DELETE /v2/videos/collections/{id}`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def delete_video_collection(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoCollectionErrorBody]`
- **Error**: `DeleteVideoCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoCollectionErrorBody` | `shutterstock_api_explorer/errors/delete_video_collection_error.py` |

### client.videos.delete_video_collection_items

- **Route**: `DELETE /v2/videos/collections/{id}/items`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def delete_video_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `item_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoCollectionItemsErrorBody]`
- **Error**: `DeleteVideoCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoCollectionItemsErrorBody` | `shutterstock_api_explorer/errors/delete_video_collection_items_error.py` |

### client.videos.download_videos

- **Route**: `POST /v2/videos/licenses/{id}/downloads`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def download_videos(id: str, body: RedownloadVideo | RedownloadVideoDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `Url`
- **Returns (raw)**: `ApiResult[Url, DownloadVideosErrorBody]`
- **Error**: `DownloadVideosErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `RedownloadVideo` | `shutterstock_api_explorer/models/redownload_video.py` |
| `RedownloadVideoDict` | `shutterstock_api_explorer/models/redownload_video.py` |
| `Url` | `shutterstock_api_explorer/models/url.py` |
| `DownloadVideosErrorBody` | `shutterstock_api_explorer/errors/download_videos_error.py` |

### client.videos.find_similar_videos

- **Route**: `GET /v2/videos/{id}/similar`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def find_similar_videos(id: str, *, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `language` — query · `page` — query · `per_page` — query · `view` — query
- **Returns (parsed)**: `VideoSearchResults`
- **Returns (raw)**: `ApiResult[VideoSearchResults, FindSimilarVideosErrorBody]`
- **Error**: `FindSimilarVideosErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `VideoSearchResults` | `shutterstock_api_explorer/models/video_search_results.py` |
| `FindSimilarVideosErrorBody` | `shutterstock_api_explorer/errors/find_similar_videos_error.py` |

### client.videos.get_updated_videos

- **Route**: `GET /v2/videos/updated`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_updated_videos(*, start_date: str | None = None, end_date: str | None = None, interval: str | None = "1 HOUR", page: int | None = 1, per_page: int | None = 100, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `start_date` — query · `end_date` — query · `interval` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `UpdatedMediaDataList`
- **Returns (raw)**: `ApiResult[UpdatedMediaDataList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `UpdatedMediaDataList` | `shutterstock_api_explorer/models/updated_media_data_list.py` |

### client.videos.get_video

- **Route**: `GET /v2/videos/{id}`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_video(id: str, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `language` — query · `view` — query · `search_id` — query
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetVideoErrorBody]`
- **Error**: `GetVideoErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `Video` | `shutterstock_api_explorer/models/video.py` |
| `GetVideoErrorBody` | `shutterstock_api_explorer/errors/get_video_error.py` |

### client.videos.get_video_collection

- **Route**: `GET /v2/videos/collections/{id}`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_video_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `embed` — query · `share_code` — query
- **Returns (parsed)**: `Collection`
- **Returns (raw)**: `ApiResult[Collection, GetVideoCollectionErrorBody]`
- **Error**: `GetVideoCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `EmbedOrStr` | `shutterstock_api_explorer/models/enums/embed.py` |
| `Collection` | `shutterstock_api_explorer/models/collection.py` |
| `GetVideoCollectionErrorBody` | `shutterstock_api_explorer/errors/get_video_collection_error.py` |

### client.videos.get_video_collection_items

- **Route**: `GET /v2/videos/collections/{id}/items`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_video_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `page` — query · `per_page` — query · `share_code` — query · `sort` — query
- **Returns (parsed)**: `CollectionItemDataList`
- **Returns (raw)**: `ApiResult[CollectionItemDataList, GetVideoCollectionItemsErrorBody]`
- **Error**: `GetVideoCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `CollectionItemDataList` | `shutterstock_api_explorer/models/collection_item_data_list.py` |
| `GetVideoCollectionItemsErrorBody` | `shutterstock_api_explorer/errors/get_video_collection_items_error.py` |

### client.videos.get_video_collection_list

- **Route**: `GET /v2/videos/collections`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_video_collection_list(*, page: int | None = 1, per_page: int | None = 100, embed: list[EmbedOrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query · `embed` — query
- **Returns (parsed)**: `CollectionDataList`
- **Returns (raw)**: `ApiResult[CollectionDataList, GetVideoCollectionListErrorBody]`
- **Error**: `GetVideoCollectionListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `EmbedOrStr` | `shutterstock_api_explorer/models/enums/embed.py` |
| `CollectionDataList` | `shutterstock_api_explorer/models/collection_data_list.py` |
| `GetVideoCollectionListErrorBody` | `shutterstock_api_explorer/errors/get_video_collection_list_error.py` |

### client.videos.get_video_license_list

- **Route**: `GET /v2/videos/licenses`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_video_license_list(*, video_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `video_id` — query · `license` — query · `page` — query · `per_page` — query · `sort` — query · `username` — query · `start_date` — query · `end_date` — query · `download_availability` — query · `team_history` — query
- **Returns (parsed)**: `DownloadHistoryDataList`
- **Returns (raw)**: `ApiResult[DownloadHistoryDataList, GetVideoLicenseListErrorBody]`
- **Error**: `GetVideoLicenseListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `DownloadAvailabilityOrStr` | `shutterstock_api_explorer/models/enums/download_availability.py` |
| `DownloadHistoryDataList` | `shutterstock_api_explorer/models/download_history_data_list.py` |
| `GetVideoLicenseListErrorBody` | `shutterstock_api_explorer/errors/get_video_license_list_error.py` |

### client.videos.get_video_list

- **Route**: `GET /v2/videos`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_video_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query · `view` — query · `search_id` — query
- **Returns (parsed)**: `VideoDataList`
- **Returns (raw)**: `ApiResult[VideoDataList, GetVideoListErrorBody]`
- **Error**: `GetVideoListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `VideoDataList` | `shutterstock_api_explorer/models/video_data_list.py` |
| `GetVideoListErrorBody` | `shutterstock_api_explorer/errors/get_video_list_error.py` |

### client.videos.get_video_suggestions

- **Route**: `GET /v2/videos/search/suggestions`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_video_suggestions(query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query`
- **Params**: `query` — query · `limit` — query
- **Returns (parsed)**: `Suggestions`
- **Returns (raw)**: `ApiResult[Suggestions, GetVideoSuggestionsErrorBody]`
- **Error**: `GetVideoSuggestionsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Suggestions` | `shutterstock_api_explorer/models/suggestions.py` |
| `GetVideoSuggestionsErrorBody` | `shutterstock_api_explorer/errors/get_video_suggestions_error.py` |

### client.videos.license_videos

- **Route**: `POST /v2/videos/licenses`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def license_videos(body: LicenseVideoRequest | LicenseVideoRequestDict, *, subscription_id: str | None = None, size: Size16OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `subscription_id` — query · `size` — query · `search_id` — query · `body` — JSON body
- **Returns (parsed)**: `LicenseVideoResultDataList`
- **Returns (raw)**: `ApiResult[LicenseVideoResultDataList, LicenseVideosErrorBody]`
- **Error**: `LicenseVideosErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LicenseVideoRequest` | `shutterstock_api_explorer/models/license_video_request.py` |
| `LicenseVideoRequestDict` | `shutterstock_api_explorer/models/license_video_request.py` |
| `Size16OrStr` | `shutterstock_api_explorer/models/enums/size16.py` |
| `LicenseVideoResultDataList` | `shutterstock_api_explorer/models/license_video_result_data_list.py` |
| `LicenseVideosErrorBody` | `shutterstock_api_explorer/errors/license_videos_error.py` |

### client.videos.list_video_categories

- **Route**: `GET /v2/videos/categories`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def list_video_categories(*, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `language` — query
- **Returns (parsed)**: `CategoryDataList`
- **Returns (raw)**: `ApiResult[CategoryDataList, ListVideoCategoriesErrorBody]`
- **Error**: `ListVideoCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `CategoryDataList` | `shutterstock_api_explorer/models/category_data_list.py` |
| `ListVideoCategoriesErrorBody` | `shutterstock_api_explorer/errors/list_video_categories_error.py` |

### client.videos.rename_video_collection

- **Route**: `POST /v2/videos/collections/{id}`
- **Auth**: `customer_access_code`
- **Server**: `default`
- **Signature**: `def rename_video_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RenameVideoCollectionErrorBody]`
- **Error**: `RenameVideoCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionUpdateRequest` | `shutterstock_api_explorer/models/collection_update_request.py` |
| `CollectionUpdateRequestDict` | `shutterstock_api_explorer/models/collection_update_request.py` |
| `RenameVideoCollectionErrorBody` | `shutterstock_api_explorer/errors/rename_video_collection_error.py` |

### client.videos.search_videos

- **Route**: `GET /v2/videos/search`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def search_videos(*, added_date: Date | None = None, added_date_start: Date | None = None, added_date_end: Date | None = None, aspect_ratio: AspectRatioOrStr | None = None, category: str | None = None, contributor: list[str] | None = None, contributor_country: list[str] | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, fps: float | None = None, fps_from: float | None = None, fps_to: float | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[License9OrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity5OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, people_model_released: bool | None = None, query: str | None = None, resolution: ResolutionOrStr | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `added_date` — query · `added_date_start` — query · `added_date_end` — query · `aspect_ratio` — query · `category` — query · `contributor` — query · `contributor_country` — query · `duration` — query · `duration_from` — query · `duration_to` — query · `fps` — query · `fps_from` — query · `fps_to` — query · `keyword_safe_search` — query · `language` — query · `license` — query · `model` — query · `orientation` — query · `page` — query · `per_page` — query · `people_age` — query · `people_ethnicity` — query · `people_gender` — query · `people_number` — query · `people_model_released` — query · `query` — query · `resolution` — query · `safe` — query · `sort` — query · `view` — query
- **Returns (parsed)**: `VideoSearchResults`
- **Returns (raw)**: `ApiResult[VideoSearchResults, SearchVideosErrorBody]`
- **Error**: `SearchVideosErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `AspectRatioOrStr` | `shutterstock_api_explorer/models/enums/aspect_ratio.py` |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `License9OrStr` | `shutterstock_api_explorer/models/enums/license9.py` |
| `Orientation2OrStr` | `shutterstock_api_explorer/models/enums/orientation2.py` |
| `PeopleAge2OrStr` | `shutterstock_api_explorer/models/enums/people_age2.py` |
| `PeopleEthnicity5OrStr` | `shutterstock_api_explorer/models/enums/people_ethnicity5.py` |
| `PeopleGender2OrStr` | `shutterstock_api_explorer/models/enums/people_gender2.py` |
| `ResolutionOrStr` | `shutterstock_api_explorer/models/enums/resolution.py` |
| `Sort2OrStr` | `shutterstock_api_explorer/models/enums/sort2.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `VideoSearchResults` | `shutterstock_api_explorer/models/video_search_results.py` |
| `SearchVideosErrorBody` | `shutterstock_api_explorer/errors/search_videos_error.py` |

