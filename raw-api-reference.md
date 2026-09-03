# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [ShutterstockApiExplorerClient](shutterstock_api_explorer/client.py)

## AudioApi

> Source: [AudioApi](shutterstock_api_explorer/apis/audio_api.py)

<details>
<summary><code>def add_track_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, AddTrackCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint adds one or more tracks to a collection by track IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.add_track_collection_items(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddTrackCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.add_track_collection_items(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddTrackCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>body</code> | <code>[CollectionItemRequest](shutterstock_api_explorer/models/collection_item_request.py) \| [CollectionItemRequestDict](shutterstock_api_explorer/models/collection_item_request.py)</code> | List of items to add to collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [AddTrackCollectionItemsErrorBody](shutterstock_api_explorer/errors/add_track_collection_items_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[AddTrackCollectionItemsErrorBody](shutterstock_api_explorer/errors/add_track_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_track_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionCreateResponse, CreateTrackCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint creates one or more collections (soundboxes). To add tracks, use `POST /v2/audio/collections/{id}/items`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.create_track_collection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateTrackCollectionErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.create_track_collection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateTrackCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CollectionCreateRequest](shutterstock_api_explorer/models/collection_create_request.py) \| [CollectionCreateRequestDict](shutterstock_api_explorer/models/collection_create_request.py)</code> | Collection metadata |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionCreateResponse](shutterstock_api_explorer/models/collection_create_response.py), [CreateTrackCollectionErrorBody](shutterstock_api_explorer/errors/create_track_collection_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionCreateResponse](shutterstock_api_explorer/models/collection_create_response.py)</code> -- Successfully created audio collection

**On `Failure`**: `error` is <code>[CreateTrackCollectionErrorBody](shutterstock_api_explorer/errors/create_track_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_track_collection(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteTrackCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint deletes a collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.delete_track_collection(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteTrackCollectionErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.delete_track_collection(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteTrackCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [DeleteTrackCollectionErrorBody](shutterstock_api_explorer/errors/delete_track_collection_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteTrackCollectionErrorBody](shutterstock_api_explorer/errors/delete_track_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_track_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteTrackCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint removes one or more tracks from a collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.delete_track_collection_items(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteTrackCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.delete_track_collection_items(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteTrackCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>item_id</code> | <code>list&#91;str&#93; \| None</code> | One or more item IDs to remove from the collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [DeleteTrackCollectionItemsErrorBody](shutterstock_api_explorer/errors/delete_track_collection_items_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteTrackCollectionItemsErrorBody](shutterstock_api_explorer/errors/delete_track_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_tracks(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AudioUrl, DownloadTracksErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint redownloads tracks that you have already received a license for. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.download_tracks(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AudioUrl
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadTracksErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.download_tracks(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AudioUrl
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | License ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[AudioUrl](shutterstock_api_explorer/models/audio_url.py), [DownloadTracksErrorBody](shutterstock_api_explorer/errors/download_tracks_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AudioUrl](shutterstock_api_explorer/models/audio_url.py)</code> -- OK

**On `Failure`**: `error` is <code>[DownloadTracksErrorBody](shutterstock_api_explorer/errors/download_tracks_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track(id: int, *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Audio, GetTrackErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint shows information about a track, including its genres, instruments, and other attributes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.get_track(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Audio
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.get_track(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Audio
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>int</code> | Audio track ID |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Audio](shutterstock_api_explorer/models/audio.py), [GetTrackErrorBody](shutterstock_api_explorer/errors/get_track_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Audio](shutterstock_api_explorer/models/audio.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetTrackErrorBody](shutterstock_api_explorer/errors/get_track_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Collection, GetTrackCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets more detailed information about a collection, including the number of items in it and when it was last updated. To get the tracks in collections, use `GET /v2/audio/collections/{id}/items`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.get_track_collection(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Collection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackCollectionErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.get_track_collection(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Collection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock_api_explorer/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve a shared collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Collection](shutterstock_api_explorer/models/collection.py), [GetTrackCollectionErrorBody](shutterstock_api_explorer/errors/get_track_collection_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Collection](shutterstock_api_explorer/models/collection.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetTrackCollectionErrorBody](shutterstock_api_explorer/errors/get_track_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionItemDataList, GetTrackCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the IDs of tracks in a collection and the date that each was added.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.get_track_collection_items(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.get_track_collection_items(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve the contents of a shared collection<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionItemDataList](shutterstock_api_explorer/models/collection_item_data_list.py), [GetTrackCollectionItemsErrorBody](shutterstock_api_explorer/errors/get_track_collection_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionItemDataList](shutterstock_api_explorer/models/collection_item_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetTrackCollectionItemsErrorBody](shutterstock_api_explorer/errors/get_track_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_collection_list(*, page: int | None = 1, per_page: int | None = 100, embed: list[EmbedOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionDataList, GetTrackCollectionListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists your collections of audio tracks and their basic attributes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.get_track_collection_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackCollectionListErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.get_track_collection_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackCollectionListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock_api_explorer/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionDataList](shutterstock_api_explorer/models/collection_data_list.py), [GetTrackCollectionListErrorBody](shutterstock_api_explorer/errors/get_track_collection_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionDataList](shutterstock_api_explorer/models/collection_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetTrackCollectionListErrorBody](shutterstock_api_explorer/errors/get_track_collection_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_license_list(*, audio_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DownloadHistoryDataList, GetTrackLicenseListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists existing licenses. You can filter the results according to the track ID to see if you have an existing license for a specific track.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.get_track_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackLicenseListErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.get_track_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackLicenseListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>audio_id</code> | <code>str \| None</code> | Show licenses for the specified track ID<br>**Default**: <code>None</code> |
| <code>license</code> | <code>str \| None</code> | Restrict results by license.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock_api_explorer/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py), [GetTrackLicenseListErrorBody](shutterstock_api_explorer/errors/get_track_license_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetTrackLicenseListErrorBody](shutterstock_api_explorer/errors/get_track_license_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AudioDataList, GetTrackListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists information about one or more audio tracks, including the description and publication date.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.get_track_list(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AudioDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackListErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.get_track_list(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AudioDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more audio IDs |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[AudioDataList](shutterstock_api_explorer/models/audio_data_list.py), [GetTrackListErrorBody](shutterstock_api_explorer/errors/get_track_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AudioDataList](shutterstock_api_explorer/models/audio_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetTrackListErrorBody](shutterstock_api_explorer/errors/get_track_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_track(body: LicenseAudioRequest | LicenseAudioRequestDict, *, license: License10OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LicenseAudioResultDataList, LicenseTrackErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.license_track(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseAudioResultDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseTrackErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.license_track(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseAudioResultDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseAudioRequest](shutterstock_api_explorer/models/license_audio_request.py) \| [LicenseAudioRequestDict](shutterstock_api_explorer/models/license_audio_request.py)</code> | Tracks to license |
| <code>license</code> | <code>[License10OrStr](shutterstock_api_explorer/models/enums/license10.py) \| None</code> | License type<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that led to licensing this track<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[LicenseAudioResultDataList](shutterstock_api_explorer/models/license_audio_result_data_list.py), [LicenseTrackErrorBody](shutterstock_api_explorer/errors/license_track_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LicenseAudioResultDataList](shutterstock_api_explorer/models/license_audio_result_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[LicenseTrackErrorBody](shutterstock_api_explorer/errors/license_track_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_genres(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenreList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns a list of all audio genres.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.list_genres()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenreList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.list_genres()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenreList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>str \| None</code> | Which language the genres will be returned<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[GenreList](shutterstock_api_explorer/models/genre_list.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenreList](shutterstock_api_explorer/models/genre_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_instruments(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InstrumentList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns a list of all audio instruments.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.list_instruments()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstrumentList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.list_instruments()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstrumentList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>str \| None</code> | Which language the instruments will be returned in<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[InstrumentList](shutterstock_api_explorer/models/instrument_list.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InstrumentList](shutterstock_api_explorer/models/instrument_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_moods(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MoodList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns a list of all audio moods.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.list_moods()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MoodList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.list_moods()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MoodList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>str \| None</code> | Which language the moods will be returned in<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[MoodList](shutterstock_api_explorer/models/mood_list.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MoodList](shutterstock_api_explorer/models/mood_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def rename_track_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RenameTrackCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint sets a new name for a collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.rename_track_collection(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RenameTrackCollectionErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.rename_track_collection(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RenameTrackCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>body</code> | <code>[CollectionUpdateRequest](shutterstock_api_explorer/models/collection_update_request.py) \| [CollectionUpdateRequestDict](shutterstock_api_explorer/models/collection_update_request.py)</code> | Collection changes |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [RenameTrackCollectionErrorBody](shutterstock_api_explorer/errors/rename_track_collection_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RenameTrackCollectionErrorBody](shutterstock_api_explorer/errors/rename_track_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_tracks(*, artists: list[str] | None = None, bpm: int | None = None, bpm_from: int | None = None, bpm_to: int | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, genre: list[str] | None = None, is_instrumental: bool | None = None, instruments: list[str] | None = None, moods: list[str] | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, sort: Sort12OrStr | None = None, sort_order: SortOrderOrStr | None = None, vocal_description: str | None = None, view: View2OrStr | None = None, fields: str | None = None, library: Library1OrStr | None = None, language: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AudioSearchResults, SearchTracksErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.audio_api.with_raw_response.search_tracks()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AudioSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchTracksErrorBody
```

**Async**

```python
result = await async_client.audio_api.with_raw_response.search_tracks()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AudioSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>artists</code> | <code>list&#91;str&#93; \| None</code> | Show tracks with one of the specified artist names or IDs<br>**Default**: <code>None</code> |
| <code>bpm</code> | <code>int \| None</code> | (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute<br>**Default**: <code>None</code> |
| <code>bpm_from</code> | <code>int \| None</code> | Show tracks with the specified beats per minute or faster<br>**Default**: <code>None</code> |
| <code>bpm_to</code> | <code>int \| None</code> | Show tracks with the specified beats per minute or slower<br>**Default**: <code>None</code> |
| <code>duration</code> | <code>int \| None</code> | Show tracks with the specified duration in seconds<br>**Default**: <code>None</code> |
| <code>duration_from</code> | <code>int \| None</code> | Show tracks with the specified duration or longer in seconds<br>**Default**: <code>None</code> |
| <code>duration_to</code> | <code>int \| None</code> | Show tracks with the specified duration or shorter in seconds<br>**Default**: <code>None</code> |
| <code>genre</code> | <code>list&#91;str&#93; \| None</code> | Show tracks with each of the specified genres; to get the list of genres, use `GET /v2/audio/genres`<br>**Default**: <code>None</code> |
| <code>is_instrumental</code> | <code>bool \| None</code> | Show instrumental music only<br>**Default**: <code>None</code> |
| <code>instruments</code> | <code>list&#91;str&#93; \| None</code> | Show tracks with each of the specified instruments; to get the list of instruments, use `GET /v2/audio/instruments`<br>**Default**: <code>None</code> |
| <code>moods</code> | <code>list&#91;str&#93; \| None</code> | Show tracks with each of the specified moods; to get the list of moods, use `GET /v2/audio/moods`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort12OrStr](shutterstock_api_explorer/models/enums/sort12.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](shutterstock_api_explorer/models/enums/sort_order.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>vocal_description</code> | <code>str \| None</code> | Show tracks with the specified vocal description (male, female)<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Fields to display in the response; see the documentation for the fields parameter in the overview section<br>**Default**: <code>None</code> |
| <code>library</code> | <code>[Library1OrStr](shutterstock_api_explorer/models/enums/library1.py) \| None</code> | Which library to search<br>**Default**: <code>None</code> |
| <code>language</code> | <code>str \| None</code> | Which language to search in<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[AudioSearchResults](shutterstock_api_explorer/models/audio_search_results.py), [SearchTracksErrorBody](shutterstock_api_explorer/errors/search_tracks_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AudioSearchResults](shutterstock_api_explorer/models/audio_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[SearchTracksErrorBody](shutterstock_api_explorer/errors/search_tracks_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Catalog

> Source: [Catalog](shutterstock_api_explorer/apis/catalog.py)

<details>
<summary><code>def add_to_collection(collection_id: str, body: CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CatalogCollection, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user's account's catalog.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.add_to_collection(collection_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.add_to_collection(collection_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>collection_id</code> | <code>str</code> | The ID of the collection to add assets to |
| <code>body</code> | <code>[CreateCatalogCollectionItems](shutterstock_api_explorer/models/create_catalog_collection_items.py) \| [CreateCatalogCollectionItemsDict](shutterstock_api_explorer/models/create_catalog_collection_items.py)</code> | Collection item attributes to add to collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CatalogCollection](shutterstock_api_explorer/models/catalog_collection.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CatalogCollection](shutterstock_api_explorer/models/catalog_collection.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_collection(body: CreateCatalogCollection | CreateCatalogCollectionDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CatalogCollection, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later, use `PATCH /v2/catalog/collections/{collection_id}/items`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.create_collection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.create_collection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateCatalogCollection](shutterstock_api_explorer/models/create_catalog_collection.py) \| [CreateCatalogCollectionDict](shutterstock_api_explorer/models/create_catalog_collection.py)</code> | Create a catalog collection and, optionally, add items. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CatalogCollection](shutterstock_api_explorer/models/catalog_collection.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CatalogCollection](shutterstock_api_explorer/models/catalog_collection.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_collection(collection_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint deletes a catalog collection. It does not remove the assets from the user's account's catalog.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.delete_collection(collection_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteCollectionErrorBody
```

**Async**

```python
result = await async_client.catalog.with_raw_response.delete_collection(collection_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>collection_id</code> | <code>str</code> | The ID of the collection to delete |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [DeleteCollectionErrorBody](shutterstock_api_explorer/errors/delete_collection_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteCollectionErrorBody](shutterstock_api_explorer/errors/delete_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_from_collection(collection_id: str, body: RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CatalogCollection, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint removes assets from a catalog collection. It does not remove the assets from the user's account's catalog.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.delete_from_collection(collection_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.delete_from_collection(collection_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>collection_id</code> | <code>str</code> | The ID of the collection to remove assets from |
| <code>body</code> | <code>[RemoveCatalogCollectionItems](shutterstock_api_explorer/models/remove_catalog_collection_items.py) \| [RemoveCatalogCollectionItemsDict](shutterstock_api_explorer/models/remove_catalog_collection_items.py)</code> | Items to remove from the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CatalogCollection](shutterstock_api_explorer/models/catalog_collection.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CatalogCollection](shutterstock_api_explorer/models/catalog_collection.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_collections(*, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, shared: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CatalogCollectionDataList, GetCollectionsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns a list of catalog collections.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.get_collections()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCollectionsErrorBody
```

**Async**

```python
result = await async_client.catalog.with_raw_response.get_collections()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCollectionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>shared</code> | <code>bool \| None</code> | Set to true to omit collections that you own and return only collections  that are shared with you<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CatalogCollectionDataList](shutterstock_api_explorer/models/catalog_collection_data_list.py), [GetCollectionsErrorBody](shutterstock_api_explorer/errors/get_collections_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CatalogCollectionDataList](shutterstock_api_explorer/models/catalog_collection_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetCollectionsErrorBody](shutterstock_api_explorer/errors/get_collections_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_catalog(*, sort: Sort5OrStr | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, collection_id: list[str] | None = None, asset_type: list[AssetTypeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CatalogCollectionItemDataList, SearchCatalogErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint searches for assets in the account's catalog. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.search_catalog()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchCatalogErrorBody
```

**Async**

```python
result = await async_client.catalog.with_raw_response.search_catalog()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchCatalogErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces<br>**Default**: <code>None</code> |
| <code>collection_id</code> | <code>list&#91;str&#93; \| None</code> | Filter by collection id<br>**Default**: <code>None</code> |
| <code>asset_type</code> | <code>list&#91;[AssetTypeOrStr](shutterstock_api_explorer/models/enums/asset_type.py)&#93; \| None</code> | Filter by asset type<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CatalogCollectionItemDataList](shutterstock_api_explorer/models/catalog_collection_item_data_list.py), [SearchCatalogErrorBody](shutterstock_api_explorer/errors/search_catalog_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CatalogCollectionItemDataList](shutterstock_api_explorer/models/catalog_collection_item_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[SearchCatalogErrorBody](shutterstock_api_explorer/errors/search_catalog_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_collection(collection_id: str, body: UpdateCatalogCollection | UpdateCatalogCollectionDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CatalogCollection, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint updates the metadata of a catalog collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.update_collection(collection_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.update_collection(collection_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>collection_id</code> | <code>str</code> | ID of collection that needs to be modified |
| <code>body</code> | <code>[UpdateCatalogCollection](shutterstock_api_explorer/models/update_catalog_collection.py) \| [UpdateCatalogCollectionDict](shutterstock_api_explorer/models/update_catalog_collection.py)</code> | Collections Metadata to update |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CatalogCollection](shutterstock_api_explorer/models/catalog_collection.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CatalogCollection](shutterstock_api_explorer/models/catalog_collection.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ComputerVision

> Source: [ComputerVision](shutterstock_api_explorer/apis/computer_vision.py)

<details>
<summary><code>def get_keywords(asset_id: AssetId | AssetIdDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[KeywordDataList, GetKeywordsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns a list of suggested keywords for a media item that you specify or upload.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.computer_vision.with_raw_response.get_keywords(asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type KeywordDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetKeywordsErrorBody
```

**Async**

```python
result = await async_client.computer_vision.with_raw_response.get_keywords(asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type KeywordDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetKeywordsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset_id</code> | <code>[AssetId](shutterstock_api_explorer/models/unions/asset_id.py) \| [AssetIdDict](shutterstock_api_explorer/models/unions/asset_id.py)</code> | The asset ID or upload ID to suggest keywords for |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[KeywordDataList](shutterstock_api_explorer/models/keyword_data_list.py), [GetKeywordsErrorBody](shutterstock_api_explorer/errors/get_keywords_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[KeywordDataList](shutterstock_api_explorer/models/keyword_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetKeywordsErrorBody](shutterstock_api_explorer/errors/get_keywords_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 415 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_similar_images(asset_id: str, *, license: list[License9OrStr] | None = None, safe: bool | None = True, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ImageSearchResults, GetSimilarImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns images that are visually similar to an image that you specify or upload.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.computer_vision.with_raw_response.get_similar_images(asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ImageSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSimilarImagesErrorBody
```

**Async**

```python
result = await async_client.computer_vision.with_raw_response.get_similar_images(asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ImageSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSimilarImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset_id</code> | <code>str</code> | The asset ID or upload ID to find similar images for |
| <code>license</code> | <code>list&#91;[License9OrStr](shutterstock_api_explorer/models/enums/license9.py)&#93; \| None</code> | Show only images with the specified license<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[ImageSearchResults](shutterstock_api_explorer/models/image_search_results.py), [GetSimilarImagesErrorBody](shutterstock_api_explorer/errors/get_similar_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ImageSearchResults](shutterstock_api_explorer/models/image_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetSimilarImagesErrorBody](shutterstock_api_explorer/errors/get_similar_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_similar_videos(asset_id: str, *, license: list[License9OrStr] | None = None, safe: bool | None = True, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[VideoSearchResults, GetSimilarVideosErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns videos that are visually similar to an image that you specify or upload.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.computer_vision.with_raw_response.get_similar_videos(asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VideoSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSimilarVideosErrorBody
```

**Async**

```python
result = await async_client.computer_vision.with_raw_response.get_similar_videos(asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VideoSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSimilarVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset_id</code> | <code>str</code> | The asset ID or upload ID to find similar videos for |
| <code>license</code> | <code>list&#91;[License9OrStr](shutterstock_api_explorer/models/enums/license9.py)&#93; \| None</code> | Show only videos with the specified license<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[VideoSearchResults](shutterstock_api_explorer/models/video_search_results.py), [GetSimilarVideosErrorBody](shutterstock_api_explorer/errors/get_similar_videos_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[VideoSearchResults](shutterstock_api_explorer/models/video_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetSimilarVideosErrorBody](shutterstock_api_explorer/errors/get_similar_videos_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upload_image(body: ImageCreateRequest | ImageCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ComputerVisionImageCreateResponse, UploadImageErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.computer_vision.with_raw_response.upload_image(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ComputerVisionImageCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UploadImageErrorBody
```

**Async**

```python
result = await async_client.computer_vision.with_raw_response.upload_image(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ComputerVisionImageCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UploadImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ImageCreateRequest](shutterstock_api_explorer/models/image_create_request.py) \| [ImageCreateRequestDict](shutterstock_api_explorer/models/image_create_request.py)</code> | A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[ComputerVisionImageCreateResponse](shutterstock_api_explorer/models/computer_vision_image_create_response.py), [UploadImageErrorBody](shutterstock_api_explorer/errors/upload_image_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ComputerVisionImageCreateResponse](shutterstock_api_explorer/models/computer_vision_image_create_response.py)</code> -- Created

**On `Failure`**: `error` is <code>[UploadImageErrorBody](shutterstock_api_explorer/errors/upload_image_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 413, 415 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Contributors

> Source: [Contributors](shutterstock_api_explorer/apis/contributors.py)

<details>
<summary><code>def get_contributor(contributor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ContributorProfile, GetContributorErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint shows information about a single contributor, including contributor type, equipment they use, and other attributes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.contributors.with_raw_response.get_contributor(contributor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ContributorProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorErrorBody
```

**Async**

```python
result = await async_client.contributors.with_raw_response.get_contributor(contributor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ContributorProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>contributor_id</code> | <code>str</code> | Contributor ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[ContributorProfile](shutterstock_api_explorer/models/contributor_profile.py), [GetContributorErrorBody](shutterstock_api_explorer/errors/get_contributor_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ContributorProfile](shutterstock_api_explorer/models/contributor_profile.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetContributorErrorBody](shutterstock_api_explorer/errors/get_contributor_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_contributor_collection_items(contributor_id: str, id: str, *, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionItemDataList, GetContributorCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the IDs of items in a contributor's collection and the date that each was added.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.contributors.with_raw_response.get_contributor_collection_items(contributor_id, id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.contributors.with_raw_response.get_contributor_collection_items(contributor_id, id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>contributor_id</code> | <code>str</code> | Contributor ID |
| <code>id</code> | <code>str</code> | Collection ID that belongs to the contributor |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionItemDataList](shutterstock_api_explorer/models/collection_item_data_list.py), [GetContributorCollectionItemsErrorBody](shutterstock_api_explorer/errors/get_contributor_collection_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionItemDataList](shutterstock_api_explorer/models/collection_item_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetContributorCollectionItemsErrorBody](shutterstock_api_explorer/errors/get_contributor_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_contributor_collections(contributor_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Collection, GetContributorCollectionsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets more detailed information about a contributor's collection, including its cover image, timestamps for its creation, and most recent update. To get the items in collections, use GET /v2/contributors/{contributor_id}/collections/{id}/items.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.contributors.with_raw_response.get_contributor_collections(contributor_id, id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Collection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorCollectionsErrorBody
```

**Async**

```python
result = await async_client.contributors.with_raw_response.get_contributor_collections(contributor_id, id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Collection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorCollectionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>contributor_id</code> | <code>str</code> | Contributor ID |
| <code>id</code> | <code>str</code> | Collection ID that belongs to the contributor |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Collection](shutterstock_api_explorer/models/collection.py), [GetContributorCollectionsErrorBody](shutterstock_api_explorer/errors/get_contributor_collections_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Collection](shutterstock_api_explorer/models/collection.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetContributorCollectionsErrorBody](shutterstock_api_explorer/errors/get_contributor_collections_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_contributor_collections_list(contributor_id: str, *, sort: Sort24OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionDataList, GetContributorCollectionsListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists collections based on contributor ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.contributors.with_raw_response.get_contributor_collections_list(contributor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorCollectionsListErrorBody
```

**Async**

```python
result = await async_client.contributors.with_raw_response.get_contributor_collections_list(contributor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorCollectionsListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>contributor_id</code> | <code>str</code> | Contributor ID |
| <code>sort</code> | <code>[Sort24OrStr](shutterstock_api_explorer/models/enums/sort24.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionDataList](shutterstock_api_explorer/models/collection_data_list.py), [GetContributorCollectionsListErrorBody](shutterstock_api_explorer/errors/get_contributor_collections_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionDataList](shutterstock_api_explorer/models/collection_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetContributorCollectionsListErrorBody](shutterstock_api_explorer/errors/get_contributor_collections_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_contributor_list(id: list[str], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ContributorProfileDataList, GetContributorListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists information about one or more contributors, including contributor type, equipment they use and other attributes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.contributors.with_raw_response.get_contributor_list(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ContributorProfileDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorListErrorBody
```

**Async**

```python
result = await async_client.contributors.with_raw_response.get_contributor_list(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ContributorProfileDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetContributorListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more contributor IDs |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[ContributorProfileDataList](shutterstock_api_explorer/models/contributor_profile_data_list.py), [GetContributorListErrorBody](shutterstock_api_explorer/errors/get_contributor_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ContributorProfileDataList](shutterstock_api_explorer/models/contributor_profile_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetContributorListErrorBody](shutterstock_api_explorer/errors/get_contributor_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## EditorialImages

> Source: [EditorialImages](shutterstock_api_explorer/apis/editorial_images.py)

<details>
<summary><code>def get_editorial_categories(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialCategoryResults, GetEditorialCategoriesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated; use `GET /v2/editorial/images/categories` instead. This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialCategoryResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialCategoriesErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialCategoryResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialCategoryResults](shutterstock_api_explorer/models/editorial_category_results.py), [GetEditorialCategoriesErrorBody](shutterstock_api_explorer/errors/get_editorial_categories_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialCategoryResults](shutterstock_api_explorer/models/editorial_category_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialCategoriesErrorBody](shutterstock_api_explorer/errors/get_editorial_categories_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialContent, GetEditorialImageErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_image(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialContent
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_image(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialContent
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Editorial ID |
| <code>country</code> | <code>str</code> | Returns only if the content is available for distribution in a certain country |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialContent](shutterstock_api_explorer/models/editorial_content.py), [GetEditorialImageErrorBody](shutterstock_api_explorer/errors/get_editorial_image_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialContent](shutterstock_api_explorer/models/editorial_content.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialImageErrorBody](shutterstock_api_explorer/errors/get_editorial_image_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image2(id: str, country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialContent, GetEditorialImage2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated; use `GET /v2/editorial/images/{id}` instead to show information about an editorial image, including a URL to a preview image and the sizes that it is available in.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_image2(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialContent
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImage2ErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_image2(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialContent
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImage2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Editorial ID |
| <code>country</code> | <code>str</code> | Returns only if the content is available for distribution in a certain country |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialContent](shutterstock_api_explorer/models/editorial_content.py), [GetEditorialImage2ErrorBody](shutterstock_api_explorer/errors/get_editorial_image2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialContent](shutterstock_api_explorer/models/editorial_content.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialImage2ErrorBody](shutterstock_api_explorer/errors/get_editorial_image2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image_license_list(*, image_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DownloadHistoryDataList, GetEditorialImageLicenseListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists existing editorial image licenses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_image_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageLicenseListErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_image_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageLicenseListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>image_id</code> | <code>str \| None</code> | Show licenses for the specified editorial image ID<br>**Default**: <code>None</code> |
| <code>license</code> | <code>str \| None</code> | Show editorial images that are available with the specified license name<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock_api_explorer/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py), [GetEditorialImageLicenseListErrorBody](shutterstock_api_explorer/errors/get_editorial_image_license_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialImageLicenseListErrorBody](shutterstock_api_explorer/errors/get_editorial_image_license_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image_livefeed(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialImageLivefeed, GetEditorialImageLivefeedErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_image_livefeed(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageLivefeed
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageLivefeedErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_image_livefeed(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageLivefeed
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageLivefeedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Editorial livefeed ID; must be an URI encoded string |
| <code>country</code> | <code>str</code> | Returns only if the livefeed is available for distribution in a certain country |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialImageLivefeed](shutterstock_api_explorer/models/editorial_image_livefeed.py), [GetEditorialImageLivefeedErrorBody](shutterstock_api_explorer/errors/get_editorial_image_livefeed_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialImageLivefeed](shutterstock_api_explorer/models/editorial_image_livefeed.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialImageLivefeedErrorBody](shutterstock_api_explorer/errors/get_editorial_image_livefeed_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image_livefeed_items(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialContentDataList, GetEditorialImageLivefeedItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_image_livefeed_items(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialContentDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageLivefeedItemsErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_image_livefeed_items(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialContentDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageLivefeedItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Editorial livefeed ID; must be an URI encoded string |
| <code>country</code> | <code>str</code> | Returns only if the livefeed items are available for distribution in a certain country |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialContentDataList](shutterstock_api_explorer/models/editorial_content_data_list.py), [GetEditorialImageLivefeedItemsErrorBody](shutterstock_api_explorer/errors/get_editorial_image_livefeed_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialContentDataList](shutterstock_api_explorer/models/editorial_content_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialImageLivefeedItemsErrorBody](shutterstock_api_explorer/errors/get_editorial_image_livefeed_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image_livefeed_list(country: str, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialImageLivefeedList, GetEditorialImageLivefeedListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_image_livefeed_list(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageLivefeedList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageLivefeedListErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_image_livefeed_list(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageLivefeedList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialImageLivefeedListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>country</code> | <code>str</code> | Returns only livefeeds that are available for distribution in a certain country |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialImageLivefeedList](shutterstock_api_explorer/models/editorial_image_livefeed_list.py), [GetEditorialImageLivefeedListErrorBody](shutterstock_api_explorer/errors/get_editorial_image_livefeed_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialImageLivefeedList](shutterstock_api_explorer/models/editorial_image_livefeed_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialImageLivefeedListErrorBody](shutterstock_api_explorer/errors/get_editorial_image_livefeed_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_livefeed(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialImageLivefeed, GetEditorialLivefeedErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated: use `GET /v2/editorial/images/livefeeds/{id}` instead to get an editorial livefeed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_livefeed(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageLivefeed
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialLivefeedErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_livefeed(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageLivefeed
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialLivefeedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Editorial livefeed ID; must be an URI encoded string |
| <code>country</code> | <code>str</code> | Returns only if the livefeed is available for distribution in a certain country |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialImageLivefeed](shutterstock_api_explorer/models/editorial_image_livefeed.py), [GetEditorialLivefeedErrorBody](shutterstock_api_explorer/errors/get_editorial_livefeed_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialImageLivefeed](shutterstock_api_explorer/models/editorial_image_livefeed.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialLivefeedErrorBody](shutterstock_api_explorer/errors/get_editorial_livefeed_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_livefeed_items(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialContentDataList, GetEditorialLivefeedItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated; use `GET /v2/editorial/images/livefeeds/{id}/items` instead to get editorial livefeed items.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_livefeed_items(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialContentDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialLivefeedItemsErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_livefeed_items(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialContentDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialLivefeedItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Editorial livefeed ID; must be an URI encoded string |
| <code>country</code> | <code>str</code> | Returns only if the livefeed items are available for distribution in a certain country |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialContentDataList](shutterstock_api_explorer/models/editorial_content_data_list.py), [GetEditorialLivefeedItemsErrorBody](shutterstock_api_explorer/errors/get_editorial_livefeed_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialContentDataList](shutterstock_api_explorer/models/editorial_content_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialLivefeedItemsErrorBody](shutterstock_api_explorer/errors/get_editorial_livefeed_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_livefeed_list(country: str, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialImageLivefeedList, GetEditorialLivefeedListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated; use `GET /v2/editorial/images/livefeeds` instead to get a list of editorial livefeeds.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_editorial_livefeed_list(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageLivefeedList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialLivefeedListErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_editorial_livefeed_list(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageLivefeedList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialLivefeedListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>country</code> | <code>str</code> | Returns only livefeeds that are available for distribution in a certain country |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialImageLivefeedList](shutterstock_api_explorer/models/editorial_image_livefeed_list.py), [GetEditorialLivefeedListErrorBody](shutterstock_api_explorer/errors/get_editorial_livefeed_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialImageLivefeedList](shutterstock_api_explorer/models/editorial_image_livefeed_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialLivefeedListErrorBody](shutterstock_api_explorer/errors/get_editorial_livefeed_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_updated_editorial_image(type_: Type5OrStr, date_updated_start: RFC3339DateTime, date_updated_end: RFC3339DateTime, country: str, *, date_taken_start: Date | None = None, date_taken_end: Date | None = None, cursor: str | None = None, sort: Sort5OrStr | None = None, supplier_code: list[str] | None = None, per_page: int | None = 500, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialUpdatedResults, GetUpdatedEditorialImageErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated; use `GET /v2/editorial/images/updated` instead to get recently updated items.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_updated_editorial_image(
    type_, date_updated_start, date_updated_end, country
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialUpdatedResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUpdatedEditorialImageErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_updated_editorial_image(
    type_, date_updated_start, date_updated_end, country
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialUpdatedResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUpdatedEditorialImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type5OrStr](shutterstock_api_explorer/models/enums/type5.py)</code> | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted |
| <code>date_updated_start</code> | <code>RFC3339DateTime</code> | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. |
| <code>date_updated_end</code> | <code>RFC3339DateTime</code> | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. |
| <code>country</code> | <code>str</code> | Show only editorial content that is available for distribution in a certain country |
| <code>date_taken_start</code> | <code>Date \| None</code> | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets<br>**Default**: <code>None</code> |
| <code>date_taken_end</code> | <code>Date \| None</code> | Show images that were taken before the specified date<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial content from certain suppliers<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>500</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialUpdatedResults](shutterstock_api_explorer/models/editorial_updated_results.py), [GetUpdatedEditorialImageErrorBody](shutterstock_api_explorer/errors/get_updated_editorial_image_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialUpdatedResults](shutterstock_api_explorer/models/editorial_updated_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetUpdatedEditorialImageErrorBody](shutterstock_api_explorer/errors/get_updated_editorial_image_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_updated_editorial_images(type_: Type5OrStr, date_updated_start: RFC3339DateTime, date_updated_end: RFC3339DateTime, country: str, *, date_taken_start: Date | None = None, date_taken_end: Date | None = None, cursor: str | None = None, sort: Sort5OrStr | None = None, supplier_code: list[str] | None = None, per_page: int | None = 500, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialUpdatedResults, GetUpdatedEditorialImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists editorial images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was taken.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.get_updated_editorial_images(
    type_, date_updated_start, date_updated_end, country
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialUpdatedResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUpdatedEditorialImagesErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.get_updated_editorial_images(
    type_, date_updated_start, date_updated_end, country
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialUpdatedResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUpdatedEditorialImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type5OrStr](shutterstock_api_explorer/models/enums/type5.py)</code> | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted |
| <code>date_updated_start</code> | <code>RFC3339DateTime</code> | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. |
| <code>date_updated_end</code> | <code>RFC3339DateTime</code> | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. |
| <code>country</code> | <code>str</code> | Show only editorial content that is available for distribution in a certain country |
| <code>date_taken_start</code> | <code>Date \| None</code> | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets<br>**Default**: <code>None</code> |
| <code>date_taken_end</code> | <code>Date \| None</code> | Show images that were taken before the specified date<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial content from certain suppliers<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>500</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialUpdatedResults](shutterstock_api_explorer/models/editorial_updated_results.py), [GetUpdatedEditorialImagesErrorBody](shutterstock_api_explorer/errors/get_updated_editorial_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialUpdatedResults](shutterstock_api_explorer/models/editorial_updated_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetUpdatedEditorialImagesErrorBody](shutterstock_api_explorer/errors/get_updated_editorial_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_editorial_image(body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialImageErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated; use `POST /v2/editorial/images/licenses` instead to get licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.license_editorial_image(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseEditorialContentResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseEditorialImageErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.license_editorial_image(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseEditorialContentResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseEditorialImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseEditorialContentRequest](shutterstock_api_explorer/models/license_editorial_content_request.py) \| [LicenseEditorialContentRequestDict](shutterstock_api_explorer/models/license_editorial_content_request.py)</code> | License editorial content |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[LicenseEditorialContentResults](shutterstock_api_explorer/models/license_editorial_content_results.py), [LicenseEditorialImageErrorBody](shutterstock_api_explorer/errors/license_editorial_image_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LicenseEditorialContentResults](shutterstock_api_explorer/models/license_editorial_content_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[LicenseEditorialImageErrorBody](shutterstock_api_explorer/errors/license_editorial_image_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_editorial_images(body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.license_editorial_images(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseEditorialContentResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseEditorialImagesErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.license_editorial_images(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseEditorialContentResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseEditorialImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseEditorialContentRequest](shutterstock_api_explorer/models/license_editorial_content_request.py) \| [LicenseEditorialContentRequestDict](shutterstock_api_explorer/models/license_editorial_content_request.py)</code> | License editorial content |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[LicenseEditorialContentResults](shutterstock_api_explorer/models/license_editorial_content_results.py), [LicenseEditorialImagesErrorBody](shutterstock_api_explorer/errors/license_editorial_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LicenseEditorialContentResults](shutterstock_api_explorer/models/license_editorial_content_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[LicenseEditorialImagesErrorBody](shutterstock_api_explorer/errors/license_editorial_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_editorial_image_categories(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialImageCategoryResults, ListEditorialImageCategoriesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.list_editorial_image_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageCategoryResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListEditorialImageCategoriesErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.list_editorial_image_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageCategoryResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListEditorialImageCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialImageCategoryResults](shutterstock_api_explorer/models/editorial_image_category_results.py), [ListEditorialImageCategoriesErrorBody](shutterstock_api_explorer/errors/list_editorial_image_categories_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialImageCategoryResults](shutterstock_api_explorer/models/editorial_image_category_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[ListEditorialImageCategoriesErrorBody](shutterstock_api_explorer/errors/list_editorial_image_categories_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_editorial_images(id: list[str], country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialImageResults, ListEditorialImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the details of editorial images.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.list_editorial_images(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListEditorialImagesErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.list_editorial_images(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialImageResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListEditorialImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | ID of the editorial image to list details for |
| <code>country</code> | <code>str</code> | Show only editorial image content that is available for distribution in a certain country |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialImageResults](shutterstock_api_explorer/models/editorial_image_results.py), [ListEditorialImagesErrorBody](shutterstock_api_explorer/errors/list_editorial_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialImageResults](shutterstock_api_explorer/models/editorial_image_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[ListEditorialImagesErrorBody](shutterstock_api_explorer/errors/list_editorial_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_editorial(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialSearchResults, SearchEditorialErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated; use `GET /v2/editorial/images/search` instead to search for editorial images.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.search_editorial(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchEditorialErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.search_editorial(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchEditorialErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>country</code> | <code>str</code> | Show only editorial content that is available for distribution in a certain country |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort17OrStr](shutterstock_api_explorer/models/enums/sort17.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show editorial content within a certain editorial category; specify by category name<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial content from certain suppliers<br>**Default**: <code>None</code> |
| <code>date_start</code> | <code>Date \| None</code> | Show only editorial content generated on or after a specific date<br>**Default**: <code>None</code> |
| <code>date_end</code> | <code>Date \| None</code> | Show only editorial content generated on or before a specific date<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialSearchResults](shutterstock_api_explorer/models/editorial_search_results.py), [SearchEditorialErrorBody](shutterstock_api_explorer/errors/search_editorial_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialSearchResults](shutterstock_api_explorer/models/editorial_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[SearchEditorialErrorBody](shutterstock_api_explorer/errors/search_editorial_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_editorial_images(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialSearchResults, SearchEditorialImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the `category` parameter to "Alone,Performing" and also specify a `query` parameter, the results include only images that match the query and are in both the Alone and Performing categories. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_images.with_raw_response.search_editorial_images(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchEditorialImagesErrorBody
```

**Async**

```python
result = await async_client.editorial_images.with_raw_response.search_editorial_images(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchEditorialImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>country</code> | <code>str</code> | Show only editorial content that is available for distribution in a certain country |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort17OrStr](shutterstock_api_explorer/models/enums/sort17.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial content from certain suppliers<br>**Default**: <code>None</code> |
| <code>date_start</code> | <code>Date \| None</code> | Show only editorial content generated on or after a specific date<br>**Default**: <code>None</code> |
| <code>date_end</code> | <code>Date \| None</code> | Show only editorial content generated on or before a specific date<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialSearchResults](shutterstock_api_explorer/models/editorial_search_results.py), [SearchEditorialImagesErrorBody](shutterstock_api_explorer/errors/search_editorial_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialSearchResults](shutterstock_api_explorer/models/editorial_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[SearchEditorialImagesErrorBody](shutterstock_api_explorer/errors/search_editorial_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## EditorialVideo

> Source: [EditorialVideo](shutterstock_api_explorer/apis/editorial_video.py)

<details>
<summary><code>def get_editorial_video(id: str, country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialVideoContent, GetEditorialVideoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_video.with_raw_response.get_editorial_video(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialVideoContent
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialVideoErrorBody
```

**Async**

```python
result = await async_client.editorial_video.with_raw_response.get_editorial_video(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialVideoContent
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialVideoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Editorial ID |
| <code>country</code> | <code>str</code> | Returns only if the content is available for distribution in a certain country |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialVideoContent](shutterstock_api_explorer/models/editorial_video_content.py), [GetEditorialVideoErrorBody](shutterstock_api_explorer/errors/get_editorial_video_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialVideoContent](shutterstock_api_explorer/models/editorial_video_content.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialVideoErrorBody](shutterstock_api_explorer/errors/get_editorial_video_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_video_license_list(*, video_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DownloadHistoryDataList, GetEditorialVideoLicenseListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists existing editorial video licenses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_video.with_raw_response.get_editorial_video_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialVideoLicenseListErrorBody
```

**Async**

```python
result = await async_client.editorial_video.with_raw_response.get_editorial_video_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEditorialVideoLicenseListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>video_id</code> | <code>str \| None</code> | Show licenses for the specified editorial video ID<br>**Default**: <code>None</code> |
| <code>license</code> | <code>str \| None</code> | Show editorial videos that are available with the specified license name<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock_api_explorer/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py), [GetEditorialVideoLicenseListErrorBody](shutterstock_api_explorer/errors/get_editorial_video_license_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetEditorialVideoLicenseListErrorBody](shutterstock_api_explorer/errors/get_editorial_video_license_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_editorial_video(body: LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialVideoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more editorial videos to license. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_video.with_raw_response.license_editorial_video(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseEditorialContentResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseEditorialVideoErrorBody
```

**Async**

```python
result = await async_client.editorial_video.with_raw_response.license_editorial_video(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseEditorialContentResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseEditorialVideoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseEditorialVideoContentRequest](shutterstock_api_explorer/models/license_editorial_video_content_request.py) \| [LicenseEditorialVideoContentRequestDict](shutterstock_api_explorer/models/license_editorial_video_content_request.py)</code> | License editorial video content |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[LicenseEditorialContentResults](shutterstock_api_explorer/models/license_editorial_content_results.py), [LicenseEditorialVideoErrorBody](shutterstock_api_explorer/errors/license_editorial_video_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LicenseEditorialContentResults](shutterstock_api_explorer/models/license_editorial_content_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[LicenseEditorialVideoErrorBody](shutterstock_api_explorer/errors/license_editorial_video_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_editorial_video_categories(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialVideoCategoryResults, ListEditorialVideoCategoriesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the categories that editorial videos can belong to, which are separate from the categories that other types of assets can belong to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_video.with_raw_response.list_editorial_video_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialVideoCategoryResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListEditorialVideoCategoriesErrorBody
```

**Async**

```python
result = await async_client.editorial_video.with_raw_response.list_editorial_video_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialVideoCategoryResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListEditorialVideoCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialVideoCategoryResults](shutterstock_api_explorer/models/editorial_video_category_results.py), [ListEditorialVideoCategoriesErrorBody](shutterstock_api_explorer/errors/list_editorial_video_categories_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialVideoCategoryResults](shutterstock_api_explorer/models/editorial_video_category_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[ListEditorialVideoCategoriesErrorBody](shutterstock_api_explorer/errors/list_editorial_video_categories_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_editorial_videos(id: list[str], country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialVideoResults, ListEditorialVideosErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the details of editorial videos by ID list.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_video.with_raw_response.list_editorial_videos(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialVideoResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListEditorialVideosErrorBody
```

**Async**

```python
result = await async_client.editorial_video.with_raw_response.list_editorial_videos(id, country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialVideoResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListEditorialVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | ID of the editorial video to list details for |
| <code>country</code> | <code>str</code> | Show only editorial video content that is available for distribution in a certain country |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialVideoResults](shutterstock_api_explorer/models/editorial_video_results.py), [ListEditorialVideosErrorBody](shutterstock_api_explorer/errors/list_editorial_videos_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialVideoResults](shutterstock_api_explorer/models/editorial_video_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[ListEditorialVideosErrorBody](shutterstock_api_explorer/errors/list_editorial_videos_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_editorial_videos(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, resolution: ResolutionOrStr | None = None, fps: float | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EditorialVideoSearchResults, SearchEditorialVideosErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the `category` parameter to "Alone,Performing" and also specify a `query` parameter, the results include only videos that match the query and are in both the Alone and Performing categories.  You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.editorial_video.with_raw_response.search_editorial_videos(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialVideoSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchEditorialVideosErrorBody
```

**Async**

```python
result = await async_client.editorial_video.with_raw_response.search_editorial_videos(country)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EditorialVideoSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchEditorialVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>country</code> | <code>str</code> | Show only editorial video content that is available for distribution in a certain country |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort17OrStr](shutterstock_api_explorer/models/enums/sort17.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial video content from certain suppliers<br>**Default**: <code>None</code> |
| <code>date_start</code> | <code>Date \| None</code> | Show only editorial video content generated on or after a specific date<br>**Default**: <code>None</code> |
| <code>date_end</code> | <code>Date \| None</code> | Show only editorial video content generated on or before a specific date<br>**Default**: <code>None</code> |
| <code>resolution</code> | <code>[ResolutionOrStr](shutterstock_api_explorer/models/enums/resolution.py) \| None</code> | Show only editorial video content with specific resolution<br>**Default**: <code>None</code> |
| <code>fps</code> | <code>float \| None</code> | Show only editorial video content generated with specific frames per second<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[EditorialVideoSearchResults](shutterstock_api_explorer/models/editorial_video_search_results.py), [SearchEditorialVideosErrorBody](shutterstock_api_explorer/errors/search_editorial_videos_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EditorialVideoSearchResults](shutterstock_api_explorer/models/editorial_video_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[SearchEditorialVideosErrorBody](shutterstock_api_explorer/errors/search_editorial_videos_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Images

> Source: [Images](shutterstock_api_explorer/apis/images.py)

<details>
<summary><code>def add_image_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, AddImageCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint adds one or more images to a collection by image IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.add_image_collection_items(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddImageCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.add_image_collection_items(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddImageCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>body</code> | <code>[CollectionItemRequest](shutterstock_api_explorer/models/collection_item_request.py) \| [CollectionItemRequestDict](shutterstock_api_explorer/models/collection_item_request.py)</code> | Array of image IDs to add to the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [AddImageCollectionItemsErrorBody](shutterstock_api_explorer/errors/add_image_collection_items_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[AddImageCollectionItemsErrorBody](shutterstock_api_explorer/errors/add_image_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_search_images(body: list[SearchImage | SearchImageDict], *, added_date: Date | None = None, added_date_start: Date | None = None, aspect_ratio_min: float | None = None, aspect_ratio_max: float | None = None, aspect_ratio: float | None = None, added_date_end: Date | None = None, category: str | None = None, color: str | None = None, contributor: list[str] | None = None, contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None, fields: str | None = None, height: int | None = None, height_from: int | None = None, height_to: int | None = None, image_type: list[ImageType2OrStr] | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[LicenseOrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_model_released: bool | None = None, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity2OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, region: RegionModel | RegionModelDict | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, spellcheck_query: bool | None = True, view: View2OrStr | None = None, width: int | None = None, width_from: int | None = None, width_to: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkImageSearchResults, BulkSearchImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You can provide global search parameters in the query parameters and override them for each search in the body parameter. The query and body parameters are the same as in the `GET /v2/images/search` endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.bulk_search_images(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkImageSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkSearchImagesErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.bulk_search_images(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkImageSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkSearchImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>list&#91;[SearchImage](shutterstock_api_explorer/models/search_image.py) \| [SearchImageDict](shutterstock_api_explorer/models/search_image.py)&#93;</code> | List of queries to request results for and filters to apply per query; these values override the defaults in the query parameters |
| <code>added_date</code> | <code>Date \| None</code> | Show images added on the specified date<br>**Default**: <code>None</code> |
| <code>added_date_start</code> | <code>Date \| None</code> | Show images added on or after the specified date<br>**Default**: <code>None</code> |
| <code>aspect_ratio_min</code> | <code>float \| None</code> | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>aspect_ratio_max</code> | <code>float \| None</code> | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>aspect_ratio</code> | <code>float \| None</code> | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>added_date_end</code> | <code>Date \| None</code> | Show images added before the specified date<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show images with the specified Shutterstock-defined category; specify a category name or ID<br>**Default**: <code>None</code> |
| <code>color</code> | <code>str \| None</code> | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors<br>**Default**: <code>None</code> |
| <code>contributor</code> | <code>list&#91;str&#93; \| None</code> | Show images with the specified contributor names or IDs, allows multiple<br>**Default**: <code>None</code> |
| <code>contributor_country</code> | <code>[ContributorCountryModel](shutterstock_api_explorer/models/unions/contributor_country_model.py) \| [ContributorCountryModelDict](shutterstock_api_explorer/models/unions/contributor_country_model.py) \| None</code> | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Fields to display in the response; see the documentation for the fields parameter in the overview section<br>**Default**: <code>None</code> |
| <code>height</code> | <code>int \| None</code> | (Deprecated; use height_from and height_to instead) Show images with the specified height<br>**Default**: <code>None</code> |
| <code>height_from</code> | <code>int \| None</code> | Show images with the specified height or larger, in pixels<br>**Default**: <code>None</code> |
| <code>height_to</code> | <code>int \| None</code> | Show images with the specified height or smaller, in pixels<br>**Default**: <code>None</code> |
| <code>image_type</code> | <code>list&#91;[ImageType2OrStr](shutterstock_api_explorer/models/enums/image_type2.py)&#93; \| None</code> | Show images of the specified type<br>**Default**: <code>None</code> |
| <code>keyword_safe_search</code> | <code>bool \| None</code> | Hide results with potentially unsafe keywords<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Set query and result language (uses Accept-Language header if not set)<br>**Default**: <code>None</code> |
| <code>license</code> | <code>list&#91;[LicenseOrStr](shutterstock_api_explorer/models/enums/license.py)&#93; \| None</code> | Show only images with the specified license<br>**Default**: <code>None</code> |
| <code>model</code> | <code>list&#91;str&#93; \| None</code> | Show image results with the specified model IDs<br>**Default**: <code>None</code> |
| <code>orientation</code> | <code>[Orientation2OrStr](shutterstock_api_explorer/models/enums/orientation2.py) \| None</code> | Show image results with horizontal or vertical orientation<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>people_model_released</code> | <code>bool \| None</code> | Show images of people with a signed model release<br>**Default**: <code>None</code> |
| <code>people_age</code> | <code>[PeopleAge2OrStr](shutterstock_api_explorer/models/enums/people_age2.py) \| None</code> | Show images that feature people of the specified age category<br>**Default**: <code>None</code> |
| <code>people_ethnicity</code> | <code>list&#91;[PeopleEthnicity2OrStr](shutterstock_api_explorer/models/enums/people_ethnicity2.py)&#93; \| None</code> | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities<br>**Default**: <code>None</code> |
| <code>people_gender</code> | <code>[PeopleGender2OrStr](shutterstock_api_explorer/models/enums/people_gender2.py) \| None</code> | Show images with people of the specified gender<br>**Default**: <code>None</code> |
| <code>people_number</code> | <code>int \| None</code> | Show images with the specified number of people<br>**Default**: <code>None</code> |
| <code>region</code> | <code>[RegionModel](shutterstock_api_explorer/models/unions/region_model.py) \| [RegionModelDict](shutterstock_api_explorer/models/unions/region_model.py) \| None</code> | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>sort</code> | <code>[Sort2OrStr](shutterstock_api_explorer/models/enums/sort2.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>spellcheck_query</code> | <code>bool \| None</code> | Spellcheck the search query and return results on suggested spellings<br>**Default**: <code>True</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>width</code> | <code>int \| None</code> | (Deprecated; use width_from and width_to instead) Show images with the specified width<br>**Default**: <code>None</code> |
| <code>width_from</code> | <code>int \| None</code> | Show images with the specified width or larger, in pixels<br>**Default**: <code>None</code> |
| <code>width_to</code> | <code>int \| None</code> | Show images with the specified width or smaller, in pixels<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[BulkImageSearchResults](shutterstock_api_explorer/models/bulk_image_search_results.py), [BulkSearchImagesErrorBody](shutterstock_api_explorer/errors/bulk_search_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkImageSearchResults](shutterstock_api_explorer/models/bulk_image_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[BulkSearchImagesErrorBody](shutterstock_api_explorer/errors/bulk_search_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_image_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionCreateResponse, CreateImageCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint creates one or more image collections (lightboxes). To add images to the collections, use `POST /v2/images/collections/{id}/items`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.create_image_collection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateImageCollectionErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.create_image_collection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateImageCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CollectionCreateRequest](shutterstock_api_explorer/models/collection_create_request.py) \| [CollectionCreateRequestDict](shutterstock_api_explorer/models/collection_create_request.py)</code> | The names of the new collections |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionCreateResponse](shutterstock_api_explorer/models/collection_create_response.py), [CreateImageCollectionErrorBody](shutterstock_api_explorer/errors/create_image_collection_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionCreateResponse](shutterstock_api_explorer/models/collection_create_response.py)</code> -- Successfully created image collection

**On `Failure`**: `error` is <code>[CreateImageCollectionErrorBody](shutterstock_api_explorer/errors/create_image_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_image_collection(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteImageCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint deletes an image collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.delete_image_collection(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteImageCollectionErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.delete_image_collection(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteImageCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [DeleteImageCollectionErrorBody](shutterstock_api_explorer/errors/delete_image_collection_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteImageCollectionErrorBody](shutterstock_api_explorer/errors/delete_image_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_image_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteImageCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint removes one or more images from a collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.delete_image_collection_items(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteImageCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.delete_image_collection_items(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteImageCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>item_id</code> | <code>list&#91;str&#93; \| None</code> | One or more image IDs to remove from the collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [DeleteImageCollectionItemsErrorBody](shutterstock_api_explorer/errors/delete_image_collection_items_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteImageCollectionItemsErrorBody](shutterstock_api_explorer/errors/delete_image_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_image(id: str, body: RedownloadImage | RedownloadImageDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Url, DownloadImageErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint redownloads images that you have already received a license for. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.download_image(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Url
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadImageErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.download_image(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Url
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | License ID |
| <code>body</code> | <code>[RedownloadImage](shutterstock_api_explorer/models/redownload_image.py) \| [RedownloadImageDict](shutterstock_api_explorer/models/redownload_image.py)</code> | Information about the images to redownload |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Url](shutterstock_api_explorer/models/url.py), [DownloadImageErrorBody](shutterstock_api_explorer/errors/download_image_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Url](shutterstock_api_explorer/models/url.py)</code> -- OK

**On `Failure`**: `error` is <code>[DownloadImageErrorBody](shutterstock_api_explorer/errors/download_image_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image(id: str, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Image, GetImageErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint shows information about an image, including a URL to a preview image and the sizes that it is available in.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Image
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Image
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Image ID |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Image](shutterstock_api_explorer/models/image.py), [GetImageErrorBody](shutterstock_api_explorer/errors/get_image_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Image](shutterstock_api_explorer/models/image.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageErrorBody](shutterstock_api_explorer/errors/get_image_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Collection, GetImageCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets more detailed information about a collection, including its cover image and timestamps for its creation and most recent update. To get the images in collections, use `GET /v2/images/collections/{id}/items`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image_collection(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Collection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageCollectionErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image_collection(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Collection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock_api_explorer/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve a shared collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Collection](shutterstock_api_explorer/models/collection.py), [GetImageCollectionErrorBody](shutterstock_api_explorer/errors/get_image_collection_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Collection](shutterstock_api_explorer/models/collection.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageCollectionErrorBody](shutterstock_api_explorer/errors/get_image_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionItemDataList, GetImageCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the IDs of images in a collection and the date that each was added.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image_collection_items(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image_collection_items(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve the contents of a shared collection<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionItemDataList](shutterstock_api_explorer/models/collection_item_data_list.py), [GetImageCollectionItemsErrorBody](shutterstock_api_explorer/errors/get_image_collection_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionItemDataList](shutterstock_api_explorer/models/collection_item_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageCollectionItemsErrorBody](shutterstock_api_explorer/errors/get_image_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_collection_list(*, embed: list[EmbedOrStr] | None = None, page: int | None = 1, per_page: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionDataList, GetImageCollectionListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists your collections of images and their basic attributes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image_collection_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageCollectionListErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image_collection_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageCollectionListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock_api_explorer/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionDataList](shutterstock_api_explorer/models/collection_data_list.py), [GetImageCollectionListErrorBody](shutterstock_api_explorer/errors/get_image_collection_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionDataList](shutterstock_api_explorer/models/collection_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageCollectionListErrorBody](shutterstock_api_explorer/errors/get_image_collection_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_keyword_suggestions(body: SearchEntitiesRequest | SearchEntitiesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchEntitiesResponse, GetImageKeywordSuggestionsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns up to 10 important keywords from a block of plain text.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image_keyword_suggestions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchEntitiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageKeywordSuggestionsErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image_keyword_suggestions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchEntitiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageKeywordSuggestionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchEntitiesRequest](shutterstock_api_explorer/models/search_entities_request.py) \| [SearchEntitiesRequestDict](shutterstock_api_explorer/models/search_entities_request.py)</code> | Plain text to extract keywords from |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[SearchEntitiesResponse](shutterstock_api_explorer/models/search_entities_response.py), [GetImageKeywordSuggestionsErrorBody](shutterstock_api_explorer/errors/get_image_keyword_suggestions_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchEntitiesResponse](shutterstock_api_explorer/models/search_entities_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageKeywordSuggestionsErrorBody](shutterstock_api_explorer/errors/get_image_keyword_suggestions_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_license_list(*, image_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DownloadHistoryDataList, GetImageLicenseListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists existing licenses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageLicenseListErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageLicenseListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>image_id</code> | <code>str \| None</code> | Show licenses for the specified image ID<br>**Default**: <code>None</code> |
| <code>license</code> | <code>str \| None</code> | Show images that are available with the specified license, such as `standard` or `enhanced`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock_api_explorer/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py), [GetImageLicenseListErrorBody](shutterstock_api_explorer/errors/get_image_license_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageLicenseListErrorBody](shutterstock_api_explorer/errors/get_image_license_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ImageDataList, GetImageListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists information about one or more images, including the available sizes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image_list(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ImageDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageListErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image_list(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ImageDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more image IDs |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[ImageDataList](shutterstock_api_explorer/models/image_data_list.py), [GetImageListErrorBody](shutterstock_api_explorer/errors/get_image_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ImageDataList](shutterstock_api_explorer/models/image_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageListErrorBody](shutterstock_api_explorer/errors/get_image_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_recommendations(id: list[str], *, max_items: int | None = 20, safe: bool | None = True, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RecommendationDataList, GetImageRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns images that customers put in the same collection as the specified image IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image_recommendations(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RecommendationDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageRecommendationsErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image_recommendations(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RecommendationDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | Image IDs |
| <code>max_items</code> | <code>int \| None</code> | Maximum number of results returned in the response<br>**Default**: <code>20</code> |
| <code>safe</code> | <code>bool \| None</code> | Restrict results to safe images<br>**Default**: <code>True</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[RecommendationDataList](shutterstock_api_explorer/models/recommendation_data_list.py), [GetImageRecommendationsErrorBody](shutterstock_api_explorer/errors/get_image_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RecommendationDataList](shutterstock_api_explorer/models/recommendation_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageRecommendationsErrorBody](shutterstock_api_explorer/errors/get_image_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_suggestions(query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Suggestions, GetImageSuggestionsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint provides autocomplete suggestions for partial search terms.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_image_suggestions(query)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Suggestions
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageSuggestionsErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.get_image_suggestions(query)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Suggestions
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetImageSuggestionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query</code> | <code>str</code> | Search term for which you want keyword suggestions |
| <code>limit</code> | <code>int \| None</code> | Limit the number of suggestions<br>**Default**: <code>10</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Suggestions](shutterstock_api_explorer/models/suggestions.py), [GetImageSuggestionsErrorBody](shutterstock_api_explorer/errors/get_image_suggestions_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Suggestions](shutterstock_api_explorer/models/suggestions.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetImageSuggestionsErrorBody](shutterstock_api_explorer/errors/get_image_suggestions_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_updated_images(*, type_: list[Type4OrStr] | None = None, start_date: str | None = None, end_date: str | None = None, interval: str | None = "1 HOUR", page: int | None = 1, per_page: int | None = 100, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdatedMediaDataList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the `interval` parameter to show images that were updated recently, but you can also use the `start_date` and `end_date` parameters to specify a range of no more than three days. Do not use the `interval` parameter with either `start_date` or `end_date`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.get_updated_images()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdatedMediaDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.images.with_raw_response.get_updated_images()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdatedMediaDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>list&#91;[Type4OrStr](shutterstock_api_explorer/models/enums/type4.py)&#93; \| None</code> | Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | Show images updated on or after the specified date. The API will default to UTC (00:00:00) if no specific time is provided, ensuring consistency.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | Show images updated before the specified date. The API will default to UTC (00:00:00) if no specific time is provided, ensuring consistency. Please note that the end date must be at least 5 minutes after the start date.<br>**Default**: <code>None</code> |
| <code>interval</code> | <code>str \| None</code> | Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request<br>**Default**: <code>"1 HOUR"</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[UpdatedMediaDataList](shutterstock_api_explorer/models/updated_media_data_list.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdatedMediaDataList](shutterstock_api_explorer/models/updated_media_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_images(body: LicenseImageRequest | LicenseImageRequestDict, *, subscription_id: str | None = None, format: Format15OrStr | None = None, size: Size12OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LicenseImageResultDataList, LicenseImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and other details like the format, size, and subscription ID either in the query parameter or with each image ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.license_images(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseImageResultDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseImagesErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.license_images(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseImageResultDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseImageRequest](shutterstock_api_explorer/models/license_image_request.py) \| [LicenseImageRequestDict](shutterstock_api_explorer/models/license_image_request.py)</code> | List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters |
| <code>subscription_id</code> | <code>str \| None</code> | Subscription ID to use to license the image<br>**Default**: <code>None</code> |
| <code>format</code> | <code>[Format15OrStr](shutterstock_api_explorer/models/enums/format15.py) \| None</code> | (Deprecated) Image format<br>**Default**: <code>None</code> |
| <code>size</code> | <code>[Size12OrStr](shutterstock_api_explorer/models/enums/size12.py) \| None</code> | Image size<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | Search ID that was provided in the results of an image search<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[LicenseImageResultDataList](shutterstock_api_explorer/models/license_image_result_data_list.py), [LicenseImagesErrorBody](shutterstock_api_explorer/errors/license_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LicenseImageResultDataList](shutterstock_api_explorer/models/license_image_result_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[LicenseImagesErrorBody](shutterstock_api_explorer/errors/license_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_image_categories(*, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CategoryDataList, ListImageCategoriesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.list_image_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CategoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListImageCategoriesErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.list_image_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CategoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListImageCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CategoryDataList](shutterstock_api_explorer/models/category_data_list.py), [ListImageCategoriesErrorBody](shutterstock_api_explorer/errors/list_image_categories_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CategoryDataList](shutterstock_api_explorer/models/category_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[ListImageCategoriesErrorBody](shutterstock_api_explorer/errors/list_image_categories_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_similar_images(id: str, *, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ImageSearchResults, ListSimilarImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns images that are visually similar to an image that you specify.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.list_similar_images(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ImageSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListSimilarImagesErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.list_similar_images(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ImageSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListSimilarImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Image ID |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[ImageSearchResults](shutterstock_api_explorer/models/image_search_results.py), [ListSimilarImagesErrorBody](shutterstock_api_explorer/errors/list_similar_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ImageSearchResults](shutterstock_api_explorer/models/image_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[ListSimilarImagesErrorBody](shutterstock_api_explorer/errors/list_similar_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def rename_image_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RenameImageCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint sets a new name for an image collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.rename_image_collection(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RenameImageCollectionErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.rename_image_collection(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RenameImageCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>body</code> | <code>[CollectionUpdateRequest](shutterstock_api_explorer/models/collection_update_request.py) \| [CollectionUpdateRequestDict](shutterstock_api_explorer/models/collection_update_request.py)</code> | The new name for the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [RenameImageCollectionErrorBody](shutterstock_api_explorer/errors/rename_image_collection_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RenameImageCollectionErrorBody](shutterstock_api_explorer/errors/rename_image_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_images(*, library: list[LibraryOrStr] | None = None, added_date: Date | None = None, added_date_start: Date | None = None, aspect_ratio_min: float | None = None, aspect_ratio_max: float | None = None, aspect_ratio: float | None = None, added_date_end: Date | None = None, category: str | None = None, color: str | None = None, contributor: list[str] | None = None, contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None, fields: str | None = None, height: int | None = None, height_from: int | None = None, height_to: int | None = None, image_type: list[ImageType2OrStr] | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[LicenseOrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_model_released: bool | None = None, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity2OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, query: str | None = None, region: RegionModel | RegionModelDict | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, spellcheck_query: bool | None = True, view: View2OrStr | None = None, width: int | None = None, width_from: int | None = None, width_to: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ImageSearchResults, SearchImagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint searches for images. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media, not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.images.with_raw_response.search_images()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ImageSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchImagesErrorBody
```

**Async**

```python
result = await async_client.images.with_raw_response.search_images()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ImageSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>library</code> | <code>list&#91;[LibraryOrStr](shutterstock_api_explorer/models/enums/library.py)&#93; \| None</code> | Search within different Shutterstock owned libraries<br>**Default**: <code>None</code> |
| <code>added_date</code> | <code>Date \| None</code> | Show images added on the specified date<br>**Default**: <code>None</code> |
| <code>added_date_start</code> | <code>Date \| None</code> | Show images added on or after the specified date<br>**Default**: <code>None</code> |
| <code>aspect_ratio_min</code> | <code>float \| None</code> | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>aspect_ratio_max</code> | <code>float \| None</code> | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>aspect_ratio</code> | <code>float \| None</code> | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>added_date_end</code> | <code>Date \| None</code> | Show images added before the specified date<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show images with the specified Shutterstock-defined category; specify a category name or ID<br>**Default**: <code>None</code> |
| <code>color</code> | <code>str \| None</code> | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors<br>**Default**: <code>None</code> |
| <code>contributor</code> | <code>list&#91;str&#93; \| None</code> | Show images with the specified contributor names or IDs, allows multiple<br>**Default**: <code>None</code> |
| <code>contributor_country</code> | <code>[ContributorCountryModel](shutterstock_api_explorer/models/unions/contributor_country_model.py) \| [ContributorCountryModelDict](shutterstock_api_explorer/models/unions/contributor_country_model.py) \| None</code> | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Fields to display in the response; see the documentation for the fields parameter in the overview section<br>**Default**: <code>None</code> |
| <code>height</code> | <code>int \| None</code> | (Deprecated; use height_from and height_to instead) Show images with the specified height<br>**Default**: <code>None</code> |
| <code>height_from</code> | <code>int \| None</code> | Show images with the specified height or larger, in pixels<br>**Default**: <code>None</code> |
| <code>height_to</code> | <code>int \| None</code> | Show images with the specified height or smaller, in pixels<br>**Default**: <code>None</code> |
| <code>image_type</code> | <code>list&#91;[ImageType2OrStr](shutterstock_api_explorer/models/enums/image_type2.py)&#93; \| None</code> | Show images of the specified type<br>**Default**: <code>None</code> |
| <code>keyword_safe_search</code> | <code>bool \| None</code> | Hide results with potentially unsafe keywords<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Set query and result language (uses Accept-Language header if not set)<br>**Default**: <code>None</code> |
| <code>license</code> | <code>list&#91;[LicenseOrStr](shutterstock_api_explorer/models/enums/license.py)&#93; \| None</code> | Show only images with the specified license<br>**Default**: <code>None</code> |
| <code>model</code> | <code>list&#91;str&#93; \| None</code> | Show image results with the specified model IDs<br>**Default**: <code>None</code> |
| <code>orientation</code> | <code>[Orientation2OrStr](shutterstock_api_explorer/models/enums/orientation2.py) \| None</code> | Show image results with horizontal or vertical orientation<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>people_model_released</code> | <code>bool \| None</code> | Show images of people with a signed model release<br>**Default**: <code>None</code> |
| <code>people_age</code> | <code>[PeopleAge2OrStr](shutterstock_api_explorer/models/enums/people_age2.py) \| None</code> | Show images that feature people of the specified age category<br>**Default**: <code>None</code> |
| <code>people_ethnicity</code> | <code>list&#91;[PeopleEthnicity2OrStr](shutterstock_api_explorer/models/enums/people_ethnicity2.py)&#93; \| None</code> | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities<br>**Default**: <code>None</code> |
| <code>people_gender</code> | <code>[PeopleGender2OrStr](shutterstock_api_explorer/models/enums/people_gender2.py) \| None</code> | Show images with people of the specified gender<br>**Default**: <code>None</code> |
| <code>people_number</code> | <code>int \| None</code> | Show images with the specified number of people<br>**Default**: <code>None</code> |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces; you can use NOT to filter out images that match a term<br>**Default**: <code>None</code> |
| <code>region</code> | <code>[RegionModel](shutterstock_api_explorer/models/unions/region_model.py) \| [RegionModelDict](shutterstock_api_explorer/models/unions/region_model.py) \| None</code> | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>sort</code> | <code>[Sort2OrStr](shutterstock_api_explorer/models/enums/sort2.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>spellcheck_query</code> | <code>bool \| None</code> | Spellcheck the search query and return results on suggested spellings<br>**Default**: <code>True</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>width</code> | <code>int \| None</code> | (Deprecated; use width_from and width_to instead) Show images with the specified width<br>**Default**: <code>None</code> |
| <code>width_from</code> | <code>int \| None</code> | Show images with the specified width or larger, in pixels<br>**Default**: <code>None</code> |
| <code>width_to</code> | <code>int \| None</code> | Show images with the specified width or smaller, in pixels<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[ImageSearchResults](shutterstock_api_explorer/models/image_search_results.py), [SearchImagesErrorBody](shutterstock_api_explorer/errors/search_images_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ImageSearchResults](shutterstock_api_explorer/models/image_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[SearchImagesErrorBody](shutterstock_api_explorer/errors/search_images_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Oauth

> Source: [Oauth](shutterstock_api_explorer/apis/oauth.py)

<details>
<summary><code>def authorize(client_id: str, redirect_uri: str, response_type: ResponseTypeOrStr, state: str, *, realm: Realm2OrStr | None = None, scope: str | None = "user.view", request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, AuthorizeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns a redirect URI (in the 'Location' header) that the customer uses to authorize your application and, together with POST /v2/oauth/access_token, generate an access token that represents that authorization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.oauth.with_raw_response.authorize(client_id, redirect_uri, response_type, state)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AuthorizeErrorBody
```

**Async**

```python
result = await async_client.oauth.with_raw_response.authorize(client_id, redirect_uri, response_type, state)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AuthorizeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | Client ID (Consumer Key) of your application |
| <code>redirect_uri</code> | <code>str</code> | The callback URI to send the request to after authorization; must use a host name that is registered with your application |
| <code>response_type</code> | <code>[ResponseTypeOrStr](shutterstock_api_explorer/models/enums/response_type.py)</code> | Type of temporary authorization code that will be used to generate an access code; the only valid value is 'code' |
| <code>state</code> | <code>str</code> | Unique value used by the calling app to verify the request |
| <code>realm</code> | <code>[Realm2OrStr](shutterstock_api_explorer/models/enums/realm2.py) \| None</code> | User type to be authorized (usually 'customer')<br>**Default**: <code>None</code> |
| <code>scope</code> | <code>str \| None</code> | Space-separated list of scopes to be authorized<br>**Default**: <code>"user.view"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [AuthorizeErrorBody](shutterstock_api_explorer/errors/authorize_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[AuthorizeErrorBody](shutterstock_api_explorer/errors/authorize_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_access_token(client_id: str, grant_type: GrantTypeOrStr, *, client_secret: str | None = None, code: str | None = None, realm: Realm3OrStr | None = None, expires: ExpiresOrStr | None = None, refresh_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OauthAccessTokenResponse, CreateAccessTokenErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns an access token for the specified user and with the specified scopes. The token does not expire until the user changes their password. The body parameters must be encoded as form data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.oauth.with_raw_response.create_access_token(client_id, grant_type)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthAccessTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateAccessTokenErrorBody
```

**Async**

```python
result = await async_client.oauth.with_raw_response.create_access_token(client_id, grant_type)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthAccessTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateAccessTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | Client ID (Consumer Key) of your application |
| <code>grant_type</code> | <code>[GrantTypeOrStr](shutterstock_api_explorer/models/enums/grant_type.py)</code> | Grant type: authorization_code generates user tokens, client_credentials generates short-lived client grants |
| <code>client_secret</code> | <code>str \| None</code> | Client Secret (Consumer Secret) of your application<br>**Default**: <code>None</code> |
| <code>code</code> | <code>str \| None</code> | Response code from the /oauth/authorize flow; required if grant_type=authorization_code<br>**Default**: <code>None</code> |
| <code>realm</code> | <code>[Realm3OrStr](shutterstock_api_explorer/models/enums/realm3.py) \| None</code> | User type to be authorized (usually 'customer')<br>**Default**: <code>None</code> |
| <code>expires</code> | <code>[ExpiresOrStr](shutterstock_api_explorer/models/enums/expires.py) \| None</code> | Whether or not the token expires, expiring tokens come with a refresh_token to renew the access_token<br>**Default**: <code>None</code> |
| <code>refresh_token</code> | <code>str \| None</code> | Pass this along with grant_type=refresh_token to get a fresh access token<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[OauthAccessTokenResponse](shutterstock_api_explorer/models/oauth_access_token_response.py), [CreateAccessTokenErrorBody](shutterstock_api_explorer/errors/create_access_token_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[OauthAccessTokenResponse](shutterstock_api_explorer/models/oauth_access_token_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[CreateAccessTokenErrorBody](shutterstock_api_explorer/errors/create_access_token_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoundEffects

> Source: [SoundEffects](shutterstock_api_explorer/apis/sound_effects.py)

<details>
<summary><code>def download_sfx(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SfxUrl, DownloadSfxErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint redownloads sound effects that you have already received a license for. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sound_effects.with_raw_response.download_sfx(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SfxUrl
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadSfxErrorBody
```

**Async**

```python
result = await async_client.sound_effects.with_raw_response.download_sfx(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SfxUrl
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadSfxErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | License ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[SfxUrl](shutterstock_api_explorer/models/sfx_url.py), [DownloadSfxErrorBody](shutterstock_api_explorer/errors/download_sfx_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SfxUrl](shutterstock_api_explorer/models/sfx_url.py)</code> -- OK

**On `Failure`**: `error` is <code>[DownloadSfxErrorBody](shutterstock_api_explorer/errors/download_sfx_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_sfx_details(id: int, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, library: Library2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Sfx, GetSfxDetailsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint shows information about a sound effect.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sound_effects.with_raw_response.get_sfx_details(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Sfx
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSfxDetailsErrorBody
```

**Async**

```python
result = await async_client.sound_effects.with_raw_response.get_sfx_details(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Sfx
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSfxDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>int</code> | Audio track ID |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>library</code> | <code>[Library2OrStr](shutterstock_api_explorer/models/enums/library2.py) \| None</code> | Which library to fetch from<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Sfx](shutterstock_api_explorer/models/sfx.py), [GetSfxDetailsErrorBody](shutterstock_api_explorer/errors/get_sfx_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Sfx](shutterstock_api_explorer/models/sfx.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetSfxDetailsErrorBody](shutterstock_api_explorer/errors/get_sfx_details_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 503 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_sfx_license_list(*, sfx_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, license_id: str | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DownloadHistoryDataList, GetSfxLicenseListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists existing licenses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sound_effects.with_raw_response.get_sfx_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSfxLicenseListErrorBody
```

**Async**

```python
result = await async_client.sound_effects.with_raw_response.get_sfx_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSfxLicenseListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sfx_id</code> | <code>str \| None</code> | Show licenses for the specified sound effects ID<br>**Default**: <code>None</code> |
| <code>license</code> | <code>str \| None</code> | Show sound effects that are available with the specified license, such as `standard` or `enhanced`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>license_id</code> | <code>str \| None</code> | Filter by the license ID<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock_api_explorer/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py), [GetSfxLicenseListErrorBody](shutterstock_api_explorer/errors/get_sfx_license_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetSfxLicenseListErrorBody](shutterstock_api_explorer/errors/get_sfx_license_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_sfx_list_details(id: list[str], *, view: View2OrStr | None = None, language: LanguageOrStr | None = None, library: Library2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SfxdataList, GetSfxListDetailsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint shows information about sound effects.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sound_effects.with_raw_response.get_sfx_list_details(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SfxdataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSfxListDetailsErrorBody
```

**Async**

```python
result = await async_client.sound_effects.with_raw_response.get_sfx_list_details(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SfxdataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSfxListDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more sound effect IDs |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>library</code> | <code>[Library2OrStr](shutterstock_api_explorer/models/enums/library2.py) \| None</code> | Which library to fetch from<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[SfxdataList](shutterstock_api_explorer/models/sfxdata_list.py), [GetSfxListDetailsErrorBody](shutterstock_api_explorer/errors/get_sfx_list_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SfxdataList](shutterstock_api_explorer/models/sfxdata_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetSfxListDetailsErrorBody](shutterstock_api_explorer/errors/get_sfx_list_details_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def licenses_sfx(body: LicenseSfxrequest | LicenseSfxrequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LicenseSfxresultDataList, LicensesSfxErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint licenses sounds effect assets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sound_effects.with_raw_response.licenses_sfx(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseSfxresultDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicensesSfxErrorBody
```

**Async**

```python
result = await async_client.sound_effects.with_raw_response.licenses_sfx(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseSfxresultDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicensesSfxErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseSfxrequest](shutterstock_api_explorer/models/license_sfxrequest.py) \| [LicenseSfxrequestDict](shutterstock_api_explorer/models/license_sfxrequest.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[LicenseSfxresultDataList](shutterstock_api_explorer/models/license_sfxresult_data_list.py), [LicensesSfxErrorBody](shutterstock_api_explorer/errors/licenses_sfx_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LicenseSfxresultDataList](shutterstock_api_explorer/models/license_sfxresult_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[LicensesSfxErrorBody](shutterstock_api_explorer/errors/licenses_sfx_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_sfx(*, added_date: Date | None = None, added_date_start: Date | None = None, added_date_end: Date | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, safe: bool | None = True, sort: Sort15OrStr | None = None, view: View2OrStr | None = None, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SfxsearchResults, SearchSfxErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND condition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sound_effects.with_raw_response.search_sfx()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SfxsearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchSfxErrorBody
```

**Async**

```python
result = await async_client.sound_effects.with_raw_response.search_sfx()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SfxsearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchSfxErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>added_date</code> | <code>Date \| None</code> | Show sound effects added on the specified date<br>**Default**: <code>None</code> |
| <code>added_date_start</code> | <code>Date \| None</code> | Show sound effects added on or after the specified date<br>**Default**: <code>None</code> |
| <code>added_date_end</code> | <code>Date \| None</code> | Show sound effects added before the specified date<br>**Default**: <code>None</code> |
| <code>duration</code> | <code>int \| None</code> | Show sound effects with the specified duration in seconds<br>**Default**: <code>None</code> |
| <code>duration_from</code> | <code>int \| None</code> | Show sound effects with the specified duration or longer in seconds<br>**Default**: <code>None</code> |
| <code>duration_to</code> | <code>int \| None</code> | Show sound effects with the specified duration or shorter in seconds<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>sort</code> | <code>[Sort15OrStr](shutterstock_api_explorer/models/enums/sort15.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Set query and result language (uses Accept-Language header if not set)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[SfxsearchResults](shutterstock_api_explorer/models/sfxsearch_results.py), [SearchSfxErrorBody](shutterstock_api_explorer/errors/search_sfx_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SfxsearchResults](shutterstock_api_explorer/models/sfxsearch_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[SearchSfxErrorBody](shutterstock_api_explorer/errors/search_sfx_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 503 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Test

> Source: [Test](shutterstock_api_explorer/apis/test.py)

<details>
<summary><code>def echo(*, text: str | None = "ok", request_options: RequestOptionsOrDict | None = None) -> ApiResult[TestEcho, EchoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.test.with_raw_response.echo()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TestEcho
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EchoErrorBody
```

**Async**

```python
result = await async_client.test.with_raw_response.echo()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TestEcho
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EchoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>text</code> | <code>str \| None</code> | Text to echo<br>**Default**: <code>"ok"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[TestEcho](shutterstock_api_explorer/models/test_echo.py), [EchoErrorBody](shutterstock_api_explorer/errors/echo_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TestEcho](shutterstock_api_explorer/models/test_echo.py)</code> -- OK

**On `Failure`**: `error` is <code>[EchoErrorBody](shutterstock_api_explorer/errors/echo_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def validate(id: int, *, tag: list[str] | None = None, user_agent: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TestValidate, ValidateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.test.with_raw_response.validate(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TestValidate
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ValidateErrorBody
```

**Async**

```python
result = await async_client.test.with_raw_response.validate(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TestValidate
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ValidateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>int</code> | Integer ID |
| <code>tag</code> | <code>list&#91;str&#93; \| None</code> | List of tags<br>**Default**: <code>None</code> |
| <code>user_agent</code> | <code>str \| None</code> | User agent<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[TestValidate](shutterstock_api_explorer/models/test_validate.py), [ValidateErrorBody](shutterstock_api_explorer/errors/validate_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TestValidate](shutterstock_api_explorer/models/test_validate.py)</code> -- OK

**On `Failure`**: `error` is <code>[ValidateErrorBody](shutterstock_api_explorer/errors/validate_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Users

> Source: [Users](shutterstock_api_explorer/apis/users.py)

<details>
<summary><code>def get_access_token(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccessTokenDetails, GetAccessTokenErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.users.with_raw_response.get_access_token()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccessTokenDetails
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccessTokenErrorBody
```

**Async**

```python
result = await async_client.users.with_raw_response.get_access_token()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccessTokenDetails
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccessTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[AccessTokenDetails](shutterstock_api_explorer/models/access_token_details.py), [GetAccessTokenErrorBody](shutterstock_api_explorer/errors/get_access_token_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccessTokenDetails](shutterstock_api_explorer/models/access_token_details.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetAccessTokenErrorBody](shutterstock_api_explorer/errors/get_access_token_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserDetails, GetUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.users.with_raw_response.get_user()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserDetails
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUserErrorBody
```

**Async**

```python
result = await async_client.users.with_raw_response.get_user()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserDetails
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[UserDetails](shutterstock_api_explorer/models/user_details.py), [GetUserErrorBody](shutterstock_api_explorer/errors/get_user_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserDetails](shutterstock_api_explorer/models/user_details.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetUserErrorBody](shutterstock_api_explorer/errors/get_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_subscription_list(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SubscriptionDataList, GetUserSubscriptionListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.users.with_raw_response.get_user_subscription_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SubscriptionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUserSubscriptionListErrorBody
```

**Async**

```python
result = await async_client.users.with_raw_response.get_user_subscription_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SubscriptionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUserSubscriptionListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[SubscriptionDataList](shutterstock_api_explorer/models/subscription_data_list.py), [GetUserSubscriptionListErrorBody](shutterstock_api_explorer/errors/get_user_subscription_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SubscriptionDataList](shutterstock_api_explorer/models/subscription_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetUserSubscriptionListErrorBody](shutterstock_api_explorer/errors/get_user_subscription_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Videos

> Source: [Videos](shutterstock_api_explorer/apis/videos.py)

<details>
<summary><code>def add_video_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, AddVideoCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint adds one or more videos to a collection by video IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.add_video_collection_items(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddVideoCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.add_video_collection_items(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddVideoCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the collection to which items should be added |
| <code>body</code> | <code>[CollectionItemRequest](shutterstock_api_explorer/models/collection_item_request.py) \| [CollectionItemRequestDict](shutterstock_api_explorer/models/collection_item_request.py)</code> | Array of video IDs to add to the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [AddVideoCollectionItemsErrorBody](shutterstock_api_explorer/errors/add_video_collection_items_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[AddVideoCollectionItemsErrorBody](shutterstock_api_explorer/errors/add_video_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_video_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionCreateResponse, CreateVideoCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint creates one or more collections (clipboxes). To add videos to collections, use `POST /v2/videos/collections/{id}/items`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.create_video_collection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateVideoCollectionErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.create_video_collection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateVideoCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CollectionCreateRequest](shutterstock_api_explorer/models/collection_create_request.py) \| [CollectionCreateRequestDict](shutterstock_api_explorer/models/collection_create_request.py)</code> | Collection metadata |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionCreateResponse](shutterstock_api_explorer/models/collection_create_response.py), [CreateVideoCollectionErrorBody](shutterstock_api_explorer/errors/create_video_collection_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionCreateResponse](shutterstock_api_explorer/models/collection_create_response.py)</code> -- Successfully created video collection

**On `Failure`**: `error` is <code>[CreateVideoCollectionErrorBody](shutterstock_api_explorer/errors/create_video_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_video_collection(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteVideoCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint deletes a collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.delete_video_collection(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteVideoCollectionErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.delete_video_collection(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteVideoCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the collection to delete |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [DeleteVideoCollectionErrorBody](shutterstock_api_explorer/errors/delete_video_collection_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteVideoCollectionErrorBody](shutterstock_api_explorer/errors/delete_video_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_video_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteVideoCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint removes one or more videos from a collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.delete_video_collection_items(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteVideoCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.delete_video_collection_items(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteVideoCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the Collection from which items will be deleted |
| <code>item_id</code> | <code>list&#91;str&#93; \| None</code> | One or more video IDs to remove from the collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [DeleteVideoCollectionItemsErrorBody](shutterstock_api_explorer/errors/delete_video_collection_items_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteVideoCollectionItemsErrorBody](shutterstock_api_explorer/errors/delete_video_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_videos(id: str, body: RedownloadVideo | RedownloadVideoDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Url, DownloadVideosErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint redownloads videos that you have already received a license for.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.download_videos(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Url
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadVideosErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.download_videos(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Url
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The license ID of the item to (re)download. The download links in the response are valid for 8 hours. |
| <code>body</code> | <code>[RedownloadVideo](shutterstock_api_explorer/models/redownload_video.py) \| [RedownloadVideoDict](shutterstock_api_explorer/models/redownload_video.py)</code> | Information about the videos to redownload |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Url](shutterstock_api_explorer/models/url.py), [DownloadVideosErrorBody](shutterstock_api_explorer/errors/download_videos_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Url](shutterstock_api_explorer/models/url.py)</code> -- OK

**On `Failure`**: `error` is <code>[DownloadVideosErrorBody](shutterstock_api_explorer/errors/download_videos_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_similar_videos(id: str, *, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[VideoSearchResults, FindSimilarVideosErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint searches for videos that are similar to a video that you specify.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.find_similar_videos(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VideoSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FindSimilarVideosErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.find_similar_videos(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VideoSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FindSimilarVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of a video for which similar videos should be returned |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[VideoSearchResults](shutterstock_api_explorer/models/video_search_results.py), [FindSimilarVideosErrorBody](shutterstock_api_explorer/errors/find_similar_videos_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[VideoSearchResults](shutterstock_api_explorer/models/video_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[FindSimilarVideosErrorBody](shutterstock_api_explorer/errors/find_similar_videos_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_updated_videos(*, start_date: str | None = None, end_date: str | None = None, interval: str | None = "1 HOUR", page: int | None = 1, per_page: int | None = 100, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdatedMediaDataList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists videos that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the `interval` parameter to show videos that were updated recently, but you can also use the `start_date` and `end_date` parameters to specify a range of no more than three days. Do not use the `interval` parameter with either `start_date` or `end_date`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.get_updated_videos()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdatedMediaDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.videos.with_raw_response.get_updated_videos()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdatedMediaDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>start_date</code> | <code>str \| None</code> | Show videos updated on or after the specified date. The API will default to UTC (00:00:00) if no specific time is provided, ensuring consistency.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | Show videos updated before the specified date. The API will default to UTC (00:00:00) if no specific time is provided, ensuring consistency. Please note that the end date must be at least 5 minutes after the start date.<br>**Default**: <code>None</code> |
| <code>interval</code> | <code>str \| None</code> | Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request<br>**Default**: <code>"1 HOUR"</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort by oldest or newest videos first<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[UpdatedMediaDataList](shutterstock_api_explorer/models/updated_media_data_list.py), [RawError](shutterstock_api_explorer/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdatedMediaDataList](shutterstock_api_explorer/models/updated_media_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](shutterstock_api_explorer/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video(id: str, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Video, GetVideoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint shows information about a video, including URLs to previews and the sizes that it is available in.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.get_video(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Video
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.get_video(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Video
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Video ID |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Video](shutterstock_api_explorer/models/video.py), [GetVideoErrorBody](shutterstock_api_explorer/errors/get_video_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Video](shutterstock_api_explorer/models/video.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetVideoErrorBody](shutterstock_api_explorer/errors/get_video_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Collection, GetVideoCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets more detailed information about a collection, including the timestamp for its creation and the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.get_video_collection(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Collection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoCollectionErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.get_video_collection(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Collection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the collection to return |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock_api_explorer/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve a shared collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Collection](shutterstock_api_explorer/models/collection.py), [GetVideoCollectionErrorBody](shutterstock_api_explorer/errors/get_video_collection_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Collection](shutterstock_api_explorer/models/collection.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetVideoCollectionErrorBody](shutterstock_api_explorer/errors/get_video_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionItemDataList, GetVideoCollectionItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the IDs of videos in a collection and the date that each was added.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.get_video_collection_items(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoCollectionItemsErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.get_video_collection_items(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionItemDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve the contents of a shared collection<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionItemDataList](shutterstock_api_explorer/models/collection_item_data_list.py), [GetVideoCollectionItemsErrorBody](shutterstock_api_explorer/errors/get_video_collection_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionItemDataList](shutterstock_api_explorer/models/collection_item_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetVideoCollectionItemsErrorBody](shutterstock_api_explorer/errors/get_video_collection_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_collection_list(*, page: int | None = 1, per_page: int | None = 100, embed: list[EmbedOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CollectionDataList, GetVideoCollectionListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists your collections of videos and their basic attributes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.get_video_collection_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoCollectionListErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.get_video_collection_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CollectionDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoCollectionListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock_api_explorer/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CollectionDataList](shutterstock_api_explorer/models/collection_data_list.py), [GetVideoCollectionListErrorBody](shutterstock_api_explorer/errors/get_video_collection_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CollectionDataList](shutterstock_api_explorer/models/collection_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetVideoCollectionListErrorBody](shutterstock_api_explorer/errors/get_video_collection_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_license_list(*, video_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DownloadHistoryDataList, GetVideoLicenseListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists existing licenses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.get_video_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoLicenseListErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.get_video_license_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadHistoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoLicenseListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>video_id</code> | <code>str \| None</code> | Show licenses for the specified video ID<br>**Default**: <code>None</code> |
| <code>license</code> | <code>str \| None</code> | Show videos that are available with the specified license, such as `standard` or `enhanced`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock_api_explorer/models/enums/sort5.py) \| None</code> | Sort by oldest or newest videos first<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock_api_explorer/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py), [GetVideoLicenseListErrorBody](shutterstock_api_explorer/errors/get_video_license_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DownloadHistoryDataList](shutterstock_api_explorer/models/download_history_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetVideoLicenseListErrorBody](shutterstock_api_explorer/errors/get_video_license_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[VideoDataList, GetVideoListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.get_video_list(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VideoDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoListErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.get_video_list(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VideoDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more video IDs |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[VideoDataList](shutterstock_api_explorer/models/video_data_list.py), [GetVideoListErrorBody](shutterstock_api_explorer/errors/get_video_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[VideoDataList](shutterstock_api_explorer/models/video_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetVideoListErrorBody](shutterstock_api_explorer/errors/get_video_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_suggestions(query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Suggestions, GetVideoSuggestionsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint provides autocomplete suggestions for partial search terms.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.get_video_suggestions(query)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Suggestions
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoSuggestionsErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.get_video_suggestions(query)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Suggestions
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetVideoSuggestionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query</code> | <code>str</code> | Search term for which you want keyword suggestions |
| <code>limit</code> | <code>int \| None</code> | Limit the number of the suggestions<br>**Default**: <code>10</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[Suggestions](shutterstock_api_explorer/models/suggestions.py), [GetVideoSuggestionsErrorBody](shutterstock_api_explorer/errors/get_video_suggestions_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Suggestions](shutterstock_api_explorer/models/suggestions.py)</code> -- OK

**On `Failure`**: `error` is <code>[GetVideoSuggestionsErrorBody](shutterstock_api_explorer/errors/get_video_suggestions_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_videos(body: LicenseVideoRequest | LicenseVideoRequestDict, *, subscription_id: str | None = None, size: Size16OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LicenseVideoResultDataList, LicenseVideosErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.license_videos(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseVideoResultDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseVideosErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.license_videos(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LicenseVideoResultDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LicenseVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseVideoRequest](shutterstock_api_explorer/models/license_video_request.py) \| [LicenseVideoRequestDict](shutterstock_api_explorer/models/license_video_request.py)</code> | List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters |
| <code>subscription_id</code> | <code>str \| None</code> | The subscription ID to use for licensing<br>**Default**: <code>None</code> |
| <code>size</code> | <code>[Size16OrStr](shutterstock_api_explorer/models/enums/size16.py) \| None</code> | The size of the video to license<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The Search ID that led to this licensing event<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[LicenseVideoResultDataList](shutterstock_api_explorer/models/license_video_result_data_list.py), [LicenseVideosErrorBody](shutterstock_api_explorer/errors/license_videos_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LicenseVideoResultDataList](shutterstock_api_explorer/models/license_video_result_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[LicenseVideosErrorBody](shutterstock_api_explorer/errors/license_videos_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_video_categories(*, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CategoryDataList, ListVideoCategoriesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.list_video_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CategoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListVideoCategoriesErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.list_video_categories()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CategoryDataList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListVideoCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[CategoryDataList](shutterstock_api_explorer/models/category_data_list.py), [ListVideoCategoriesErrorBody](shutterstock_api_explorer/errors/list_video_categories_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CategoryDataList](shutterstock_api_explorer/models/category_data_list.py)</code> -- OK

**On `Failure`**: `error` is <code>[ListVideoCategoriesErrorBody](shutterstock_api_explorer/errors/list_video_categories_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def rename_video_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RenameVideoCollectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint sets a new name for a collection.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.rename_video_collection(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RenameVideoCollectionErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.rename_video_collection(id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RenameVideoCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the collection to rename |
| <code>body</code> | <code>[CollectionUpdateRequest](shutterstock_api_explorer/models/collection_update_request.py) \| [CollectionUpdateRequestDict](shutterstock_api_explorer/models/collection_update_request.py)</code> | The new name for the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;None, [RenameVideoCollectionErrorBody](shutterstock_api_explorer/errors/rename_video_collection_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RenameVideoCollectionErrorBody](shutterstock_api_explorer/errors/rename_video_collection_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_videos(*, added_date: Date | None = None, added_date_start: Date | None = None, added_date_end: Date | None = None, aspect_ratio: AspectRatioOrStr | None = None, category: str | None = None, contributor: list[str] | None = None, contributor_country: list[str] | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, fps: float | None = None, fps_from: float | None = None, fps_to: float | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[License9OrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity5OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, people_model_released: bool | None = None, query: str | None = None, resolution: ResolutionOrStr | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[VideoSearchResults, SearchVideosErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.videos.with_raw_response.search_videos()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VideoSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchVideosErrorBody
```

**Async**

```python
result = await async_client.videos.with_raw_response.search_videos()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VideoSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>added_date</code> | <code>Date \| None</code> | Show videos added on the specified date<br>**Default**: <code>None</code> |
| <code>added_date_start</code> | <code>Date \| None</code> | Show videos added on or after the specified date<br>**Default**: <code>None</code> |
| <code>added_date_end</code> | <code>Date \| None</code> | Show videos added before the specified date<br>**Default**: <code>None</code> |
| <code>aspect_ratio</code> | <code>[AspectRatioOrStr](shutterstock_api_explorer/models/enums/aspect_ratio.py) \| None</code> | Show videos with the specified aspect ratio<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show videos with the specified Shutterstock-defined category; specify a category name or ID<br>**Default**: <code>None</code> |
| <code>contributor</code> | <code>list&#91;str&#93; \| None</code> | Show videos with the specified artist names or IDs<br>**Default**: <code>None</code> |
| <code>contributor_country</code> | <code>list&#91;str&#93; \| None</code> | Show videos from contributors in one or more specified countries<br>**Default**: <code>None</code> |
| <code>duration</code> | <code>int \| None</code> | (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in seconds<br>**Default**: <code>None</code> |
| <code>duration_from</code> | <code>int \| None</code> | Show videos with the specified duration or longer in seconds<br>**Default**: <code>None</code> |
| <code>duration_to</code> | <code>int \| None</code> | Show videos with the specified duration or shorter in seconds<br>**Default**: <code>None</code> |
| <code>fps</code> | <code>float \| None</code> | (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second<br>**Default**: <code>None</code> |
| <code>fps_from</code> | <code>float \| None</code> | Show videos with the specified frames per second or more<br>**Default**: <code>None</code> |
| <code>fps_to</code> | <code>float \| None</code> | Show videos with the specified frames per second or fewer<br>**Default**: <code>None</code> |
| <code>keyword_safe_search</code> | <code>bool \| None</code> | Hide results with potentially unsafe keywords<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock_api_explorer/models/enums/language.py) \| None</code> | Set query and result language (uses Accept-Language header if not set)<br>**Default**: <code>None</code> |
| <code>license</code> | <code>list&#91;[License9OrStr](shutterstock_api_explorer/models/enums/license9.py)&#93; \| None</code> | Show only videos with the specified license or licenses<br>**Default**: <code>None</code> |
| <code>model</code> | <code>list&#91;str&#93; \| None</code> | Show videos with each of the specified models<br>**Default**: <code>None</code> |
| <code>orientation</code> | <code>[Orientation2OrStr](shutterstock_api_explorer/models/enums/orientation2.py) \| None</code> | Search for videos in a specific orientation<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>people_age</code> | <code>[PeopleAge2OrStr](shutterstock_api_explorer/models/enums/people_age2.py) \| None</code> | Show videos that feature people of the specified age range<br>**Default**: <code>None</code> |
| <code>people_ethnicity</code> | <code>list&#91;[PeopleEthnicity5OrStr](shutterstock_api_explorer/models/enums/people_ethnicity5.py)&#93; \| None</code> | Show videos with people of the specified ethnicities<br>**Default**: <code>None</code> |
| <code>people_gender</code> | <code>[PeopleGender2OrStr](shutterstock_api_explorer/models/enums/people_gender2.py) \| None</code> | Show videos with people with the specified gender<br>**Default**: <code>None</code> |
| <code>people_number</code> | <code>int \| None</code> | Show videos with the specified number of people<br>**Default**: <code>None</code> |
| <code>people_model_released</code> | <code>bool \| None</code> | Show only videos of people with a signed model release<br>**Default**: <code>None</code> |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces; you can use NOT to filter out videos that match a term<br>**Default**: <code>None</code> |
| <code>resolution</code> | <code>[ResolutionOrStr](shutterstock_api_explorer/models/enums/resolution.py) \| None</code> | Show videos with the specified resolution<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>sort</code> | <code>[Sort2OrStr](shutterstock_api_explorer/models/enums/sort2.py) \| None</code> | Sort by one of these categories<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock_api_explorer/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock_api_explorer/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](shutterstock_api_explorer/core/results.py)&#91;[VideoSearchResults](shutterstock_api_explorer/models/video_search_results.py), [SearchVideosErrorBody](shutterstock_api_explorer/errors/search_videos_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[VideoSearchResults](shutterstock_api_explorer/models/video_search_results.py)</code> -- OK

**On `Failure`**: `error` is <code>[SearchVideosErrorBody](shutterstock_api_explorer/errors/search_videos_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock_api_explorer/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

