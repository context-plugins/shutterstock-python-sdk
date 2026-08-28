<!-- Generated file — do not edit; regenerated with the SDK. -->

# Images — operations

Accessor: `client.images` · Source: `shutterstock_api_explorer/apis/images.py` · 21 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.images.add_image_collection_items

- **Route**: `POST /v2/images/collections/{id}/items`
- **Server**: `default`
- **Signature**: `def add_image_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddImageCollectionItemsErrorBody]`
- **Error**: `AddImageCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionItemRequest` | `shutterstock_api_explorer/models/collection_item_request.py` |
| `CollectionItemRequestDict` | `shutterstock_api_explorer/models/collection_item_request.py` |
| `AddImageCollectionItemsErrorBody` | `shutterstock_api_explorer/errors/add_image_collection_items_error.py` |

### client.images.bulk_search_images

- **Route**: `POST /v2/bulk_search/images`
- **Server**: `default`
- **Signature**: `def bulk_search_images(body: list[SearchImage | SearchImageDict], *, added_date: Date | None = None, added_date_start: Date | None = None, aspect_ratio_min: float | None = None, aspect_ratio_max: float | None = None, aspect_ratio: float | None = None, added_date_end: Date | None = None, category: str | None = None, color: str | None = None, contributor: list[str] | None = None, contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None, fields: str | None = None, height: int | None = None, height_from: int | None = None, height_to: int | None = None, image_type: list[ImageType2OrStr] | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[LicenseOrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_model_released: bool | None = None, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity2OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, region: RegionModel | RegionModelDict | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, spellcheck_query: bool | None = True, view: View2OrStr | None = None, width: int | None = None, width_from: int | None = None, width_to: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `added_date` — query · `added_date_start` — query · `aspect_ratio_min` — query · `aspect_ratio_max` — query · `aspect_ratio` — query · `added_date_end` — query · `category` — query · `color` — query · `contributor` — query · `contributor_country` — query · `fields` — query · `height` — query · `height_from` — query · `height_to` — query · `image_type` — query · `keyword_safe_search` — query · `language` — query · `license` — query · `model` — query · `orientation` — query · `page` — query · `per_page` — query · `people_model_released` — query · `people_age` — query · `people_ethnicity` — query · `people_gender` — query · `people_number` — query · `region` — query · `safe` — query · `sort` — query · `spellcheck_query` — query · `view` — query · `width` — query · `width_from` — query · `width_to` — query · `body` — JSON body
- **Returns (parsed)**: `BulkImageSearchResults`
- **Returns (raw)**: `ApiResult[BulkImageSearchResults, BulkSearchImagesErrorBody]`
- **Error**: `BulkSearchImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `SearchImage` | `shutterstock_api_explorer/models/search_image.py` |
| `SearchImageDict` | `shutterstock_api_explorer/models/search_image.py` |
| `ContributorCountryModel` | `shutterstock_api_explorer/models/unions/contributor_country_model.py` |
| `ContributorCountryModelDict` | `shutterstock_api_explorer/models/unions/contributor_country_model.py` |
| `ImageType2OrStr` | `shutterstock_api_explorer/models/enums/image_type2.py` |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `LicenseOrStr` | `shutterstock_api_explorer/models/enums/license.py` |
| `Orientation2OrStr` | `shutterstock_api_explorer/models/enums/orientation2.py` |
| `PeopleAge2OrStr` | `shutterstock_api_explorer/models/enums/people_age2.py` |
| `PeopleEthnicity2OrStr` | `shutterstock_api_explorer/models/enums/people_ethnicity2.py` |
| `PeopleGender2OrStr` | `shutterstock_api_explorer/models/enums/people_gender2.py` |
| `RegionModel` | `shutterstock_api_explorer/models/unions/region_model.py` |
| `RegionModelDict` | `shutterstock_api_explorer/models/unions/region_model.py` |
| `Sort2OrStr` | `shutterstock_api_explorer/models/enums/sort2.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `BulkImageSearchResults` | `shutterstock_api_explorer/models/bulk_image_search_results.py` |
| `BulkSearchImagesErrorBody` | `shutterstock_api_explorer/errors/bulk_search_images_error.py` |

### client.images.create_image_collection

- **Route**: `POST /v2/images/collections`
- **Server**: `default`
- **Signature**: `def create_image_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CollectionCreateResponse`
- **Returns (raw)**: `ApiResult[CollectionCreateResponse, CreateImageCollectionErrorBody]`
- **Error**: `CreateImageCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionCreateRequest` | `shutterstock_api_explorer/models/collection_create_request.py` |
| `CollectionCreateRequestDict` | `shutterstock_api_explorer/models/collection_create_request.py` |
| `CollectionCreateResponse` | `shutterstock_api_explorer/models/collection_create_response.py` |
| `CreateImageCollectionErrorBody` | `shutterstock_api_explorer/errors/create_image_collection_error.py` |

### client.images.delete_image_collection

- **Route**: `DELETE /v2/images/collections/{id}`
- **Server**: `default`
- **Signature**: `def delete_image_collection(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteImageCollectionErrorBody]`
- **Error**: `DeleteImageCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteImageCollectionErrorBody` | `shutterstock_api_explorer/errors/delete_image_collection_error.py` |

### client.images.delete_image_collection_items

- **Route**: `DELETE /v2/images/collections/{id}/items`
- **Server**: `default`
- **Signature**: `def delete_image_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `item_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteImageCollectionItemsErrorBody]`
- **Error**: `DeleteImageCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteImageCollectionItemsErrorBody` | `shutterstock_api_explorer/errors/delete_image_collection_items_error.py` |

### client.images.download_image

- **Route**: `POST /v2/images/licenses/{id}/downloads`
- **Server**: `default`
- **Signature**: `def download_image(id: str, body: RedownloadImage | RedownloadImageDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `Url`
- **Returns (raw)**: `ApiResult[Url, DownloadImageErrorBody]`
- **Error**: `DownloadImageErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `RedownloadImage` | `shutterstock_api_explorer/models/redownload_image.py` |
| `RedownloadImageDict` | `shutterstock_api_explorer/models/redownload_image.py` |
| `Url` | `shutterstock_api_explorer/models/url.py` |
| `DownloadImageErrorBody` | `shutterstock_api_explorer/errors/download_image_error.py` |

### client.images.get_image

- **Route**: `GET /v2/images/{id}`
- **Server**: `default`
- **Signature**: `def get_image(id: str, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `language` — query · `view` — query · `search_id` — query
- **Returns (parsed)**: `Image`
- **Returns (raw)**: `ApiResult[Image, GetImageErrorBody]`
- **Error**: `GetImageErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `Image` | `shutterstock_api_explorer/models/image.py` |
| `GetImageErrorBody` | `shutterstock_api_explorer/errors/get_image_error.py` |

### client.images.get_image_collection

- **Route**: `GET /v2/images/collections/{id}`
- **Server**: `default`
- **Signature**: `def get_image_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `embed` — query · `share_code` — query
- **Returns (parsed)**: `Collection`
- **Returns (raw)**: `ApiResult[Collection, GetImageCollectionErrorBody]`
- **Error**: `GetImageCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `EmbedOrStr` | `shutterstock_api_explorer/models/enums/embed.py` |
| `Collection` | `shutterstock_api_explorer/models/collection.py` |
| `GetImageCollectionErrorBody` | `shutterstock_api_explorer/errors/get_image_collection_error.py` |

### client.images.get_image_collection_items

- **Route**: `GET /v2/images/collections/{id}/items`
- **Server**: `default`
- **Signature**: `def get_image_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `page` — query · `per_page` — query · `share_code` — query · `sort` — query
- **Returns (parsed)**: `CollectionItemDataList`
- **Returns (raw)**: `ApiResult[CollectionItemDataList, GetImageCollectionItemsErrorBody]`
- **Error**: `GetImageCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `CollectionItemDataList` | `shutterstock_api_explorer/models/collection_item_data_list.py` |
| `GetImageCollectionItemsErrorBody` | `shutterstock_api_explorer/errors/get_image_collection_items_error.py` |

### client.images.get_image_collection_list

- **Route**: `GET /v2/images/collections`
- **Server**: `default`
- **Signature**: `def get_image_collection_list(*, embed: list[EmbedOrStr] | None = None, page: int | None = 1, per_page: int | None = 100, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `embed` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `CollectionDataList`
- **Returns (raw)**: `ApiResult[CollectionDataList, GetImageCollectionListErrorBody]`
- **Error**: `GetImageCollectionListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `EmbedOrStr` | `shutterstock_api_explorer/models/enums/embed.py` |
| `CollectionDataList` | `shutterstock_api_explorer/models/collection_data_list.py` |
| `GetImageCollectionListErrorBody` | `shutterstock_api_explorer/errors/get_image_collection_list_error.py` |

### client.images.get_image_keyword_suggestions

- **Route**: `POST /v2/images/search/suggestions`
- **Server**: `default`
- **Signature**: `def get_image_keyword_suggestions(body: SearchEntitiesRequest | SearchEntitiesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchEntitiesResponse`
- **Returns (raw)**: `ApiResult[SearchEntitiesResponse, GetImageKeywordSuggestionsErrorBody]`
- **Error**: `GetImageKeywordSuggestionsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `SearchEntitiesRequest` | `shutterstock_api_explorer/models/search_entities_request.py` |
| `SearchEntitiesRequestDict` | `shutterstock_api_explorer/models/search_entities_request.py` |
| `SearchEntitiesResponse` | `shutterstock_api_explorer/models/search_entities_response.py` |
| `GetImageKeywordSuggestionsErrorBody` | `shutterstock_api_explorer/errors/get_image_keyword_suggestions_error.py` |

### client.images.get_image_license_list

- **Route**: `GET /v2/images/licenses`
- **Server**: `default`
- **Signature**: `def get_image_license_list(*, image_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `image_id` — query · `license` — query · `page` — query · `per_page` — query · `sort` — query · `username` — query · `start_date` — query · `end_date` — query · `download_availability` — query · `team_history` — query
- **Returns (parsed)**: `DownloadHistoryDataList`
- **Returns (raw)**: `ApiResult[DownloadHistoryDataList, GetImageLicenseListErrorBody]`
- **Error**: `GetImageLicenseListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `DownloadAvailabilityOrStr` | `shutterstock_api_explorer/models/enums/download_availability.py` |
| `DownloadHistoryDataList` | `shutterstock_api_explorer/models/download_history_data_list.py` |
| `GetImageLicenseListErrorBody` | `shutterstock_api_explorer/errors/get_image_license_list_error.py` |

### client.images.get_image_list

- **Route**: `GET /v2/images`
- **Server**: `default`
- **Signature**: `def get_image_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query · `view` — query · `search_id` — query
- **Returns (parsed)**: `ImageDataList`
- **Returns (raw)**: `ApiResult[ImageDataList, GetImageListErrorBody]`
- **Error**: `GetImageListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `ImageDataList` | `shutterstock_api_explorer/models/image_data_list.py` |
| `GetImageListErrorBody` | `shutterstock_api_explorer/errors/get_image_list_error.py` |

### client.images.get_image_recommendations

- **Route**: `GET /v2/images/recommendations`
- **Server**: `default`
- **Signature**: `def get_image_recommendations(id: list[str], *, max_items: int | None = 20, safe: bool | None = True, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query · `max_items` — query · `safe` — query
- **Returns (parsed)**: `RecommendationDataList`
- **Returns (raw)**: `ApiResult[RecommendationDataList, GetImageRecommendationsErrorBody]`
- **Error**: `GetImageRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `RecommendationDataList` | `shutterstock_api_explorer/models/recommendation_data_list.py` |
| `GetImageRecommendationsErrorBody` | `shutterstock_api_explorer/errors/get_image_recommendations_error.py` |

### client.images.get_image_suggestions

- **Route**: `GET /v2/images/search/suggestions`
- **Server**: `default`
- **Signature**: `def get_image_suggestions(query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query`
- **Params**: `query` — query · `limit` — query
- **Returns (parsed)**: `Suggestions`
- **Returns (raw)**: `ApiResult[Suggestions, GetImageSuggestionsErrorBody]`
- **Error**: `GetImageSuggestionsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Suggestions` | `shutterstock_api_explorer/models/suggestions.py` |
| `GetImageSuggestionsErrorBody` | `shutterstock_api_explorer/errors/get_image_suggestions_error.py` |

### client.images.get_updated_images

- **Route**: `GET /v2/images/updated`
- **Server**: `default`
- **Signature**: `def get_updated_images(*, type_: list[Type4OrStr] | None = None, start_date: str | None = None, end_date: str | None = None, interval: str | None = "1 HOUR", page: int | None = 1, per_page: int | None = 100, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `type_` — query `type` · `start_date` — query · `end_date` — query · `interval` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `UpdatedMediaDataList`
- **Returns (raw)**: `ApiResult[UpdatedMediaDataList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Type4OrStr` | `shutterstock_api_explorer/models/enums/type4.py` |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `UpdatedMediaDataList` | `shutterstock_api_explorer/models/updated_media_data_list.py` |

### client.images.license_images

- **Route**: `POST /v2/images/licenses`
- **Server**: `default`
- **Signature**: `def license_images(body: LicenseImageRequest | LicenseImageRequestDict, *, subscription_id: str | None = None, format: Format15OrStr | None = None, size: Size12OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `subscription_id` — query · `format` — query · `size` — query · `search_id` — query · `body` — JSON body
- **Returns (parsed)**: `LicenseImageResultDataList`
- **Returns (raw)**: `ApiResult[LicenseImageResultDataList, LicenseImagesErrorBody]`
- **Error**: `LicenseImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LicenseImageRequest` | `shutterstock_api_explorer/models/license_image_request.py` |
| `LicenseImageRequestDict` | `shutterstock_api_explorer/models/license_image_request.py` |
| `Format15OrStr` | `shutterstock_api_explorer/models/enums/format15.py` |
| `Size12OrStr` | `shutterstock_api_explorer/models/enums/size12.py` |
| `LicenseImageResultDataList` | `shutterstock_api_explorer/models/license_image_result_data_list.py` |
| `LicenseImagesErrorBody` | `shutterstock_api_explorer/errors/license_images_error.py` |

### client.images.list_image_categories

- **Route**: `GET /v2/images/categories`
- **Server**: `default`
- **Signature**: `def list_image_categories(*, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `language` — query
- **Returns (parsed)**: `CategoryDataList`
- **Returns (raw)**: `ApiResult[CategoryDataList, ListImageCategoriesErrorBody]`
- **Error**: `ListImageCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `CategoryDataList` | `shutterstock_api_explorer/models/category_data_list.py` |
| `ListImageCategoriesErrorBody` | `shutterstock_api_explorer/errors/list_image_categories_error.py` |

### client.images.list_similar_images

- **Route**: `GET /v2/images/{id}/similar`
- **Server**: `default`
- **Signature**: `def list_similar_images(id: str, *, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `language` — query · `page` — query · `per_page` — query · `view` — query
- **Returns (parsed)**: `ImageSearchResults`
- **Returns (raw)**: `ApiResult[ImageSearchResults, ListSimilarImagesErrorBody]`
- **Error**: `ListSimilarImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `ImageSearchResults` | `shutterstock_api_explorer/models/image_search_results.py` |
| `ListSimilarImagesErrorBody` | `shutterstock_api_explorer/errors/list_similar_images_error.py` |

### client.images.rename_image_collection

- **Route**: `POST /v2/images/collections/{id}`
- **Server**: `default`
- **Signature**: `def rename_image_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RenameImageCollectionErrorBody]`
- **Error**: `RenameImageCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionUpdateRequest` | `shutterstock_api_explorer/models/collection_update_request.py` |
| `CollectionUpdateRequestDict` | `shutterstock_api_explorer/models/collection_update_request.py` |
| `RenameImageCollectionErrorBody` | `shutterstock_api_explorer/errors/rename_image_collection_error.py` |

### client.images.search_images

- **Route**: `GET /v2/images/search`
- **Server**: `default`
- **Signature**: `def search_images(*, library: list[LibraryOrStr] | None = None, added_date: Date | None = None, added_date_start: Date | None = None, aspect_ratio_min: float | None = None, aspect_ratio_max: float | None = None, aspect_ratio: float | None = None, added_date_end: Date | None = None, category: str | None = None, color: str | None = None, contributor: list[str] | None = None, contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None, fields: str | None = None, height: int | None = None, height_from: int | None = None, height_to: int | None = None, image_type: list[ImageType2OrStr] | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[LicenseOrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_model_released: bool | None = None, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity2OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, query: str | None = None, region: RegionModel | RegionModelDict | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, spellcheck_query: bool | None = True, view: View2OrStr | None = None, width: int | None = None, width_from: int | None = None, width_to: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `library` — query · `added_date` — query · `added_date_start` — query · `aspect_ratio_min` — query · `aspect_ratio_max` — query · `aspect_ratio` — query · `added_date_end` — query · `category` — query · `color` — query · `contributor` — query · `contributor_country` — query · `fields` — query · `height` — query · `height_from` — query · `height_to` — query · `image_type` — query · `keyword_safe_search` — query · `language` — query · `license` — query · `model` — query · `orientation` — query · `page` — query · `per_page` — query · `people_model_released` — query · `people_age` — query · `people_ethnicity` — query · `people_gender` — query · `people_number` — query · `query` — query · `region` — query · `safe` — query · `sort` — query · `spellcheck_query` — query · `view` — query · `width` — query · `width_from` — query · `width_to` — query
- **Returns (parsed)**: `ImageSearchResults`
- **Returns (raw)**: `ApiResult[ImageSearchResults, SearchImagesErrorBody]`
- **Error**: `SearchImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LibraryOrStr` | `shutterstock_api_explorer/models/enums/library.py` |
| `ContributorCountryModel` | `shutterstock_api_explorer/models/unions/contributor_country_model.py` |
| `ContributorCountryModelDict` | `shutterstock_api_explorer/models/unions/contributor_country_model.py` |
| `ImageType2OrStr` | `shutterstock_api_explorer/models/enums/image_type2.py` |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `LicenseOrStr` | `shutterstock_api_explorer/models/enums/license.py` |
| `Orientation2OrStr` | `shutterstock_api_explorer/models/enums/orientation2.py` |
| `PeopleAge2OrStr` | `shutterstock_api_explorer/models/enums/people_age2.py` |
| `PeopleEthnicity2OrStr` | `shutterstock_api_explorer/models/enums/people_ethnicity2.py` |
| `PeopleGender2OrStr` | `shutterstock_api_explorer/models/enums/people_gender2.py` |
| `RegionModel` | `shutterstock_api_explorer/models/unions/region_model.py` |
| `RegionModelDict` | `shutterstock_api_explorer/models/unions/region_model.py` |
| `Sort2OrStr` | `shutterstock_api_explorer/models/enums/sort2.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `ImageSearchResults` | `shutterstock_api_explorer/models/image_search_results.py` |
| `SearchImagesErrorBody` | `shutterstock_api_explorer/errors/search_images_error.py` |

