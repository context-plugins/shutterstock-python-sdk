from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    Date,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_editorial_video_error import GetEditorialVideoErrorBody, get_editorial_video_error_mapper
from ..errors.get_editorial_video_license_list_error import (
    GetEditorialVideoLicenseListErrorBody,
    get_editorial_video_license_list_error_mapper,
)
from ..errors.license_editorial_video_error import LicenseEditorialVideoErrorBody, license_editorial_video_error_mapper
from ..errors.list_editorial_video_categories_error import (
    ListEditorialVideoCategoriesErrorBody,
    list_editorial_video_categories_error_mapper,
)
from ..errors.list_editorial_videos_error import ListEditorialVideosErrorBody, list_editorial_videos_error_mapper
from ..errors.search_editorial_videos_error import SearchEditorialVideosErrorBody, search_editorial_videos_error_mapper
from ..models.download_history_data_list import DownloadHistoryDataList
from ..models.editorial_video_category_results import EditorialVideoCategoryResults
from ..models.editorial_video_content import EditorialVideoContent
from ..models.editorial_video_results import EditorialVideoResults
from ..models.editorial_video_search_results import EditorialVideoSearchResults
from ..models.enums.download_availability import DownloadAvailabilityOrStr
from ..models.enums.resolution import ResolutionOrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.enums.sort17 import Sort17OrStr
from ..models.license_editorial_content_results import LicenseEditorialContentResults
from ..models.license_editorial_video_content_request import (
    LicenseEditorialVideoContentRequest,
    LicenseEditorialVideoContentRequestDict,
)
from ..server.server import Server


class EditorialVideo:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EditorialVideoWithRawResponse(client, server, auth)

    def get_editorial_video(
        self,
        id: str,
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialVideoContent:
        """This endpoint shows information about an editorial image, including a URL to a preview image and the sizes
        that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_video(
            id, country, search_id=search_id, request_options=request_options
        ).unwrap()

    def get_editorial_video_license_list(
        self,
        *,
        video_id: str | None = None,
        license: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        username: str | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        download_availability: DownloadAvailabilityOrStr | None = None,
        team_history: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DownloadHistoryDataList:
        """This endpoint lists existing editorial video licenses.

        Args:
            video_id: Show licenses for the specified editorial video ID
            license: Show editorial videos that are available with the specified license name
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            username: Filter licenses by username of licensee
            start_date: Show licenses created on or after the specified date
            end_date: Show licenses created before the specified date
            download_availability: Filter licenses by download availability
            team_history: Set to true to see license history for all members of your team.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_video_license_list(
            video_id=video_id,
            license=license,
            page=page,
            per_page=per_page,
            sort=sort,
            username=username,
            start_date=start_date,
            end_date=end_date,
            download_availability=download_availability,
            team_history=team_history,
            request_options=request_options,
        ).unwrap()

    def license_editorial_video(
        self,
        body: LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseEditorialContentResults:
        """This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more
        editorial videos to license. The download links in the response are valid for 8 hours.

        Args:
            body: License editorial video content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.license_editorial_video(body, request_options=request_options).unwrap()

    def list_editorial_video_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialVideoCategoryResults:
        """This endpoint lists the categories that editorial videos can belong to, which are separate from the
        categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.list_editorial_video_categories(request_options=request_options).unwrap()

    def list_editorial_videos(
        self,
        id: list[str],
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialVideoResults:
        """This endpoint lists the details of editorial videos by ID list.

        Args:
            id: ID of the editorial video to list details for
            country: Show only editorial video content that is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.list_editorial_videos(
            id, country, search_id=search_id, request_options=request_options
        ).unwrap()

    def search_editorial_videos(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        resolution: ResolutionOrStr | None = None,
        fps: float | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialVideoSearchResults:
        """This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an
        AND condition. For example, if you set the ``category`` parameter to "Alone,Performing" and also specify a
        ``query`` parameter, the results include only videos that match the query and are in both the Alone and
        Performing categories. You can also filter search terms out in the ``query`` parameter by prefixing the term
        with NOT.

        Args:
            country: Show only editorial video content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content with each of the specified editorial categories; specify category names in
                a comma-separated list
            supplier_code: Show only editorial video content from certain suppliers
            date_start: Show only editorial video content generated on or after a specific date
            date_end: Show only editorial video content generated on or before a specific date
            resolution: Show only editorial video content with specific resolution
            fps: Show only editorial video content generated with specific frames per second
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.search_editorial_videos(
            country,
            query=query,
            sort=sort,
            category=category,
            supplier_code=supplier_code,
            date_start=date_start,
            date_end=date_end,
            resolution=resolution,
            fps=fps,
            per_page=per_page,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> EditorialVideoWithRawResponse:
        return self._with_raw_response


class AsyncEditorialVideo:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEditorialVideoWithRawResponse(client, server, auth)

    async def get_editorial_video(
        self,
        id: str,
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialVideoContent:
        """This endpoint shows information about an editorial image, including a URL to a preview image and the sizes
        that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_video(
                id, country, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def get_editorial_video_license_list(
        self,
        *,
        video_id: str | None = None,
        license: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        username: str | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        download_availability: DownloadAvailabilityOrStr | None = None,
        team_history: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DownloadHistoryDataList:
        """This endpoint lists existing editorial video licenses.

        Args:
            video_id: Show licenses for the specified editorial video ID
            license: Show editorial videos that are available with the specified license name
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            username: Filter licenses by username of licensee
            start_date: Show licenses created on or after the specified date
            end_date: Show licenses created before the specified date
            download_availability: Filter licenses by download availability
            team_history: Set to true to see license history for all members of your team.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_video_license_list(
                video_id=video_id,
                license=license,
                page=page,
                per_page=per_page,
                sort=sort,
                username=username,
                start_date=start_date,
                end_date=end_date,
                download_availability=download_availability,
                team_history=team_history,
                request_options=request_options,
            )
        ).unwrap()

    async def license_editorial_video(
        self,
        body: LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseEditorialContentResults:
        """This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more
        editorial videos to license. The download links in the response are valid for 8 hours.

        Args:
            body: License editorial video content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.license_editorial_video(body, request_options=request_options)).unwrap()

    async def list_editorial_video_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialVideoCategoryResults:
        """This endpoint lists the categories that editorial videos can belong to, which are separate from the
        categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_editorial_video_categories(request_options=request_options)).unwrap()

    async def list_editorial_videos(
        self,
        id: list[str],
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialVideoResults:
        """This endpoint lists the details of editorial videos by ID list.

        Args:
            id: ID of the editorial video to list details for
            country: Show only editorial video content that is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_editorial_videos(
                id, country, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def search_editorial_videos(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        resolution: ResolutionOrStr | None = None,
        fps: float | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialVideoSearchResults:
        """This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an
        AND condition. For example, if you set the ``category`` parameter to "Alone,Performing" and also specify a
        ``query`` parameter, the results include only videos that match the query and are in both the Alone and
        Performing categories. You can also filter search terms out in the ``query`` parameter by prefixing the term
        with NOT.

        Args:
            country: Show only editorial video content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content with each of the specified editorial categories; specify category names in
                a comma-separated list
            supplier_code: Show only editorial video content from certain suppliers
            date_start: Show only editorial video content generated on or after a specific date
            date_end: Show only editorial video content generated on or before a specific date
            resolution: Show only editorial video content with specific resolution
            fps: Show only editorial video content generated with specific frames per second
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_editorial_videos(
                country,
                query=query,
                sort=sort,
                category=category,
                supplier_code=supplier_code,
                date_start=date_start,
                date_end=date_end,
                resolution=resolution,
                fps=fps,
                per_page=per_page,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEditorialVideoWithRawResponse:
        return self._with_raw_response


class EditorialVideoWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_editorial_video(
        self,
        id: str,
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialVideoContent, GetEditorialVideoErrorBody]:
        """This endpoint shows information about an editorial image, including a URL to a preview image and the sizes
        that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country), param[str | None]("search_id", search_id)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialVideoContent],
            error_mapper=get_editorial_video_error_mapper,
            request_options=request_options,
        )

    def get_editorial_video_license_list(
        self,
        *,
        video_id: str | None = None,
        license: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        username: str | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        download_availability: DownloadAvailabilityOrStr | None = None,
        team_history: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DownloadHistoryDataList, GetEditorialVideoLicenseListErrorBody]:
        """This endpoint lists existing editorial video licenses.

        Args:
            video_id: Show licenses for the specified editorial video ID
            license: Show editorial videos that are available with the specified license name
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            username: Filter licenses by username of licensee
            start_date: Show licenses created on or after the specified date
            end_date: Show licenses created before the specified date
            download_availability: Filter licenses by download availability
            team_history: Set to true to see license history for all members of your team.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos/licenses"),
            query_params=[
                param[str | None]("video_id", video_id),
                param[str | None]("license", license),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
                param[str | None]("username", username),
                param[RFC3339DateTime | None]("start_date", start_date),
                param[RFC3339DateTime | None]("end_date", end_date),
                param[DownloadAvailabilityOrStr | None]("download_availability", download_availability),
                param[bool | None]("team_history", team_history),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[DownloadHistoryDataList],
            error_mapper=get_editorial_video_license_list_error_mapper,
            request_options=request_options,
        )

    def license_editorial_video(
        self,
        body: LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialVideoErrorBody]:
        """This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more
        editorial videos to license. The download links in the response are valid for 8 hours.

        Args:
            body: License editorial video content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/editorial/videos/licenses"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseEditorialContentResults],
            error_mapper=license_editorial_video_error_mapper,
            request_options=request_options,
        )

    def list_editorial_video_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialVideoCategoryResults, ListEditorialVideoCategoriesErrorBody]:
        """This endpoint lists the categories that editorial videos can belong to, which are separate from the
        categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos/categories"),
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialVideoCategoryResults],
            error_mapper=list_editorial_video_categories_error_mapper,
            request_options=request_options,
        )

    def list_editorial_videos(
        self,
        id: list[str],
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialVideoResults, ListEditorialVideosErrorBody]:
        """This endpoint lists the details of editorial videos by ID list.

        Args:
            id: ID of the editorial video to list details for
            country: Show only editorial video content that is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos"),
            query_params=[
                param[list[str]]("id", id), param[str]("country", country), param[str | None]("search_id", search_id)
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialVideoResults],
            error_mapper=list_editorial_videos_error_mapper,
            request_options=request_options,
        )

    def search_editorial_videos(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        resolution: ResolutionOrStr | None = None,
        fps: float | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialVideoSearchResults, SearchEditorialVideosErrorBody]:
        """This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an
        AND condition. For example, if you set the ``category`` parameter to "Alone,Performing" and also specify a
        ``query`` parameter, the results include only videos that match the query and are in both the Alone and
        Performing categories. You can also filter search terms out in the ``query`` parameter by prefixing the term
        with NOT.

        Args:
            country: Show only editorial video content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content with each of the specified editorial categories; specify category names in
                a comma-separated list
            supplier_code: Show only editorial video content from certain suppliers
            date_start: Show only editorial video content generated on or after a specific date
            date_end: Show only editorial video content generated on or before a specific date
            resolution: Show only editorial video content with specific resolution
            fps: Show only editorial video content generated with specific frames per second
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos/search"),
            query_params=[
                param[str]("country", country),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
                param[str | None]("category", category),
                param[list[str] | None]("supplier_code", supplier_code),
                param[Date | None]("date_start", date_start),
                param[Date | None]("date_end", date_end),
                param[ResolutionOrStr | None]("resolution", resolution),
                param[float | None]("fps", fps),
                param[int | None]("per_page", per_page),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialVideoSearchResults],
            error_mapper=search_editorial_videos_error_mapper,
            request_options=request_options,
        )


class AsyncEditorialVideoWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_editorial_video(
        self,
        id: str,
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialVideoContent, GetEditorialVideoErrorBody]:
        """This endpoint shows information about an editorial image, including a URL to a preview image and the sizes
        that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country), param[str | None]("search_id", search_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialVideoContent],
            error_mapper=get_editorial_video_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_video_license_list(
        self,
        *,
        video_id: str | None = None,
        license: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        username: str | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        download_availability: DownloadAvailabilityOrStr | None = None,
        team_history: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DownloadHistoryDataList, GetEditorialVideoLicenseListErrorBody]:
        """This endpoint lists existing editorial video licenses.

        Args:
            video_id: Show licenses for the specified editorial video ID
            license: Show editorial videos that are available with the specified license name
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            username: Filter licenses by username of licensee
            start_date: Show licenses created on or after the specified date
            end_date: Show licenses created before the specified date
            download_availability: Filter licenses by download availability
            team_history: Set to true to see license history for all members of your team.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos/licenses"),
            query_params=[
                param[str | None]("video_id", video_id),
                param[str | None]("license", license),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
                param[str | None]("username", username),
                param[RFC3339DateTime | None]("start_date", start_date),
                param[RFC3339DateTime | None]("end_date", end_date),
                param[DownloadAvailabilityOrStr | None]("download_availability", download_availability),
                param[bool | None]("team_history", team_history),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[DownloadHistoryDataList],
            error_mapper=get_editorial_video_license_list_error_mapper,
            request_options=request_options,
        )

    async def license_editorial_video(
        self,
        body: LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialVideoErrorBody]:
        """This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more
        editorial videos to license. The download links in the response are valid for 8 hours.

        Args:
            body: License editorial video content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/editorial/videos/licenses"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseEditorialVideoContentRequest | LicenseEditorialVideoContentRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseEditorialContentResults],
            error_mapper=license_editorial_video_error_mapper,
            request_options=request_options,
        )

    async def list_editorial_video_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialVideoCategoryResults, ListEditorialVideoCategoriesErrorBody]:
        """This endpoint lists the categories that editorial videos can belong to, which are separate from the
        categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos/categories"),
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialVideoCategoryResults],
            error_mapper=list_editorial_video_categories_error_mapper,
            request_options=request_options,
        )

    async def list_editorial_videos(
        self,
        id: list[str],
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialVideoResults, ListEditorialVideosErrorBody]:
        """This endpoint lists the details of editorial videos by ID list.

        Args:
            id: ID of the editorial video to list details for
            country: Show only editorial video content that is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos"),
            query_params=[
                param[list[str]]("id", id), param[str]("country", country), param[str | None]("search_id", search_id)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialVideoResults],
            error_mapper=list_editorial_videos_error_mapper,
            request_options=request_options,
        )

    async def search_editorial_videos(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        resolution: ResolutionOrStr | None = None,
        fps: float | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialVideoSearchResults, SearchEditorialVideosErrorBody]:
        """This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an
        AND condition. For example, if you set the ``category`` parameter to "Alone,Performing" and also specify a
        ``query`` parameter, the results include only videos that match the query and are in both the Alone and
        Performing categories. You can also filter search terms out in the ``query`` parameter by prefixing the term
        with NOT.

        Args:
            country: Show only editorial video content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content with each of the specified editorial categories; specify category names in
                a comma-separated list
            supplier_code: Show only editorial video content from certain suppliers
            date_start: Show only editorial video content generated on or after a specific date
            date_end: Show only editorial video content generated on or before a specific date
            resolution: Show only editorial video content with specific resolution
            fps: Show only editorial video content generated with specific frames per second
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/videos/search"),
            query_params=[
                param[str]("country", country),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
                param[str | None]("category", category),
                param[list[str] | None]("supplier_code", supplier_code),
                param[Date | None]("date_start", date_start),
                param[Date | None]("date_end", date_end),
                param[ResolutionOrStr | None]("resolution", resolution),
                param[float | None]("fps", fps),
                param[int | None]("per_page", per_page),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialVideoSearchResults],
            error_mapper=search_editorial_videos_error_mapper,
            request_options=request_options,
        )
