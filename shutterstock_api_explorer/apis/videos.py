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
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.add_video_collection_items_error import (
    AddVideoCollectionItemsErrorBody,
    add_video_collection_items_error_mapper,
)
from ..errors.create_video_collection_error import CreateVideoCollectionErrorBody, create_video_collection_error_mapper
from ..errors.delete_video_collection_error import DeleteVideoCollectionErrorBody, delete_video_collection_error_mapper
from ..errors.delete_video_collection_items_error import (
    DeleteVideoCollectionItemsErrorBody,
    delete_video_collection_items_error_mapper,
)
from ..errors.download_videos_error import DownloadVideosErrorBody, download_videos_error_mapper
from ..errors.find_similar_videos_error import FindSimilarVideosErrorBody, find_similar_videos_error_mapper
from ..errors.get_video_collection_error import GetVideoCollectionErrorBody, get_video_collection_error_mapper
from ..errors.get_video_collection_items_error import (
    GetVideoCollectionItemsErrorBody,
    get_video_collection_items_error_mapper,
)
from ..errors.get_video_collection_list_error import (
    GetVideoCollectionListErrorBody,
    get_video_collection_list_error_mapper,
)
from ..errors.get_video_error import GetVideoErrorBody, get_video_error_mapper
from ..errors.get_video_license_list_error import GetVideoLicenseListErrorBody, get_video_license_list_error_mapper
from ..errors.get_video_list_error import GetVideoListErrorBody, get_video_list_error_mapper
from ..errors.get_video_suggestions_error import GetVideoSuggestionsErrorBody, get_video_suggestions_error_mapper
from ..errors.license_videos_error import LicenseVideosErrorBody, license_videos_error_mapper
from ..errors.list_video_categories_error import ListVideoCategoriesErrorBody, list_video_categories_error_mapper
from ..errors.rename_video_collection_error import RenameVideoCollectionErrorBody, rename_video_collection_error_mapper
from ..errors.search_videos_error import SearchVideosErrorBody, search_videos_error_mapper
from ..models.category_data_list import CategoryDataList
from ..models.collection import Collection
from ..models.collection_create_request import CollectionCreateRequest, CollectionCreateRequestDict
from ..models.collection_create_response import CollectionCreateResponse
from ..models.collection_data_list import CollectionDataList
from ..models.collection_item_data_list import CollectionItemDataList
from ..models.collection_item_request import CollectionItemRequest, CollectionItemRequestDict
from ..models.collection_update_request import CollectionUpdateRequest, CollectionUpdateRequestDict
from ..models.download_history_data_list import DownloadHistoryDataList
from ..models.enums.aspect_ratio import AspectRatioOrStr
from ..models.enums.download_availability import DownloadAvailabilityOrStr
from ..models.enums.embed import EmbedOrStr
from ..models.enums.language import LanguageOrStr
from ..models.enums.license9 import License9OrStr
from ..models.enums.orientation2 import Orientation2OrStr
from ..models.enums.people_age2 import PeopleAge2OrStr
from ..models.enums.people_ethnicity5 import PeopleEthnicity5OrStr
from ..models.enums.people_gender2 import PeopleGender2OrStr
from ..models.enums.resolution import ResolutionOrStr
from ..models.enums.size16 import Size16OrStr
from ..models.enums.sort2 import Sort2OrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.enums.view2 import View2OrStr
from ..models.license_video_request import LicenseVideoRequest, LicenseVideoRequestDict
from ..models.license_video_result_data_list import LicenseVideoResultDataList
from ..models.redownload_video import RedownloadVideo, RedownloadVideoDict
from ..models.suggestions import Suggestions
from ..models.updated_media_data_list import UpdatedMediaDataList
from ..models.url import Url
from ..models.video import Video
from ..models.video_data_list import VideoDataList
from ..models.video_search_results import VideoSearchResults
from ..server.server import Server


class Videos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosWithRawResponse(client, server, auth)

    def add_video_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint adds one or more videos to a collection by video IDs.

        Args:
            id: The ID of the collection to which items should be added
            body: Array of video IDs to add to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully added collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.add_video_collection_items(id, body, request_options=request_options).unwrap()

    def create_video_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionCreateResponse:
        """This endpoint creates one or more collections (clipboxes). To add videos to collections, use ``POST
        /v2/videos/collections/{id}/items``.

        Args:
            body: Collection metadata
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully created video collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.create_video_collection(body, request_options=request_options).unwrap()

    def delete_video_collection(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This endpoint deletes a collection.

        Args:
            id: The ID of the collection to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully deleted collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_video_collection(id, request_options=request_options).unwrap()

    def delete_video_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint removes one or more videos from a collection.

        Args:
            id: The ID of the Collection from which items will be deleted
            item_id: One or more video IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully removed collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_video_collection_items(
            id, item_id=item_id, request_options=request_options
        ).unwrap()

    def download_videos(
        self,
        id: str,
        body: RedownloadVideo | RedownloadVideoDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Url:
        """This endpoint redownloads videos that you have already received a license for.

        Args:
            id: The license ID of the item to (re)download. The download links in the response are valid for 8 hours.
            body: Information about the videos to redownload
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.download_videos(id, body, request_options=request_options).unwrap()

    def find_similar_videos(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoSearchResults:
        """This endpoint searches for videos that are similar to a video that you specify.

        Args:
            id: The ID of a video for which similar videos should be returned
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.find_similar_videos(
            id, language=language, page=page, per_page=per_page, view=view, request_options=request_options
        ).unwrap()

    def get_updated_videos(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str | None = "1 HOUR",
        page: int | None = 1,
        per_page: int | None = 100,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatedMediaDataList:
        """This endpoint lists videos that have been updated in the specified time period to update content management
        systems (CMS) or digital asset management (DAM) systems. In most cases, use the ``interval`` parameter to show
        videos that were updated recently, but you can also use the ``start_date`` and ``end_date`` parameters to
        specify a range of no more than three days. Do not use the ``interval`` parameter with either ``start_date`` or
        ``end_date``.

        Args:
            start_date: Show videos updated on or after the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency.
            end_date: Show videos updated before the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency. Please note that the end date must be at least 5
                minutes after the start date.
            interval: Show videos updated in the specified time period, where the time period is an interval (like SQL
                INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were
                updated in the hour preceding the request
            page: Page number
            per_page: Number of results per page
            sort: Sort by oldest or newest videos first
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_updated_videos(
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            page=page,
            per_page=per_page,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_video(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This endpoint shows information about a video, including URLs to previews and the sizes that it is available
        in.

        Args:
            id: Video ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_video(
            id, language=language, view=view, search_id=search_id, request_options=request_options
        ).unwrap()

    def get_video_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Collection:
        """This endpoint gets more detailed information about a collection, including the timestamp for its creation and
        the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

        Args:
            id: The ID of the collection to return
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_collection(
            id, embed=embed, share_code=share_code, request_options=request_options
        ).unwrap()

    def get_video_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionItemDataList:
        """This endpoint lists the IDs of videos in a collection and the date that each was added.

        Args:
            id: Collection ID
            page: Page number
            per_page: Number of results per page
            share_code: Code to retrieve the contents of a shared collection
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_collection_items(
            id, page=page, per_page=per_page, share_code=share_code, sort=sort, request_options=request_options
        ).unwrap()

    def get_video_collection_list(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        embed: list[EmbedOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionDataList:
        """This endpoint lists your collections of videos and their basic attributes.

        Args:
            page: Page number
            per_page: Number of results per page
            embed: Which sharing information to include in the response, such as a URL to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_collection_list(
            page=page, per_page=per_page, embed=embed, request_options=request_options
        ).unwrap()

    def get_video_license_list(
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
        """This endpoint lists existing licenses.

        Args:
            video_id: Show licenses for the specified video ID
            license: Show videos that are available with the specified license, such as ``standard`` or ``enhanced``
            page: Page number
            per_page: Number of results per page
            sort: Sort by oldest or newest videos first
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
        return self._with_raw_response.get_video_license_list(
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

    def get_video_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoDataList:
        """This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

        Args:
            id: One or more video IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_list(
            id, view=view, search_id=search_id, request_options=request_options
        ).unwrap()

    def get_video_suggestions(
        self, query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None
    ) -> Suggestions:
        """This endpoint provides autocomplete suggestions for partial search terms.

        Args:
            query: Search term for which you want keyword suggestions
            limit: Limit the number of the suggestions
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_suggestions(
            query, limit=limit, request_options=request_options
        ).unwrap()

    def license_videos(
        self,
        body: LicenseVideoRequest | LicenseVideoRequestDict,
        *,
        subscription_id: str | None = None,
        size: Size16OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseVideoResultDataList:
        """This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and
        the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values
        in the body parameter override values in the query parameters. The download links in the response are valid for
        8 hours.

        Args:
            body: List of videos to request licenses for and information about each license transaction; these values
                override the defaults in the query parameters
            subscription_id: The subscription ID to use for licensing
            size: The size of the video to license
            search_id: The Search ID that led to this licensing event
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.license_videos(
            body, subscription_id=subscription_id, size=size, search_id=search_id, request_options=request_options
        ).unwrap()

    def list_video_categories(
        self, *, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CategoryDataList:
        """This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

        Args:
            language: Language for the keywords and categories in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.list_video_categories(
            language=language, request_options=request_options
        ).unwrap()

    def rename_video_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint sets a new name for a collection.

        Args:
            id: The ID of the collection to rename
            body: The new name for the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully updated collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.rename_video_collection(id, body, request_options=request_options).unwrap()

    def search_videos(
        self,
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        added_date_end: Date | None = None,
        aspect_ratio: AspectRatioOrStr | None = None,
        category: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: list[str] | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        fps: float | None = None,
        fps_from: float | None = None,
        fps_to: float | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[License9OrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity5OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        people_model_released: bool | None = None,
        query: str | None = None,
        resolution: ResolutionOrStr | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoSearchResults:
        """This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter. You can also filter search terms out in the ``query``
        parameter by prefixing the term with NOT.

        Args:
            added_date: Show videos added on the specified date
            added_date_start: Show videos added on or after the specified date
            added_date_end: Show videos added before the specified date
            aspect_ratio: Show videos with the specified aspect ratio
            category: Show videos with the specified Shutterstock-defined category; specify a category name or ID
            contributor: Show videos with the specified artist names or IDs
            contributor_country: Show videos from contributors in one or more specified countries
            duration: (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in
                seconds
            duration_from: Show videos with the specified duration or longer in seconds
            duration_to: Show videos with the specified duration or shorter in seconds
            fps: (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second
            fps_from: Show videos with the specified frames per second or more
            fps_to: Show videos with the specified frames per second or fewer
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only videos with the specified license or licenses
            model: Show videos with each of the specified models
            orientation: Search for videos in a specific orientation
            page: Page number
            per_page: Number of results per page
            people_age: Show videos that feature people of the specified age range
            people_ethnicity: Show videos with people of the specified ethnicities
            people_gender: Show videos with people with the specified gender
            people_number: Show videos with the specified number of people
            people_model_released: Show only videos of people with a signed model release
            query: One or more search terms separated by spaces; you can use NOT to filter out videos that match a term
            resolution: Show videos with the specified resolution
            safe: Enable or disable safe search
            sort: Sort by one of these categories
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not found ``error`` is ``RawError``."""
        return self._with_raw_response.search_videos(
            added_date=added_date,
            added_date_start=added_date_start,
            added_date_end=added_date_end,
            aspect_ratio=aspect_ratio,
            category=category,
            contributor=contributor,
            contributor_country=contributor_country,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            fps=fps,
            fps_from=fps_from,
            fps_to=fps_to,
            keyword_safe_search=keyword_safe_search,
            language=language,
            license=license,
            model=model,
            orientation=orientation,
            page=page,
            per_page=per_page,
            people_age=people_age,
            people_ethnicity=people_ethnicity,
            people_gender=people_gender,
            people_number=people_number,
            people_model_released=people_model_released,
            query=query,
            resolution=resolution,
            safe=safe,
            sort=sort,
            view=view,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosWithRawResponse:
        return self._with_raw_response


class AsyncVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosWithRawResponse(client, server, auth)

    async def add_video_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint adds one or more videos to a collection by video IDs.

        Args:
            id: The ID of the collection to which items should be added
            body: Array of video IDs to add to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully added collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_video_collection_items(id, body, request_options=request_options)
        ).unwrap()

    async def create_video_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionCreateResponse:
        """This endpoint creates one or more collections (clipboxes). To add videos to collections, use ``POST
        /v2/videos/collections/{id}/items``.

        Args:
            body: Collection metadata
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully created video collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_video_collection(body, request_options=request_options)).unwrap()

    async def delete_video_collection(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This endpoint deletes a collection.

        Args:
            id: The ID of the collection to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully deleted collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_video_collection(id, request_options=request_options)).unwrap()

    async def delete_video_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint removes one or more videos from a collection.

        Args:
            id: The ID of the Collection from which items will be deleted
            item_id: One or more video IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully removed collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_video_collection_items(
                id, item_id=item_id, request_options=request_options
            )
        ).unwrap()

    async def download_videos(
        self,
        id: str,
        body: RedownloadVideo | RedownloadVideoDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Url:
        """This endpoint redownloads videos that you have already received a license for.

        Args:
            id: The license ID of the item to (re)download. The download links in the response are valid for 8 hours.
            body: Information about the videos to redownload
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.download_videos(id, body, request_options=request_options)).unwrap()

    async def find_similar_videos(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoSearchResults:
        """This endpoint searches for videos that are similar to a video that you specify.

        Args:
            id: The ID of a video for which similar videos should be returned
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.find_similar_videos(
                id, language=language, page=page, per_page=per_page, view=view, request_options=request_options
            )
        ).unwrap()

    async def get_updated_videos(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str | None = "1 HOUR",
        page: int | None = 1,
        per_page: int | None = 100,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatedMediaDataList:
        """This endpoint lists videos that have been updated in the specified time period to update content management
        systems (CMS) or digital asset management (DAM) systems. In most cases, use the ``interval`` parameter to show
        videos that were updated recently, but you can also use the ``start_date`` and ``end_date`` parameters to
        specify a range of no more than three days. Do not use the ``interval`` parameter with either ``start_date`` or
        ``end_date``.

        Args:
            start_date: Show videos updated on or after the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency.
            end_date: Show videos updated before the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency. Please note that the end date must be at least 5
                minutes after the start date.
            interval: Show videos updated in the specified time period, where the time period is an interval (like SQL
                INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were
                updated in the hour preceding the request
            page: Page number
            per_page: Number of results per page
            sort: Sort by oldest or newest videos first
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_updated_videos(
                start_date=start_date,
                end_date=end_date,
                interval=interval,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_video(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This endpoint shows information about a video, including URLs to previews and the sizes that it is available
        in.

        Args:
            id: Video ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video(
                id, language=language, view=view, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def get_video_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Collection:
        """This endpoint gets more detailed information about a collection, including the timestamp for its creation and
        the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

        Args:
            id: The ID of the collection to return
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_collection(
                id, embed=embed, share_code=share_code, request_options=request_options
            )
        ).unwrap()

    async def get_video_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionItemDataList:
        """This endpoint lists the IDs of videos in a collection and the date that each was added.

        Args:
            id: Collection ID
            page: Page number
            per_page: Number of results per page
            share_code: Code to retrieve the contents of a shared collection
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_collection_items(
                id, page=page, per_page=per_page, share_code=share_code, sort=sort, request_options=request_options
            )
        ).unwrap()

    async def get_video_collection_list(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        embed: list[EmbedOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionDataList:
        """This endpoint lists your collections of videos and their basic attributes.

        Args:
            page: Page number
            per_page: Number of results per page
            embed: Which sharing information to include in the response, such as a URL to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_collection_list(
                page=page, per_page=per_page, embed=embed, request_options=request_options
            )
        ).unwrap()

    async def get_video_license_list(
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
        """This endpoint lists existing licenses.

        Args:
            video_id: Show licenses for the specified video ID
            license: Show videos that are available with the specified license, such as ``standard`` or ``enhanced``
            page: Page number
            per_page: Number of results per page
            sort: Sort by oldest or newest videos first
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
            await self._with_raw_response.get_video_license_list(
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

    async def get_video_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoDataList:
        """This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

        Args:
            id: One or more video IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_list(
                id, view=view, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def get_video_suggestions(
        self, query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None
    ) -> Suggestions:
        """This endpoint provides autocomplete suggestions for partial search terms.

        Args:
            query: Search term for which you want keyword suggestions
            limit: Limit the number of the suggestions
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_suggestions(query, limit=limit, request_options=request_options)
        ).unwrap()

    async def license_videos(
        self,
        body: LicenseVideoRequest | LicenseVideoRequestDict,
        *,
        subscription_id: str | None = None,
        size: Size16OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseVideoResultDataList:
        """This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and
        the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values
        in the body parameter override values in the query parameters. The download links in the response are valid for
        8 hours.

        Args:
            body: List of videos to request licenses for and information about each license transaction; these values
                override the defaults in the query parameters
            subscription_id: The subscription ID to use for licensing
            size: The size of the video to license
            search_id: The Search ID that led to this licensing event
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.license_videos(
                body, subscription_id=subscription_id, size=size, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def list_video_categories(
        self, *, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CategoryDataList:
        """This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

        Args:
            language: Language for the keywords and categories in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_video_categories(language=language, request_options=request_options)
        ).unwrap()

    async def rename_video_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint sets a new name for a collection.

        Args:
            id: The ID of the collection to rename
            body: The new name for the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully updated collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.rename_video_collection(id, body, request_options=request_options)
        ).unwrap()

    async def search_videos(
        self,
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        added_date_end: Date | None = None,
        aspect_ratio: AspectRatioOrStr | None = None,
        category: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: list[str] | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        fps: float | None = None,
        fps_from: float | None = None,
        fps_to: float | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[License9OrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity5OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        people_model_released: bool | None = None,
        query: str | None = None,
        resolution: ResolutionOrStr | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoSearchResults:
        """This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter. You can also filter search terms out in the ``query``
        parameter by prefixing the term with NOT.

        Args:
            added_date: Show videos added on the specified date
            added_date_start: Show videos added on or after the specified date
            added_date_end: Show videos added before the specified date
            aspect_ratio: Show videos with the specified aspect ratio
            category: Show videos with the specified Shutterstock-defined category; specify a category name or ID
            contributor: Show videos with the specified artist names or IDs
            contributor_country: Show videos from contributors in one or more specified countries
            duration: (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in
                seconds
            duration_from: Show videos with the specified duration or longer in seconds
            duration_to: Show videos with the specified duration or shorter in seconds
            fps: (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second
            fps_from: Show videos with the specified frames per second or more
            fps_to: Show videos with the specified frames per second or fewer
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only videos with the specified license or licenses
            model: Show videos with each of the specified models
            orientation: Search for videos in a specific orientation
            page: Page number
            per_page: Number of results per page
            people_age: Show videos that feature people of the specified age range
            people_ethnicity: Show videos with people of the specified ethnicities
            people_gender: Show videos with people with the specified gender
            people_number: Show videos with the specified number of people
            people_model_released: Show only videos of people with a signed model release
            query: One or more search terms separated by spaces; you can use NOT to filter out videos that match a term
            resolution: Show videos with the specified resolution
            safe: Enable or disable safe search
            sort: Sort by one of these categories
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_videos(
                added_date=added_date,
                added_date_start=added_date_start,
                added_date_end=added_date_end,
                aspect_ratio=aspect_ratio,
                category=category,
                contributor=contributor,
                contributor_country=contributor_country,
                duration=duration,
                duration_from=duration_from,
                duration_to=duration_to,
                fps=fps,
                fps_from=fps_from,
                fps_to=fps_to,
                keyword_safe_search=keyword_safe_search,
                language=language,
                license=license,
                model=model,
                orientation=orientation,
                page=page,
                per_page=per_page,
                people_age=people_age,
                people_ethnicity=people_ethnicity,
                people_gender=people_gender,
                people_number=people_number,
                people_model_released=people_model_released,
                query=query,
                resolution=resolution,
                safe=safe,
                sort=sort,
                view=view,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosWithRawResponse:
        return self._with_raw_response


class VideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideoCollectionItemsErrorBody]:
        """This endpoint adds one or more videos to a collection by video IDs.

        Args:
            id: The ID of the collection to which items should be added
            body: Array of video IDs to add to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionItemRequest | CollectionItemRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=add_video_collection_items_error_mapper,
            request_options=request_options,
        )

    def create_video_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionCreateResponse, CreateVideoCollectionErrorBody]:
        """This endpoint creates one or more collections (clipboxes). To add videos to collections, use ``POST
        /v2/videos/collections/{id}/items``.

        Args:
            body: Collection metadata
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/collections"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionCreateRequest | CollectionCreateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionCreateResponse],
            error_mapper=create_video_collection_error_mapper,
            request_options=request_options,
        )

    def delete_video_collection(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoCollectionErrorBody]:
        """This endpoint deletes a collection.

        Args:
            id: The ID of the collection to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/videos/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_video_collection_error_mapper,
            request_options=request_options,
        )

    def delete_video_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoCollectionItemsErrorBody]:
        """This endpoint removes one or more videos from a collection.

        Args:
            id: The ID of the Collection from which items will be deleted
            item_id: One or more video IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/videos/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[str] | None]("item_id", item_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_video_collection_items_error_mapper,
            request_options=request_options,
        )

    def download_videos(
        self,
        id: str,
        body: RedownloadVideo | RedownloadVideoDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Url, DownloadVideosErrorBody]:
        """This endpoint redownloads videos that you have already received a license for.

        Args:
            id: The license ID of the item to (re)download. The download links in the response are valid for 8 hours.
            body: Information about the videos to redownload
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/licenses/{id}/downloads"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RedownloadVideo | RedownloadVideoDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Url],
            error_mapper=download_videos_error_mapper,
            request_options=request_options,
        )

    def find_similar_videos(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoSearchResults, FindSimilarVideosErrorBody]:
        """This endpoint searches for videos that are similar to a video that you specify.

        Args:
            id: The ID of a video for which similar videos should be returned
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/{id}/similar"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[VideoSearchResults],
            error_mapper=find_similar_videos_error_mapper,
            request_options=request_options,
        )

    def get_updated_videos(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str | None = "1 HOUR",
        page: int | None = 1,
        per_page: int | None = 100,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatedMediaDataList, RawError]:
        """This endpoint lists videos that have been updated in the specified time period to update content management
        systems (CMS) or digital asset management (DAM) systems. In most cases, use the ``interval`` parameter to show
        videos that were updated recently, but you can also use the ``start_date`` and ``end_date`` parameters to
        specify a range of no more than three days. Do not use the ``interval`` parameter with either ``start_date`` or
        ``end_date``.

        Args:
            start_date: Show videos updated on or after the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency.
            end_date: Show videos updated before the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency. Please note that the end date must be at least 5
                minutes after the start date.
            interval: Show videos updated in the specified time period, where the time period is an interval (like SQL
                INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were
                updated in the hour preceding the request
            page: Page number
            per_page: Number of results per page
            sort: Sort by oldest or newest videos first
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/updated"),
            query_params=[
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("interval", interval),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[UpdatedMediaDataList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_video(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, GetVideoErrorBody]:
        """This endpoint shows information about a video, including URLs to previews and the sizes that it is available
        in.

        Args:
            id: Video ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Video],
            error_mapper=get_video_error_mapper,
            request_options=request_options,
        )

    def get_video_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Collection, GetVideoCollectionErrorBody]:
        """This endpoint gets more detailed information about a collection, including the timestamp for its creation and
        the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

        Args:
            id: The ID of the collection to return
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/collections/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[EmbedOrStr] | None]("embed", embed), param[str | None]("share_code", share_code)],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Collection],
            error_mapper=get_video_collection_error_mapper,
            request_options=request_options,
        )

    def get_video_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionItemDataList, GetVideoCollectionItemsErrorBody]:
        """This endpoint lists the IDs of videos in a collection and the date that each was added.

        Args:
            id: Collection ID
            page: Page number
            per_page: Number of results per page
            share_code: Code to retrieve the contents of a shared collection
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("share_code", share_code),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionItemDataList],
            error_mapper=get_video_collection_items_error_mapper,
            request_options=request_options,
        )

    def get_video_collection_list(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        embed: list[EmbedOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionDataList, GetVideoCollectionListErrorBody]:
        """This endpoint lists your collections of videos and their basic attributes.

        Args:
            page: Page number
            per_page: Number of results per page
            embed: Which sharing information to include in the response, such as a URL to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/collections"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[list[EmbedOrStr] | None]("embed", embed),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionDataList],
            error_mapper=get_video_collection_list_error_mapper,
            request_options=request_options,
        )

    def get_video_license_list(
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
    ) -> ApiResult[DownloadHistoryDataList, GetVideoLicenseListErrorBody]:
        """This endpoint lists existing licenses.

        Args:
            video_id: Show licenses for the specified video ID
            license: Show videos that are available with the specified license, such as ``standard`` or ``enhanced``
            page: Page number
            per_page: Number of results per page
            sort: Sort by oldest or newest videos first
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
            url_template=self._server.default("/v2/videos/licenses"),
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
            error_mapper=get_video_license_list_error_mapper,
            request_options=request_options,
        )

    def get_video_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoDataList, GetVideoListErrorBody]:
        """This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

        Args:
            id: One or more video IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos"),
            query_params=[
                param[list[str]]("id", id),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[VideoDataList],
            error_mapper=get_video_list_error_mapper,
            request_options=request_options,
        )

    def get_video_suggestions(
        self, query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Suggestions, GetVideoSuggestionsErrorBody]:
        """This endpoint provides autocomplete suggestions for partial search terms.

        Args:
            query: Search term for which you want keyword suggestions
            limit: Limit the number of the suggestions
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/search/suggestions"),
            query_params=[param[str]("query", query), param[int | None]("limit", limit)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Suggestions],
            error_mapper=get_video_suggestions_error_mapper,
            request_options=request_options,
        )

    def license_videos(
        self,
        body: LicenseVideoRequest | LicenseVideoRequestDict,
        *,
        subscription_id: str | None = None,
        size: Size16OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseVideoResultDataList, LicenseVideosErrorBody]:
        """This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and
        the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values
        in the body parameter override values in the query parameters. The download links in the response are valid for
        8 hours.

        Args:
            body: List of videos to request licenses for and information about each license transaction; these values
                override the defaults in the query parameters
            subscription_id: The subscription ID to use for licensing
            size: The size of the video to license
            search_id: The Search ID that led to this licensing event
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/licenses"),
            query_params=[
                param[str | None]("subscription_id", subscription_id),
                param[Size16OrStr | None]("size", size),
                param[str | None]("search_id", search_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseVideoRequest | LicenseVideoRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseVideoResultDataList],
            error_mapper=license_videos_error_mapper,
            request_options=request_options,
        )

    def list_video_categories(
        self, *, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoryDataList, ListVideoCategoriesErrorBody]:
        """This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

        Args:
            language: Language for the keywords and categories in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/categories"),
            query_params=[param[LanguageOrStr | None]("language", language)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[CategoryDataList],
            error_mapper=list_video_categories_error_mapper,
            request_options=request_options,
        )

    def rename_video_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RenameVideoCollectionErrorBody]:
        """This endpoint sets a new name for a collection.

        Args:
            id: The ID of the collection to rename
            body: The new name for the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionUpdateRequest | CollectionUpdateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=rename_video_collection_error_mapper,
            request_options=request_options,
        )

    def search_videos(
        self,
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        added_date_end: Date | None = None,
        aspect_ratio: AspectRatioOrStr | None = None,
        category: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: list[str] | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        fps: float | None = None,
        fps_from: float | None = None,
        fps_to: float | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[License9OrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity5OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        people_model_released: bool | None = None,
        query: str | None = None,
        resolution: ResolutionOrStr | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoSearchResults, SearchVideosErrorBody]:
        """This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter. You can also filter search terms out in the ``query``
        parameter by prefixing the term with NOT.

        Args:
            added_date: Show videos added on the specified date
            added_date_start: Show videos added on or after the specified date
            added_date_end: Show videos added before the specified date
            aspect_ratio: Show videos with the specified aspect ratio
            category: Show videos with the specified Shutterstock-defined category; specify a category name or ID
            contributor: Show videos with the specified artist names or IDs
            contributor_country: Show videos from contributors in one or more specified countries
            duration: (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in
                seconds
            duration_from: Show videos with the specified duration or longer in seconds
            duration_to: Show videos with the specified duration or shorter in seconds
            fps: (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second
            fps_from: Show videos with the specified frames per second or more
            fps_to: Show videos with the specified frames per second or fewer
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only videos with the specified license or licenses
            model: Show videos with each of the specified models
            orientation: Search for videos in a specific orientation
            page: Page number
            per_page: Number of results per page
            people_age: Show videos that feature people of the specified age range
            people_ethnicity: Show videos with people of the specified ethnicities
            people_gender: Show videos with people with the specified gender
            people_number: Show videos with the specified number of people
            people_model_released: Show only videos of people with a signed model release
            query: One or more search terms separated by spaces; you can use NOT to filter out videos that match a term
            resolution: Show videos with the specified resolution
            safe: Enable or disable safe search
            sort: Sort by one of these categories
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/search"),
            query_params=[
                param[Date | None]("added_date", added_date),
                param[Date | None]("added_date_start", added_date_start),
                param[Date | None]("added_date_end", added_date_end),
                param[AspectRatioOrStr | None]("aspect_ratio", aspect_ratio),
                param[str | None]("category", category),
                param[list[str] | None]("contributor", contributor),
                param[list[str] | None]("contributor_country", contributor_country),
                param[int | None]("duration", duration),
                param[int | None]("duration_from", duration_from),
                param[int | None]("duration_to", duration_to),
                param[float | None]("fps", fps),
                param[float | None]("fps_from", fps_from),
                param[float | None]("fps_to", fps_to),
                param[bool | None]("keyword_safe_search", keyword_safe_search),
                param[LanguageOrStr | None]("language", language),
                param[list[License9OrStr] | None]("license", license),
                param[list[str] | None]("model", model),
                param[Orientation2OrStr | None]("orientation", orientation),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[PeopleAge2OrStr | None]("people_age", people_age),
                param[list[PeopleEthnicity5OrStr] | None]("people_ethnicity", people_ethnicity),
                param[PeopleGender2OrStr | None]("people_gender", people_gender),
                param[int | None]("people_number", people_number),
                param[bool | None]("people_model_released", people_model_released),
                param[str | None]("query", query),
                param[ResolutionOrStr | None]("resolution", resolution),
                param[bool | None]("safe", safe),
                param[Sort2OrStr | None]("sort", sort),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[VideoSearchResults],
            error_mapper=search_videos_error_mapper,
            request_options=request_options,
        )


class AsyncVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideoCollectionItemsErrorBody]:
        """This endpoint adds one or more videos to a collection by video IDs.

        Args:
            id: The ID of the collection to which items should be added
            body: Array of video IDs to add to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionItemRequest | CollectionItemRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=add_video_collection_items_error_mapper,
            request_options=request_options,
        )

    async def create_video_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionCreateResponse, CreateVideoCollectionErrorBody]:
        """This endpoint creates one or more collections (clipboxes). To add videos to collections, use ``POST
        /v2/videos/collections/{id}/items``.

        Args:
            body: Collection metadata
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/collections"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionCreateRequest | CollectionCreateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionCreateResponse],
            error_mapper=create_video_collection_error_mapper,
            request_options=request_options,
        )

    async def delete_video_collection(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoCollectionErrorBody]:
        """This endpoint deletes a collection.

        Args:
            id: The ID of the collection to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/videos/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_video_collection_error_mapper,
            request_options=request_options,
        )

    async def delete_video_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoCollectionItemsErrorBody]:
        """This endpoint removes one or more videos from a collection.

        Args:
            id: The ID of the Collection from which items will be deleted
            item_id: One or more video IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/videos/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[str] | None]("item_id", item_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_video_collection_items_error_mapper,
            request_options=request_options,
        )

    async def download_videos(
        self,
        id: str,
        body: RedownloadVideo | RedownloadVideoDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Url, DownloadVideosErrorBody]:
        """This endpoint redownloads videos that you have already received a license for.

        Args:
            id: The license ID of the item to (re)download. The download links in the response are valid for 8 hours.
            body: Information about the videos to redownload
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/licenses/{id}/downloads"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RedownloadVideo | RedownloadVideoDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Url],
            error_mapper=download_videos_error_mapper,
            request_options=request_options,
        )

    async def find_similar_videos(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoSearchResults, FindSimilarVideosErrorBody]:
        """This endpoint searches for videos that are similar to a video that you specify.

        Args:
            id: The ID of a video for which similar videos should be returned
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/{id}/similar"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[VideoSearchResults],
            error_mapper=find_similar_videos_error_mapper,
            request_options=request_options,
        )

    async def get_updated_videos(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str | None = "1 HOUR",
        page: int | None = 1,
        per_page: int | None = 100,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatedMediaDataList, RawError]:
        """This endpoint lists videos that have been updated in the specified time period to update content management
        systems (CMS) or digital asset management (DAM) systems. In most cases, use the ``interval`` parameter to show
        videos that were updated recently, but you can also use the ``start_date`` and ``end_date`` parameters to
        specify a range of no more than three days. Do not use the ``interval`` parameter with either ``start_date`` or
        ``end_date``.

        Args:
            start_date: Show videos updated on or after the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency.
            end_date: Show videos updated before the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency. Please note that the end date must be at least 5
                minutes after the start date.
            interval: Show videos updated in the specified time period, where the time period is an interval (like SQL
                INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were
                updated in the hour preceding the request
            page: Page number
            per_page: Number of results per page
            sort: Sort by oldest or newest videos first
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/updated"),
            query_params=[
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("interval", interval),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[UpdatedMediaDataList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_video(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, GetVideoErrorBody]:
        """This endpoint shows information about a video, including URLs to previews and the sizes that it is available
        in.

        Args:
            id: Video ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Video],
            error_mapper=get_video_error_mapper,
            request_options=request_options,
        )

    async def get_video_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Collection, GetVideoCollectionErrorBody]:
        """This endpoint gets more detailed information about a collection, including the timestamp for its creation and
        the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

        Args:
            id: The ID of the collection to return
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/collections/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[EmbedOrStr] | None]("embed", embed), param[str | None]("share_code", share_code)],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Collection],
            error_mapper=get_video_collection_error_mapper,
            request_options=request_options,
        )

    async def get_video_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionItemDataList, GetVideoCollectionItemsErrorBody]:
        """This endpoint lists the IDs of videos in a collection and the date that each was added.

        Args:
            id: Collection ID
            page: Page number
            per_page: Number of results per page
            share_code: Code to retrieve the contents of a shared collection
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("share_code", share_code),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionItemDataList],
            error_mapper=get_video_collection_items_error_mapper,
            request_options=request_options,
        )

    async def get_video_collection_list(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        embed: list[EmbedOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionDataList, GetVideoCollectionListErrorBody]:
        """This endpoint lists your collections of videos and their basic attributes.

        Args:
            page: Page number
            per_page: Number of results per page
            embed: Which sharing information to include in the response, such as a URL to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/collections"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[list[EmbedOrStr] | None]("embed", embed),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionDataList],
            error_mapper=get_video_collection_list_error_mapper,
            request_options=request_options,
        )

    async def get_video_license_list(
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
    ) -> ApiResult[DownloadHistoryDataList, GetVideoLicenseListErrorBody]:
        """This endpoint lists existing licenses.

        Args:
            video_id: Show licenses for the specified video ID
            license: Show videos that are available with the specified license, such as ``standard`` or ``enhanced``
            page: Page number
            per_page: Number of results per page
            sort: Sort by oldest or newest videos first
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
            url_template=self._server.default("/v2/videos/licenses"),
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
            error_mapper=get_video_license_list_error_mapper,
            request_options=request_options,
        )

    async def get_video_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoDataList, GetVideoListErrorBody]:
        """This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

        Args:
            id: One or more video IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos"),
            query_params=[
                param[list[str]]("id", id),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[VideoDataList],
            error_mapper=get_video_list_error_mapper,
            request_options=request_options,
        )

    async def get_video_suggestions(
        self, query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Suggestions, GetVideoSuggestionsErrorBody]:
        """This endpoint provides autocomplete suggestions for partial search terms.

        Args:
            query: Search term for which you want keyword suggestions
            limit: Limit the number of the suggestions
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/search/suggestions"),
            query_params=[param[str]("query", query), param[int | None]("limit", limit)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Suggestions],
            error_mapper=get_video_suggestions_error_mapper,
            request_options=request_options,
        )

    async def license_videos(
        self,
        body: LicenseVideoRequest | LicenseVideoRequestDict,
        *,
        subscription_id: str | None = None,
        size: Size16OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseVideoResultDataList, LicenseVideosErrorBody]:
        """This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and
        the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values
        in the body parameter override values in the query parameters. The download links in the response are valid for
        8 hours.

        Args:
            body: List of videos to request licenses for and information about each license transaction; these values
                override the defaults in the query parameters
            subscription_id: The subscription ID to use for licensing
            size: The size of the video to license
            search_id: The Search ID that led to this licensing event
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/licenses"),
            query_params=[
                param[str | None]("subscription_id", subscription_id),
                param[Size16OrStr | None]("size", size),
                param[str | None]("search_id", search_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseVideoRequest | LicenseVideoRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseVideoResultDataList],
            error_mapper=license_videos_error_mapper,
            request_options=request_options,
        )

    async def list_video_categories(
        self, *, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoryDataList, ListVideoCategoriesErrorBody]:
        """This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

        Args:
            language: Language for the keywords and categories in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/categories"),
            query_params=[param[LanguageOrStr | None]("language", language)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[CategoryDataList],
            error_mapper=list_video_categories_error_mapper,
            request_options=request_options,
        )

    async def rename_video_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RenameVideoCollectionErrorBody]:
        """This endpoint sets a new name for a collection.

        Args:
            id: The ID of the collection to rename
            body: The new name for the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/videos/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionUpdateRequest | CollectionUpdateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=rename_video_collection_error_mapper,
            request_options=request_options,
        )

    async def search_videos(
        self,
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        added_date_end: Date | None = None,
        aspect_ratio: AspectRatioOrStr | None = None,
        category: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: list[str] | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        fps: float | None = None,
        fps_from: float | None = None,
        fps_to: float | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[License9OrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity5OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        people_model_released: bool | None = None,
        query: str | None = None,
        resolution: ResolutionOrStr | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoSearchResults, SearchVideosErrorBody]:
        """This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter. You can also filter search terms out in the ``query``
        parameter by prefixing the term with NOT.

        Args:
            added_date: Show videos added on the specified date
            added_date_start: Show videos added on or after the specified date
            added_date_end: Show videos added before the specified date
            aspect_ratio: Show videos with the specified aspect ratio
            category: Show videos with the specified Shutterstock-defined category; specify a category name or ID
            contributor: Show videos with the specified artist names or IDs
            contributor_country: Show videos from contributors in one or more specified countries
            duration: (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in
                seconds
            duration_from: Show videos with the specified duration or longer in seconds
            duration_to: Show videos with the specified duration or shorter in seconds
            fps: (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second
            fps_from: Show videos with the specified frames per second or more
            fps_to: Show videos with the specified frames per second or fewer
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only videos with the specified license or licenses
            model: Show videos with each of the specified models
            orientation: Search for videos in a specific orientation
            page: Page number
            per_page: Number of results per page
            people_age: Show videos that feature people of the specified age range
            people_ethnicity: Show videos with people of the specified ethnicities
            people_gender: Show videos with people with the specified gender
            people_number: Show videos with the specified number of people
            people_model_released: Show only videos of people with a signed model release
            query: One or more search terms separated by spaces; you can use NOT to filter out videos that match a term
            resolution: Show videos with the specified resolution
            safe: Enable or disable safe search
            sort: Sort by one of these categories
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/videos/search"),
            query_params=[
                param[Date | None]("added_date", added_date),
                param[Date | None]("added_date_start", added_date_start),
                param[Date | None]("added_date_end", added_date_end),
                param[AspectRatioOrStr | None]("aspect_ratio", aspect_ratio),
                param[str | None]("category", category),
                param[list[str] | None]("contributor", contributor),
                param[list[str] | None]("contributor_country", contributor_country),
                param[int | None]("duration", duration),
                param[int | None]("duration_from", duration_from),
                param[int | None]("duration_to", duration_to),
                param[float | None]("fps", fps),
                param[float | None]("fps_from", fps_from),
                param[float | None]("fps_to", fps_to),
                param[bool | None]("keyword_safe_search", keyword_safe_search),
                param[LanguageOrStr | None]("language", language),
                param[list[License9OrStr] | None]("license", license),
                param[list[str] | None]("model", model),
                param[Orientation2OrStr | None]("orientation", orientation),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[PeopleAge2OrStr | None]("people_age", people_age),
                param[list[PeopleEthnicity5OrStr] | None]("people_ethnicity", people_ethnicity),
                param[PeopleGender2OrStr | None]("people_gender", people_gender),
                param[int | None]("people_number", people_number),
                param[bool | None]("people_model_released", people_model_released),
                param[str | None]("query", query),
                param[ResolutionOrStr | None]("resolution", resolution),
                param[bool | None]("safe", safe),
                param[Sort2OrStr | None]("sort", sort),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[VideoSearchResults],
            error_mapper=search_videos_error_mapper,
            request_options=request_options,
        )
