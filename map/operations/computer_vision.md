<!-- Generated file — do not edit; regenerated with the SDK. -->

# ComputerVision — operations

Accessor: `client.computer_vision` · Source: `shutterstock_api_explorer/apis/computer_vision.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.computer_vision.get_keywords

- **Route**: `GET /v2/cv/keywords`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_keywords(asset_id: AssetId | AssetIdDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset_id`
- **Params**: `asset_id` — query
- **Returns (parsed)**: `KeywordDataList`
- **Returns (raw)**: `ApiResult[KeywordDataList, GetKeywordsErrorBody]`
- **Error**: `GetKeywordsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 415, anything unmapped]

| Type | Source |
| --- | --- |
| `AssetId` | `shutterstock_api_explorer/models/unions/asset_id.py` |
| `AssetIdDict` | `shutterstock_api_explorer/models/unions/asset_id.py` |
| `KeywordDataList` | `shutterstock_api_explorer/models/keyword_data_list.py` |
| `GetKeywordsErrorBody` | `shutterstock_api_explorer/errors/get_keywords_error.py` |

### client.computer_vision.get_similar_images

- **Route**: `GET /v2/cv/similar/images`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_similar_images(asset_id: str, *, license: list[License9OrStr] | None = None, safe: bool | None = True, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset_id`
- **Params**: `asset_id` — query · `license` — query · `safe` — query · `language` — query · `page` — query · `per_page` — query · `view` — query
- **Returns (parsed)**: `ImageSearchResults`
- **Returns (raw)**: `ApiResult[ImageSearchResults, GetSimilarImagesErrorBody]`
- **Error**: `GetSimilarImagesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `License9OrStr` | `shutterstock_api_explorer/models/enums/license9.py` |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `ImageSearchResults` | `shutterstock_api_explorer/models/image_search_results.py` |
| `GetSimilarImagesErrorBody` | `shutterstock_api_explorer/errors/get_similar_images_error.py` |

### client.computer_vision.get_similar_videos

- **Route**: `GET /v2/cv/similar/videos`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def get_similar_videos(asset_id: str, *, license: list[License9OrStr] | None = None, safe: bool | None = True, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset_id`
- **Params**: `asset_id` — query · `license` — query · `safe` — query · `language` — query · `page` — query · `per_page` — query · `view` — query
- **Returns (parsed)**: `VideoSearchResults`
- **Returns (raw)**: `ApiResult[VideoSearchResults, GetSimilarVideosErrorBody]`
- **Error**: `GetSimilarVideosErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `License9OrStr` | `shutterstock_api_explorer/models/enums/license9.py` |
| `LanguageOrStr` | `shutterstock_api_explorer/models/enums/language.py` |
| `View2OrStr` | `shutterstock_api_explorer/models/enums/view2.py` |
| `VideoSearchResults` | `shutterstock_api_explorer/models/video_search_results.py` |
| `GetSimilarVideosErrorBody` | `shutterstock_api_explorer/errors/get_similar_videos_error.py` |

### client.computer_vision.upload_image

- **Route**: `POST /v2/cv/images`
- **Auth**: `basic` OR `customer_access_code`
- **Server**: `default`
- **Signature**: `def upload_image(body: ImageCreateRequest | ImageCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ComputerVisionImageCreateResponse`
- **Returns (raw)**: `ApiResult[ComputerVisionImageCreateResponse, UploadImageErrorBody]`
- **Error**: `UploadImageErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 413, 415, anything unmapped]

| Type | Source |
| --- | --- |
| `ImageCreateRequest` | `shutterstock_api_explorer/models/image_create_request.py` |
| `ImageCreateRequestDict` | `shutterstock_api_explorer/models/image_create_request.py` |
| `ComputerVisionImageCreateResponse` | `shutterstock_api_explorer/models/computer_vision_image_create_response.py` |
| `UploadImageErrorBody` | `shutterstock_api_explorer/errors/upload_image_error.py` |

