from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.delete_collection_error import DeleteCollectionErrorBody, delete_collection_error_mapper
from ..errors.get_collections_error import GetCollectionsErrorBody, get_collections_error_mapper
from ..errors.search_catalog_error import SearchCatalogErrorBody, search_catalog_error_mapper
from ..models.catalog_collection import CatalogCollection
from ..models.catalog_collection_data_list import CatalogCollectionDataList
from ..models.catalog_collection_item_data_list import CatalogCollectionItemDataList
from ..models.create_catalog_collection import CreateCatalogCollection, CreateCatalogCollectionDict
from ..models.create_catalog_collection_items import CreateCatalogCollectionItems, CreateCatalogCollectionItemsDict
from ..models.enums.asset_type import AssetTypeOrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.remove_catalog_collection_items import RemoveCatalogCollectionItems, RemoveCatalogCollectionItemsDict
from ..models.update_catalog_collection import UpdateCatalogCollection, UpdateCatalogCollectionDict
from ..server.server import Server


class Catalog:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CatalogWithRawResponse(client, server, auth)

    def add_to_collection(
        self,
        collection_id: str,
        body: CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollection:
        """This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user's
        account's catalog.

        Args:
            collection_id: The ID of the collection to add assets to
            body: Collection item attributes to add to collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.add_to_collection(collection_id, body, request_options=request_options).unwrap()

    def create_collection(
        self,
        body: CreateCatalogCollection | CreateCatalogCollectionDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollection:
        """This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later,
        use ``PATCH /v2/catalog/collections/{collection_id}/items``.

        Args:
            body: Create a catalog collection and, optionally, add items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_collection(body, request_options=request_options).unwrap()

    def delete_collection(self, collection_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This endpoint deletes a catalog collection. It does not remove the assets from the user's account's catalog.

        Args:
            collection_id: The ID of the collection to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_collection(collection_id, request_options=request_options).unwrap()

    def delete_from_collection(
        self,
        collection_id: str,
        body: RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollection:
        """This endpoint removes assets from a catalog collection. It does not remove the assets from the user's
        account's catalog.

        Args:
            collection_id: The ID of the collection to remove assets from
            body: Items to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_from_collection(
            collection_id, body, request_options=request_options
        ).unwrap()

    def get_collections(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        shared: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollectionDataList:
        """This endpoint returns a list of catalog collections.

        Args:
            page: Page number
            per_page: Number of results per page
            sort: Sort by
            shared: Set to true to omit collections that you own and return only collections that are shared with you
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Invalid status value ``error`` is ``RawError``."""
        return self._with_raw_response.get_collections(
            page=page, per_page=per_page, sort=sort, shared=shared, request_options=request_options
        ).unwrap()

    def search_catalog(
        self,
        *,
        sort: Sort5OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        collection_id: list[str] | None = None,
        asset_type: list[AssetTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollectionItemDataList:
        """This endpoint searches for assets in the account's catalog. If you specify more than one search parameter,
        the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an
        AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in
        the ``query`` parameter by prefixing the term with NOT.

        Args:
            sort: Sort by
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            collection_id: Filter by collection id
            asset_type: Filter by asset type
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.search_catalog(
            sort=sort,
            page=page,
            per_page=per_page,
            query=query,
            collection_id=collection_id,
            asset_type=asset_type,
            request_options=request_options,
        ).unwrap()

    def update_collection(
        self,
        collection_id: str,
        body: UpdateCatalogCollection | UpdateCatalogCollectionDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollection:
        """This endpoint updates the metadata of a catalog collection.

        Args:
            collection_id: ID of collection that needs to be modified
            body: Collections Metadata to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_collection(collection_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CatalogWithRawResponse:
        return self._with_raw_response


class AsyncCatalog:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCatalogWithRawResponse(client, server, auth)

    async def add_to_collection(
        self,
        collection_id: str,
        body: CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollection:
        """This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user's
        account's catalog.

        Args:
            collection_id: The ID of the collection to add assets to
            body: Collection item attributes to add to collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_to_collection(collection_id, body, request_options=request_options)
        ).unwrap()

    async def create_collection(
        self,
        body: CreateCatalogCollection | CreateCatalogCollectionDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollection:
        """This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later,
        use ``PATCH /v2/catalog/collections/{collection_id}/items``.

        Args:
            body: Create a catalog collection and, optionally, add items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_collection(body, request_options=request_options)).unwrap()

    async def delete_collection(
        self, collection_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint deletes a catalog collection. It does not remove the assets from the user's account's catalog.

        Args:
            collection_id: The ID of the collection to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_collection(collection_id, request_options=request_options)
        ).unwrap()

    async def delete_from_collection(
        self,
        collection_id: str,
        body: RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollection:
        """This endpoint removes assets from a catalog collection. It does not remove the assets from the user's
        account's catalog.

        Args:
            collection_id: The ID of the collection to remove assets from
            body: Items to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_from_collection(collection_id, body, request_options=request_options)
        ).unwrap()

    async def get_collections(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        shared: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollectionDataList:
        """This endpoint returns a list of catalog collections.

        Args:
            page: Page number
            per_page: Number of results per page
            sort: Sort by
            shared: Set to true to omit collections that you own and return only collections that are shared with you
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Invalid status value ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_collections(
                page=page, per_page=per_page, sort=sort, shared=shared, request_options=request_options
            )
        ).unwrap()

    async def search_catalog(
        self,
        *,
        sort: Sort5OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        collection_id: list[str] | None = None,
        asset_type: list[AssetTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollectionItemDataList:
        """This endpoint searches for assets in the account's catalog. If you specify more than one search parameter,
        the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an
        AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in
        the ``query`` parameter by prefixing the term with NOT.

        Args:
            sort: Sort by
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            collection_id: Filter by collection id
            asset_type: Filter by asset type
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_catalog(
                sort=sort,
                page=page,
                per_page=per_page,
                query=query,
                collection_id=collection_id,
                asset_type=asset_type,
                request_options=request_options,
            )
        ).unwrap()

    async def update_collection(
        self,
        collection_id: str,
        body: UpdateCatalogCollection | UpdateCatalogCollectionDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CatalogCollection:
        """This endpoint updates the metadata of a catalog collection.

        Args:
            collection_id: ID of collection that needs to be modified
            body: Collections Metadata to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_collection(collection_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCatalogWithRawResponse:
        return self._with_raw_response


class CatalogWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_to_collection(
        self,
        collection_id: str,
        body: CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollection, RawError]:
        """This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user's
        account's catalog.

        Args:
            collection_id: The ID of the collection to add assets to
            body: Collection item attributes to add to collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/collections/{collection_id}/items"),
            path_params=[param[str]("collection_id", collection_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_collection(
        self,
        body: CreateCatalogCollection | CreateCatalogCollectionDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollection, RawError]:
        """This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later,
        use ``PATCH /v2/catalog/collections/{collection_id}/items``.

        Args:
            body: Create a catalog collection and, optionally, add items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/collections"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCatalogCollection | CreateCatalogCollectionDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_collection(
        self, collection_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCollectionErrorBody]:
        """This endpoint deletes a catalog collection. It does not remove the assets from the user's account's catalog.

        Args:
            collection_id: The ID of the collection to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/catalog/collections/{collection_id}"),
            path_params=[param[str]("collection_id", collection_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_collection_error_mapper,
            request_options=request_options,
        )

    def delete_from_collection(
        self,
        collection_id: str,
        body: RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollection, RawError]:
        """This endpoint removes assets from a catalog collection. It does not remove the assets from the user's
        account's catalog.

        Args:
            collection_id: The ID of the collection to remove assets from
            body: Items to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/catalog/collections/{collection_id}/items"),
            path_params=[param[str]("collection_id", collection_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_collections(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        shared: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollectionDataList, GetCollectionsErrorBody]:
        """This endpoint returns a list of catalog collections.

        Args:
            page: Page number
            per_page: Number of results per page
            sort: Sort by
            shared: Set to true to omit collections that you own and return only collections that are shared with you
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/collections"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
                param[bool | None]("shared", shared),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollectionDataList],
            error_mapper=get_collections_error_mapper,
            request_options=request_options,
        )

    def search_catalog(
        self,
        *,
        sort: Sort5OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        collection_id: list[str] | None = None,
        asset_type: list[AssetTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollectionItemDataList, SearchCatalogErrorBody]:
        """This endpoint searches for assets in the account's catalog. If you specify more than one search parameter,
        the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an
        AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in
        the ``query`` parameter by prefixing the term with NOT.

        Args:
            sort: Sort by
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            collection_id: Filter by collection id
            asset_type: Filter by asset type
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/search"),
            query_params=[
                param[Sort5OrStr | None]("sort", sort),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("query", query),
                param[list[str] | None]("collection_id", collection_id),
                param[list[AssetTypeOrStr] | None]("asset_type", asset_type),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollectionItemDataList],
            error_mapper=search_catalog_error_mapper,
            request_options=request_options,
        )

    def update_collection(
        self,
        collection_id: str,
        body: UpdateCatalogCollection | UpdateCatalogCollectionDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollection, RawError]:
        """This endpoint updates the metadata of a catalog collection.

        Args:
            collection_id: ID of collection that needs to be modified
            body: Collections Metadata to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/catalog/collections/{collection_id}"),
            path_params=[param[str]("collection_id", collection_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCatalogCollection | UpdateCatalogCollectionDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCatalogWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_to_collection(
        self,
        collection_id: str,
        body: CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollection, RawError]:
        """This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user's
        account's catalog.

        Args:
            collection_id: The ID of the collection to add assets to
            body: Collection item attributes to add to collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/collections/{collection_id}/items"),
            path_params=[param[str]("collection_id", collection_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCatalogCollectionItems | CreateCatalogCollectionItemsDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_collection(
        self,
        body: CreateCatalogCollection | CreateCatalogCollectionDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollection, RawError]:
        """This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later,
        use ``PATCH /v2/catalog/collections/{collection_id}/items``.

        Args:
            body: Create a catalog collection and, optionally, add items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/collections"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCatalogCollection | CreateCatalogCollectionDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_collection(
        self, collection_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCollectionErrorBody]:
        """This endpoint deletes a catalog collection. It does not remove the assets from the user's account's catalog.

        Args:
            collection_id: The ID of the collection to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/catalog/collections/{collection_id}"),
            path_params=[param[str]("collection_id", collection_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_collection_error_mapper,
            request_options=request_options,
        )

    async def delete_from_collection(
        self,
        collection_id: str,
        body: RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollection, RawError]:
        """This endpoint removes assets from a catalog collection. It does not remove the assets from the user's
        account's catalog.

        Args:
            collection_id: The ID of the collection to remove assets from
            body: Items to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/catalog/collections/{collection_id}/items"),
            path_params=[param[str]("collection_id", collection_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveCatalogCollectionItems | RemoveCatalogCollectionItemsDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_collections(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        shared: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollectionDataList, GetCollectionsErrorBody]:
        """This endpoint returns a list of catalog collections.

        Args:
            page: Page number
            per_page: Number of results per page
            sort: Sort by
            shared: Set to true to omit collections that you own and return only collections that are shared with you
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/collections"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
                param[bool | None]("shared", shared),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollectionDataList],
            error_mapper=get_collections_error_mapper,
            request_options=request_options,
        )

    async def search_catalog(
        self,
        *,
        sort: Sort5OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        collection_id: list[str] | None = None,
        asset_type: list[AssetTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollectionItemDataList, SearchCatalogErrorBody]:
        """This endpoint searches for assets in the account's catalog. If you specify more than one search parameter,
        the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an
        AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in
        the ``query`` parameter by prefixing the term with NOT.

        Args:
            sort: Sort by
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            collection_id: Filter by collection id
            asset_type: Filter by asset type
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/search"),
            query_params=[
                param[Sort5OrStr | None]("sort", sort),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("query", query),
                param[list[str] | None]("collection_id", collection_id),
                param[list[AssetTypeOrStr] | None]("asset_type", asset_type),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollectionItemDataList],
            error_mapper=search_catalog_error_mapper,
            request_options=request_options,
        )

    async def update_collection(
        self,
        collection_id: str,
        body: UpdateCatalogCollection | UpdateCatalogCollectionDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CatalogCollection, RawError]:
        """This endpoint updates the metadata of a catalog collection.

        Args:
            collection_id: ID of collection that needs to be modified
            body: Collections Metadata to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/catalog/collections/{collection_id}"),
            path_params=[param[str]("collection_id", collection_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCatalogCollection | UpdateCatalogCollectionDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CatalogCollection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
