# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [ShutterstockClient](shutterstock/client.py)

## AudioApi

> Source: [AudioApi](shutterstock/apis/audio_api.py)

<details>
<summary><code>def add_track_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.audio_api.add_track_collection_items(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddTrackCollectionItemsErrorBody
```

**Async**

```python
try:
    await async_client.audio_api.add_track_collection_items(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddTrackCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>body</code> | <code>[CollectionItemRequest](shutterstock/models/collection_item_request.py) \| [CollectionItemRequestDict](shutterstock/models/collection_item_request.py)</code> | List of items to add to collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[AddTrackCollectionItemsErrorBody](shutterstock/errors/add_track_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_track_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CollectionCreateResponse</code></summary>

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
try:
    response = client.audio_api.create_track_collection(body)
    # TODO: Handle 'response' of type CollectionCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateTrackCollectionErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.create_track_collection(body)
    # TODO: Handle 'response' of type CollectionCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateTrackCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CollectionCreateRequest](shutterstock/models/collection_create_request.py) \| [CollectionCreateRequestDict](shutterstock/models/collection_create_request.py)</code> | Collection metadata |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionCreateResponse](shutterstock/models/collection_create_response.py)</code> -- Successfully created audio collection

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[CreateTrackCollectionErrorBody](shutterstock/errors/create_track_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_track_collection(id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.audio_api.delete_track_collection(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteTrackCollectionErrorBody
```

**Async**

```python
try:
    await async_client.audio_api.delete_track_collection(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteTrackCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DeleteTrackCollectionErrorBody](shutterstock/errors/delete_track_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_track_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.audio_api.delete_track_collection_items(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteTrackCollectionItemsErrorBody
```

**Async**

```python
try:
    await async_client.audio_api.delete_track_collection_items(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteTrackCollectionItemsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DeleteTrackCollectionItemsErrorBody](shutterstock/errors/delete_track_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_tracks(id: str, *, request_options: RequestOptionsOrDict | None = None) -> AudioUrl</code></summary>

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
try:
    response = client.audio_api.download_tracks(id)
    # TODO: Handle 'response' of type AudioUrl
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.download_tracks(id)
    # TODO: Handle 'response' of type AudioUrl
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadTracksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | License ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AudioUrl](shutterstock/models/audio_url.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DownloadTracksErrorBody](shutterstock/errors/download_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track(id: int, *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Audio</code></summary>

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
try:
    response = client.audio_api.get_track(id)
    # TODO: Handle 'response' of type Audio
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.get_track(id)
    # TODO: Handle 'response' of type Audio
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>int</code> | Audio track ID |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Audio](shutterstock/models/audio.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetTrackErrorBody](shutterstock/errors/get_track_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Collection</code></summary>

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
try:
    response = client.audio_api.get_track_collection(id)
    # TODO: Handle 'response' of type Collection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackCollectionErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.get_track_collection(id)
    # TODO: Handle 'response' of type Collection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve a shared collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Collection](shutterstock/models/collection.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetTrackCollectionErrorBody](shutterstock/errors/get_track_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CollectionItemDataList</code></summary>

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
try:
    response = client.audio_api.get_track_collection_items(id)
    # TODO: Handle 'response' of type CollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackCollectionItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.get_track_collection_items(id)
    # TODO: Handle 'response' of type CollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackCollectionItemsErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionItemDataList](shutterstock/models/collection_item_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetTrackCollectionItemsErrorBody](shutterstock/errors/get_track_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_collection_list(*, page: int | None = 1, per_page: int | None = 100, embed: list[EmbedOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> CollectionDataList</code></summary>

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
try:
    response = client.audio_api.get_track_collection_list()
    # TODO: Handle 'response' of type CollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackCollectionListErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.get_track_collection_list()
    # TODO: Handle 'response' of type CollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackCollectionListErrorBody
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
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionDataList](shutterstock/models/collection_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetTrackCollectionListErrorBody](shutterstock/errors/get_track_collection_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_license_list(*, audio_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> DownloadHistoryDataList</code></summary>

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
try:
    response = client.audio_api.get_track_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackLicenseListErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.get_track_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackLicenseListErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DownloadHistoryDataList](shutterstock/models/download_history_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetTrackLicenseListErrorBody](shutterstock/errors/get_track_license_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_track_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AudioDataList</code></summary>

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
try:
    response = client.audio_api.get_track_list(id)
    # TODO: Handle 'response' of type AudioDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackListErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.get_track_list(id)
    # TODO: Handle 'response' of type AudioDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more audio IDs |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AudioDataList](shutterstock/models/audio_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetTrackListErrorBody](shutterstock/errors/get_track_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_track(body: LicenseAudioRequest | LicenseAudioRequestDict, *, license: License10OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> LicenseAudioResultDataList</code></summary>

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
try:
    response = client.audio_api.license_track(body)
    # TODO: Handle 'response' of type LicenseAudioResultDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseTrackErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.license_track(body)
    # TODO: Handle 'response' of type LicenseAudioResultDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseTrackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseAudioRequest](shutterstock/models/license_audio_request.py) \| [LicenseAudioRequestDict](shutterstock/models/license_audio_request.py)</code> | Tracks to license |
| <code>license</code> | <code>[License10OrStr](shutterstock/models/enums/license10.py) \| None</code> | License type<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that led to licensing this track<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LicenseAudioResultDataList](shutterstock/models/license_audio_result_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[LicenseTrackErrorBody](shutterstock/errors/license_track_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_genres(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GenreList</code></summary>

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
try:
    response = client.audio_api.list_genres()
    # TODO: Handle 'response' of type GenreList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.audio_api.list_genres()
    # TODO: Handle 'response' of type GenreList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>str \| None</code> | Which language the genres will be returned<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenreList](shutterstock/models/genre_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_instruments(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None) -> InstrumentList</code></summary>

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
try:
    response = client.audio_api.list_instruments()
    # TODO: Handle 'response' of type InstrumentList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.audio_api.list_instruments()
    # TODO: Handle 'response' of type InstrumentList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>str \| None</code> | Which language the instruments will be returned in<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InstrumentList](shutterstock/models/instrument_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_moods(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None) -> MoodList</code></summary>

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
try:
    response = client.audio_api.list_moods()
    # TODO: Handle 'response' of type MoodList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.audio_api.list_moods()
    # TODO: Handle 'response' of type MoodList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>str \| None</code> | Which language the moods will be returned in<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MoodList](shutterstock/models/mood_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def rename_track_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.audio_api.rename_track_collection(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RenameTrackCollectionErrorBody
```

**Async**

```python
try:
    await async_client.audio_api.rename_track_collection(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RenameTrackCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>body</code> | <code>[CollectionUpdateRequest](shutterstock/models/collection_update_request.py) \| [CollectionUpdateRequestDict](shutterstock/models/collection_update_request.py)</code> | Collection changes |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RenameTrackCollectionErrorBody](shutterstock/errors/rename_track_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_tracks(*, artists: list[str] | None = None, bpm: int | None = None, bpm_from: int | None = None, bpm_to: int | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, genre: list[str] | None = None, is_instrumental: bool | None = None, instruments: list[str] | None = None, moods: list[str] | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, sort: Sort12OrStr | None = None, sort_order: SortOrderOrStr | None = None, vocal_description: str | None = None, view: View2OrStr | None = None, fields: str | None = None, library: Library1OrStr | None = None, language: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AudioSearchResults</code></summary>

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
try:
    response = client.audio_api.search_tracks()
    # TODO: Handle 'response' of type AudioSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchTracksErrorBody
```

**Async**

```python
try:
    response = await async_client.audio_api.search_tracks()
    # TODO: Handle 'response' of type AudioSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchTracksErrorBody
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
| <code>sort</code> | <code>[Sort12OrStr](shutterstock/models/enums/sort12.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](shutterstock/models/enums/sort_order.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>vocal_description</code> | <code>str \| None</code> | Show tracks with the specified vocal description (male, female)<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Fields to display in the response; see the documentation for the fields parameter in the overview section<br>**Default**: <code>None</code> |
| <code>library</code> | <code>[Library1OrStr](shutterstock/models/enums/library1.py) \| None</code> | Which library to search<br>**Default**: <code>None</code> |
| <code>language</code> | <code>str \| None</code> | Which language to search in<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AudioSearchResults](shutterstock/models/audio_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[SearchTracksErrorBody](shutterstock/errors/search_tracks_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Catalog

> Source: [Catalog](shutterstock/apis/catalog.py)

<details>
<summary><code>def add_to_collection(collection_id: str, body: CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict, *, request_options: RequestOptionsOrDict | None = None) -> CatalogCollection</code></summary>

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
try:
    response = client.catalog.add_to_collection(collection_id, body)
    # TODO: Handle 'response' of type CatalogCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.catalog.add_to_collection(collection_id, body)
    # TODO: Handle 'response' of type CatalogCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>collection_id</code> | <code>str</code> | The ID of the collection to add assets to |
| <code>body</code> | <code>[CreateCatalogCollectionItems](shutterstock/models/create_catalog_collection_items.py) \| [CreateCatalogCollectionItemsDict](shutterstock/models/create_catalog_collection_items.py)</code> | Collection item attributes to add to collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CatalogCollection](shutterstock/models/catalog_collection.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_collection(body: CreateCatalogCollection | CreateCatalogCollectionDict, *, request_options: RequestOptionsOrDict | None = None) -> CatalogCollection</code></summary>

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
try:
    response = client.catalog.create_collection(body)
    # TODO: Handle 'response' of type CatalogCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.catalog.create_collection(body)
    # TODO: Handle 'response' of type CatalogCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateCatalogCollection](shutterstock/models/create_catalog_collection.py) \| [CreateCatalogCollectionDict](shutterstock/models/create_catalog_collection.py)</code> | Create a catalog collection and, optionally, add items. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CatalogCollection](shutterstock/models/catalog_collection.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_collection(collection_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.catalog.delete_collection(collection_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteCollectionErrorBody
```

**Async**

```python
try:
    await async_client.catalog.delete_collection(collection_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>collection_id</code> | <code>str</code> | The ID of the collection to delete |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DeleteCollectionErrorBody](shutterstock/errors/delete_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_from_collection(collection_id: str, body: RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict, *, request_options: RequestOptionsOrDict | None = None) -> CatalogCollection</code></summary>

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
try:
    response = client.catalog.delete_from_collection(collection_id, body)
    # TODO: Handle 'response' of type CatalogCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.catalog.delete_from_collection(collection_id, body)
    # TODO: Handle 'response' of type CatalogCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>collection_id</code> | <code>str</code> | The ID of the collection to remove assets from |
| <code>body</code> | <code>[RemoveCatalogCollectionItems](shutterstock/models/remove_catalog_collection_items.py) \| [RemoveCatalogCollectionItemsDict](shutterstock/models/remove_catalog_collection_items.py)</code> | Items to remove from the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CatalogCollection](shutterstock/models/catalog_collection.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_collections(*, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, shared: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> CatalogCollectionDataList</code></summary>

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
try:
    response = client.catalog.get_collections()
    # TODO: Handle 'response' of type CatalogCollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCollectionsErrorBody
```

**Async**

```python
try:
    response = await async_client.catalog.get_collections()
    # TODO: Handle 'response' of type CatalogCollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCollectionsErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>shared</code> | <code>bool \| None</code> | Set to true to omit collections that you own and return only collections  that are shared with you<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CatalogCollectionDataList](shutterstock/models/catalog_collection_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetCollectionsErrorBody](shutterstock/errors/get_collections_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_catalog(*, sort: Sort5OrStr | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, collection_id: list[str] | None = None, asset_type: list[AssetTypeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> CatalogCollectionItemDataList</code></summary>

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
try:
    response = client.catalog.search_catalog()
    # TODO: Handle 'response' of type CatalogCollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchCatalogErrorBody
```

**Async**

```python
try:
    response = await async_client.catalog.search_catalog()
    # TODO: Handle 'response' of type CatalogCollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchCatalogErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces<br>**Default**: <code>None</code> |
| <code>collection_id</code> | <code>list&#91;str&#93; \| None</code> | Filter by collection id<br>**Default**: <code>None</code> |
| <code>asset_type</code> | <code>list&#91;[AssetTypeOrStr](shutterstock/models/enums/asset_type.py)&#93; \| None</code> | Filter by asset type<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CatalogCollectionItemDataList](shutterstock/models/catalog_collection_item_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[SearchCatalogErrorBody](shutterstock/errors/search_catalog_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_collection(collection_id: str, body: UpdateCatalogCollection | UpdateCatalogCollectionDict, *, request_options: RequestOptionsOrDict | None = None) -> CatalogCollection</code></summary>

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
try:
    response = client.catalog.update_collection(collection_id, body)
    # TODO: Handle 'response' of type CatalogCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.catalog.update_collection(collection_id, body)
    # TODO: Handle 'response' of type CatalogCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>collection_id</code> | <code>str</code> | ID of collection that needs to be modified |
| <code>body</code> | <code>[UpdateCatalogCollection](shutterstock/models/update_catalog_collection.py) \| [UpdateCatalogCollectionDict](shutterstock/models/update_catalog_collection.py)</code> | Collections Metadata to update |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CatalogCollection](shutterstock/models/catalog_collection.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ComputerVision

> Source: [ComputerVision](shutterstock/apis/computer_vision.py)

<details>
<summary><code>def get_keywords(asset_id: AssetId | AssetIdDict, *, request_options: RequestOptionsOrDict | None = None) -> KeywordDataList</code></summary>

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
try:
    response = client.computer_vision.get_keywords(asset_id)
    # TODO: Handle 'response' of type KeywordDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetKeywordsErrorBody
```

**Async**

```python
try:
    response = await async_client.computer_vision.get_keywords(asset_id)
    # TODO: Handle 'response' of type KeywordDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetKeywordsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset_id</code> | <code>[AssetId](shutterstock/models/unions/asset_id.py) \| [AssetIdDict](shutterstock/models/unions/asset_id.py)</code> | The asset ID or upload ID to suggest keywords for |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[KeywordDataList](shutterstock/models/keyword_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetKeywordsErrorBody](shutterstock/errors/get_keywords_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 415 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_similar_images(asset_id: str, *, license: list[License9OrStr] | None = None, safe: bool | None = True, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ImageSearchResults</code></summary>

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
try:
    response = client.computer_vision.get_similar_images(asset_id)
    # TODO: Handle 'response' of type ImageSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSimilarImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.computer_vision.get_similar_images(asset_id)
    # TODO: Handle 'response' of type ImageSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSimilarImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset_id</code> | <code>str</code> | The asset ID or upload ID to find similar images for |
| <code>license</code> | <code>list&#91;[License9OrStr](shutterstock/models/enums/license9.py)&#93; \| None</code> | Show only images with the specified license<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ImageSearchResults](shutterstock/models/image_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetSimilarImagesErrorBody](shutterstock/errors/get_similar_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_similar_videos(asset_id: str, *, license: list[License9OrStr] | None = None, safe: bool | None = True, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> VideoSearchResults</code></summary>

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
try:
    response = client.computer_vision.get_similar_videos(asset_id)
    # TODO: Handle 'response' of type VideoSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSimilarVideosErrorBody
```

**Async**

```python
try:
    response = await async_client.computer_vision.get_similar_videos(asset_id)
    # TODO: Handle 'response' of type VideoSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSimilarVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset_id</code> | <code>str</code> | The asset ID or upload ID to find similar videos for |
| <code>license</code> | <code>list&#91;[License9OrStr](shutterstock/models/enums/license9.py)&#93; \| None</code> | Show only videos with the specified license<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[VideoSearchResults](shutterstock/models/video_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetSimilarVideosErrorBody](shutterstock/errors/get_similar_videos_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upload_image(body: ImageCreateRequest | ImageCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ComputerVisionImageCreateResponse</code></summary>

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
try:
    response = client.computer_vision.upload_image(body)
    # TODO: Handle 'response' of type ComputerVisionImageCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UploadImageErrorBody
```

**Async**

```python
try:
    response = await async_client.computer_vision.upload_image(body)
    # TODO: Handle 'response' of type ComputerVisionImageCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UploadImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ImageCreateRequest](shutterstock/models/image_create_request.py) \| [ImageCreateRequestDict](shutterstock/models/image_create_request.py)</code> | A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComputerVisionImageCreateResponse](shutterstock/models/computer_vision_image_create_response.py)</code> -- Created

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[UploadImageErrorBody](shutterstock/errors/upload_image_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 413, 415 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Contributors

> Source: [Contributors](shutterstock/apis/contributors.py)

<details>
<summary><code>def get_contributor(contributor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ContributorProfile</code></summary>

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
try:
    response = client.contributors.get_contributor(contributor_id)
    # TODO: Handle 'response' of type ContributorProfile
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorErrorBody
```

**Async**

```python
try:
    response = await async_client.contributors.get_contributor(contributor_id)
    # TODO: Handle 'response' of type ContributorProfile
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>contributor_id</code> | <code>str</code> | Contributor ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ContributorProfile](shutterstock/models/contributor_profile.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetContributorErrorBody](shutterstock/errors/get_contributor_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_contributor_collection_items(contributor_id: str, id: str, *, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CollectionItemDataList</code></summary>

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
try:
    response = client.contributors.get_contributor_collection_items(contributor_id, id)
    # TODO: Handle 'response' of type CollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorCollectionItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.contributors.get_contributor_collection_items(contributor_id, id)
    # TODO: Handle 'response' of type CollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorCollectionItemsErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionItemDataList](shutterstock/models/collection_item_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetContributorCollectionItemsErrorBody](shutterstock/errors/get_contributor_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_contributor_collections(contributor_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None) -> Collection</code></summary>

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
try:
    response = client.contributors.get_contributor_collections(contributor_id, id)
    # TODO: Handle 'response' of type Collection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorCollectionsErrorBody
```

**Async**

```python
try:
    response = await async_client.contributors.get_contributor_collections(contributor_id, id)
    # TODO: Handle 'response' of type Collection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorCollectionsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Collection](shutterstock/models/collection.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetContributorCollectionsErrorBody](shutterstock/errors/get_contributor_collections_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_contributor_collections_list(contributor_id: str, *, sort: Sort24OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CollectionDataList</code></summary>

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
try:
    response = client.contributors.get_contributor_collections_list(contributor_id)
    # TODO: Handle 'response' of type CollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorCollectionsListErrorBody
```

**Async**

```python
try:
    response = await async_client.contributors.get_contributor_collections_list(contributor_id)
    # TODO: Handle 'response' of type CollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorCollectionsListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>contributor_id</code> | <code>str</code> | Contributor ID |
| <code>sort</code> | <code>[Sort24OrStr](shutterstock/models/enums/sort24.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionDataList](shutterstock/models/collection_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetContributorCollectionsListErrorBody](shutterstock/errors/get_contributor_collections_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_contributor_list(id: list[str], *, request_options: RequestOptionsOrDict | None = None) -> ContributorProfileDataList</code></summary>

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
try:
    response = client.contributors.get_contributor_list(id)
    # TODO: Handle 'response' of type ContributorProfileDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorListErrorBody
```

**Async**

```python
try:
    response = await async_client.contributors.get_contributor_list(id)
    # TODO: Handle 'response' of type ContributorProfileDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetContributorListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more contributor IDs |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ContributorProfileDataList](shutterstock/models/contributor_profile_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetContributorListErrorBody](shutterstock/errors/get_contributor_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## EditorialImages

> Source: [EditorialImages](shutterstock/apis/editorial_images.py)

<details>
<summary><code>def get_editorial_categories(*, request_options: RequestOptionsOrDict | None = None) -> EditorialCategoryResults</code></summary>

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
try:
    response = client.editorial_images.get_editorial_categories()
    # TODO: Handle 'response' of type EditorialCategoryResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialCategoriesErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_categories()
    # TODO: Handle 'response' of type EditorialCategoryResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialCategoryResults](shutterstock/models/editorial_category_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialCategoriesErrorBody](shutterstock/errors/get_editorial_categories_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> EditorialContent</code></summary>

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
try:
    response = client.editorial_images.get_editorial_image(id, country)
    # TODO: Handle 'response' of type EditorialContent
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_image(id, country)
    # TODO: Handle 'response' of type EditorialContent
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialContent](shutterstock/models/editorial_content.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialImageErrorBody](shutterstock/errors/get_editorial_image_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image2(id: str, country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> EditorialContent</code></summary>

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
try:
    response = client.editorial_images.get_editorial_image2(id, country)
    # TODO: Handle 'response' of type EditorialContent
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImage2ErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_image2(id, country)
    # TODO: Handle 'response' of type EditorialContent
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImage2ErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialContent](shutterstock/models/editorial_content.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialImage2ErrorBody](shutterstock/errors/get_editorial_image2_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image_license_list(*, image_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> DownloadHistoryDataList</code></summary>

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
try:
    response = client.editorial_images.get_editorial_image_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageLicenseListErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_image_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageLicenseListErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DownloadHistoryDataList](shutterstock/models/download_history_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialImageLicenseListErrorBody](shutterstock/errors/get_editorial_image_license_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image_livefeed(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> EditorialImageLivefeed</code></summary>

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
try:
    response = client.editorial_images.get_editorial_image_livefeed(id, country)
    # TODO: Handle 'response' of type EditorialImageLivefeed
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageLivefeedErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_image_livefeed(id, country)
    # TODO: Handle 'response' of type EditorialImageLivefeed
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageLivefeedErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialImageLivefeed](shutterstock/models/editorial_image_livefeed.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialImageLivefeedErrorBody](shutterstock/errors/get_editorial_image_livefeed_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image_livefeed_items(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> EditorialContentDataList</code></summary>

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
try:
    response = client.editorial_images.get_editorial_image_livefeed_items(id, country)
    # TODO: Handle 'response' of type EditorialContentDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageLivefeedItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_image_livefeed_items(id, country)
    # TODO: Handle 'response' of type EditorialContentDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageLivefeedItemsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialContentDataList](shutterstock/models/editorial_content_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialImageLivefeedItemsErrorBody](shutterstock/errors/get_editorial_image_livefeed_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_image_livefeed_list(country: str, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> EditorialImageLivefeedList</code></summary>

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
try:
    response = client.editorial_images.get_editorial_image_livefeed_list(country)
    # TODO: Handle 'response' of type EditorialImageLivefeedList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageLivefeedListErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_image_livefeed_list(country)
    # TODO: Handle 'response' of type EditorialImageLivefeedList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialImageLivefeedListErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialImageLivefeedList](shutterstock/models/editorial_image_livefeed_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialImageLivefeedListErrorBody](shutterstock/errors/get_editorial_image_livefeed_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_livefeed(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> EditorialImageLivefeed</code></summary>

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
try:
    response = client.editorial_images.get_editorial_livefeed(id, country)
    # TODO: Handle 'response' of type EditorialImageLivefeed
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialLivefeedErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_livefeed(id, country)
    # TODO: Handle 'response' of type EditorialImageLivefeed
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialLivefeedErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialImageLivefeed](shutterstock/models/editorial_image_livefeed.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialLivefeedErrorBody](shutterstock/errors/get_editorial_livefeed_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_livefeed_items(id: str, country: str, *, request_options: RequestOptionsOrDict | None = None) -> EditorialContentDataList</code></summary>

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
try:
    response = client.editorial_images.get_editorial_livefeed_items(id, country)
    # TODO: Handle 'response' of type EditorialContentDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialLivefeedItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_livefeed_items(id, country)
    # TODO: Handle 'response' of type EditorialContentDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialLivefeedItemsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialContentDataList](shutterstock/models/editorial_content_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialLivefeedItemsErrorBody](shutterstock/errors/get_editorial_livefeed_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_livefeed_list(country: str, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> EditorialImageLivefeedList</code></summary>

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
try:
    response = client.editorial_images.get_editorial_livefeed_list(country)
    # TODO: Handle 'response' of type EditorialImageLivefeedList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialLivefeedListErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_editorial_livefeed_list(country)
    # TODO: Handle 'response' of type EditorialImageLivefeedList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialLivefeedListErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialImageLivefeedList](shutterstock/models/editorial_image_livefeed_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialLivefeedListErrorBody](shutterstock/errors/get_editorial_livefeed_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_updated_editorial_image(type_: Type15OrStr, date_updated_start: RFC3339DateTime, date_updated_end: RFC3339DateTime, country: str, *, date_taken_start: Date | None = None, date_taken_end: Date | None = None, cursor: str | None = None, sort: Sort5OrStr | None = None, supplier_code: list[str] | None = None, per_page: int | None = 500, request_options: RequestOptionsOrDict | None = None) -> EditorialUpdatedResults</code></summary>

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
try:
    response = client.editorial_images.get_updated_editorial_image(type_, date_updated_start, date_updated_end, country)
    # TODO: Handle 'response' of type EditorialUpdatedResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUpdatedEditorialImageErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_updated_editorial_image(
        type_, date_updated_start, date_updated_end, country
    )
    # TODO: Handle 'response' of type EditorialUpdatedResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUpdatedEditorialImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type15OrStr](shutterstock/models/enums/type15.py)</code> | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted |
| <code>date_updated_start</code> | <code>RFC3339DateTime</code> | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. |
| <code>date_updated_end</code> | <code>RFC3339DateTime</code> | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. |
| <code>country</code> | <code>str</code> | Show only editorial content that is available for distribution in a certain country |
| <code>date_taken_start</code> | <code>Date \| None</code> | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets<br>**Default**: <code>None</code> |
| <code>date_taken_end</code> | <code>Date \| None</code> | Show images that were taken before the specified date<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial content from certain suppliers<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>500</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialUpdatedResults](shutterstock/models/editorial_updated_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetUpdatedEditorialImageErrorBody](shutterstock/errors/get_updated_editorial_image_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_updated_editorial_images(type_: Type15OrStr, date_updated_start: RFC3339DateTime, date_updated_end: RFC3339DateTime, country: str, *, date_taken_start: Date | None = None, date_taken_end: Date | None = None, cursor: str | None = None, sort: Sort5OrStr | None = None, supplier_code: list[str] | None = None, per_page: int | None = 500, request_options: RequestOptionsOrDict | None = None) -> EditorialUpdatedResults</code></summary>

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
try:
    response = client.editorial_images.get_updated_editorial_images(
        type_, date_updated_start, date_updated_end, country
    )
    # TODO: Handle 'response' of type EditorialUpdatedResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUpdatedEditorialImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.get_updated_editorial_images(
        type_, date_updated_start, date_updated_end, country
    )
    # TODO: Handle 'response' of type EditorialUpdatedResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUpdatedEditorialImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type15OrStr](shutterstock/models/enums/type15.py)</code> | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted |
| <code>date_updated_start</code> | <code>RFC3339DateTime</code> | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. |
| <code>date_updated_end</code> | <code>RFC3339DateTime</code> | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. |
| <code>country</code> | <code>str</code> | Show only editorial content that is available for distribution in a certain country |
| <code>date_taken_start</code> | <code>Date \| None</code> | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets<br>**Default**: <code>None</code> |
| <code>date_taken_end</code> | <code>Date \| None</code> | Show images that were taken before the specified date<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial content from certain suppliers<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>500</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialUpdatedResults](shutterstock/models/editorial_updated_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetUpdatedEditorialImagesErrorBody](shutterstock/errors/get_updated_editorial_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_editorial_image(body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LicenseEditorialContentResults</code></summary>

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
try:
    response = client.editorial_images.license_editorial_image(body)
    # TODO: Handle 'response' of type LicenseEditorialContentResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseEditorialImageErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.license_editorial_image(body)
    # TODO: Handle 'response' of type LicenseEditorialContentResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseEditorialImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseEditorialContentRequest](shutterstock/models/license_editorial_content_request.py) \| [LicenseEditorialContentRequestDict](shutterstock/models/license_editorial_content_request.py)</code> | License editorial content |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LicenseEditorialContentResults](shutterstock/models/license_editorial_content_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[LicenseEditorialImageErrorBody](shutterstock/errors/license_editorial_image_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_editorial_images(body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LicenseEditorialContentResults</code></summary>

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
try:
    response = client.editorial_images.license_editorial_images(body)
    # TODO: Handle 'response' of type LicenseEditorialContentResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseEditorialImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.license_editorial_images(body)
    # TODO: Handle 'response' of type LicenseEditorialContentResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseEditorialImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseEditorialContentRequest](shutterstock/models/license_editorial_content_request.py) \| [LicenseEditorialContentRequestDict](shutterstock/models/license_editorial_content_request.py)</code> | License editorial content |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LicenseEditorialContentResults](shutterstock/models/license_editorial_content_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[LicenseEditorialImagesErrorBody](shutterstock/errors/license_editorial_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_editorial_image_categories(*, request_options: RequestOptionsOrDict | None = None) -> EditorialImageCategoryResults</code></summary>

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
try:
    response = client.editorial_images.list_editorial_image_categories()
    # TODO: Handle 'response' of type EditorialImageCategoryResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListEditorialImageCategoriesErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.list_editorial_image_categories()
    # TODO: Handle 'response' of type EditorialImageCategoryResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListEditorialImageCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialImageCategoryResults](shutterstock/models/editorial_image_category_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[ListEditorialImageCategoriesErrorBody](shutterstock/errors/list_editorial_image_categories_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_editorial_images(id: list[str], country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> EditorialImageResults</code></summary>

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
try:
    response = client.editorial_images.list_editorial_images(id, country)
    # TODO: Handle 'response' of type EditorialImageResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListEditorialImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.list_editorial_images(id, country)
    # TODO: Handle 'response' of type EditorialImageResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListEditorialImagesErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialImageResults](shutterstock/models/editorial_image_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[ListEditorialImagesErrorBody](shutterstock/errors/list_editorial_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_editorial(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> EditorialSearchResults</code></summary>

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
try:
    response = client.editorial_images.search_editorial(country)
    # TODO: Handle 'response' of type EditorialSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchEditorialErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.search_editorial(country)
    # TODO: Handle 'response' of type EditorialSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchEditorialErrorBody
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
| <code>sort</code> | <code>[Sort17OrStr](shutterstock/models/enums/sort17.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show editorial content within a certain editorial category; specify by category name<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial content from certain suppliers<br>**Default**: <code>None</code> |
| <code>date_start</code> | <code>Date \| None</code> | Show only editorial content generated on or after a specific date<br>**Default**: <code>None</code> |
| <code>date_end</code> | <code>Date \| None</code> | Show only editorial content generated on or before a specific date<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialSearchResults](shutterstock/models/editorial_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[SearchEditorialErrorBody](shutterstock/errors/search_editorial_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_editorial_images(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> EditorialSearchResults</code></summary>

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
try:
    response = client.editorial_images.search_editorial_images(country)
    # TODO: Handle 'response' of type EditorialSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchEditorialImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_images.search_editorial_images(country)
    # TODO: Handle 'response' of type EditorialSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchEditorialImagesErrorBody
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
| <code>sort</code> | <code>[Sort17OrStr](shutterstock/models/enums/sort17.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial content from certain suppliers<br>**Default**: <code>None</code> |
| <code>date_start</code> | <code>Date \| None</code> | Show only editorial content generated on or after a specific date<br>**Default**: <code>None</code> |
| <code>date_end</code> | <code>Date \| None</code> | Show only editorial content generated on or before a specific date<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialSearchResults](shutterstock/models/editorial_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[SearchEditorialImagesErrorBody](shutterstock/errors/search_editorial_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## EditorialVideo

> Source: [EditorialVideo](shutterstock/apis/editorial_video.py)

<details>
<summary><code>def get_editorial_video(id: str, country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> EditorialVideoContent</code></summary>

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
try:
    response = client.editorial_video.get_editorial_video(id, country)
    # TODO: Handle 'response' of type EditorialVideoContent
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialVideoErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_video.get_editorial_video(id, country)
    # TODO: Handle 'response' of type EditorialVideoContent
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialVideoErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialVideoContent](shutterstock/models/editorial_video_content.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialVideoErrorBody](shutterstock/errors/get_editorial_video_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_editorial_video_license_list(*, video_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> DownloadHistoryDataList</code></summary>

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
try:
    response = client.editorial_video.get_editorial_video_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialVideoLicenseListErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_video.get_editorial_video_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEditorialVideoLicenseListErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DownloadHistoryDataList](shutterstock/models/download_history_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetEditorialVideoLicenseListErrorBody](shutterstock/errors/get_editorial_video_license_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_editorial_video(body: LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LicenseEditorialContentResults</code></summary>

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
try:
    response = client.editorial_video.license_editorial_video(body)
    # TODO: Handle 'response' of type LicenseEditorialContentResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseEditorialVideoErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_video.license_editorial_video(body)
    # TODO: Handle 'response' of type LicenseEditorialContentResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseEditorialVideoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseEditorialVideoContentRequest](shutterstock/models/license_editorial_video_content_request.py) \| [LicenseEditorialVideoContentRequestDict](shutterstock/models/license_editorial_video_content_request.py)</code> | License editorial video content |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LicenseEditorialContentResults](shutterstock/models/license_editorial_content_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[LicenseEditorialVideoErrorBody](shutterstock/errors/license_editorial_video_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_editorial_video_categories(*, request_options: RequestOptionsOrDict | None = None) -> EditorialVideoCategoryResults</code></summary>

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
try:
    response = client.editorial_video.list_editorial_video_categories()
    # TODO: Handle 'response' of type EditorialVideoCategoryResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListEditorialVideoCategoriesErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_video.list_editorial_video_categories()
    # TODO: Handle 'response' of type EditorialVideoCategoryResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListEditorialVideoCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialVideoCategoryResults](shutterstock/models/editorial_video_category_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[ListEditorialVideoCategoriesErrorBody](shutterstock/errors/list_editorial_video_categories_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_editorial_videos(id: list[str], country: str, *, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> EditorialVideoResults</code></summary>

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
try:
    response = client.editorial_video.list_editorial_videos(id, country)
    # TODO: Handle 'response' of type EditorialVideoResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListEditorialVideosErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_video.list_editorial_videos(id, country)
    # TODO: Handle 'response' of type EditorialVideoResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListEditorialVideosErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialVideoResults](shutterstock/models/editorial_video_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[ListEditorialVideosErrorBody](shutterstock/errors/list_editorial_videos_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_editorial_videos(country: str, *, query: str | None = None, sort: Sort17OrStr | None = None, category: str | None = None, supplier_code: list[str] | None = None, date_start: Date | None = None, date_end: Date | None = None, resolution: ResolutionOrStr | None = None, fps: float | None = None, per_page: int | None = 20, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> EditorialVideoSearchResults</code></summary>

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
try:
    response = client.editorial_video.search_editorial_videos(country)
    # TODO: Handle 'response' of type EditorialVideoSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchEditorialVideosErrorBody
```

**Async**

```python
try:
    response = await async_client.editorial_video.search_editorial_videos(country)
    # TODO: Handle 'response' of type EditorialVideoSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchEditorialVideosErrorBody
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
| <code>sort</code> | <code>[Sort17OrStr](shutterstock/models/enums/sort17.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list<br>**Default**: <code>None</code> |
| <code>supplier_code</code> | <code>list&#91;str&#93; \| None</code> | Show only editorial video content from certain suppliers<br>**Default**: <code>None</code> |
| <code>date_start</code> | <code>Date \| None</code> | Show only editorial video content generated on or after a specific date<br>**Default**: <code>None</code> |
| <code>date_end</code> | <code>Date \| None</code> | Show only editorial video content generated on or before a specific date<br>**Default**: <code>None</code> |
| <code>resolution</code> | <code>[ResolutionOrStr](shutterstock/models/enums/resolution.py) \| None</code> | Show only editorial video content with specific resolution<br>**Default**: <code>None</code> |
| <code>fps</code> | <code>float \| None</code> | Show only editorial video content generated with specific frames per second<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor of the page with which to start fetching results; this cursor is returned from previous requests<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EditorialVideoSearchResults](shutterstock/models/editorial_video_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[SearchEditorialVideosErrorBody](shutterstock/errors/search_editorial_videos_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Images

> Source: [Images](shutterstock/apis/images.py)

<details>
<summary><code>def add_image_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.images.add_image_collection_items(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddImageCollectionItemsErrorBody
```

**Async**

```python
try:
    await async_client.images.add_image_collection_items(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddImageCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>body</code> | <code>[CollectionItemRequest](shutterstock/models/collection_item_request.py) \| [CollectionItemRequestDict](shutterstock/models/collection_item_request.py)</code> | Array of image IDs to add to the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[AddImageCollectionItemsErrorBody](shutterstock/errors/add_image_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_search_images(body: list[SearchImage | SearchImageDict], *, added_date: Date | None = None, added_date_start: Date | None = None, aspect_ratio_min: float | None = None, aspect_ratio_max: float | None = None, aspect_ratio: float | None = None, added_date_end: Date | None = None, category: str | None = None, color: str | None = None, contributor: list[str] | None = None, contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None, fields: str | None = None, height: int | None = None, height_from: int | None = None, height_to: int | None = None, image_type: list[ImageType2OrStr] | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[LicenseOrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_model_released: bool | None = None, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity2OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, region: RegionModel | RegionModelDict | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, spellcheck_query: bool | None = True, view: View2OrStr | None = None, width: int | None = None, width_from: int | None = None, width_to: int | None = None, request_options: RequestOptionsOrDict | None = None) -> BulkImageSearchResults</code></summary>

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
try:
    response = client.images.bulk_search_images(body)
    # TODO: Handle 'response' of type BulkImageSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkSearchImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.images.bulk_search_images(body)
    # TODO: Handle 'response' of type BulkImageSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkSearchImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>list&#91;[SearchImage](shutterstock/models/search_image.py) \| [SearchImageDict](shutterstock/models/search_image.py)&#93;</code> | List of queries to request results for and filters to apply per query; these values override the defaults in the query parameters |
| <code>added_date</code> | <code>Date \| None</code> | Show images added on the specified date<br>**Default**: <code>None</code> |
| <code>added_date_start</code> | <code>Date \| None</code> | Show images added on or after the specified date<br>**Default**: <code>None</code> |
| <code>aspect_ratio_min</code> | <code>float \| None</code> | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>aspect_ratio_max</code> | <code>float \| None</code> | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>aspect_ratio</code> | <code>float \| None</code> | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>added_date_end</code> | <code>Date \| None</code> | Show images added before the specified date<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show images with the specified Shutterstock-defined category; specify a category name or ID<br>**Default**: <code>None</code> |
| <code>color</code> | <code>str \| None</code> | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors<br>**Default**: <code>None</code> |
| <code>contributor</code> | <code>list&#91;str&#93; \| None</code> | Show images with the specified contributor names or IDs, allows multiple<br>**Default**: <code>None</code> |
| <code>contributor_country</code> | <code>[ContributorCountryModel](shutterstock/models/unions/contributor_country_model.py) \| [ContributorCountryModelDict](shutterstock/models/unions/contributor_country_model.py) \| None</code> | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Fields to display in the response; see the documentation for the fields parameter in the overview section<br>**Default**: <code>None</code> |
| <code>height</code> | <code>int \| None</code> | (Deprecated; use height_from and height_to instead) Show images with the specified height<br>**Default**: <code>None</code> |
| <code>height_from</code> | <code>int \| None</code> | Show images with the specified height or larger, in pixels<br>**Default**: <code>None</code> |
| <code>height_to</code> | <code>int \| None</code> | Show images with the specified height or smaller, in pixels<br>**Default**: <code>None</code> |
| <code>image_type</code> | <code>list&#91;[ImageType2OrStr](shutterstock/models/enums/image_type2.py)&#93; \| None</code> | Show images of the specified type<br>**Default**: <code>None</code> |
| <code>keyword_safe_search</code> | <code>bool \| None</code> | Hide results with potentially unsafe keywords<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Set query and result language (uses Accept-Language header if not set)<br>**Default**: <code>None</code> |
| <code>license</code> | <code>list&#91;[LicenseOrStr](shutterstock/models/enums/license.py)&#93; \| None</code> | Show only images with the specified license<br>**Default**: <code>None</code> |
| <code>model</code> | <code>list&#91;str&#93; \| None</code> | Show image results with the specified model IDs<br>**Default**: <code>None</code> |
| <code>orientation</code> | <code>[Orientation2OrStr](shutterstock/models/enums/orientation2.py) \| None</code> | Show image results with horizontal or vertical orientation<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>people_model_released</code> | <code>bool \| None</code> | Show images of people with a signed model release<br>**Default**: <code>None</code> |
| <code>people_age</code> | <code>[PeopleAge2OrStr](shutterstock/models/enums/people_age2.py) \| None</code> | Show images that feature people of the specified age category<br>**Default**: <code>None</code> |
| <code>people_ethnicity</code> | <code>list&#91;[PeopleEthnicity2OrStr](shutterstock/models/enums/people_ethnicity2.py)&#93; \| None</code> | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities<br>**Default**: <code>None</code> |
| <code>people_gender</code> | <code>[PeopleGender2OrStr](shutterstock/models/enums/people_gender2.py) \| None</code> | Show images with people of the specified gender<br>**Default**: <code>None</code> |
| <code>people_number</code> | <code>int \| None</code> | Show images with the specified number of people<br>**Default**: <code>None</code> |
| <code>region</code> | <code>[RegionModel](shutterstock/models/unions/region_model.py) \| [RegionModelDict](shutterstock/models/unions/region_model.py) \| None</code> | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>sort</code> | <code>[Sort2OrStr](shutterstock/models/enums/sort2.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>spellcheck_query</code> | <code>bool \| None</code> | Spellcheck the search query and return results on suggested spellings<br>**Default**: <code>True</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>width</code> | <code>int \| None</code> | (Deprecated; use width_from and width_to instead) Show images with the specified width<br>**Default**: <code>None</code> |
| <code>width_from</code> | <code>int \| None</code> | Show images with the specified width or larger, in pixels<br>**Default**: <code>None</code> |
| <code>width_to</code> | <code>int \| None</code> | Show images with the specified width or smaller, in pixels<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BulkImageSearchResults](shutterstock/models/bulk_image_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[BulkSearchImagesErrorBody](shutterstock/errors/bulk_search_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_image_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CollectionCreateResponse</code></summary>

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
try:
    response = client.images.create_image_collection(body)
    # TODO: Handle 'response' of type CollectionCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateImageCollectionErrorBody
```

**Async**

```python
try:
    response = await async_client.images.create_image_collection(body)
    # TODO: Handle 'response' of type CollectionCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateImageCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CollectionCreateRequest](shutterstock/models/collection_create_request.py) \| [CollectionCreateRequestDict](shutterstock/models/collection_create_request.py)</code> | The names of the new collections |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionCreateResponse](shutterstock/models/collection_create_response.py)</code> -- Successfully created image collection

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[CreateImageCollectionErrorBody](shutterstock/errors/create_image_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_image_collection(id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.images.delete_image_collection(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteImageCollectionErrorBody
```

**Async**

```python
try:
    await async_client.images.delete_image_collection(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteImageCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DeleteImageCollectionErrorBody](shutterstock/errors/delete_image_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_image_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.images.delete_image_collection_items(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteImageCollectionItemsErrorBody
```

**Async**

```python
try:
    await async_client.images.delete_image_collection_items(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteImageCollectionItemsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DeleteImageCollectionItemsErrorBody](shutterstock/errors/delete_image_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_image(id: str, body: RedownloadImage | RedownloadImageDict, *, request_options: RequestOptionsOrDict | None = None) -> Url</code></summary>

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
try:
    response = client.images.download_image(id, body)
    # TODO: Handle 'response' of type Url
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadImageErrorBody
```

**Async**

```python
try:
    response = await async_client.images.download_image(id, body)
    # TODO: Handle 'response' of type Url
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | License ID |
| <code>body</code> | <code>[RedownloadImage](shutterstock/models/redownload_image.py) \| [RedownloadImageDict](shutterstock/models/redownload_image.py)</code> | Information about the images to redownload |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Url](shutterstock/models/url.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DownloadImageErrorBody](shutterstock/errors/download_image_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image(id: str, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Image</code></summary>

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
try:
    response = client.images.get_image(id)
    # TODO: Handle 'response' of type Image
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image(id)
    # TODO: Handle 'response' of type Image
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Image ID |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Image](shutterstock/models/image.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageErrorBody](shutterstock/errors/get_image_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Collection</code></summary>

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
try:
    response = client.images.get_image_collection(id)
    # TODO: Handle 'response' of type Collection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageCollectionErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image_collection(id)
    # TODO: Handle 'response' of type Collection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve a shared collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Collection](shutterstock/models/collection.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageCollectionErrorBody](shutterstock/errors/get_image_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CollectionItemDataList</code></summary>

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
try:
    response = client.images.get_image_collection_items(id)
    # TODO: Handle 'response' of type CollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageCollectionItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image_collection_items(id)
    # TODO: Handle 'response' of type CollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageCollectionItemsErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionItemDataList](shutterstock/models/collection_item_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageCollectionItemsErrorBody](shutterstock/errors/get_image_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_collection_list(*, embed: list[EmbedOrStr] | None = None, page: int | None = 1, per_page: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> CollectionDataList</code></summary>

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
try:
    response = client.images.get_image_collection_list()
    # TODO: Handle 'response' of type CollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageCollectionListErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image_collection_list()
    # TODO: Handle 'response' of type CollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageCollectionListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionDataList](shutterstock/models/collection_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageCollectionListErrorBody](shutterstock/errors/get_image_collection_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_keyword_suggestions(body: SearchEntitiesRequest | SearchEntitiesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SearchEntitiesResponse</code></summary>

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
try:
    response = client.images.get_image_keyword_suggestions(body)
    # TODO: Handle 'response' of type SearchEntitiesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageKeywordSuggestionsErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image_keyword_suggestions(body)
    # TODO: Handle 'response' of type SearchEntitiesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageKeywordSuggestionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchEntitiesRequest](shutterstock/models/search_entities_request.py) \| [SearchEntitiesRequestDict](shutterstock/models/search_entities_request.py)</code> | Plain text to extract keywords from |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SearchEntitiesResponse](shutterstock/models/search_entities_response.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageKeywordSuggestionsErrorBody](shutterstock/errors/get_image_keyword_suggestions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_license_list(*, image_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> DownloadHistoryDataList</code></summary>

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
try:
    response = client.images.get_image_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageLicenseListErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageLicenseListErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DownloadHistoryDataList](shutterstock/models/download_history_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageLicenseListErrorBody](shutterstock/errors/get_image_license_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ImageDataList</code></summary>

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
try:
    response = client.images.get_image_list(id)
    # TODO: Handle 'response' of type ImageDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageListErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image_list(id)
    # TODO: Handle 'response' of type ImageDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more image IDs |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ImageDataList](shutterstock/models/image_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageListErrorBody](shutterstock/errors/get_image_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_recommendations(id: list[str], *, max_items: int | None = 20, safe: bool | None = True, request_options: RequestOptionsOrDict | None = None) -> RecommendationDataList</code></summary>

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
try:
    response = client.images.get_image_recommendations(id)
    # TODO: Handle 'response' of type RecommendationDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageRecommendationsErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image_recommendations(id)
    # TODO: Handle 'response' of type RecommendationDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageRecommendationsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RecommendationDataList](shutterstock/models/recommendation_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageRecommendationsErrorBody](shutterstock/errors/get_image_recommendations_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_image_suggestions(query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None) -> Suggestions</code></summary>

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
try:
    response = client.images.get_image_suggestions(query)
    # TODO: Handle 'response' of type Suggestions
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageSuggestionsErrorBody
```

**Async**

```python
try:
    response = await async_client.images.get_image_suggestions(query)
    # TODO: Handle 'response' of type Suggestions
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetImageSuggestionsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Suggestions](shutterstock/models/suggestions.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetImageSuggestionsErrorBody](shutterstock/errors/get_image_suggestions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_updated_images(*, type_: list[Type14OrStr] | None = None, start_date: str | None = None, end_date: str | None = None, interval: str | None = "1 HOUR", page: int | None = 1, per_page: int | None = 100, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> UpdatedMediaDataList</code></summary>

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
try:
    response = client.images.get_updated_images()
    # TODO: Handle 'response' of type UpdatedMediaDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.images.get_updated_images()
    # TODO: Handle 'response' of type UpdatedMediaDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>list&#91;[Type14OrStr](shutterstock/models/enums/type14.py)&#93; \| None</code> | Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | Show images updated on or after the specified date. The API will default to UTC (00:00:00) if no specific time is provided, ensuring consistency.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | Show images updated before the specified date. The API will default to UTC (00:00:00) if no specific time is provided, ensuring consistency. Please note that the end date must be at least 5 minutes after the start date.<br>**Default**: <code>None</code> |
| <code>interval</code> | <code>str \| None</code> | Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request<br>**Default**: <code>"1 HOUR"</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>100</code> |
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UpdatedMediaDataList](shutterstock/models/updated_media_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_images(body: LicenseImageRequest | LicenseImageRequestDict, *, subscription_id: str | None = None, format: Format15OrStr | None = None, size: Size12OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> LicenseImageResultDataList</code></summary>

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
try:
    response = client.images.license_images(body)
    # TODO: Handle 'response' of type LicenseImageResultDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.images.license_images(body)
    # TODO: Handle 'response' of type LicenseImageResultDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseImageRequest](shutterstock/models/license_image_request.py) \| [LicenseImageRequestDict](shutterstock/models/license_image_request.py)</code> | List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters |
| <code>subscription_id</code> | <code>str \| None</code> | Subscription ID to use to license the image<br>**Default**: <code>None</code> |
| <code>format</code> | <code>[Format15OrStr](shutterstock/models/enums/format15.py) \| None</code> | (Deprecated) Image format<br>**Default**: <code>None</code> |
| <code>size</code> | <code>[Size12OrStr](shutterstock/models/enums/size12.py) \| None</code> | Image size<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | Search ID that was provided in the results of an image search<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LicenseImageResultDataList](shutterstock/models/license_image_result_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[LicenseImagesErrorBody](shutterstock/errors/license_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_image_categories(*, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CategoryDataList</code></summary>

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
try:
    response = client.images.list_image_categories()
    # TODO: Handle 'response' of type CategoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListImageCategoriesErrorBody
```

**Async**

```python
try:
    response = await async_client.images.list_image_categories()
    # TODO: Handle 'response' of type CategoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListImageCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CategoryDataList](shutterstock/models/category_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[ListImageCategoriesErrorBody](shutterstock/errors/list_image_categories_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_similar_images(id: str, *, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ImageSearchResults</code></summary>

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
try:
    response = client.images.list_similar_images(id)
    # TODO: Handle 'response' of type ImageSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSimilarImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.images.list_similar_images(id)
    # TODO: Handle 'response' of type ImageSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSimilarImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Image ID |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ImageSearchResults](shutterstock/models/image_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[ListSimilarImagesErrorBody](shutterstock/errors/list_similar_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def rename_image_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.images.rename_image_collection(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RenameImageCollectionErrorBody
```

**Async**

```python
try:
    await async_client.images.rename_image_collection(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RenameImageCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Collection ID |
| <code>body</code> | <code>[CollectionUpdateRequest](shutterstock/models/collection_update_request.py) \| [CollectionUpdateRequestDict](shutterstock/models/collection_update_request.py)</code> | The new name for the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RenameImageCollectionErrorBody](shutterstock/errors/rename_image_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_images(*, library: list[LibraryOrStr] | None = None, added_date: Date | None = None, added_date_start: Date | None = None, aspect_ratio_min: float | None = None, aspect_ratio_max: float | None = None, aspect_ratio: float | None = None, added_date_end: Date | None = None, category: str | None = None, color: str | None = None, contributor: list[str] | None = None, contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None, fields: str | None = None, height: int | None = None, height_from: int | None = None, height_to: int | None = None, image_type: list[ImageType2OrStr] | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[LicenseOrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_model_released: bool | None = None, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity2OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, query: str | None = None, region: RegionModel | RegionModelDict | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, spellcheck_query: bool | None = True, view: View2OrStr | None = None, width: int | None = None, width_from: int | None = None, width_to: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ImageSearchResults</code></summary>

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
try:
    response = client.images.search_images()
    # TODO: Handle 'response' of type ImageSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchImagesErrorBody
```

**Async**

```python
try:
    response = await async_client.images.search_images()
    # TODO: Handle 'response' of type ImageSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchImagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>library</code> | <code>list&#91;[LibraryOrStr](shutterstock/models/enums/library.py)&#93; \| None</code> | Search within different Shutterstock owned libraries<br>**Default**: <code>None</code> |
| <code>added_date</code> | <code>Date \| None</code> | Show images added on the specified date<br>**Default**: <code>None</code> |
| <code>added_date_start</code> | <code>Date \| None</code> | Show images added on or after the specified date<br>**Default**: <code>None</code> |
| <code>aspect_ratio_min</code> | <code>float \| None</code> | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>aspect_ratio_max</code> | <code>float \| None</code> | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>aspect_ratio</code> | <code>float \| None</code> | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image<br>**Default**: <code>None</code> |
| <code>added_date_end</code> | <code>Date \| None</code> | Show images added before the specified date<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Show images with the specified Shutterstock-defined category; specify a category name or ID<br>**Default**: <code>None</code> |
| <code>color</code> | <code>str \| None</code> | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors<br>**Default**: <code>None</code> |
| <code>contributor</code> | <code>list&#91;str&#93; \| None</code> | Show images with the specified contributor names or IDs, allows multiple<br>**Default**: <code>None</code> |
| <code>contributor_country</code> | <code>[ContributorCountryModel](shutterstock/models/unions/contributor_country_model.py) \| [ContributorCountryModelDict](shutterstock/models/unions/contributor_country_model.py) \| None</code> | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Fields to display in the response; see the documentation for the fields parameter in the overview section<br>**Default**: <code>None</code> |
| <code>height</code> | <code>int \| None</code> | (Deprecated; use height_from and height_to instead) Show images with the specified height<br>**Default**: <code>None</code> |
| <code>height_from</code> | <code>int \| None</code> | Show images with the specified height or larger, in pixels<br>**Default**: <code>None</code> |
| <code>height_to</code> | <code>int \| None</code> | Show images with the specified height or smaller, in pixels<br>**Default**: <code>None</code> |
| <code>image_type</code> | <code>list&#91;[ImageType2OrStr](shutterstock/models/enums/image_type2.py)&#93; \| None</code> | Show images of the specified type<br>**Default**: <code>None</code> |
| <code>keyword_safe_search</code> | <code>bool \| None</code> | Hide results with potentially unsafe keywords<br>**Default**: <code>True</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Set query and result language (uses Accept-Language header if not set)<br>**Default**: <code>None</code> |
| <code>license</code> | <code>list&#91;[LicenseOrStr](shutterstock/models/enums/license.py)&#93; \| None</code> | Show only images with the specified license<br>**Default**: <code>None</code> |
| <code>model</code> | <code>list&#91;str&#93; \| None</code> | Show image results with the specified model IDs<br>**Default**: <code>None</code> |
| <code>orientation</code> | <code>[Orientation2OrStr](shutterstock/models/enums/orientation2.py) \| None</code> | Show image results with horizontal or vertical orientation<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>people_model_released</code> | <code>bool \| None</code> | Show images of people with a signed model release<br>**Default**: <code>None</code> |
| <code>people_age</code> | <code>[PeopleAge2OrStr](shutterstock/models/enums/people_age2.py) \| None</code> | Show images that feature people of the specified age category<br>**Default**: <code>None</code> |
| <code>people_ethnicity</code> | <code>list&#91;[PeopleEthnicity2OrStr](shutterstock/models/enums/people_ethnicity2.py)&#93; \| None</code> | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities<br>**Default**: <code>None</code> |
| <code>people_gender</code> | <code>[PeopleGender2OrStr](shutterstock/models/enums/people_gender2.py) \| None</code> | Show images with people of the specified gender<br>**Default**: <code>None</code> |
| <code>people_number</code> | <code>int \| None</code> | Show images with the specified number of people<br>**Default**: <code>None</code> |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces; you can use NOT to filter out images that match a term<br>**Default**: <code>None</code> |
| <code>region</code> | <code>[RegionModel](shutterstock/models/unions/region_model.py) \| [RegionModelDict](shutterstock/models/unions/region_model.py) \| None</code> | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>sort</code> | <code>[Sort2OrStr](shutterstock/models/enums/sort2.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>spellcheck_query</code> | <code>bool \| None</code> | Spellcheck the search query and return results on suggested spellings<br>**Default**: <code>True</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>width</code> | <code>int \| None</code> | (Deprecated; use width_from and width_to instead) Show images with the specified width<br>**Default**: <code>None</code> |
| <code>width_from</code> | <code>int \| None</code> | Show images with the specified width or larger, in pixels<br>**Default**: <code>None</code> |
| <code>width_to</code> | <code>int \| None</code> | Show images with the specified width or smaller, in pixels<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ImageSearchResults](shutterstock/models/image_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[SearchImagesErrorBody](shutterstock/errors/search_images_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Oauth

> Source: [Oauth](shutterstock/apis/oauth.py)

<details>
<summary><code>def authorize(client_id: str, redirect_uri: str, response_type: ResponseTypeOrStr, state: str, *, realm: Realm2OrStr | None = None, scope: str | None = "user.view", request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.oauth.authorize(client_id, redirect_uri, response_type, state)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AuthorizeErrorBody
```

**Async**

```python
try:
    await async_client.oauth.authorize(client_id, redirect_uri, response_type, state)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AuthorizeErrorBody
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
| <code>response_type</code> | <code>[ResponseTypeOrStr](shutterstock/models/enums/response_type.py)</code> | Type of temporary authorization code that will be used to generate an access code; the only valid value is 'code' |
| <code>state</code> | <code>str</code> | Unique value used by the calling app to verify the request |
| <code>realm</code> | <code>[Realm2OrStr](shutterstock/models/enums/realm2.py) \| None</code> | User type to be authorized (usually 'customer')<br>**Default**: <code>None</code> |
| <code>scope</code> | <code>str \| None</code> | Space-separated list of scopes to be authorized<br>**Default**: <code>"user.view"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[AuthorizeErrorBody](shutterstock/errors/authorize_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_access_token(client_id: str, grant_type: GrantTypeOrStr, *, client_secret: str | None = None, code: str | None = None, realm: Realm3OrStr | None = None, expires: ExpiresOrStr | None = None, refresh_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> OauthAccessTokenResponse</code></summary>

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
try:
    response = client.oauth.create_access_token(client_id, grant_type)
    # TODO: Handle 'response' of type OauthAccessTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAccessTokenErrorBody
```

**Async**

```python
try:
    response = await async_client.oauth.create_access_token(client_id, grant_type)
    # TODO: Handle 'response' of type OauthAccessTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAccessTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | Client ID (Consumer Key) of your application |
| <code>grant_type</code> | <code>[GrantTypeOrStr](shutterstock/models/enums/grant_type.py)</code> | Grant type: authorization_code generates user tokens, client_credentials generates short-lived client grants |
| <code>client_secret</code> | <code>str \| None</code> | Client Secret (Consumer Secret) of your application<br>**Default**: <code>None</code> |
| <code>code</code> | <code>str \| None</code> | Response code from the /oauth/authorize flow; required if grant_type=authorization_code<br>**Default**: <code>None</code> |
| <code>realm</code> | <code>[Realm3OrStr](shutterstock/models/enums/realm3.py) \| None</code> | User type to be authorized (usually 'customer')<br>**Default**: <code>None</code> |
| <code>expires</code> | <code>[ExpiresOrStr](shutterstock/models/enums/expires.py) \| None</code> | Whether or not the token expires, expiring tokens come with a refresh_token to renew the access_token<br>**Default**: <code>None</code> |
| <code>refresh_token</code> | <code>str \| None</code> | Pass this along with grant_type=refresh_token to get a fresh access token<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OauthAccessTokenResponse](shutterstock/models/oauth_access_token_response.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[CreateAccessTokenErrorBody](shutterstock/errors/create_access_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoundEffects

> Source: [SoundEffects](shutterstock/apis/sound_effects.py)

<details>
<summary><code>def download_sfx(id: str, *, request_options: RequestOptionsOrDict | None = None) -> SfxUrl</code></summary>

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
try:
    response = client.sound_effects.download_sfx(id)
    # TODO: Handle 'response' of type SfxUrl
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadSfxErrorBody
```

**Async**

```python
try:
    response = await async_client.sound_effects.download_sfx(id)
    # TODO: Handle 'response' of type SfxUrl
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadSfxErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | License ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SfxUrl](shutterstock/models/sfx_url.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DownloadSfxErrorBody](shutterstock/errors/download_sfx_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_sfx_details(id: int, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, library: Library2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Sfx</code></summary>

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
try:
    response = client.sound_effects.get_sfx_details(id)
    # TODO: Handle 'response' of type Sfx
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSfxDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.sound_effects.get_sfx_details(id)
    # TODO: Handle 'response' of type Sfx
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSfxDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>int</code> | Audio track ID |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>library</code> | <code>[Library2OrStr](shutterstock/models/enums/library2.py) \| None</code> | Which library to fetch from<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Sfx](shutterstock/models/sfx.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetSfxDetailsErrorBody](shutterstock/errors/get_sfx_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 503 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_sfx_license_list(*, sfx_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, license_id: str | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> DownloadHistoryDataList</code></summary>

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
try:
    response = client.sound_effects.get_sfx_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSfxLicenseListErrorBody
```

**Async**

```python
try:
    response = await async_client.sound_effects.get_sfx_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSfxLicenseListErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>license_id</code> | <code>str \| None</code> | Filter by the license ID<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DownloadHistoryDataList](shutterstock/models/download_history_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetSfxLicenseListErrorBody](shutterstock/errors/get_sfx_license_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_sfx_list_details(id: list[str], *, view: View2OrStr | None = None, language: LanguageOrStr | None = None, library: Library2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> SfxdataList</code></summary>

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
try:
    response = client.sound_effects.get_sfx_list_details(id)
    # TODO: Handle 'response' of type SfxdataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSfxListDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.sound_effects.get_sfx_list_details(id)
    # TODO: Handle 'response' of type SfxdataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSfxListDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more sound effect IDs |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>library</code> | <code>[Library2OrStr](shutterstock/models/enums/library2.py) \| None</code> | Which library to fetch from<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SfxdataList](shutterstock/models/sfxdata_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetSfxListDetailsErrorBody](shutterstock/errors/get_sfx_list_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def licenses_sfx(body: LicenseSfxrequest | LicenseSfxrequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LicenseSfxresultDataList</code></summary>

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
try:
    response = client.sound_effects.licenses_sfx(body)
    # TODO: Handle 'response' of type LicenseSfxresultDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicensesSfxErrorBody
```

**Async**

```python
try:
    response = await async_client.sound_effects.licenses_sfx(body)
    # TODO: Handle 'response' of type LicenseSfxresultDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicensesSfxErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseSfxrequest](shutterstock/models/license_sfxrequest.py) \| [LicenseSfxrequestDict](shutterstock/models/license_sfxrequest.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LicenseSfxresultDataList](shutterstock/models/license_sfxresult_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[LicensesSfxErrorBody](shutterstock/errors/licenses_sfx_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_sfx(*, added_date: Date | None = None, added_date_start: Date | None = None, added_date_end: Date | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, safe: bool | None = True, sort: Sort15OrStr | None = None, view: View2OrStr | None = None, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> SfxsearchResults</code></summary>

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
try:
    response = client.sound_effects.search_sfx()
    # TODO: Handle 'response' of type SfxsearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchSfxErrorBody
```

**Async**

```python
try:
    response = await async_client.sound_effects.search_sfx()
    # TODO: Handle 'response' of type SfxsearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchSfxErrorBody
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
| <code>sort</code> | <code>[Sort15OrStr](shutterstock/models/enums/sort15.py) \| None</code> | Sort by<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Set query and result language (uses Accept-Language header if not set)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SfxsearchResults](shutterstock/models/sfxsearch_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[SearchSfxErrorBody](shutterstock/errors/search_sfx_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 503 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Test

> Source: [Test](shutterstock/apis/test.py)

<details>
<summary><code>def echo(*, text: str | None = "ok", request_options: RequestOptionsOrDict | None = None) -> TestEcho</code></summary>

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
try:
    response = client.test.echo()
    # TODO: Handle 'response' of type TestEcho
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EchoErrorBody
```

**Async**

```python
try:
    response = await async_client.test.echo()
    # TODO: Handle 'response' of type TestEcho
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EchoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>text</code> | <code>str \| None</code> | Text to echo<br>**Default**: <code>"ok"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TestEcho](shutterstock/models/test_echo.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[EchoErrorBody](shutterstock/errors/echo_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def validate(id: int, *, tag: list[str] | None = None, user_agent: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TestValidate</code></summary>

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
try:
    response = client.test.validate(id)
    # TODO: Handle 'response' of type TestValidate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ValidateErrorBody
```

**Async**

```python
try:
    response = await async_client.test.validate(id)
    # TODO: Handle 'response' of type TestValidate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ValidateErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TestValidate](shutterstock/models/test_validate.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[ValidateErrorBody](shutterstock/errors/validate_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Users

> Source: [Users](shutterstock/apis/users.py)

<details>
<summary><code>def get_access_token(*, request_options: RequestOptionsOrDict | None = None) -> AccessTokenDetails</code></summary>

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
try:
    response = client.users.get_access_token()
    # TODO: Handle 'response' of type AccessTokenDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccessTokenErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_access_token()
    # TODO: Handle 'response' of type AccessTokenDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccessTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AccessTokenDetails](shutterstock/models/access_token_details.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetAccessTokenErrorBody](shutterstock/errors/get_access_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user(*, request_options: RequestOptionsOrDict | None = None) -> UserDetails</code></summary>

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
try:
    response = client.users.get_user()
    # TODO: Handle 'response' of type UserDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUserErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_user()
    # TODO: Handle 'response' of type UserDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UserDetails](shutterstock/models/user_details.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetUserErrorBody](shutterstock/errors/get_user_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_subscription_list(*, request_options: RequestOptionsOrDict | None = None) -> SubscriptionDataList</code></summary>

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
try:
    response = client.users.get_user_subscription_list()
    # TODO: Handle 'response' of type SubscriptionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUserSubscriptionListErrorBody
```

**Async**

```python
try:
    response = await async_client.users.get_user_subscription_list()
    # TODO: Handle 'response' of type SubscriptionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetUserSubscriptionListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionDataList](shutterstock/models/subscription_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetUserSubscriptionListErrorBody](shutterstock/errors/get_user_subscription_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Videos

> Source: [Videos](shutterstock/apis/videos.py)

<details>
<summary><code>def add_video_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.videos.add_video_collection_items(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddVideoCollectionItemsErrorBody
```

**Async**

```python
try:
    await async_client.videos.add_video_collection_items(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddVideoCollectionItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the collection to which items should be added |
| <code>body</code> | <code>[CollectionItemRequest](shutterstock/models/collection_item_request.py) \| [CollectionItemRequestDict](shutterstock/models/collection_item_request.py)</code> | Array of video IDs to add to the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[AddVideoCollectionItemsErrorBody](shutterstock/errors/add_video_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_video_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CollectionCreateResponse</code></summary>

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
try:
    response = client.videos.create_video_collection(body)
    # TODO: Handle 'response' of type CollectionCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateVideoCollectionErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.create_video_collection(body)
    # TODO: Handle 'response' of type CollectionCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateVideoCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CollectionCreateRequest](shutterstock/models/collection_create_request.py) \| [CollectionCreateRequestDict](shutterstock/models/collection_create_request.py)</code> | Collection metadata |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionCreateResponse](shutterstock/models/collection_create_response.py)</code> -- Successfully created video collection

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[CreateVideoCollectionErrorBody](shutterstock/errors/create_video_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_video_collection(id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.videos.delete_video_collection(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteVideoCollectionErrorBody
```

**Async**

```python
try:
    await async_client.videos.delete_video_collection(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteVideoCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the collection to delete |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DeleteVideoCollectionErrorBody](shutterstock/errors/delete_video_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_video_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.videos.delete_video_collection_items(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteVideoCollectionItemsErrorBody
```

**Async**

```python
try:
    await async_client.videos.delete_video_collection_items(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteVideoCollectionItemsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DeleteVideoCollectionItemsErrorBody](shutterstock/errors/delete_video_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_videos(id: str, body: RedownloadVideo | RedownloadVideoDict, *, request_options: RequestOptionsOrDict | None = None) -> Url</code></summary>

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
try:
    response = client.videos.download_videos(id, body)
    # TODO: Handle 'response' of type Url
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadVideosErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.download_videos(id, body)
    # TODO: Handle 'response' of type Url
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The license ID of the item to (re)download. The download links in the response are valid for 8 hours. |
| <code>body</code> | <code>[RedownloadVideo](shutterstock/models/redownload_video.py) \| [RedownloadVideoDict](shutterstock/models/redownload_video.py)</code> | Information about the videos to redownload |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Url](shutterstock/models/url.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[DownloadVideosErrorBody](shutterstock/errors/download_videos_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_similar_videos(id: str, *, language: LanguageOrStr | None = None, page: int | None = 1, per_page: int | None = 20, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> VideoSearchResults</code></summary>

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
try:
    response = client.videos.find_similar_videos(id)
    # TODO: Handle 'response' of type VideoSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FindSimilarVideosErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.find_similar_videos(id)
    # TODO: Handle 'response' of type VideoSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FindSimilarVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of a video for which similar videos should be returned |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[VideoSearchResults](shutterstock/models/video_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[FindSimilarVideosErrorBody](shutterstock/errors/find_similar_videos_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_updated_videos(*, start_date: str | None = None, end_date: str | None = None, interval: str | None = "1 HOUR", page: int | None = 1, per_page: int | None = 100, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> UpdatedMediaDataList</code></summary>

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
try:
    response = client.videos.get_updated_videos()
    # TODO: Handle 'response' of type UpdatedMediaDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.videos.get_updated_videos()
    # TODO: Handle 'response' of type UpdatedMediaDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort by oldest or newest videos first<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UpdatedMediaDataList](shutterstock/models/updated_media_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RawError](shutterstock/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video(id: str, *, language: LanguageOrStr | None = None, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Video</code></summary>

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
try:
    response = client.videos.get_video(id)
    # TODO: Handle 'response' of type Video
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.get_video(id)
    # TODO: Handle 'response' of type Video
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Video ID |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Video](shutterstock/models/video.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetVideoErrorBody](shutterstock/errors/get_video_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Collection</code></summary>

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
try:
    response = client.videos.get_video_collection(id)
    # TODO: Handle 'response' of type Collection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoCollectionErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.get_video_collection(id)
    # TODO: Handle 'response' of type Collection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the collection to return |
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>share_code</code> | <code>str \| None</code> | Code to retrieve a shared collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Collection](shutterstock/models/collection.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetVideoCollectionErrorBody](shutterstock/errors/get_video_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CollectionItemDataList</code></summary>

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
try:
    response = client.videos.get_video_collection_items(id)
    # TODO: Handle 'response' of type CollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoCollectionItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.get_video_collection_items(id)
    # TODO: Handle 'response' of type CollectionItemDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoCollectionItemsErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort order<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionItemDataList](shutterstock/models/collection_item_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetVideoCollectionItemsErrorBody](shutterstock/errors/get_video_collection_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_collection_list(*, page: int | None = 1, per_page: int | None = 100, embed: list[EmbedOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> CollectionDataList</code></summary>

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
try:
    response = client.videos.get_video_collection_list()
    # TODO: Handle 'response' of type CollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoCollectionListErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.get_video_collection_list()
    # TODO: Handle 'response' of type CollectionDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoCollectionListErrorBody
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
| <code>embed</code> | <code>list&#91;[EmbedOrStr](shutterstock/models/enums/embed.py)&#93; \| None</code> | Which sharing information to include in the response, such as a URL to the collection<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CollectionDataList](shutterstock/models/collection_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetVideoCollectionListErrorBody](shutterstock/errors/get_video_collection_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_license_list(*, video_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> DownloadHistoryDataList</code></summary>

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
try:
    response = client.videos.get_video_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoLicenseListErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.get_video_license_list()
    # TODO: Handle 'response' of type DownloadHistoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoLicenseListErrorBody
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
| <code>sort</code> | <code>[Sort5OrStr](shutterstock/models/enums/sort5.py) \| None</code> | Sort by oldest or newest videos first<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Filter licenses by username of licensee<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created on or after the specified date<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>RFC3339DateTime \| None</code> | Show licenses created before the specified date<br>**Default**: <code>None</code> |
| <code>download_availability</code> | <code>[DownloadAvailabilityOrStr](shutterstock/models/enums/download_availability.py) \| None</code> | Filter licenses by download availability<br>**Default**: <code>None</code> |
| <code>team_history</code> | <code>bool \| None</code> | Set to true to see license history for all members of your team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DownloadHistoryDataList](shutterstock/models/download_history_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetVideoLicenseListErrorBody](shutterstock/errors/get_video_license_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> VideoDataList</code></summary>

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
try:
    response = client.videos.get_video_list(id)
    # TODO: Handle 'response' of type VideoDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoListErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.get_video_list(id)
    # TODO: Handle 'response' of type VideoDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>list&#91;str&#93;</code> | One or more video IDs |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The ID of the search that is related to this request<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[VideoDataList](shutterstock/models/video_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetVideoListErrorBody](shutterstock/errors/get_video_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_video_suggestions(query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None) -> Suggestions</code></summary>

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
try:
    response = client.videos.get_video_suggestions(query)
    # TODO: Handle 'response' of type Suggestions
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoSuggestionsErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.get_video_suggestions(query)
    # TODO: Handle 'response' of type Suggestions
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVideoSuggestionsErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Suggestions](shutterstock/models/suggestions.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[GetVideoSuggestionsErrorBody](shutterstock/errors/get_video_suggestions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def license_videos(body: LicenseVideoRequest | LicenseVideoRequestDict, *, subscription_id: str | None = None, size: Size16OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> LicenseVideoResultDataList</code></summary>

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
try:
    response = client.videos.license_videos(body)
    # TODO: Handle 'response' of type LicenseVideoResultDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseVideosErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.license_videos(body)
    # TODO: Handle 'response' of type LicenseVideoResultDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LicenseVideosErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LicenseVideoRequest](shutterstock/models/license_video_request.py) \| [LicenseVideoRequestDict](shutterstock/models/license_video_request.py)</code> | List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters |
| <code>subscription_id</code> | <code>str \| None</code> | The subscription ID to use for licensing<br>**Default**: <code>None</code> |
| <code>size</code> | <code>[Size16OrStr](shutterstock/models/enums/size16.py) \| None</code> | The size of the video to license<br>**Default**: <code>None</code> |
| <code>search_id</code> | <code>str \| None</code> | The Search ID that led to this licensing event<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LicenseVideoResultDataList](shutterstock/models/license_video_result_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[LicenseVideosErrorBody](shutterstock/errors/license_videos_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_video_categories(*, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CategoryDataList</code></summary>

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
try:
    response = client.videos.list_video_categories()
    # TODO: Handle 'response' of type CategoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListVideoCategoriesErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.list_video_categories()
    # TODO: Handle 'response' of type CategoryDataList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListVideoCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Language for the keywords and categories in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CategoryDataList](shutterstock/models/category_data_list.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[ListVideoCategoriesErrorBody](shutterstock/errors/list_video_categories_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def rename_video_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.videos.rename_video_collection(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RenameVideoCollectionErrorBody
```

**Async**

```python
try:
    await async_client.videos.rename_video_collection(id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RenameVideoCollectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the collection to rename |
| <code>body</code> | <code>[CollectionUpdateRequest](shutterstock/models/collection_update_request.py) \| [CollectionUpdateRequestDict](shutterstock/models/collection_update_request.py)</code> | The new name for the collection |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[RenameVideoCollectionErrorBody](shutterstock/errors/rename_video_collection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_videos(*, added_date: Date | None = None, added_date_start: Date | None = None, added_date_end: Date | None = None, aspect_ratio: AspectRatioOrStr | None = None, category: str | None = None, contributor: list[str] | None = None, contributor_country: list[str] | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, fps: float | None = None, fps_from: float | None = None, fps_to: float | None = None, keyword_safe_search: bool | None = True, language: LanguageOrStr | None = None, license: list[License9OrStr] | None = None, model: list[str] | None = None, orientation: Orientation2OrStr | None = None, page: int | None = 1, per_page: int | None = 20, people_age: PeopleAge2OrStr | None = None, people_ethnicity: list[PeopleEthnicity5OrStr] | None = None, people_gender: PeopleGender2OrStr | None = None, people_number: int | None = None, people_model_released: bool | None = None, query: str | None = None, resolution: ResolutionOrStr | None = None, safe: bool | None = True, sort: Sort2OrStr | None = None, view: View2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> VideoSearchResults</code></summary>

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
try:
    response = client.videos.search_videos()
    # TODO: Handle 'response' of type VideoSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchVideosErrorBody
```

**Async**

```python
try:
    response = await async_client.videos.search_videos()
    # TODO: Handle 'response' of type VideoSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchVideosErrorBody
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
| <code>aspect_ratio</code> | <code>[AspectRatioOrStr](shutterstock/models/enums/aspect_ratio.py) \| None</code> | Show videos with the specified aspect ratio<br>**Default**: <code>None</code> |
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
| <code>language</code> | <code>[LanguageOrStr](shutterstock/models/enums/language.py) \| None</code> | Set query and result language (uses Accept-Language header if not set)<br>**Default**: <code>None</code> |
| <code>license</code> | <code>list&#91;[License9OrStr](shutterstock/models/enums/license9.py)&#93; \| None</code> | Show only videos with the specified license or licenses<br>**Default**: <code>None</code> |
| <code>model</code> | <code>list&#91;str&#93; \| None</code> | Show videos with each of the specified models<br>**Default**: <code>None</code> |
| <code>orientation</code> | <code>[Orientation2OrStr](shutterstock/models/enums/orientation2.py) \| None</code> | Search for videos in a specific orientation<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | Number of results per page<br>**Default**: <code>20</code> |
| <code>people_age</code> | <code>[PeopleAge2OrStr](shutterstock/models/enums/people_age2.py) \| None</code> | Show videos that feature people of the specified age range<br>**Default**: <code>None</code> |
| <code>people_ethnicity</code> | <code>list&#91;[PeopleEthnicity5OrStr](shutterstock/models/enums/people_ethnicity5.py)&#93; \| None</code> | Show videos with people of the specified ethnicities<br>**Default**: <code>None</code> |
| <code>people_gender</code> | <code>[PeopleGender2OrStr](shutterstock/models/enums/people_gender2.py) \| None</code> | Show videos with people with the specified gender<br>**Default**: <code>None</code> |
| <code>people_number</code> | <code>int \| None</code> | Show videos with the specified number of people<br>**Default**: <code>None</code> |
| <code>people_model_released</code> | <code>bool \| None</code> | Show only videos of people with a signed model release<br>**Default**: <code>None</code> |
| <code>query</code> | <code>str \| None</code> | One or more search terms separated by spaces; you can use NOT to filter out videos that match a term<br>**Default**: <code>None</code> |
| <code>resolution</code> | <code>[ResolutionOrStr](shutterstock/models/enums/resolution.py) \| None</code> | Show videos with the specified resolution<br>**Default**: <code>None</code> |
| <code>safe</code> | <code>bool \| None</code> | Enable or disable safe search<br>**Default**: <code>True</code> |
| <code>sort</code> | <code>[Sort2OrStr](shutterstock/models/enums/sort2.py) \| None</code> | Sort by one of these categories<br>**Default**: <code>None</code> |
| <code>view</code> | <code>[View2OrStr](shutterstock/models/enums/view2.py) \| None</code> | Amount of detail to render in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](shutterstock/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[VideoSearchResults](shutterstock/models/video_search_results.py)</code> -- OK

**OnError**: <code>[ApiError](shutterstock/core/exceptions.py)&#91;[SearchVideosErrorBody](shutterstock/errors/search_videos_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404 | <code>[RawError](shutterstock/core/results.py)</code> |
| anything unmapped | <code>[RawError](shutterstock/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

