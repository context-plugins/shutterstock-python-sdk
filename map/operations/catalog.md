<!-- Generated file — do not edit; regenerated with the SDK. -->

# Catalog — operations

Accessor: `client.catalog` · Source: `shutterstock_api_explorer/apis/catalog.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.catalog.add_to_collection

- **Route**: `POST /v2/catalog/collections/{collection_id}/items`
- **Server**: `default`
- **Signature**: `def add_to_collection(collection_id: str, body: CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `collection_id`, `body`
- **Params**: `collection_id` — path · `body` — JSON body
- **Returns (parsed)**: `CatalogCollection`
- **Returns (raw)**: `ApiResult[CatalogCollection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCatalogCollectionItems` | `shutterstock_api_explorer/models/create_catalog_collection_items.py` |
| `CreateCatalogCollectionItemsDict` | `shutterstock_api_explorer/models/create_catalog_collection_items.py` |
| `CatalogCollection` | `shutterstock_api_explorer/models/catalog_collection.py` |

### client.catalog.create_collection

- **Route**: `POST /v2/catalog/collections`
- **Server**: `default`
- **Signature**: `def create_collection(body: CreateCatalogCollection | CreateCatalogCollectionDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CatalogCollection`
- **Returns (raw)**: `ApiResult[CatalogCollection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCatalogCollection` | `shutterstock_api_explorer/models/create_catalog_collection.py` |
| `CreateCatalogCollectionDict` | `shutterstock_api_explorer/models/create_catalog_collection.py` |
| `CatalogCollection` | `shutterstock_api_explorer/models/catalog_collection.py` |

### client.catalog.delete_collection

- **Route**: `DELETE /v2/catalog/collections/{collection_id}`
- **Server**: `default`
- **Signature**: `def delete_collection(collection_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `collection_id`
- **Params**: `collection_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteCollectionErrorBody]`
- **Error**: `DeleteCollectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteCollectionErrorBody` | `shutterstock_api_explorer/errors/delete_collection_error.py` |

### client.catalog.delete_from_collection

- **Route**: `DELETE /v2/catalog/collections/{collection_id}/items`
- **Server**: `default`
- **Signature**: `def delete_from_collection(collection_id: str, body: RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `collection_id`, `body`
- **Params**: `collection_id` — path · `body` — JSON body
- **Returns (parsed)**: `CatalogCollection`
- **Returns (raw)**: `ApiResult[CatalogCollection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RemoveCatalogCollectionItems` | `shutterstock_api_explorer/models/remove_catalog_collection_items.py` |
| `RemoveCatalogCollectionItemsDict` | `shutterstock_api_explorer/models/remove_catalog_collection_items.py` |
| `CatalogCollection` | `shutterstock_api_explorer/models/catalog_collection.py` |

### client.catalog.get_collections

- **Route**: `GET /v2/catalog/collections`
- **Server**: `default`
- **Signature**: `def get_collections(*, page: int | None = 1, per_page: int | None = 20, sort: Sort5OrStr | None = None, shared: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query · `sort` — query · `shared` — query
- **Returns (parsed)**: `CatalogCollectionDataList`
- **Returns (raw)**: `ApiResult[CatalogCollectionDataList, GetCollectionsErrorBody]`
- **Error**: `GetCollectionsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `CatalogCollectionDataList` | `shutterstock_api_explorer/models/catalog_collection_data_list.py` |
| `GetCollectionsErrorBody` | `shutterstock_api_explorer/errors/get_collections_error.py` |

### client.catalog.search_catalog

- **Route**: `GET /v2/catalog/search`
- **Server**: `default`
- **Signature**: `def search_catalog(*, sort: Sort5OrStr | None = None, page: int | None = 1, per_page: int | None = 20, query: str | None = None, collection_id: list[str] | None = None, asset_type: list[AssetTypeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `sort` — query · `page` — query · `per_page` — query · `query` — query · `collection_id` — query · `asset_type` — query
- **Returns (parsed)**: `CatalogCollectionItemDataList`
- **Returns (raw)**: `ApiResult[CatalogCollectionItemDataList, SearchCatalogErrorBody]`
- **Error**: `SearchCatalogErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `Sort5OrStr` | `shutterstock_api_explorer/models/enums/sort5.py` |
| `AssetTypeOrStr` | `shutterstock_api_explorer/models/enums/asset_type.py` |
| `CatalogCollectionItemDataList` | `shutterstock_api_explorer/models/catalog_collection_item_data_list.py` |
| `SearchCatalogErrorBody` | `shutterstock_api_explorer/errors/search_catalog_error.py` |

### client.catalog.update_collection

- **Route**: `PATCH /v2/catalog/collections/{collection_id}`
- **Server**: `default`
- **Signature**: `def update_collection(collection_id: str, body: UpdateCatalogCollection | UpdateCatalogCollectionDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `collection_id`, `body`
- **Params**: `collection_id` — path · `body` — JSON body
- **Returns (parsed)**: `CatalogCollection`
- **Returns (raw)**: `ApiResult[CatalogCollection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateCatalogCollection` | `shutterstock_api_explorer/models/update_catalog_collection.py` |
| `UpdateCatalogCollectionDict` | `shutterstock_api_explorer/models/update_catalog_collection.py` |
| `CatalogCollection` | `shutterstock_api_explorer/models/catalog_collection.py` |

