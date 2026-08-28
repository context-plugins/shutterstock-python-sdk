from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.get_contributor_collection_items_error import (
    GetContributorCollectionItemsErrorBody,
    get_contributor_collection_items_error_mapper,
)
from ..errors.get_contributor_collections_error import (
    GetContributorCollectionsErrorBody,
    get_contributor_collections_error_mapper,
)
from ..errors.get_contributor_collections_list_error import (
    GetContributorCollectionsListErrorBody,
    get_contributor_collections_list_error_mapper,
)
from ..errors.get_contributor_error import GetContributorErrorBody, get_contributor_error_mapper
from ..errors.get_contributor_list_error import GetContributorListErrorBody, get_contributor_list_error_mapper
from ..models.collection import Collection
from ..models.collection_data_list import CollectionDataList
from ..models.collection_item_data_list import CollectionItemDataList
from ..models.contributor_profile import ContributorProfile
from ..models.contributor_profile_data_list import ContributorProfileDataList
from ..models.enums.sort5 import Sort5OrStr
from ..models.enums.sort24 import Sort24OrStr
from ..server.server import Server


class Contributors:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ContributorsWithRawResponse(client, server, auth)

    def get_contributor(
        self, contributor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ContributorProfile:
        """This endpoint shows information about a single contributor, including contributor type, equipment they use,
        and other attributes.

        Args:
            contributor_id: Contributor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_contributor(contributor_id, request_options=request_options).unwrap()

    def get_contributor_collection_items(
        self,
        contributor_id: str,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionItemDataList:
        """This endpoint lists the IDs of items in a contributor's collection and the date that each was added.

        Args:
            contributor_id: Contributor ID
            id: Collection ID that belongs to the contributor
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Set not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_contributor_collection_items(
            contributor_id, id, page=page, per_page=per_page, sort=sort, request_options=request_options
        ).unwrap()

    def get_contributor_collections(
        self, contributor_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Collection:
        """This endpoint gets more detailed information about a contributor's collection, including its cover image,
        timestamps for its creation, and most recent update. To get the items in collections, use GET
        /v2/contributors/{contributor_id}/collections/{id}/items.

        Args:
            contributor_id: Contributor ID
            id: Collection ID that belongs to the contributor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Set not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_contributor_collections(
            contributor_id, id, request_options=request_options
        ).unwrap()

    def get_contributor_collections_list(
        self,
        contributor_id: str,
        *,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionDataList:
        """This endpoint lists collections based on contributor ID.

        Args:
            contributor_id: Contributor ID
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Contributor not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_contributor_collections_list(
            contributor_id, sort=sort, request_options=request_options
        ).unwrap()

    def get_contributor_list(
        self, id: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ContributorProfileDataList:
        """This endpoint lists information about one or more contributors, including contributor type, equipment they
        use and other attributes.

        Args:
            id: One or more contributor IDs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_contributor_list(id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ContributorsWithRawResponse:
        return self._with_raw_response


class AsyncContributors:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncContributorsWithRawResponse(client, server, auth)

    async def get_contributor(
        self, contributor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ContributorProfile:
        """This endpoint shows information about a single contributor, including contributor type, equipment they use,
        and other attributes.

        Args:
            contributor_id: Contributor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_contributor(contributor_id, request_options=request_options)).unwrap()

    async def get_contributor_collection_items(
        self,
        contributor_id: str,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionItemDataList:
        """This endpoint lists the IDs of items in a contributor's collection and the date that each was added.

        Args:
            contributor_id: Contributor ID
            id: Collection ID that belongs to the contributor
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Set not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_contributor_collection_items(
                contributor_id, id, page=page, per_page=per_page, sort=sort, request_options=request_options
            )
        ).unwrap()

    async def get_contributor_collections(
        self, contributor_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Collection:
        """This endpoint gets more detailed information about a contributor's collection, including its cover image,
        timestamps for its creation, and most recent update. To get the items in collections, use GET
        /v2/contributors/{contributor_id}/collections/{id}/items.

        Args:
            contributor_id: Contributor ID
            id: Collection ID that belongs to the contributor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Set not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_contributor_collections(
                contributor_id, id, request_options=request_options
            )
        ).unwrap()

    async def get_contributor_collections_list(
        self,
        contributor_id: str,
        *,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionDataList:
        """This endpoint lists collections based on contributor ID.

        Args:
            contributor_id: Contributor ID
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Contributor not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_contributor_collections_list(
                contributor_id, sort=sort, request_options=request_options
            )
        ).unwrap()

    async def get_contributor_list(
        self, id: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ContributorProfileDataList:
        """This endpoint lists information about one or more contributors, including contributor type, equipment they
        use and other attributes.

        Args:
            id: One or more contributor IDs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_contributor_list(id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncContributorsWithRawResponse:
        return self._with_raw_response


class ContributorsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_contributor(
        self, contributor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContributorProfile, GetContributorErrorBody]:
        """This endpoint shows information about a single contributor, including contributor type, equipment they use,
        and other attributes.

        Args:
            contributor_id: Contributor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors/{contributor_id}"),
            path_params=[param[str]("contributor_id", contributor_id)],
            auth_scheme=AnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[ContributorProfile],
            error_mapper=get_contributor_error_mapper,
            request_options=request_options,
        )

    def get_contributor_collection_items(
        self,
        contributor_id: str,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionItemDataList, GetContributorCollectionItemsErrorBody]:
        """This endpoint lists the IDs of items in a contributor's collection and the date that each was added.

        Args:
            contributor_id: Contributor ID
            id: Collection ID that belongs to the contributor
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors/{contributor_id}/collections/{id}/items"),
            path_params=[param[str]("contributor_id", contributor_id), param[str]("id", id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[CollectionItemDataList],
            error_mapper=get_contributor_collection_items_error_mapper,
            request_options=request_options,
        )

    def get_contributor_collections(
        self, contributor_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Collection, GetContributorCollectionsErrorBody]:
        """This endpoint gets more detailed information about a contributor's collection, including its cover image,
        timestamps for its creation, and most recent update. To get the items in collections, use GET
        /v2/contributors/{contributor_id}/collections/{id}/items.

        Args:
            contributor_id: Contributor ID
            id: Collection ID that belongs to the contributor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors/{contributor_id}/collections/{id}"),
            path_params=[param[str]("contributor_id", contributor_id), param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[Collection],
            error_mapper=get_contributor_collections_error_mapper,
            request_options=request_options,
        )

    def get_contributor_collections_list(
        self,
        contributor_id: str,
        *,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionDataList, GetContributorCollectionsListErrorBody]:
        """This endpoint lists collections based on contributor ID.

        Args:
            contributor_id: Contributor ID
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors/{contributor_id}/collections"),
            path_params=[param[str]("contributor_id", contributor_id)],
            query_params=[param[Sort24OrStr | None]("sort", sort)],
            auth_scheme=AnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[CollectionDataList],
            error_mapper=get_contributor_collections_list_error_mapper,
            request_options=request_options,
        )

    def get_contributor_list(
        self, id: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContributorProfileDataList, GetContributorListErrorBody]:
        """This endpoint lists information about one or more contributors, including contributor type, equipment they
        use and other attributes.

        Args:
            id: One or more contributor IDs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors"),
            query_params=[param[list[str]]("id", id)],
            auth_scheme=AnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[ContributorProfileDataList],
            error_mapper=get_contributor_list_error_mapper,
            request_options=request_options,
        )


class AsyncContributorsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_contributor(
        self, contributor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContributorProfile, GetContributorErrorBody]:
        """This endpoint shows information about a single contributor, including contributor type, equipment they use,
        and other attributes.

        Args:
            contributor_id: Contributor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors/{contributor_id}"),
            path_params=[param[str]("contributor_id", contributor_id)],
            auth_scheme=AsyncAnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[ContributorProfile],
            error_mapper=get_contributor_error_mapper,
            request_options=request_options,
        )

    async def get_contributor_collection_items(
        self,
        contributor_id: str,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionItemDataList, GetContributorCollectionItemsErrorBody]:
        """This endpoint lists the IDs of items in a contributor's collection and the date that each was added.

        Args:
            contributor_id: Contributor ID
            id: Collection ID that belongs to the contributor
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors/{contributor_id}/collections/{id}/items"),
            path_params=[param[str]("contributor_id", contributor_id), param[str]("id", id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[CollectionItemDataList],
            error_mapper=get_contributor_collection_items_error_mapper,
            request_options=request_options,
        )

    async def get_contributor_collections(
        self, contributor_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Collection, GetContributorCollectionsErrorBody]:
        """This endpoint gets more detailed information about a contributor's collection, including its cover image,
        timestamps for its creation, and most recent update. To get the items in collections, use GET
        /v2/contributors/{contributor_id}/collections/{id}/items.

        Args:
            contributor_id: Contributor ID
            id: Collection ID that belongs to the contributor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors/{contributor_id}/collections/{id}"),
            path_params=[param[str]("contributor_id", contributor_id), param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[Collection],
            error_mapper=get_contributor_collections_error_mapper,
            request_options=request_options,
        )

    async def get_contributor_collections_list(
        self,
        contributor_id: str,
        *,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionDataList, GetContributorCollectionsListErrorBody]:
        """This endpoint lists collections based on contributor ID.

        Args:
            contributor_id: Contributor ID
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors/{contributor_id}/collections"),
            path_params=[param[str]("contributor_id", contributor_id)],
            query_params=[param[Sort24OrStr | None]("sort", sort)],
            auth_scheme=AsyncAnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[CollectionDataList],
            error_mapper=get_contributor_collections_list_error_mapper,
            request_options=request_options,
        )

    async def get_contributor_list(
        self, id: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContributorProfileDataList, GetContributorListErrorBody]:
        """This endpoint lists information about one or more contributors, including contributor type, equipment they
        use and other attributes.

        Args:
            id: One or more contributor IDs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/contributors"),
            query_params=[param[list[str]]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.customer_access_code, self._auth.basic),
            decoder=json_decoder[ContributorProfileDataList],
            error_mapper=get_contributor_list_error_mapper,
            request_options=request_options,
        )
