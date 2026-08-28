from __future__ import annotations

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
from ..errors.get_editorial_categories_error import (
    GetEditorialCategoriesErrorBody,
    get_editorial_categories_error_mapper,
)
from ..errors.get_editorial_image2_error import GetEditorialImage2ErrorBody, get_editorial_image2_error_mapper
from ..errors.get_editorial_image_error import GetEditorialImageErrorBody, get_editorial_image_error_mapper
from ..errors.get_editorial_image_license_list_error import (
    GetEditorialImageLicenseListErrorBody,
    get_editorial_image_license_list_error_mapper,
)
from ..errors.get_editorial_image_livefeed_error import (
    GetEditorialImageLivefeedErrorBody,
    get_editorial_image_livefeed_error_mapper,
)
from ..errors.get_editorial_image_livefeed_items_error import (
    GetEditorialImageLivefeedItemsErrorBody,
    get_editorial_image_livefeed_items_error_mapper,
)
from ..errors.get_editorial_image_livefeed_list_error import (
    GetEditorialImageLivefeedListErrorBody,
    get_editorial_image_livefeed_list_error_mapper,
)
from ..errors.get_editorial_livefeed_error import GetEditorialLivefeedErrorBody, get_editorial_livefeed_error_mapper
from ..errors.get_editorial_livefeed_items_error import (
    GetEditorialLivefeedItemsErrorBody,
    get_editorial_livefeed_items_error_mapper,
)
from ..errors.get_editorial_livefeed_list_error import (
    GetEditorialLivefeedListErrorBody,
    get_editorial_livefeed_list_error_mapper,
)
from ..errors.get_updated_editorial_image_error import (
    GetUpdatedEditorialImageErrorBody,
    get_updated_editorial_image_error_mapper,
)
from ..errors.get_updated_editorial_images_error import (
    GetUpdatedEditorialImagesErrorBody,
    get_updated_editorial_images_error_mapper,
)
from ..errors.license_editorial_image_error import LicenseEditorialImageErrorBody, license_editorial_image_error_mapper
from ..errors.license_editorial_images_error import (
    LicenseEditorialImagesErrorBody,
    license_editorial_images_error_mapper,
)
from ..errors.list_editorial_image_categories_error import (
    ListEditorialImageCategoriesErrorBody,
    list_editorial_image_categories_error_mapper,
)
from ..errors.list_editorial_images_error import ListEditorialImagesErrorBody, list_editorial_images_error_mapper
from ..errors.search_editorial_error import SearchEditorialErrorBody, search_editorial_error_mapper
from ..errors.search_editorial_images_error import SearchEditorialImagesErrorBody, search_editorial_images_error_mapper
from ..models.download_history_data_list import DownloadHistoryDataList
from ..models.editorial_category_results import EditorialCategoryResults
from ..models.editorial_content import EditorialContent
from ..models.editorial_content_data_list import EditorialContentDataList
from ..models.editorial_image_category_results import EditorialImageCategoryResults
from ..models.editorial_image_livefeed import EditorialImageLivefeed
from ..models.editorial_image_livefeed_list import EditorialImageLivefeedList
from ..models.editorial_image_results import EditorialImageResults
from ..models.editorial_search_results import EditorialSearchResults
from ..models.editorial_updated_results import EditorialUpdatedResults
from ..models.enums.download_availability import DownloadAvailabilityOrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.enums.sort17 import Sort17OrStr
from ..models.enums.type15 import Type15OrStr
from ..models.license_editorial_content_request import (
    LicenseEditorialContentRequest,
    LicenseEditorialContentRequestDict,
)
from ..models.license_editorial_content_results import LicenseEditorialContentResults
from ..server.server import Server


class EditorialImages:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EditorialImagesWithRawResponse(client, server, auth)

    def get_editorial_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialCategoryResults:
        """Deprecated; use ``GET /v2/editorial/images/categories`` instead. This endpoint lists the categories that
        editorial images can belong to, which are separate from the categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_categories(request_options=request_options).unwrap()

    def get_editorial_image(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialContent:
        """This endpoint shows information about an editorial image, including a URL to a preview image and the sizes
        that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_image(id, country, request_options=request_options).unwrap()

    def get_editorial_image2(
        self,
        id: str,
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialContent:
        """Deprecated; use ``GET /v2/editorial/images/{id}`` instead to show information about an editorial image,
        including a URL to a preview image and the sizes that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_image2(
            id, country, search_id=search_id, request_options=request_options
        ).unwrap()

    def get_editorial_image_license_list(
        self,
        *,
        image_id: str | None = None,
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
        """This endpoint lists existing editorial image licenses.

        Args:
            image_id: Show licenses for the specified editorial image ID
            license: Show editorial images that are available with the specified license name
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
        return self._with_raw_response.get_editorial_image_license_list(
            image_id=image_id,
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

    def get_editorial_image_livefeed(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialImageLivefeed:
        """Send a ``GET`` request.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_image_livefeed(
            id, country, request_options=request_options
        ).unwrap()

    def get_editorial_image_livefeed_items(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialContentDataList:
        """Send a ``GET`` request.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed items are available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_image_livefeed_items(
            id, country, request_options=request_options
        ).unwrap()

    def get_editorial_image_livefeed_list(
        self,
        country: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialImageLivefeedList:
        """Send a ``GET`` request.

        Args:
            country: Returns only livefeeds that are available for distribution in a certain country
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_image_livefeed_list(
            country, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_editorial_livefeed(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialImageLivefeed:
        """Deprecated: use ``GET /v2/editorial/images/livefeeds/{id}`` instead to get an editorial livefeed.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_livefeed(id, country, request_options=request_options).unwrap()

    def get_editorial_livefeed_items(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialContentDataList:
        """Deprecated; use ``GET /v2/editorial/images/livefeeds/{id}/items`` instead to get editorial livefeed items.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed items are available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_livefeed_items(
            id, country, request_options=request_options
        ).unwrap()

    def get_editorial_livefeed_list(
        self,
        country: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialImageLivefeedList:
        """Deprecated; use ``GET /v2/editorial/images/livefeeds`` instead to get a list of editorial livefeeds.

        Args:
            country: Returns only livefeeds that are available for distribution in a certain country
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.get_editorial_livefeed_list(
            country, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_updated_editorial_image(
        self,
        type_: Type15OrStr,
        date_updated_start: RFC3339DateTime,
        date_updated_end: RFC3339DateTime,
        country: str,
        *,
        date_taken_start: Date | None = None,
        date_taken_end: Date | None = None,
        cursor: str | None = None,
        sort: Sort5OrStr | None = None,
        supplier_code: list[str] | None = None,
        per_page: int | None = 500,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialUpdatedResults:
        """Deprecated; use ``GET /v2/editorial/images/updated`` instead to get recently updated items.

        Args:
            type_: Specify ``addition`` to return only images that were added or ``edit`` to return only images that
                were edited or deleted
            date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            country: Show only editorial content that is available for distribution in a certain country
            date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want
                recently created images from the collection instead of updated older assets
            date_taken_end: Show images that were taken before the specified date
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            sort: Sort by
            supplier_code: Show only editorial content from certain suppliers
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.get_updated_editorial_image(
            type_,
            date_updated_start,
            date_updated_end,
            country,
            date_taken_start=date_taken_start,
            date_taken_end=date_taken_end,
            cursor=cursor,
            sort=sort,
            supplier_code=supplier_code,
            per_page=per_page,
            request_options=request_options,
        ).unwrap()

    def get_updated_editorial_images(
        self,
        type_: Type15OrStr,
        date_updated_start: RFC3339DateTime,
        date_updated_end: RFC3339DateTime,
        country: str,
        *,
        date_taken_start: Date | None = None,
        date_taken_end: Date | None = None,
        cursor: str | None = None,
        sort: Sort5OrStr | None = None,
        supplier_code: list[str] | None = None,
        per_page: int | None = 500,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialUpdatedResults:
        """This endpoint lists editorial images that have been updated in the specified time period to update content
        management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start
        and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use
        the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was
        taken.

        Args:
            type_: Specify ``addition`` to return only images that were added or ``edit`` to return only images that
                were edited or deleted
            date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            country: Show only editorial content that is available for distribution in a certain country
            date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want
                recently created images from the collection instead of updated older assets
            date_taken_end: Show images that were taken before the specified date
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            sort: Sort by
            supplier_code: Show only editorial content from certain suppliers
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.get_updated_editorial_images(
            type_,
            date_updated_start,
            date_updated_end,
            country,
            date_taken_start=date_taken_start,
            date_taken_end=date_taken_end,
            cursor=cursor,
            sort=sort,
            supplier_code=supplier_code,
            per_page=per_page,
            request_options=request_options,
        ).unwrap()

    def license_editorial_image(
        self,
        body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseEditorialContentResults:
        """Deprecated; use ``POST /v2/editorial/images/licenses`` instead to get licenses for one or more editorial
        images. You must specify the country and one or more editorial images to license. The download links in the
        response are valid for 8 hours.

        Args:
            body: License editorial content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.license_editorial_image(body, request_options=request_options).unwrap()

    def license_editorial_images(
        self,
        body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseEditorialContentResults:
        """This endpoint gets licenses for one or more editorial images. You must specify the country and one or more
        editorial images to license. The download links in the response are valid for 8 hours.

        Args:
            body: License editorial content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.license_editorial_images(body, request_options=request_options).unwrap()

    def list_editorial_image_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialImageCategoryResults:
        """This endpoint lists the categories that editorial images can belong to, which are separate from the
        categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.list_editorial_image_categories(request_options=request_options).unwrap()

    def list_editorial_images(
        self,
        id: list[str],
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialImageResults:
        """This endpoint lists the details of editorial images.

        Args:
            id: ID of the editorial image to list details for
            country: Show only editorial image content that is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.list_editorial_images(
            id, country, search_id=search_id, request_options=request_options
        ).unwrap()

    def search_editorial(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialSearchResults:
        """Deprecated; use ``GET /v2/editorial/images/search`` instead to search for editorial images.

        Args:
            country: Show only editorial content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content within a certain editorial category; specify by category name
            supplier_code: Show only editorial content from certain suppliers
            date_start: Show only editorial content generated on or after a specific date
            date_end: Show only editorial content generated on or before a specific date
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.search_editorial(
            country,
            query=query,
            sort=sort,
            category=category,
            supplier_code=supplier_code,
            date_start=date_start,
            date_end=date_end,
            per_page=per_page,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def search_editorial_images(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialSearchResults:
        """This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an
        AND condition. For example, if you set the ``category`` parameter to "Alone,Performing" and also specify a
        ``query`` parameter, the results include only images that match the query and are in both the Alone and
        Performing categories. You can also filter search terms out in the ``query`` parameter by prefixing the term
        with NOT.

        Args:
            country: Show only editorial content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content with each of the specified editorial categories; specify category names in
                a comma-separated list
            supplier_code: Show only editorial content from certain suppliers
            date_start: Show only editorial content generated on or after a specific date
            date_end: Show only editorial content generated on or before a specific date
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return self._with_raw_response.search_editorial_images(
            country,
            query=query,
            sort=sort,
            category=category,
            supplier_code=supplier_code,
            date_start=date_start,
            date_end=date_end,
            per_page=per_page,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> EditorialImagesWithRawResponse:
        return self._with_raw_response


class AsyncEditorialImages:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEditorialImagesWithRawResponse(client, server, auth)

    async def get_editorial_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialCategoryResults:
        """Deprecated; use ``GET /v2/editorial/images/categories`` instead. This endpoint lists the categories that
        editorial images can belong to, which are separate from the categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_editorial_categories(request_options=request_options)).unwrap()

    async def get_editorial_image(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialContent:
        """This endpoint shows information about an editorial image, including a URL to a preview image and the sizes
        that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_image(id, country, request_options=request_options)
        ).unwrap()

    async def get_editorial_image2(
        self,
        id: str,
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialContent:
        """Deprecated; use ``GET /v2/editorial/images/{id}`` instead to show information about an editorial image,
        including a URL to a preview image and the sizes that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_image2(
                id, country, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def get_editorial_image_license_list(
        self,
        *,
        image_id: str | None = None,
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
        """This endpoint lists existing editorial image licenses.

        Args:
            image_id: Show licenses for the specified editorial image ID
            license: Show editorial images that are available with the specified license name
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
            await self._with_raw_response.get_editorial_image_license_list(
                image_id=image_id,
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

    async def get_editorial_image_livefeed(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialImageLivefeed:
        """Send a ``GET`` request.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_image_livefeed(id, country, request_options=request_options)
        ).unwrap()

    async def get_editorial_image_livefeed_items(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialContentDataList:
        """Send a ``GET`` request.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed items are available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_image_livefeed_items(
                id, country, request_options=request_options
            )
        ).unwrap()

    async def get_editorial_image_livefeed_list(
        self,
        country: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialImageLivefeedList:
        """Send a ``GET`` request.

        Args:
            country: Returns only livefeeds that are available for distribution in a certain country
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_image_livefeed_list(
                country, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_editorial_livefeed(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialImageLivefeed:
        """Deprecated: use ``GET /v2/editorial/images/livefeeds/{id}`` instead to get an editorial livefeed.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_livefeed(id, country, request_options=request_options)
        ).unwrap()

    async def get_editorial_livefeed_items(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialContentDataList:
        """Deprecated; use ``GET /v2/editorial/images/livefeeds/{id}/items`` instead to get editorial livefeed items.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed items are available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_livefeed_items(id, country, request_options=request_options)
        ).unwrap()

    async def get_editorial_livefeed_list(
        self,
        country: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialImageLivefeedList:
        """Deprecated; use ``GET /v2/editorial/images/livefeeds`` instead to get a list of editorial livefeeds.

        Args:
            country: Returns only livefeeds that are available for distribution in a certain country
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_editorial_livefeed_list(
                country, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_updated_editorial_image(
        self,
        type_: Type15OrStr,
        date_updated_start: RFC3339DateTime,
        date_updated_end: RFC3339DateTime,
        country: str,
        *,
        date_taken_start: Date | None = None,
        date_taken_end: Date | None = None,
        cursor: str | None = None,
        sort: Sort5OrStr | None = None,
        supplier_code: list[str] | None = None,
        per_page: int | None = 500,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialUpdatedResults:
        """Deprecated; use ``GET /v2/editorial/images/updated`` instead to get recently updated items.

        Args:
            type_: Specify ``addition`` to return only images that were added or ``edit`` to return only images that
                were edited or deleted
            date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            country: Show only editorial content that is available for distribution in a certain country
            date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want
                recently created images from the collection instead of updated older assets
            date_taken_end: Show images that were taken before the specified date
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            sort: Sort by
            supplier_code: Show only editorial content from certain suppliers
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_updated_editorial_image(
                type_,
                date_updated_start,
                date_updated_end,
                country,
                date_taken_start=date_taken_start,
                date_taken_end=date_taken_end,
                cursor=cursor,
                sort=sort,
                supplier_code=supplier_code,
                per_page=per_page,
                request_options=request_options,
            )
        ).unwrap()

    async def get_updated_editorial_images(
        self,
        type_: Type15OrStr,
        date_updated_start: RFC3339DateTime,
        date_updated_end: RFC3339DateTime,
        country: str,
        *,
        date_taken_start: Date | None = None,
        date_taken_end: Date | None = None,
        cursor: str | None = None,
        sort: Sort5OrStr | None = None,
        supplier_code: list[str] | None = None,
        per_page: int | None = 500,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialUpdatedResults:
        """This endpoint lists editorial images that have been updated in the specified time period to update content
        management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start
        and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use
        the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was
        taken.

        Args:
            type_: Specify ``addition`` to return only images that were added or ``edit`` to return only images that
                were edited or deleted
            date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            country: Show only editorial content that is available for distribution in a certain country
            date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want
                recently created images from the collection instead of updated older assets
            date_taken_end: Show images that were taken before the specified date
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            sort: Sort by
            supplier_code: Show only editorial content from certain suppliers
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_updated_editorial_images(
                type_,
                date_updated_start,
                date_updated_end,
                country,
                date_taken_start=date_taken_start,
                date_taken_end=date_taken_end,
                cursor=cursor,
                sort=sort,
                supplier_code=supplier_code,
                per_page=per_page,
                request_options=request_options,
            )
        ).unwrap()

    async def license_editorial_image(
        self,
        body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseEditorialContentResults:
        """Deprecated; use ``POST /v2/editorial/images/licenses`` instead to get licenses for one or more editorial
        images. You must specify the country and one or more editorial images to license. The download links in the
        response are valid for 8 hours.

        Args:
            body: License editorial content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (await self._with_raw_response.license_editorial_image(body, request_options=request_options)).unwrap()

    async def license_editorial_images(
        self,
        body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseEditorialContentResults:
        """This endpoint gets licenses for one or more editorial images. You must specify the country and one or more
        editorial images to license. The download links in the response are valid for 8 hours.

        Args:
            body: License editorial content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (await self._with_raw_response.license_editorial_images(body, request_options=request_options)).unwrap()

    async def list_editorial_image_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> EditorialImageCategoryResults:
        """This endpoint lists the categories that editorial images can belong to, which are separate from the
        categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_editorial_image_categories(request_options=request_options)).unwrap()

    async def list_editorial_images(
        self,
        id: list[str],
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialImageResults:
        """This endpoint lists the details of editorial images.

        Args:
            id: ID of the editorial image to list details for
            country: Show only editorial image content that is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_editorial_images(
                id, country, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def search_editorial(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialSearchResults:
        """Deprecated; use ``GET /v2/editorial/images/search`` instead to search for editorial images.

        Args:
            country: Show only editorial content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content within a certain editorial category; specify by category name
            supplier_code: Show only editorial content from certain suppliers
            date_start: Show only editorial content generated on or after a specific date
            date_end: Show only editorial content generated on or before a specific date
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_editorial(
                country,
                query=query,
                sort=sort,
                category=category,
                supplier_code=supplier_code,
                date_start=date_start,
                date_end=date_end,
                per_page=per_page,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def search_editorial_images(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EditorialSearchResults:
        """This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an
        AND condition. For example, if you set the ``category`` parameter to "Alone,Performing" and also specify a
        ``query`` parameter, the results include only images that match the query and are in both the Alone and
        Performing categories. You can also filter search terms out in the ``query`` parameter by prefixing the term
        with NOT.

        Args:
            country: Show only editorial content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content with each of the specified editorial categories; specify category names in
                a comma-separated list
            supplier_code: Show only editorial content from certain suppliers
            date_start: Show only editorial content generated on or after a specific date
            date_end: Show only editorial content generated on or before a specific date
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not Acceptable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_editorial_images(
                country,
                query=query,
                sort=sort,
                category=category,
                supplier_code=supplier_code,
                date_start=date_start,
                date_end=date_end,
                per_page=per_page,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEditorialImagesWithRawResponse:
        return self._with_raw_response


class EditorialImagesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_editorial_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialCategoryResults, GetEditorialCategoriesErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/categories`` instead. This endpoint lists the categories that
        editorial images can belong to, which are separate from the categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/categories"),
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialCategoryResults],
            error_mapper=get_editorial_categories_error_mapper,
            request_options=request_options,
        )

    def get_editorial_image(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialContent, GetEditorialImageErrorBody]:
        """This endpoint shows information about an editorial image, including a URL to a preview image and the sizes
        that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialContent],
            error_mapper=get_editorial_image_error_mapper,
            request_options=request_options,
        )

    def get_editorial_image2(
        self,
        id: str,
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialContent, GetEditorialImage2ErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/{id}`` instead to show information about an editorial image,
        including a URL to a preview image and the sizes that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country), param[str | None]("search_id", search_id)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialContent],
            error_mapper=get_editorial_image2_error_mapper,
            request_options=request_options,
        )

    def get_editorial_image_license_list(
        self,
        *,
        image_id: str | None = None,
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
    ) -> ApiResult[DownloadHistoryDataList, GetEditorialImageLicenseListErrorBody]:
        """This endpoint lists existing editorial image licenses.

        Args:
            image_id: Show licenses for the specified editorial image ID
            license: Show editorial images that are available with the specified license name
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
            url_template=self._server.default("/v2/editorial/images/licenses"),
            query_params=[
                param[str | None]("image_id", image_id),
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
            error_mapper=get_editorial_image_license_list_error_mapper,
            request_options=request_options,
        )

    def get_editorial_image_livefeed(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialImageLivefeed, GetEditorialImageLivefeedErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/livefeeds/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageLivefeed],
            error_mapper=get_editorial_image_livefeed_error_mapper,
            request_options=request_options,
        )

    def get_editorial_image_livefeed_items(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialContentDataList, GetEditorialImageLivefeedItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed items are available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/livefeeds/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialContentDataList],
            error_mapper=get_editorial_image_livefeed_items_error_mapper,
            request_options=request_options,
        )

    def get_editorial_image_livefeed_list(
        self,
        country: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialImageLivefeedList, GetEditorialImageLivefeedListErrorBody]:
        """Send a ``GET`` request.

        Args:
            country: Returns only livefeeds that are available for distribution in a certain country
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/livefeeds"),
            query_params=[
                param[str]("country", country), param[int | None]("page", page), param[int | None]("per_page", per_page)
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageLivefeedList],
            error_mapper=get_editorial_image_livefeed_list_error_mapper,
            request_options=request_options,
        )

    def get_editorial_livefeed(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialImageLivefeed, GetEditorialLivefeedErrorBody]:
        """Deprecated: use ``GET /v2/editorial/images/livefeeds/{id}`` instead to get an editorial livefeed.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/livefeeds/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageLivefeed],
            error_mapper=get_editorial_livefeed_error_mapper,
            request_options=request_options,
        )

    def get_editorial_livefeed_items(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialContentDataList, GetEditorialLivefeedItemsErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/livefeeds/{id}/items`` instead to get editorial livefeed items.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed items are available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/livefeeds/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialContentDataList],
            error_mapper=get_editorial_livefeed_items_error_mapper,
            request_options=request_options,
        )

    def get_editorial_livefeed_list(
        self,
        country: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialImageLivefeedList, GetEditorialLivefeedListErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/livefeeds`` instead to get a list of editorial livefeeds.

        Args:
            country: Returns only livefeeds that are available for distribution in a certain country
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/livefeeds"),
            query_params=[
                param[str]("country", country), param[int | None]("page", page), param[int | None]("per_page", per_page)
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageLivefeedList],
            error_mapper=get_editorial_livefeed_list_error_mapper,
            request_options=request_options,
        )

    def get_updated_editorial_image(
        self,
        type_: Type15OrStr,
        date_updated_start: RFC3339DateTime,
        date_updated_end: RFC3339DateTime,
        country: str,
        *,
        date_taken_start: Date | None = None,
        date_taken_end: Date | None = None,
        cursor: str | None = None,
        sort: Sort5OrStr | None = None,
        supplier_code: list[str] | None = None,
        per_page: int | None = 500,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialUpdatedResults, GetUpdatedEditorialImageErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/updated`` instead to get recently updated items.

        Args:
            type_: Specify ``addition`` to return only images that were added or ``edit`` to return only images that
                were edited or deleted
            date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            country: Show only editorial content that is available for distribution in a certain country
            date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want
                recently created images from the collection instead of updated older assets
            date_taken_end: Show images that were taken before the specified date
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            sort: Sort by
            supplier_code: Show only editorial content from certain suppliers
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/updated"),
            query_params=[
                param[Type15OrStr]("type", type_),
                param[RFC3339DateTime]("date_updated_start", date_updated_start),
                param[RFC3339DateTime]("date_updated_end", date_updated_end),
                param[str]("country", country),
                param[Date | None]("date_taken_start", date_taken_start),
                param[Date | None]("date_taken_end", date_taken_end),
                param[str | None]("cursor", cursor),
                param[Sort5OrStr | None]("sort", sort),
                param[list[str] | None]("supplier_code", supplier_code),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialUpdatedResults],
            error_mapper=get_updated_editorial_image_error_mapper,
            request_options=request_options,
        )

    def get_updated_editorial_images(
        self,
        type_: Type15OrStr,
        date_updated_start: RFC3339DateTime,
        date_updated_end: RFC3339DateTime,
        country: str,
        *,
        date_taken_start: Date | None = None,
        date_taken_end: Date | None = None,
        cursor: str | None = None,
        sort: Sort5OrStr | None = None,
        supplier_code: list[str] | None = None,
        per_page: int | None = 500,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialUpdatedResults, GetUpdatedEditorialImagesErrorBody]:
        """This endpoint lists editorial images that have been updated in the specified time period to update content
        management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start
        and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use
        the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was
        taken.

        Args:
            type_: Specify ``addition`` to return only images that were added or ``edit`` to return only images that
                were edited or deleted
            date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            country: Show only editorial content that is available for distribution in a certain country
            date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want
                recently created images from the collection instead of updated older assets
            date_taken_end: Show images that were taken before the specified date
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            sort: Sort by
            supplier_code: Show only editorial content from certain suppliers
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/updated"),
            query_params=[
                param[Type15OrStr]("type", type_),
                param[RFC3339DateTime]("date_updated_start", date_updated_start),
                param[RFC3339DateTime]("date_updated_end", date_updated_end),
                param[str]("country", country),
                param[Date | None]("date_taken_start", date_taken_start),
                param[Date | None]("date_taken_end", date_taken_end),
                param[str | None]("cursor", cursor),
                param[Sort5OrStr | None]("sort", sort),
                param[list[str] | None]("supplier_code", supplier_code),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialUpdatedResults],
            error_mapper=get_updated_editorial_images_error_mapper,
            request_options=request_options,
        )

    def license_editorial_image(
        self,
        body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialImageErrorBody]:
        """Deprecated; use ``POST /v2/editorial/images/licenses`` instead to get licenses for one or more editorial
        images. You must specify the country and one or more editorial images to license. The download links in the
        response are valid for 8 hours.

        Args:
            body: License editorial content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/editorial/licenses"),
            body=json_body[LicenseEditorialContentRequest | LicenseEditorialContentRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseEditorialContentResults],
            error_mapper=license_editorial_image_error_mapper,
            request_options=request_options,
        )

    def license_editorial_images(
        self,
        body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialImagesErrorBody]:
        """This endpoint gets licenses for one or more editorial images. You must specify the country and one or more
        editorial images to license. The download links in the response are valid for 8 hours.

        Args:
            body: License editorial content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/editorial/images/licenses"),
            body=json_body[LicenseEditorialContentRequest | LicenseEditorialContentRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseEditorialContentResults],
            error_mapper=license_editorial_images_error_mapper,
            request_options=request_options,
        )

    def list_editorial_image_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialImageCategoryResults, ListEditorialImageCategoriesErrorBody]:
        """This endpoint lists the categories that editorial images can belong to, which are separate from the
        categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/categories"),
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageCategoryResults],
            error_mapper=list_editorial_image_categories_error_mapper,
            request_options=request_options,
        )

    def list_editorial_images(
        self,
        id: list[str],
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialImageResults, ListEditorialImagesErrorBody]:
        """This endpoint lists the details of editorial images.

        Args:
            id: ID of the editorial image to list details for
            country: Show only editorial image content that is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images"),
            query_params=[
                param[list[str]]("id", id), param[str]("country", country), param[str | None]("search_id", search_id)
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageResults],
            error_mapper=list_editorial_images_error_mapper,
            request_options=request_options,
        )

    def search_editorial(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialSearchResults, SearchEditorialErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/search`` instead to search for editorial images.

        Args:
            country: Show only editorial content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content within a certain editorial category; specify by category name
            supplier_code: Show only editorial content from certain suppliers
            date_start: Show only editorial content generated on or after a specific date
            date_end: Show only editorial content generated on or before a specific date
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/search"),
            query_params=[
                param[str]("country", country),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
                param[str | None]("category", category),
                param[list[str] | None]("supplier_code", supplier_code),
                param[Date | None]("date_start", date_start),
                param[Date | None]("date_end", date_end),
                param[int | None]("per_page", per_page),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialSearchResults],
            error_mapper=search_editorial_error_mapper,
            request_options=request_options,
        )

    def search_editorial_images(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialSearchResults, SearchEditorialImagesErrorBody]:
        """This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an
        AND condition. For example, if you set the ``category`` parameter to "Alone,Performing" and also specify a
        ``query`` parameter, the results include only images that match the query and are in both the Alone and
        Performing categories. You can also filter search terms out in the ``query`` parameter by prefixing the term
        with NOT.

        Args:
            country: Show only editorial content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content with each of the specified editorial categories; specify category names in
                a comma-separated list
            supplier_code: Show only editorial content from certain suppliers
            date_start: Show only editorial content generated on or after a specific date
            date_end: Show only editorial content generated on or before a specific date
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/search"),
            query_params=[
                param[str]("country", country),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
                param[str | None]("category", category),
                param[list[str] | None]("supplier_code", supplier_code),
                param[Date | None]("date_start", date_start),
                param[Date | None]("date_end", date_end),
                param[int | None]("per_page", per_page),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialSearchResults],
            error_mapper=search_editorial_images_error_mapper,
            request_options=request_options,
        )


class AsyncEditorialImagesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_editorial_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialCategoryResults, GetEditorialCategoriesErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/categories`` instead. This endpoint lists the categories that
        editorial images can belong to, which are separate from the categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/categories"),
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialCategoryResults],
            error_mapper=get_editorial_categories_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_image(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialContent, GetEditorialImageErrorBody]:
        """This endpoint shows information about an editorial image, including a URL to a preview image and the sizes
        that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialContent],
            error_mapper=get_editorial_image_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_image2(
        self,
        id: str,
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialContent, GetEditorialImage2ErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/{id}`` instead to show information about an editorial image,
        including a URL to a preview image and the sizes that it is available in.

        Args:
            id: Editorial ID
            country: Returns only if the content is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country), param[str | None]("search_id", search_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialContent],
            error_mapper=get_editorial_image2_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_image_license_list(
        self,
        *,
        image_id: str | None = None,
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
    ) -> ApiResult[DownloadHistoryDataList, GetEditorialImageLicenseListErrorBody]:
        """This endpoint lists existing editorial image licenses.

        Args:
            image_id: Show licenses for the specified editorial image ID
            license: Show editorial images that are available with the specified license name
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
            url_template=self._server.default("/v2/editorial/images/licenses"),
            query_params=[
                param[str | None]("image_id", image_id),
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
            error_mapper=get_editorial_image_license_list_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_image_livefeed(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialImageLivefeed, GetEditorialImageLivefeedErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/livefeeds/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageLivefeed],
            error_mapper=get_editorial_image_livefeed_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_image_livefeed_items(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialContentDataList, GetEditorialImageLivefeedItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed items are available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/livefeeds/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialContentDataList],
            error_mapper=get_editorial_image_livefeed_items_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_image_livefeed_list(
        self,
        country: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialImageLivefeedList, GetEditorialImageLivefeedListErrorBody]:
        """Send a ``GET`` request.

        Args:
            country: Returns only livefeeds that are available for distribution in a certain country
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/livefeeds"),
            query_params=[
                param[str]("country", country), param[int | None]("page", page), param[int | None]("per_page", per_page)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageLivefeedList],
            error_mapper=get_editorial_image_livefeed_list_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_livefeed(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialImageLivefeed, GetEditorialLivefeedErrorBody]:
        """Deprecated: use ``GET /v2/editorial/images/livefeeds/{id}`` instead to get an editorial livefeed.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed is available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/livefeeds/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageLivefeed],
            error_mapper=get_editorial_livefeed_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_livefeed_items(
        self, id: str, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialContentDataList, GetEditorialLivefeedItemsErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/livefeeds/{id}/items`` instead to get editorial livefeed items.

        Args:
            id: Editorial livefeed ID; must be an URI encoded string
            country: Returns only if the livefeed items are available for distribution in a certain country
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/livefeeds/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("country", country)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialContentDataList],
            error_mapper=get_editorial_livefeed_items_error_mapper,
            request_options=request_options,
        )

    async def get_editorial_livefeed_list(
        self,
        country: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialImageLivefeedList, GetEditorialLivefeedListErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/livefeeds`` instead to get a list of editorial livefeeds.

        Args:
            country: Returns only livefeeds that are available for distribution in a certain country
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/livefeeds"),
            query_params=[
                param[str]("country", country), param[int | None]("page", page), param[int | None]("per_page", per_page)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageLivefeedList],
            error_mapper=get_editorial_livefeed_list_error_mapper,
            request_options=request_options,
        )

    async def get_updated_editorial_image(
        self,
        type_: Type15OrStr,
        date_updated_start: RFC3339DateTime,
        date_updated_end: RFC3339DateTime,
        country: str,
        *,
        date_taken_start: Date | None = None,
        date_taken_end: Date | None = None,
        cursor: str | None = None,
        sort: Sort5OrStr | None = None,
        supplier_code: list[str] | None = None,
        per_page: int | None = 500,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialUpdatedResults, GetUpdatedEditorialImageErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/updated`` instead to get recently updated items.

        Args:
            type_: Specify ``addition`` to return only images that were added or ``edit`` to return only images that
                were edited or deleted
            date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            country: Show only editorial content that is available for distribution in a certain country
            date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want
                recently created images from the collection instead of updated older assets
            date_taken_end: Show images that were taken before the specified date
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            sort: Sort by
            supplier_code: Show only editorial content from certain suppliers
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/updated"),
            query_params=[
                param[Type15OrStr]("type", type_),
                param[RFC3339DateTime]("date_updated_start", date_updated_start),
                param[RFC3339DateTime]("date_updated_end", date_updated_end),
                param[str]("country", country),
                param[Date | None]("date_taken_start", date_taken_start),
                param[Date | None]("date_taken_end", date_taken_end),
                param[str | None]("cursor", cursor),
                param[Sort5OrStr | None]("sort", sort),
                param[list[str] | None]("supplier_code", supplier_code),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialUpdatedResults],
            error_mapper=get_updated_editorial_image_error_mapper,
            request_options=request_options,
        )

    async def get_updated_editorial_images(
        self,
        type_: Type15OrStr,
        date_updated_start: RFC3339DateTime,
        date_updated_end: RFC3339DateTime,
        country: str,
        *,
        date_taken_start: Date | None = None,
        date_taken_end: Date | None = None,
        cursor: str | None = None,
        sort: Sort5OrStr | None = None,
        supplier_code: list[str] | None = None,
        per_page: int | None = 500,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialUpdatedResults, GetUpdatedEditorialImagesErrorBody]:
        """This endpoint lists editorial images that have been updated in the specified time period to update content
        management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start
        and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use
        the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was
        taken.

        Args:
            type_: Specify ``addition`` to return only images that were added or ``edit`` to return only images that
                were edited or deleted
            date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range
                is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
            country: Show only editorial content that is available for distribution in a certain country
            date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want
                recently created images from the collection instead of updated older assets
            date_taken_end: Show images that were taken before the specified date
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            sort: Sort by
            supplier_code: Show only editorial content from certain suppliers
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/updated"),
            query_params=[
                param[Type15OrStr]("type", type_),
                param[RFC3339DateTime]("date_updated_start", date_updated_start),
                param[RFC3339DateTime]("date_updated_end", date_updated_end),
                param[str]("country", country),
                param[Date | None]("date_taken_start", date_taken_start),
                param[Date | None]("date_taken_end", date_taken_end),
                param[str | None]("cursor", cursor),
                param[Sort5OrStr | None]("sort", sort),
                param[list[str] | None]("supplier_code", supplier_code),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialUpdatedResults],
            error_mapper=get_updated_editorial_images_error_mapper,
            request_options=request_options,
        )

    async def license_editorial_image(
        self,
        body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialImageErrorBody]:
        """Deprecated; use ``POST /v2/editorial/images/licenses`` instead to get licenses for one or more editorial
        images. You must specify the country and one or more editorial images to license. The download links in the
        response are valid for 8 hours.

        Args:
            body: License editorial content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/editorial/licenses"),
            body=json_body[LicenseEditorialContentRequest | LicenseEditorialContentRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseEditorialContentResults],
            error_mapper=license_editorial_image_error_mapper,
            request_options=request_options,
        )

    async def license_editorial_images(
        self,
        body: LicenseEditorialContentRequest | LicenseEditorialContentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseEditorialContentResults, LicenseEditorialImagesErrorBody]:
        """This endpoint gets licenses for one or more editorial images. You must specify the country and one or more
        editorial images to license. The download links in the response are valid for 8 hours.

        Args:
            body: License editorial content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/editorial/images/licenses"),
            body=json_body[LicenseEditorialContentRequest | LicenseEditorialContentRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseEditorialContentResults],
            error_mapper=license_editorial_images_error_mapper,
            request_options=request_options,
        )

    async def list_editorial_image_categories(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EditorialImageCategoryResults, ListEditorialImageCategoriesErrorBody]:
        """This endpoint lists the categories that editorial images can belong to, which are separate from the
        categories that other types of assets can belong to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/categories"),
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageCategoryResults],
            error_mapper=list_editorial_image_categories_error_mapper,
            request_options=request_options,
        )

    async def list_editorial_images(
        self,
        id: list[str],
        country: str,
        *,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialImageResults, ListEditorialImagesErrorBody]:
        """This endpoint lists the details of editorial images.

        Args:
            id: ID of the editorial image to list details for
            country: Show only editorial image content that is available for distribution in a certain country
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images"),
            query_params=[
                param[list[str]]("id", id), param[str]("country", country), param[str | None]("search_id", search_id)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialImageResults],
            error_mapper=list_editorial_images_error_mapper,
            request_options=request_options,
        )

    async def search_editorial(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialSearchResults, SearchEditorialErrorBody]:
        """Deprecated; use ``GET /v2/editorial/images/search`` instead to search for editorial images.

        Args:
            country: Show only editorial content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content within a certain editorial category; specify by category name
            supplier_code: Show only editorial content from certain suppliers
            date_start: Show only editorial content generated on or after a specific date
            date_end: Show only editorial content generated on or before a specific date
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/search"),
            query_params=[
                param[str]("country", country),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
                param[str | None]("category", category),
                param[list[str] | None]("supplier_code", supplier_code),
                param[Date | None]("date_start", date_start),
                param[Date | None]("date_end", date_end),
                param[int | None]("per_page", per_page),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialSearchResults],
            error_mapper=search_editorial_error_mapper,
            request_options=request_options,
        )

    async def search_editorial_images(
        self,
        country: str,
        *,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        category: str | None = None,
        supplier_code: list[str] | None = None,
        date_start: Date | None = None,
        date_end: Date | None = None,
        per_page: int | None = 20,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EditorialSearchResults, SearchEditorialImagesErrorBody]:
        """This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an
        AND condition. For example, if you set the ``category`` parameter to "Alone,Performing" and also specify a
        ``query`` parameter, the results include only images that match the query and are in both the Alone and
        Performing categories. You can also filter search terms out in the ``query`` parameter by prefixing the term
        with NOT.

        Args:
            country: Show only editorial content that is available for distribution in a certain country
            query: One or more search terms separated by spaces
            sort: Sort by
            category: Show editorial content with each of the specified editorial categories; specify category names in
                a comma-separated list
            supplier_code: Show only editorial content from certain suppliers
            date_start: Show only editorial content generated on or after a specific date
            date_end: Show only editorial content generated on or before a specific date
            per_page: Number of results per page
            cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous
                requests
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/editorial/images/search"),
            query_params=[
                param[str]("country", country),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
                param[str | None]("category", category),
                param[list[str] | None]("supplier_code", supplier_code),
                param[Date | None]("date_start", date_start),
                param[Date | None]("date_end", date_end),
                param[int | None]("per_page", per_page),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[EditorialSearchResults],
            error_mapper=search_editorial_images_error_mapper,
            request_options=request_options,
        )
