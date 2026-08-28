<!-- Generated file — do not edit; regenerated with the SDK. -->

# AudioApi — operations

Accessor: `client.audio_api` · Source: `shutterstock/apis/audio_api.py` · 17 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.audio_api.add_track_collection_items

- **Route**: `POST /v2/audio/collections/{id}/items`
- **Server**: `default`
- **Signature**: `def add_track_collection_items(id: str, body: CollectionItemRequest | CollectionItemRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddTrackCollectionItemsErrorBody]`
- **Error**: `AddTrackCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionItemRequest` | `shutterstock/models/collection_item_request.py` |
| `CollectionItemRequestDict` | `shutterstock/models/collection_item_request.py` |
| `AddTrackCollectionItemsErrorBody` | `shutterstock/errors/add_track_collection_items_error.py` |

### client.audio_api.create_track_collection

- **Route**: `POST /v2/audio/collections`
- **Server**: `default`
- **Signature**: `def create_track_collection(body: CollectionCreateRequest | CollectionCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CollectionCreateResponse`
- **Returns (raw)**: `ApiResult[CollectionCreateResponse, CreateTrackCollectionErrorBody]`
- **Error**: `CreateTrackCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionCreateRequest` | `shutterstock/models/collection_create_request.py` |
| `CollectionCreateRequestDict` | `shutterstock/models/collection_create_request.py` |
| `CollectionCreateResponse` | `shutterstock/models/collection_create_response.py` |
| `CreateTrackCollectionErrorBody` | `shutterstock/errors/create_track_collection_error.py` |

### client.audio_api.delete_track_collection

- **Route**: `DELETE /v2/audio/collections/{id}`
- **Server**: `default`
- **Signature**: `def delete_track_collection(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteTrackCollectionErrorBody]`
- **Error**: `DeleteTrackCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteTrackCollectionErrorBody` | `shutterstock/errors/delete_track_collection_error.py` |

### client.audio_api.delete_track_collection_items

- **Route**: `DELETE /v2/audio/collections/{id}/items`
- **Server**: `default`
- **Signature**: `def delete_track_collection_items(id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `item_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteTrackCollectionItemsErrorBody]`
- **Error**: `DeleteTrackCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteTrackCollectionItemsErrorBody` | `shutterstock/errors/delete_track_collection_items_error.py` |

### client.audio_api.download_tracks

- **Route**: `POST /v2/audio/licenses/{id}/downloads`
- **Server**: `default`
- **Signature**: `def download_tracks(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `AudioUrl`
- **Returns (raw)**: `ApiResult[AudioUrl, DownloadTracksErrorBody]`
- **Error**: `DownloadTracksErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `AudioUrl` | `shutterstock/models/audio_url.py` |
| `DownloadTracksErrorBody` | `shutterstock/errors/download_tracks_error.py` |

### client.audio_api.get_track

- **Route**: `GET /v2/audio/{id}`
- **Server**: `default`
- **Signature**: `def get_track(id: int, *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `view` — query · `search_id` — query
- **Returns (parsed)**: `Audio`
- **Returns (raw)**: `ApiResult[Audio, GetTrackErrorBody]`
- **Error**: `GetTrackErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `View2OrStr` | `shutterstock/models/enums/view2.py` |
| `Audio` | `shutterstock/models/audio.py` |
| `GetTrackErrorBody` | `shutterstock/errors/get_track_error.py` |

### client.audio_api.get_track_collection

- **Route**: `GET /v2/audio/collections/{id}`
- **Server**: `default`
- **Signature**: `def get_track_collection(id: str, *, embed: list[EmbedOrStr] | None = None, share_code: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `embed` — query · `share_code` — query
- **Returns (parsed)**: `Collection`
- **Returns (raw)**: `ApiResult[Collection, GetTrackCollectionErrorBody]`
- **Error**: `GetTrackCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `EmbedOrStr` | `shutterstock/models/enums/embed.py` |
| `Collection` | `shutterstock/models/collection.py` |
| `GetTrackCollectionErrorBody` | `shutterstock/errors/get_track_collection_error.py` |

### client.audio_api.get_track_collection_items

- **Route**: `GET /v2/audio/collections/{id}/items`
- **Server**: `default`
- **Signature**: `def get_track_collection_items(id: str, *, page: int | None = 1, per_page: int | None = 100, share_code: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `page` — query · `per_page` — query · `share_code` — query · `sort` — query
- **Returns (parsed)**: `CollectionItemDataList`
- **Returns (raw)**: `ApiResult[CollectionItemDataList, GetTrackCollectionItemsErrorBody]`
- **Error**: `GetTrackCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock/models/enums/sort5.py` |
| `CollectionItemDataList` | `shutterstock/models/collection_item_data_list.py` |
| `GetTrackCollectionItemsErrorBody` | `shutterstock/errors/get_track_collection_items_error.py` |

### client.audio_api.get_track_collection_list

- **Route**: `GET /v2/audio/collections`
- **Server**: `default`
- **Signature**: `def get_track_collection_list(*, page: int | None = 1, per_page: int | None = 100, embed: list[EmbedOrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query · `embed` — query
- **Returns (parsed)**: `CollectionDataList`
- **Returns (raw)**: `ApiResult[CollectionDataList, GetTrackCollectionListErrorBody]`
- **Error**: `GetTrackCollectionListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `EmbedOrStr` | `shutterstock/models/enums/embed.py` |
| `CollectionDataList` | `shutterstock/models/collection_data_list.py` |
| `GetTrackCollectionListErrorBody` | `shutterstock/errors/get_track_collection_list_error.py` |

### client.audio_api.get_track_license_list

- **Route**: `GET /v2/audio/licenses`
- **Server**: `default`
- **Signature**: `def get_track_license_list(*, audio_id: str | None = None, license: str | None = None, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, username: str | None = None, start_date: RFC3339DateTime | None = None, end_date: RFC3339DateTime | None = None, download_availability: DownloadAvailabilityOrStr | None = None, team_history: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `audio_id` — query · `license` — query · `page` — query · `per_page` — query · `sort` — query · `username` — query · `start_date` — query · `end_date` — query · `download_availability` — query · `team_history` — query
- **Returns (parsed)**: `DownloadHistoryDataList`
- **Returns (raw)**: `ApiResult[DownloadHistoryDataList, GetTrackLicenseListErrorBody]`
- **Error**: `GetTrackLicenseListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock/models/enums/sort5.py` |
| `DownloadAvailabilityOrStr` | `shutterstock/models/enums/download_availability.py` |
| `DownloadHistoryDataList` | `shutterstock/models/download_history_data_list.py` |
| `GetTrackLicenseListErrorBody` | `shutterstock/errors/get_track_license_list_error.py` |

### client.audio_api.get_track_list

- **Route**: `GET /v2/audio`
- **Server**: `default`
- **Signature**: `def get_track_list(id: list[str], *, view: View2OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query · `view` — query · `search_id` — query
- **Returns (parsed)**: `AudioDataList`
- **Returns (raw)**: `ApiResult[AudioDataList, GetTrackListErrorBody]`
- **Error**: `GetTrackListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `View2OrStr` | `shutterstock/models/enums/view2.py` |
| `AudioDataList` | `shutterstock/models/audio_data_list.py` |
| `GetTrackListErrorBody` | `shutterstock/errors/get_track_list_error.py` |

### client.audio_api.license_track

- **Route**: `POST /v2/audio/licenses`
- **Server**: `default`
- **Signature**: `def license_track(body: LicenseAudioRequest | LicenseAudioRequestDict, *, license: License10OrStr | None = None, search_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `license` — query · `search_id` — query · `body` — JSON body
- **Returns (parsed)**: `LicenseAudioResultDataList`
- **Returns (raw)**: `ApiResult[LicenseAudioResultDataList, LicenseTrackErrorBody]`
- **Error**: `LicenseTrackErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `LicenseAudioRequest` | `shutterstock/models/license_audio_request.py` |
| `LicenseAudioRequestDict` | `shutterstock/models/license_audio_request.py` |
| `License10OrStr` | `shutterstock/models/enums/license10.py` |
| `LicenseAudioResultDataList` | `shutterstock/models/license_audio_result_data_list.py` |
| `LicenseTrackErrorBody` | `shutterstock/errors/license_track_error.py` |

### client.audio_api.list_genres

- **Route**: `GET /v2/audio/genres`
- **Server**: `default`
- **Signature**: `def list_genres(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `language` — query
- **Returns (parsed)**: `GenreList`
- **Returns (raw)**: `ApiResult[GenreList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenreList` | `shutterstock/models/genre_list.py` |

### client.audio_api.list_instruments

- **Route**: `GET /v2/audio/instruments`
- **Server**: `default`
- **Signature**: `def list_instruments(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `language` — query
- **Returns (parsed)**: `InstrumentList`
- **Returns (raw)**: `ApiResult[InstrumentList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstrumentList` | `shutterstock/models/instrument_list.py` |

### client.audio_api.list_moods

- **Route**: `GET /v2/audio/moods`
- **Server**: `default`
- **Signature**: `def list_moods(*, language: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `language` — query
- **Returns (parsed)**: `MoodList`
- **Returns (raw)**: `ApiResult[MoodList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MoodList` | `shutterstock/models/mood_list.py` |

### client.audio_api.rename_track_collection

- **Route**: `POST /v2/audio/collections/{id}`
- **Server**: `default`
- **Signature**: `def rename_track_collection(id: str, body: CollectionUpdateRequest | CollectionUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RenameTrackCollectionErrorBody]`
- **Error**: `RenameTrackCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `CollectionUpdateRequest` | `shutterstock/models/collection_update_request.py` |
| `CollectionUpdateRequestDict` | `shutterstock/models/collection_update_request.py` |
| `RenameTrackCollectionErrorBody` | `shutterstock/errors/rename_track_collection_error.py` |

### client.audio_api.search_tracks

- **Route**: `GET /v2/audio/search`
- **Server**: `default`
- **Signature**: `def search_tracks(*, artists: list[str] | None = None, bpm: int | None = None, bpm_from: int | None = None, bpm_to: int | None = None, duration: int | None = None, duration_from: int | None = None, duration_to: int | None = None, genre: list[str] | None = None, is_instrumental: bool | None = None, instruments: list[str] | None = None, moods: list[str] | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, sort: Sort12OrStr | None = None, sort_order: SortOrderOrStr | None = None, vocal_description: str | None = None, view: View2OrStr | None = None, fields: str | None = None, library: Library1OrStr | None = None, language: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `artists` — query · `bpm` — query · `bpm_from` — query · `bpm_to` — query · `duration` — query · `duration_from` — query · `duration_to` — query · `genre` — query · `is_instrumental` — query · `instruments` — query · `moods` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query · `sort_order` — query · `vocal_description` — query · `view` — query · `fields` — query · `library` — query · `language` — query
- **Returns (parsed)**: `AudioSearchResults`
- **Returns (raw)**: `ApiResult[AudioSearchResults, SearchTracksErrorBody]`
- **Error**: `SearchTracksErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort12OrStr` | `shutterstock/models/enums/sort12.py` |
| `SortOrderOrStr` | `shutterstock/models/enums/sort_order.py` |
| `View2OrStr` | `shutterstock/models/enums/view2.py` |
| `Library1OrStr` | `shutterstock/models/enums/library1.py` |
| `AudioSearchResults` | `shutterstock/models/audio_search_results.py` |
| `SearchTracksErrorBody` | `shutterstock/errors/search_tracks_error.py` |

