<!-- Generated file — do not edit; regenerated with the SDK. -->

# Contributors — operations

Accessor: `client.contributors` · Source: `shutterstock/apis/contributors.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.contributors.get_contributor

- **Route**: `GET /v2/contributors/{contributor_id}`
- **Server**: `default`
- **Signature**: `def get_contributor(contributor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `contributor_id`
- **Params**: `contributor_id` — path
- **Returns (parsed)**: `ContributorProfile`
- **Returns (raw)**: `ApiResult[ContributorProfile, GetContributorErrorBody]`
- **Error**: `GetContributorErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `ContributorProfile` | `shutterstock/models/contributor_profile.py` |
| `GetContributorErrorBody` | `shutterstock/errors/get_contributor_error.py` |

### client.contributors.get_contributor_collection_items

- **Route**: `GET /v2/contributors/{contributor_id}/collections/{id}/items`
- **Server**: `default`
- **Signature**: `def get_contributor_collection_items(contributor_id: str, id: str, *, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `contributor_id`, `id`
- **Params**: `contributor_id` — path · `id` — path · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `CollectionItemDataList`
- **Returns (raw)**: `ApiResult[CollectionItemDataList, GetContributorCollectionItemsErrorBody]`
- **Error**: `GetContributorCollectionItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock/models/enums/sort5.py` |
| `CollectionItemDataList` | `shutterstock/models/collection_item_data_list.py` |
| `GetContributorCollectionItemsErrorBody` | `shutterstock/errors/get_contributor_collection_items_error.py` |

### client.contributors.get_contributor_collections

- **Route**: `GET /v2/contributors/{contributor_id}/collections/{id}`
- **Server**: `default`
- **Signature**: `def get_contributor_collections(contributor_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `contributor_id`, `id`
- **Params**: `contributor_id` — path · `id` — path
- **Returns (parsed)**: `Collection`
- **Returns (raw)**: `ApiResult[Collection, GetContributorCollectionsErrorBody]`
- **Error**: `GetContributorCollectionsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `Collection` | `shutterstock/models/collection.py` |
| `GetContributorCollectionsErrorBody` | `shutterstock/errors/get_contributor_collections_error.py` |

### client.contributors.get_contributor_collections_list

- **Route**: `GET /v2/contributors/{contributor_id}/collections`
- **Server**: `default`
- **Signature**: `def get_contributor_collections_list(contributor_id: str, *, sort: Sort24OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `contributor_id`
- **Params**: `contributor_id` — path · `sort` — query
- **Returns (parsed)**: `CollectionDataList`
- **Returns (raw)**: `ApiResult[CollectionDataList, GetContributorCollectionsListErrorBody]`
- **Error**: `GetContributorCollectionsListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort24OrStr` | `shutterstock/models/enums/sort24.py` |
| `CollectionDataList` | `shutterstock/models/collection_data_list.py` |
| `GetContributorCollectionsListErrorBody` | `shutterstock/errors/get_contributor_collections_list_error.py` |

### client.contributors.get_contributor_list

- **Route**: `GET /v2/contributors`
- **Server**: `default`
- **Signature**: `def get_contributor_list(id: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query
- **Returns (parsed)**: `ContributorProfileDataList`
- **Returns (raw)**: `ApiResult[ContributorProfileDataList, GetContributorListErrorBody]`
- **Error**: `GetContributorListErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `ContributorProfileDataList` | `shutterstock/models/contributor_profile_data_list.py` |
| `GetContributorListErrorBody` | `shutterstock/errors/get_contributor_list_error.py` |

