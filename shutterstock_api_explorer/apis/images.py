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
from ..errors.add_image_collection_items_error import (
    AddImageCollectionItemsErrorBody,
    add_image_collection_items_error_mapper,
)
from ..errors.bulk_search_images_error import BulkSearchImagesErrorBody, bulk_search_images_error_mapper
from ..errors.create_image_collection_error import CreateImageCollectionErrorBody, create_image_collection_error_mapper
from ..errors.delete_image_collection_error import DeleteImageCollectionErrorBody, delete_image_collection_error_mapper
from ..errors.delete_image_collection_items_error import (
    DeleteImageCollectionItemsErrorBody,
    delete_image_collection_items_error_mapper,
)
from ..errors.download_image_error import DownloadImageErrorBody, download_image_error_mapper
from ..errors.get_image_collection_error import GetImageCollectionErrorBody, get_image_collection_error_mapper
from ..errors.get_image_collection_items_error import (
    GetImageCollectionItemsErrorBody,
    get_image_collection_items_error_mapper,
)
from ..errors.get_image_collection_list_error import (
    GetImageCollectionListErrorBody,
    get_image_collection_list_error_mapper,
)
from ..errors.get_image_error import GetImageErrorBody, get_image_error_mapper
from ..errors.get_image_keyword_suggestions_error import (
    GetImageKeywordSuggestionsErrorBody,
    get_image_keyword_suggestions_error_mapper,
)
from ..errors.get_image_license_list_error import GetImageLicenseListErrorBody, get_image_license_list_error_mapper
from ..errors.get_image_list_error import GetImageListErrorBody, get_image_list_error_mapper
from ..errors.get_image_recommendations_error import (
    GetImageRecommendationsErrorBody,
    get_image_recommendations_error_mapper,
)
from ..errors.get_image_suggestions_error import GetImageSuggestionsErrorBody, get_image_suggestions_error_mapper
from ..errors.license_images_error import LicenseImagesErrorBody, license_images_error_mapper
from ..errors.list_image_categories_error import ListImageCategoriesErrorBody, list_image_categories_error_mapper
from ..errors.list_similar_images_error import ListSimilarImagesErrorBody, list_similar_images_error_mapper
from ..errors.rename_image_collection_error import RenameImageCollectionErrorBody, rename_image_collection_error_mapper
from ..errors.search_images_error import SearchImagesErrorBody, search_images_error_mapper
from ..models.bulk_image_search_results import BulkImageSearchResults
from ..models.category_data_list import CategoryDataList
from ..models.collection import Collection
from ..models.collection_create_request import CollectionCreateRequest, CollectionCreateRequestDict
from ..models.collection_create_response import CollectionCreateResponse
from ..models.collection_data_list import CollectionDataList
from ..models.collection_item_data_list import CollectionItemDataList
from ..models.collection_item_request import CollectionItemRequest, CollectionItemRequestDict
from ..models.collection_update_request import CollectionUpdateRequest, CollectionUpdateRequestDict
from ..models.download_history_data_list import DownloadHistoryDataList
from ..models.enums.download_availability import DownloadAvailabilityOrStr
from ..models.enums.embed import EmbedOrStr
from ..models.enums.format15 import Format15OrStr
from ..models.enums.image_type2 import ImageType2OrStr
from ..models.enums.language import LanguageOrStr
from ..models.enums.library import LibraryOrStr
from ..models.enums.license import LicenseOrStr
from ..models.enums.orientation2 import Orientation2OrStr
from ..models.enums.people_age2 import PeopleAge2OrStr
from ..models.enums.people_ethnicity2 import PeopleEthnicity2OrStr
from ..models.enums.people_gender2 import PeopleGender2OrStr
from ..models.enums.size12 import Size12OrStr
from ..models.enums.sort2 import Sort2OrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.enums.type4 import Type4OrStr
from ..models.enums.view2 import View2OrStr
from ..models.image import Image
from ..models.image_data_list import ImageDataList
from ..models.image_search_results import ImageSearchResults
from ..models.license_image_request import LicenseImageRequest, LicenseImageRequestDict
from ..models.license_image_result_data_list import LicenseImageResultDataList
from ..models.recommendation_data_list import RecommendationDataList
from ..models.redownload_image import RedownloadImage, RedownloadImageDict
from ..models.search_entities_request import SearchEntitiesRequest, SearchEntitiesRequestDict
from ..models.search_entities_response import SearchEntitiesResponse
from ..models.search_image import SearchImage, SearchImageDict
from ..models.suggestions import Suggestions
from ..models.unions.contributor_country_model import ContributorCountryModel, ContributorCountryModelDict
from ..models.unions.region_model import RegionModel, RegionModelDict
from ..models.updated_media_data_list import UpdatedMediaDataList
from ..models.url import Url
from ..server.server import Server


class Images:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ImagesWithRawResponse(client, server, auth)

    def add_image_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint adds one or more images to a collection by image IDs.

        Args:
            id: Collection ID
            body: Array of image IDs to add to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully added collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.add_image_collection_items(id, body, request_options=request_options).unwrap()

    def bulk_search_images(
        self,
        body: list[SearchImage | SearchImageDict],
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        aspect_ratio_min: float | None = None,
        aspect_ratio_max: float | None = None,
        aspect_ratio: float | None = None,
        added_date_end: Date | None = None,
        category: str | None = None,
        color: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None,
        fields: str | None = None,
        height: int | None = None,
        height_from: int | None = None,
        height_to: int | None = None,
        image_type: list[ImageType2OrStr] | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[LicenseOrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_model_released: bool | None = None,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity2OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        region: RegionModel | RegionModelDict | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        spellcheck_query: bool | None = True,
        view: View2OrStr | None = None,
        width: int | None = None,
        width_from: int | None = None,
        width_to: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkImageSearchResults:
        """This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You
        can provide global search parameters in the query parameters and override them for each search in the body
        parameter. The query and body parameters are the same as in the ``GET /v2/images/search`` endpoint.

        Args:
            body: List of queries to request results for and filters to apply per query; these values override the
                defaults in the query parameters
            added_date: Show images added on the specified date
            added_date_start: Show images added on or after the specified date
            aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by
                the height, such as 1.7778 for a 16:9 image
            added_date_end: Show images added before the specified date
            category: Show images with the specified Shutterstock-defined category; specify a category name or ID
            color: Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that
                use similar colors
            contributor: Show images with the specified contributor names or IDs, allows multiple
            contributor_country: Show images from contributors in one or more specified countries, or start with NOT to
                exclude a country from the search
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            height: (Deprecated; use height_from and height_to instead) Show images with the specified height
            height_from: Show images with the specified height or larger, in pixels
            height_to: Show images with the specified height or smaller, in pixels
            image_type: Show images of the specified type
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only images with the specified license
            model: Show image results with the specified model IDs
            orientation: Show image results with horizontal or vertical orientation
            page: Page number
            per_page: Number of results per page
            people_model_released: Show images of people with a signed model release
            people_age: Show images that feature people of the specified age category
            people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images
                without those ethnicities
            people_gender: Show images with people of the specified gender
            people_number: Show images with the specified number of people
            region: Raise or lower search result rankings based on the result's relevance to a specified region; you can
                provide a country code or an IP address from which the API infers a country
            safe: Enable or disable safe search
            sort: Sort by
            spellcheck_query: Spellcheck the search query and return results on suggested spellings
            view: Amount of detail to render in the response
            width: (Deprecated; use width_from and width_to instead) Show images with the specified width
            width_from: Show images with the specified width or larger, in pixels
            width_to: Show images with the specified width or smaller, in pixels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_search_images(
            body,
            added_date=added_date,
            added_date_start=added_date_start,
            aspect_ratio_min=aspect_ratio_min,
            aspect_ratio_max=aspect_ratio_max,
            aspect_ratio=aspect_ratio,
            added_date_end=added_date_end,
            category=category,
            color=color,
            contributor=contributor,
            contributor_country=contributor_country,
            fields=fields,
            height=height,
            height_from=height_from,
            height_to=height_to,
            image_type=image_type,
            keyword_safe_search=keyword_safe_search,
            language=language,
            license=license,
            model=model,
            orientation=orientation,
            page=page,
            per_page=per_page,
            people_model_released=people_model_released,
            people_age=people_age,
            people_ethnicity=people_ethnicity,
            people_gender=people_gender,
            people_number=people_number,
            region=region,
            safe=safe,
            sort=sort,
            spellcheck_query=spellcheck_query,
            view=view,
            width=width,
            width_from=width_from,
            width_to=width_to,
            request_options=request_options,
        ).unwrap()

    def create_image_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionCreateResponse:
        """This endpoint creates one or more image collections (lightboxes). To add images to the collections, use
        ``POST /v2/images/collections/{id}/items``.

        Args:
            body: The names of the new collections
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully created image collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.create_image_collection(body, request_options=request_options).unwrap()

    def delete_image_collection(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This endpoint deletes an image collection.

        Args:
            id: Collection ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully deleted collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_image_collection(id, request_options=request_options).unwrap()

    def delete_image_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint removes one or more images from a collection.

        Args:
            id: Collection ID
            item_id: One or more image IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully removed collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_image_collection_items(
            id, item_id=item_id, request_options=request_options
        ).unwrap()

    def download_image(
        self,
        id: str,
        body: RedownloadImage | RedownloadImageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Url:
        """This endpoint redownloads images that you have already received a license for. The download links in the
        response are valid for 8 hours.

        Args:
            id: License ID
            body: Information about the images to redownload
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.download_image(id, body, request_options=request_options).unwrap()

    def get_image(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Image:
        """This endpoint shows information about an image, including a URL to a preview image and the sizes that it is
        available in.

        Args:
            id: Image ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_image(
            id, language=language, view=view, search_id=search_id, request_options=request_options
        ).unwrap()

    def get_image_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Collection:
        """This endpoint gets more detailed information about a collection, including its cover image and timestamps for
        its creation and most recent update. To get the images in collections, use ``GET
        /v2/images/collections/{id}/items``.

        Args:
            id: Collection ID
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_image_collection(
            id, embed=embed, share_code=share_code, request_options=request_options
        ).unwrap()

    def get_image_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionItemDataList:
        """This endpoint lists the IDs of images in a collection and the date that each was added.

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
        return self._with_raw_response.get_image_collection_items(
            id, page=page, per_page=per_page, share_code=share_code, sort=sort, request_options=request_options
        ).unwrap()

    def get_image_collection_list(
        self,
        *,
        embed: list[EmbedOrStr] | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionDataList:
        """This endpoint lists your collections of images and their basic attributes.

        Args:
            embed: Which sharing information to include in the response, such as a URL to the collection
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_image_collection_list(
            embed=embed, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_image_keyword_suggestions(
        self,
        body: SearchEntitiesRequest | SearchEntitiesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchEntitiesResponse:
        """This endpoint returns up to 10 important keywords from a block of plain text.

        Args:
            body: Plain text to extract keywords from
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_image_keyword_suggestions(body, request_options=request_options).unwrap()

    def get_image_license_list(
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
        """This endpoint lists existing licenses.

        Args:
            image_id: Show licenses for the specified image ID
            license: Show images that are available with the specified license, such as ``standard`` or ``enhanced``
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
        return self._with_raw_response.get_image_license_list(
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

    def get_image_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ImageDataList:
        """This endpoint lists information about one or more images, including the available sizes.

        Args:
            id: One or more image IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_image_list(
            id, view=view, search_id=search_id, request_options=request_options
        ).unwrap()

    def get_image_recommendations(
        self,
        id: list[str],
        *,
        max_items: int | None = 20,
        safe: bool | None = True,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecommendationDataList:
        """This endpoint returns images that customers put in the same collection as the specified image IDs.

        Args:
            id: Image IDs
            max_items: Maximum number of results returned in the response
            safe: Restrict results to safe images
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_image_recommendations(
            id, max_items=max_items, safe=safe, request_options=request_options
        ).unwrap()

    def get_image_suggestions(
        self, query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None
    ) -> Suggestions:
        """This endpoint provides autocomplete suggestions for partial search terms.

        Args:
            query: Search term for which you want keyword suggestions
            limit: Limit the number of suggestions
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_image_suggestions(
            query, limit=limit, request_options=request_options
        ).unwrap()

    def get_updated_images(
        self,
        *,
        type_: list[Type4OrStr] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str | None = "1 HOUR",
        page: int | None = 1,
        per_page: int | None = 100,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatedMediaDataList:
        """This endpoint lists images that have been updated in the specified time period to update content management
        systems (CMS) or digital asset management (DAM) systems. In most cases, use the ``interval`` parameter to show
        images that were updated recently, but you can also use the ``start_date`` and ``end_date`` parameters to
        specify a range of no more than three days. Do not use the ``interval`` parameter with either ``start_date`` or
        ``end_date``.

        Args:
            type_: Show images that were added, deleted, or edited; by default, the endpoint returns images that were
                updated in any of these ways
            start_date: Show images updated on or after the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency.
            end_date: Show images updated before the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency. Please note that the end date must be at least 5
                minutes after the start date.
            interval: Show images updated in the specified time period, where the time period is an interval (like SQL
                INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were
                updated in the hour preceding the request
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_updated_images(
            type_=type_,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            page=page,
            per_page=per_page,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def license_images(
        self,
        body: LicenseImageRequest | LicenseImageRequestDict,
        *,
        subscription_id: str | None = None,
        format: Format15OrStr | None = None,
        size: Size12OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseImageResultDataList:
        """This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and
        other details like the format, size, and subscription ID either in the query parameter or with each image ID in
        the body parameter. Values in the body parameter override values in the query parameters. The download links in
        the response are valid for 8 hours.

        Args:
            body: List of images to request licenses for and information about each license transaction; these values
                override the defaults in the query parameters
            subscription_id: Subscription ID to use to license the image
            format: (Deprecated) Image format
            size: Image size
            search_id: Search ID that was provided in the results of an image search
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.license_images(
            body,
            subscription_id=subscription_id,
            format=format,
            size=size,
            search_id=search_id,
            request_options=request_options,
        ).unwrap()

    def list_image_categories(
        self, *, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CategoryDataList:
        """This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

        Args:
            language: Language for the keywords and categories in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.list_image_categories(
            language=language, request_options=request_options
        ).unwrap()

    def list_similar_images(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ImageSearchResults:
        """This endpoint returns images that are visually similar to an image that you specify.

        Args:
            id: Image ID
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.list_similar_images(
            id, language=language, page=page, per_page=per_page, view=view, request_options=request_options
        ).unwrap()

    def rename_image_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint sets a new name for an image collection.

        Args:
            id: Collection ID
            body: The new name for the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully updated collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.rename_image_collection(id, body, request_options=request_options).unwrap()

    def search_images(
        self,
        *,
        library: list[LibraryOrStr] | None = None,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        aspect_ratio_min: float | None = None,
        aspect_ratio_max: float | None = None,
        aspect_ratio: float | None = None,
        added_date_end: Date | None = None,
        category: str | None = None,
        color: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None,
        fields: str | None = None,
        height: int | None = None,
        height_from: int | None = None,
        height_to: int | None = None,
        image_type: list[ImageType2OrStr] | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[LicenseOrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_model_released: bool | None = None,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity2OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        query: str | None = None,
        region: RegionModel | RegionModelDict | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        spellcheck_query: bool | None = True,
        view: View2OrStr | None = None,
        width: int | None = None,
        width_from: int | None = None,
        width_to: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ImageSearchResults:
        """This endpoint searches for images. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter. You can also filter search terms out in the ``query``
        parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media,
        not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

        Args:
            library: Search within different Shutterstock owned libraries
            added_date: Show images added on the specified date
            added_date_start: Show images added on or after the specified date
            aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by
                the height, such as 1.7778 for a 16:9 image
            added_date_end: Show images added before the specified date
            category: Show images with the specified Shutterstock-defined category; specify a category name or ID
            color: Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that
                use similar colors
            contributor: Show images with the specified contributor names or IDs, allows multiple
            contributor_country: Show images from contributors in one or more specified countries, or start with NOT to
                exclude a country from the search
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            height: (Deprecated; use height_from and height_to instead) Show images with the specified height
            height_from: Show images with the specified height or larger, in pixels
            height_to: Show images with the specified height or smaller, in pixels
            image_type: Show images of the specified type
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only images with the specified license
            model: Show image results with the specified model IDs
            orientation: Show image results with horizontal or vertical orientation
            page: Page number
            per_page: Number of results per page
            people_model_released: Show images of people with a signed model release
            people_age: Show images that feature people of the specified age category
            people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images
                without those ethnicities
            people_gender: Show images with people of the specified gender
            people_number: Show images with the specified number of people
            query: One or more search terms separated by spaces; you can use NOT to filter out images that match a term
            region: Raise or lower search result rankings based on the result's relevance to a specified region; you can
                provide a country code or an IP address from which the API infers a country
            safe: Enable or disable safe search
            sort: Sort by
            spellcheck_query: Spellcheck the search query and return results on suggested spellings
            view: Amount of detail to render in the response
            width: (Deprecated; use width_from and width_to instead) Show images with the specified width
            width_from: Show images with the specified width or larger, in pixels
            width_to: Show images with the specified width or smaller, in pixels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.search_images(
            library=library,
            added_date=added_date,
            added_date_start=added_date_start,
            aspect_ratio_min=aspect_ratio_min,
            aspect_ratio_max=aspect_ratio_max,
            aspect_ratio=aspect_ratio,
            added_date_end=added_date_end,
            category=category,
            color=color,
            contributor=contributor,
            contributor_country=contributor_country,
            fields=fields,
            height=height,
            height_from=height_from,
            height_to=height_to,
            image_type=image_type,
            keyword_safe_search=keyword_safe_search,
            language=language,
            license=license,
            model=model,
            orientation=orientation,
            page=page,
            per_page=per_page,
            people_model_released=people_model_released,
            people_age=people_age,
            people_ethnicity=people_ethnicity,
            people_gender=people_gender,
            people_number=people_number,
            query=query,
            region=region,
            safe=safe,
            sort=sort,
            spellcheck_query=spellcheck_query,
            view=view,
            width=width,
            width_from=width_from,
            width_to=width_to,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ImagesWithRawResponse:
        return self._with_raw_response


class AsyncImages:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncImagesWithRawResponse(client, server, auth)

    async def add_image_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint adds one or more images to a collection by image IDs.

        Args:
            id: Collection ID
            body: Array of image IDs to add to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully added collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_image_collection_items(id, body, request_options=request_options)
        ).unwrap()

    async def bulk_search_images(
        self,
        body: list[SearchImage | SearchImageDict],
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        aspect_ratio_min: float | None = None,
        aspect_ratio_max: float | None = None,
        aspect_ratio: float | None = None,
        added_date_end: Date | None = None,
        category: str | None = None,
        color: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None,
        fields: str | None = None,
        height: int | None = None,
        height_from: int | None = None,
        height_to: int | None = None,
        image_type: list[ImageType2OrStr] | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[LicenseOrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_model_released: bool | None = None,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity2OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        region: RegionModel | RegionModelDict | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        spellcheck_query: bool | None = True,
        view: View2OrStr | None = None,
        width: int | None = None,
        width_from: int | None = None,
        width_to: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkImageSearchResults:
        """This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You
        can provide global search parameters in the query parameters and override them for each search in the body
        parameter. The query and body parameters are the same as in the ``GET /v2/images/search`` endpoint.

        Args:
            body: List of queries to request results for and filters to apply per query; these values override the
                defaults in the query parameters
            added_date: Show images added on the specified date
            added_date_start: Show images added on or after the specified date
            aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by
                the height, such as 1.7778 for a 16:9 image
            added_date_end: Show images added before the specified date
            category: Show images with the specified Shutterstock-defined category; specify a category name or ID
            color: Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that
                use similar colors
            contributor: Show images with the specified contributor names or IDs, allows multiple
            contributor_country: Show images from contributors in one or more specified countries, or start with NOT to
                exclude a country from the search
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            height: (Deprecated; use height_from and height_to instead) Show images with the specified height
            height_from: Show images with the specified height or larger, in pixels
            height_to: Show images with the specified height or smaller, in pixels
            image_type: Show images of the specified type
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only images with the specified license
            model: Show image results with the specified model IDs
            orientation: Show image results with horizontal or vertical orientation
            page: Page number
            per_page: Number of results per page
            people_model_released: Show images of people with a signed model release
            people_age: Show images that feature people of the specified age category
            people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images
                without those ethnicities
            people_gender: Show images with people of the specified gender
            people_number: Show images with the specified number of people
            region: Raise or lower search result rankings based on the result's relevance to a specified region; you can
                provide a country code or an IP address from which the API infers a country
            safe: Enable or disable safe search
            sort: Sort by
            spellcheck_query: Spellcheck the search query and return results on suggested spellings
            view: Amount of detail to render in the response
            width: (Deprecated; use width_from and width_to instead) Show images with the specified width
            width_from: Show images with the specified width or larger, in pixels
            width_to: Show images with the specified width or smaller, in pixels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_search_images(
                body,
                added_date=added_date,
                added_date_start=added_date_start,
                aspect_ratio_min=aspect_ratio_min,
                aspect_ratio_max=aspect_ratio_max,
                aspect_ratio=aspect_ratio,
                added_date_end=added_date_end,
                category=category,
                color=color,
                contributor=contributor,
                contributor_country=contributor_country,
                fields=fields,
                height=height,
                height_from=height_from,
                height_to=height_to,
                image_type=image_type,
                keyword_safe_search=keyword_safe_search,
                language=language,
                license=license,
                model=model,
                orientation=orientation,
                page=page,
                per_page=per_page,
                people_model_released=people_model_released,
                people_age=people_age,
                people_ethnicity=people_ethnicity,
                people_gender=people_gender,
                people_number=people_number,
                region=region,
                safe=safe,
                sort=sort,
                spellcheck_query=spellcheck_query,
                view=view,
                width=width,
                width_from=width_from,
                width_to=width_to,
                request_options=request_options,
            )
        ).unwrap()

    async def create_image_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionCreateResponse:
        """This endpoint creates one or more image collections (lightboxes). To add images to the collections, use
        ``POST /v2/images/collections/{id}/items``.

        Args:
            body: The names of the new collections
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully created image collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_image_collection(body, request_options=request_options)).unwrap()

    async def delete_image_collection(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This endpoint deletes an image collection.

        Args:
            id: Collection ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully deleted collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_image_collection(id, request_options=request_options)).unwrap()

    async def delete_image_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint removes one or more images from a collection.

        Args:
            id: Collection ID
            item_id: One or more image IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully removed collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_image_collection_items(
                id, item_id=item_id, request_options=request_options
            )
        ).unwrap()

    async def download_image(
        self,
        id: str,
        body: RedownloadImage | RedownloadImageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Url:
        """This endpoint redownloads images that you have already received a license for. The download links in the
        response are valid for 8 hours.

        Args:
            id: License ID
            body: Information about the images to redownload
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.download_image(id, body, request_options=request_options)).unwrap()

    async def get_image(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Image:
        """This endpoint shows information about an image, including a URL to a preview image and the sizes that it is
        available in.

        Args:
            id: Image ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_image(
                id, language=language, view=view, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def get_image_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Collection:
        """This endpoint gets more detailed information about a collection, including its cover image and timestamps for
        its creation and most recent update. To get the images in collections, use ``GET
        /v2/images/collections/{id}/items``.

        Args:
            id: Collection ID
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_image_collection(
                id, embed=embed, share_code=share_code, request_options=request_options
            )
        ).unwrap()

    async def get_image_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionItemDataList:
        """This endpoint lists the IDs of images in a collection and the date that each was added.

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
            await self._with_raw_response.get_image_collection_items(
                id, page=page, per_page=per_page, share_code=share_code, sort=sort, request_options=request_options
            )
        ).unwrap()

    async def get_image_collection_list(
        self,
        *,
        embed: list[EmbedOrStr] | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionDataList:
        """This endpoint lists your collections of images and their basic attributes.

        Args:
            embed: Which sharing information to include in the response, such as a URL to the collection
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_image_collection_list(
                embed=embed, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_image_keyword_suggestions(
        self,
        body: SearchEntitiesRequest | SearchEntitiesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchEntitiesResponse:
        """This endpoint returns up to 10 important keywords from a block of plain text.

        Args:
            body: Plain text to extract keywords from
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_image_keyword_suggestions(body, request_options=request_options)
        ).unwrap()

    async def get_image_license_list(
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
        """This endpoint lists existing licenses.

        Args:
            image_id: Show licenses for the specified image ID
            license: Show images that are available with the specified license, such as ``standard`` or ``enhanced``
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
            await self._with_raw_response.get_image_license_list(
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

    async def get_image_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ImageDataList:
        """This endpoint lists information about one or more images, including the available sizes.

        Args:
            id: One or more image IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_image_list(
                id, view=view, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def get_image_recommendations(
        self,
        id: list[str],
        *,
        max_items: int | None = 20,
        safe: bool | None = True,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecommendationDataList:
        """This endpoint returns images that customers put in the same collection as the specified image IDs.

        Args:
            id: Image IDs
            max_items: Maximum number of results returned in the response
            safe: Restrict results to safe images
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_image_recommendations(
                id, max_items=max_items, safe=safe, request_options=request_options
            )
        ).unwrap()

    async def get_image_suggestions(
        self, query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None
    ) -> Suggestions:
        """This endpoint provides autocomplete suggestions for partial search terms.

        Args:
            query: Search term for which you want keyword suggestions
            limit: Limit the number of suggestions
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_image_suggestions(query, limit=limit, request_options=request_options)
        ).unwrap()

    async def get_updated_images(
        self,
        *,
        type_: list[Type4OrStr] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str | None = "1 HOUR",
        page: int | None = 1,
        per_page: int | None = 100,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatedMediaDataList:
        """This endpoint lists images that have been updated in the specified time period to update content management
        systems (CMS) or digital asset management (DAM) systems. In most cases, use the ``interval`` parameter to show
        images that were updated recently, but you can also use the ``start_date`` and ``end_date`` parameters to
        specify a range of no more than three days. Do not use the ``interval`` parameter with either ``start_date`` or
        ``end_date``.

        Args:
            type_: Show images that were added, deleted, or edited; by default, the endpoint returns images that were
                updated in any of these ways
            start_date: Show images updated on or after the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency.
            end_date: Show images updated before the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency. Please note that the end date must be at least 5
                minutes after the start date.
            interval: Show images updated in the specified time period, where the time period is an interval (like SQL
                INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were
                updated in the hour preceding the request
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_updated_images(
                type_=type_,
                start_date=start_date,
                end_date=end_date,
                interval=interval,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def license_images(
        self,
        body: LicenseImageRequest | LicenseImageRequestDict,
        *,
        subscription_id: str | None = None,
        format: Format15OrStr | None = None,
        size: Size12OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseImageResultDataList:
        """This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and
        other details like the format, size, and subscription ID either in the query parameter or with each image ID in
        the body parameter. Values in the body parameter override values in the query parameters. The download links in
        the response are valid for 8 hours.

        Args:
            body: List of images to request licenses for and information about each license transaction; these values
                override the defaults in the query parameters
            subscription_id: Subscription ID to use to license the image
            format: (Deprecated) Image format
            size: Image size
            search_id: Search ID that was provided in the results of an image search
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.license_images(
                body,
                subscription_id=subscription_id,
                format=format,
                size=size,
                search_id=search_id,
                request_options=request_options,
            )
        ).unwrap()

    async def list_image_categories(
        self, *, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CategoryDataList:
        """This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

        Args:
            language: Language for the keywords and categories in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_image_categories(language=language, request_options=request_options)
        ).unwrap()

    async def list_similar_images(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ImageSearchResults:
        """This endpoint returns images that are visually similar to an image that you specify.

        Args:
            id: Image ID
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
            await self._with_raw_response.list_similar_images(
                id, language=language, page=page, per_page=per_page, view=view, request_options=request_options
            )
        ).unwrap()

    async def rename_image_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint sets a new name for an image collection.

        Args:
            id: Collection ID
            body: The new name for the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully updated collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.rename_image_collection(id, body, request_options=request_options)
        ).unwrap()

    async def search_images(
        self,
        *,
        library: list[LibraryOrStr] | None = None,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        aspect_ratio_min: float | None = None,
        aspect_ratio_max: float | None = None,
        aspect_ratio: float | None = None,
        added_date_end: Date | None = None,
        category: str | None = None,
        color: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None,
        fields: str | None = None,
        height: int | None = None,
        height_from: int | None = None,
        height_to: int | None = None,
        image_type: list[ImageType2OrStr] | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[LicenseOrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_model_released: bool | None = None,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity2OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        query: str | None = None,
        region: RegionModel | RegionModelDict | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        spellcheck_query: bool | None = True,
        view: View2OrStr | None = None,
        width: int | None = None,
        width_from: int | None = None,
        width_to: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ImageSearchResults:
        """This endpoint searches for images. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter. You can also filter search terms out in the ``query``
        parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media,
        not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

        Args:
            library: Search within different Shutterstock owned libraries
            added_date: Show images added on the specified date
            added_date_start: Show images added on or after the specified date
            aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by
                the height, such as 1.7778 for a 16:9 image
            added_date_end: Show images added before the specified date
            category: Show images with the specified Shutterstock-defined category; specify a category name or ID
            color: Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that
                use similar colors
            contributor: Show images with the specified contributor names or IDs, allows multiple
            contributor_country: Show images from contributors in one or more specified countries, or start with NOT to
                exclude a country from the search
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            height: (Deprecated; use height_from and height_to instead) Show images with the specified height
            height_from: Show images with the specified height or larger, in pixels
            height_to: Show images with the specified height or smaller, in pixels
            image_type: Show images of the specified type
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only images with the specified license
            model: Show image results with the specified model IDs
            orientation: Show image results with horizontal or vertical orientation
            page: Page number
            per_page: Number of results per page
            people_model_released: Show images of people with a signed model release
            people_age: Show images that feature people of the specified age category
            people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images
                without those ethnicities
            people_gender: Show images with people of the specified gender
            people_number: Show images with the specified number of people
            query: One or more search terms separated by spaces; you can use NOT to filter out images that match a term
            region: Raise or lower search result rankings based on the result's relevance to a specified region; you can
                provide a country code or an IP address from which the API infers a country
            safe: Enable or disable safe search
            sort: Sort by
            spellcheck_query: Spellcheck the search query and return results on suggested spellings
            view: Amount of detail to render in the response
            width: (Deprecated; use width_from and width_to instead) Show images with the specified width
            width_from: Show images with the specified width or larger, in pixels
            width_to: Show images with the specified width or smaller, in pixels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_images(
                library=library,
                added_date=added_date,
                added_date_start=added_date_start,
                aspect_ratio_min=aspect_ratio_min,
                aspect_ratio_max=aspect_ratio_max,
                aspect_ratio=aspect_ratio,
                added_date_end=added_date_end,
                category=category,
                color=color,
                contributor=contributor,
                contributor_country=contributor_country,
                fields=fields,
                height=height,
                height_from=height_from,
                height_to=height_to,
                image_type=image_type,
                keyword_safe_search=keyword_safe_search,
                language=language,
                license=license,
                model=model,
                orientation=orientation,
                page=page,
                per_page=per_page,
                people_model_released=people_model_released,
                people_age=people_age,
                people_ethnicity=people_ethnicity,
                people_gender=people_gender,
                people_number=people_number,
                query=query,
                region=region,
                safe=safe,
                sort=sort,
                spellcheck_query=spellcheck_query,
                view=view,
                width=width,
                width_from=width_from,
                width_to=width_to,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncImagesWithRawResponse:
        return self._with_raw_response


class ImagesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_image_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddImageCollectionItemsErrorBody]:
        """This endpoint adds one or more images to a collection by image IDs.

        Args:
            id: Collection ID
            body: Array of image IDs to add to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionItemRequest | CollectionItemRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=add_image_collection_items_error_mapper,
            request_options=request_options,
        )

    def bulk_search_images(
        self,
        body: list[SearchImage | SearchImageDict],
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        aspect_ratio_min: float | None = None,
        aspect_ratio_max: float | None = None,
        aspect_ratio: float | None = None,
        added_date_end: Date | None = None,
        category: str | None = None,
        color: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None,
        fields: str | None = None,
        height: int | None = None,
        height_from: int | None = None,
        height_to: int | None = None,
        image_type: list[ImageType2OrStr] | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[LicenseOrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_model_released: bool | None = None,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity2OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        region: RegionModel | RegionModelDict | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        spellcheck_query: bool | None = True,
        view: View2OrStr | None = None,
        width: int | None = None,
        width_from: int | None = None,
        width_to: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkImageSearchResults, BulkSearchImagesErrorBody]:
        """This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You
        can provide global search parameters in the query parameters and override them for each search in the body
        parameter. The query and body parameters are the same as in the ``GET /v2/images/search`` endpoint.

        Args:
            body: List of queries to request results for and filters to apply per query; these values override the
                defaults in the query parameters
            added_date: Show images added on the specified date
            added_date_start: Show images added on or after the specified date
            aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by
                the height, such as 1.7778 for a 16:9 image
            added_date_end: Show images added before the specified date
            category: Show images with the specified Shutterstock-defined category; specify a category name or ID
            color: Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that
                use similar colors
            contributor: Show images with the specified contributor names or IDs, allows multiple
            contributor_country: Show images from contributors in one or more specified countries, or start with NOT to
                exclude a country from the search
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            height: (Deprecated; use height_from and height_to instead) Show images with the specified height
            height_from: Show images with the specified height or larger, in pixels
            height_to: Show images with the specified height or smaller, in pixels
            image_type: Show images of the specified type
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only images with the specified license
            model: Show image results with the specified model IDs
            orientation: Show image results with horizontal or vertical orientation
            page: Page number
            per_page: Number of results per page
            people_model_released: Show images of people with a signed model release
            people_age: Show images that feature people of the specified age category
            people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images
                without those ethnicities
            people_gender: Show images with people of the specified gender
            people_number: Show images with the specified number of people
            region: Raise or lower search result rankings based on the result's relevance to a specified region; you can
                provide a country code or an IP address from which the API infers a country
            safe: Enable or disable safe search
            sort: Sort by
            spellcheck_query: Spellcheck the search query and return results on suggested spellings
            view: Amount of detail to render in the response
            width: (Deprecated; use width_from and width_to instead) Show images with the specified width
            width_from: Show images with the specified width or larger, in pixels
            width_to: Show images with the specified width or smaller, in pixels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bulk_search/images"),
            query_params=[
                param[Date | None]("added_date", added_date),
                param[Date | None]("added_date_start", added_date_start),
                param[float | None]("aspect_ratio_min", aspect_ratio_min),
                param[float | None]("aspect_ratio_max", aspect_ratio_max),
                param[float | None]("aspect_ratio", aspect_ratio),
                param[Date | None]("added_date_end", added_date_end),
                param[str | None]("category", category),
                param[str | None]("color", color),
                param[list[str] | None]("contributor", contributor),
                param[ContributorCountryModel | ContributorCountryModelDict | None](
                    "contributor_country", contributor_country
                ),
                param[str | None]("fields", fields),
                param[int | None]("height", height),
                param[int | None]("height_from", height_from),
                param[int | None]("height_to", height_to),
                param[list[ImageType2OrStr] | None]("image_type", image_type),
                param[bool | None]("keyword_safe_search", keyword_safe_search),
                param[LanguageOrStr | None]("language", language),
                param[list[LicenseOrStr] | None]("license", license),
                param[list[str] | None]("model", model),
                param[Orientation2OrStr | None]("orientation", orientation),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("people_model_released", people_model_released),
                param[PeopleAge2OrStr | None]("people_age", people_age),
                param[list[PeopleEthnicity2OrStr] | None]("people_ethnicity", people_ethnicity),
                param[PeopleGender2OrStr | None]("people_gender", people_gender),
                param[int | None]("people_number", people_number),
                param[RegionModel | RegionModelDict | None]("region", region),
                param[bool | None]("safe", safe),
                param[Sort2OrStr | None]("sort", sort),
                param[bool | None]("spellcheck_query", spellcheck_query),
                param[View2OrStr | None]("view", view),
                param[int | None]("width", width),
                param[int | None]("width_from", width_from),
                param[int | None]("width_to", width_to),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[SearchImage | SearchImageDict]](body),
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[BulkImageSearchResults],
            error_mapper=bulk_search_images_error_mapper,
            request_options=request_options,
        )

    def create_image_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionCreateResponse, CreateImageCollectionErrorBody]:
        """This endpoint creates one or more image collections (lightboxes). To add images to the collections, use
        ``POST /v2/images/collections/{id}/items``.

        Args:
            body: The names of the new collections
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/collections"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionCreateRequest | CollectionCreateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionCreateResponse],
            error_mapper=create_image_collection_error_mapper,
            request_options=request_options,
        )

    def delete_image_collection(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteImageCollectionErrorBody]:
        """This endpoint deletes an image collection.

        Args:
            id: Collection ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/images/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_image_collection_error_mapper,
            request_options=request_options,
        )

    def delete_image_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteImageCollectionItemsErrorBody]:
        """This endpoint removes one or more images from a collection.

        Args:
            id: Collection ID
            item_id: One or more image IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/images/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[str] | None]("item_id", item_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_image_collection_items_error_mapper,
            request_options=request_options,
        )

    def download_image(
        self,
        id: str,
        body: RedownloadImage | RedownloadImageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Url, DownloadImageErrorBody]:
        """This endpoint redownloads images that you have already received a license for. The download links in the
        response are valid for 8 hours.

        Args:
            id: License ID
            body: Information about the images to redownload
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/licenses/{id}/downloads"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RedownloadImage | RedownloadImageDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Url],
            error_mapper=download_image_error_mapper,
            request_options=request_options,
        )

    def get_image(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Image, GetImageErrorBody]:
        """This endpoint shows information about an image, including a URL to a preview image and the sizes that it is
        available in.

        Args:
            id: Image ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Image],
            error_mapper=get_image_error_mapper,
            request_options=request_options,
        )

    def get_image_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Collection, GetImageCollectionErrorBody]:
        """This endpoint gets more detailed information about a collection, including its cover image and timestamps for
        its creation and most recent update. To get the images in collections, use ``GET
        /v2/images/collections/{id}/items``.

        Args:
            id: Collection ID
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/collections/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[EmbedOrStr] | None]("embed", embed), param[str | None]("share_code", share_code)],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Collection],
            error_mapper=get_image_collection_error_mapper,
            request_options=request_options,
        )

    def get_image_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionItemDataList, GetImageCollectionItemsErrorBody]:
        """This endpoint lists the IDs of images in a collection and the date that each was added.

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
            url_template=self._server.default("/v2/images/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("share_code", share_code),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionItemDataList],
            error_mapper=get_image_collection_items_error_mapper,
            request_options=request_options,
        )

    def get_image_collection_list(
        self,
        *,
        embed: list[EmbedOrStr] | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionDataList, GetImageCollectionListErrorBody]:
        """This endpoint lists your collections of images and their basic attributes.

        Args:
            embed: Which sharing information to include in the response, such as a URL to the collection
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/collections"),
            query_params=[
                param[list[EmbedOrStr] | None]("embed", embed),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionDataList],
            error_mapper=get_image_collection_list_error_mapper,
            request_options=request_options,
        )

    def get_image_keyword_suggestions(
        self,
        body: SearchEntitiesRequest | SearchEntitiesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchEntitiesResponse, GetImageKeywordSuggestionsErrorBody]:
        """This endpoint returns up to 10 important keywords from a block of plain text.

        Args:
            body: Plain text to extract keywords from
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/search/suggestions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchEntitiesRequest | SearchEntitiesRequestDict](body),
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[SearchEntitiesResponse],
            error_mapper=get_image_keyword_suggestions_error_mapper,
            request_options=request_options,
        )

    def get_image_license_list(
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
    ) -> ApiResult[DownloadHistoryDataList, GetImageLicenseListErrorBody]:
        """This endpoint lists existing licenses.

        Args:
            image_id: Show licenses for the specified image ID
            license: Show images that are available with the specified license, such as ``standard`` or ``enhanced``
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
            url_template=self._server.default("/v2/images/licenses"),
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
            error_mapper=get_image_license_list_error_mapper,
            request_options=request_options,
        )

    def get_image_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ImageDataList, GetImageListErrorBody]:
        """This endpoint lists information about one or more images, including the available sizes.

        Args:
            id: One or more image IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images"),
            query_params=[
                param[list[str]]("id", id),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ImageDataList],
            error_mapper=get_image_list_error_mapper,
            request_options=request_options,
        )

    def get_image_recommendations(
        self,
        id: list[str],
        *,
        max_items: int | None = 20,
        safe: bool | None = True,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecommendationDataList, GetImageRecommendationsErrorBody]:
        """This endpoint returns images that customers put in the same collection as the specified image IDs.

        Args:
            id: Image IDs
            max_items: Maximum number of results returned in the response
            safe: Restrict results to safe images
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/recommendations"),
            query_params=[
                param[list[str]]("id", id), param[int | None]("max_items", max_items), param[bool | None]("safe", safe)
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[RecommendationDataList],
            error_mapper=get_image_recommendations_error_mapper,
            request_options=request_options,
        )

    def get_image_suggestions(
        self, query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Suggestions, GetImageSuggestionsErrorBody]:
        """This endpoint provides autocomplete suggestions for partial search terms.

        Args:
            query: Search term for which you want keyword suggestions
            limit: Limit the number of suggestions
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/search/suggestions"),
            query_params=[param[str]("query", query), param[int | None]("limit", limit)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Suggestions],
            error_mapper=get_image_suggestions_error_mapper,
            request_options=request_options,
        )

    def get_updated_images(
        self,
        *,
        type_: list[Type4OrStr] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str | None = "1 HOUR",
        page: int | None = 1,
        per_page: int | None = 100,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatedMediaDataList, RawError]:
        """This endpoint lists images that have been updated in the specified time period to update content management
        systems (CMS) or digital asset management (DAM) systems. In most cases, use the ``interval`` parameter to show
        images that were updated recently, but you can also use the ``start_date`` and ``end_date`` parameters to
        specify a range of no more than three days. Do not use the ``interval`` parameter with either ``start_date`` or
        ``end_date``.

        Args:
            type_: Show images that were added, deleted, or edited; by default, the endpoint returns images that were
                updated in any of these ways
            start_date: Show images updated on or after the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency.
            end_date: Show images updated before the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency. Please note that the end date must be at least 5
                minutes after the start date.
            interval: Show images updated in the specified time period, where the time period is an interval (like SQL
                INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were
                updated in the hour preceding the request
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/updated"),
            query_params=[
                param[list[Type4OrStr] | None]("type", type_),
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

    def license_images(
        self,
        body: LicenseImageRequest | LicenseImageRequestDict,
        *,
        subscription_id: str | None = None,
        format: Format15OrStr | None = None,
        size: Size12OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseImageResultDataList, LicenseImagesErrorBody]:
        """This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and
        other details like the format, size, and subscription ID either in the query parameter or with each image ID in
        the body parameter. Values in the body parameter override values in the query parameters. The download links in
        the response are valid for 8 hours.

        Args:
            body: List of images to request licenses for and information about each license transaction; these values
                override the defaults in the query parameters
            subscription_id: Subscription ID to use to license the image
            format: (Deprecated) Image format
            size: Image size
            search_id: Search ID that was provided in the results of an image search
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/licenses"),
            query_params=[
                param[str | None]("subscription_id", subscription_id),
                param[Format15OrStr | None]("format", format),
                param[Size12OrStr | None]("size", size),
                param[str | None]("search_id", search_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseImageRequest | LicenseImageRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseImageResultDataList],
            error_mapper=license_images_error_mapper,
            request_options=request_options,
        )

    def list_image_categories(
        self, *, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoryDataList, ListImageCategoriesErrorBody]:
        """This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

        Args:
            language: Language for the keywords and categories in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/categories"),
            query_params=[param[LanguageOrStr | None]("language", language)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[CategoryDataList],
            error_mapper=list_image_categories_error_mapper,
            request_options=request_options,
        )

    def list_similar_images(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ImageSearchResults, ListSimilarImagesErrorBody]:
        """This endpoint returns images that are visually similar to an image that you specify.

        Args:
            id: Image ID
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/{id}/similar"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ImageSearchResults],
            error_mapper=list_similar_images_error_mapper,
            request_options=request_options,
        )

    def rename_image_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RenameImageCollectionErrorBody]:
        """This endpoint sets a new name for an image collection.

        Args:
            id: Collection ID
            body: The new name for the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionUpdateRequest | CollectionUpdateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=rename_image_collection_error_mapper,
            request_options=request_options,
        )

    def search_images(
        self,
        *,
        library: list[LibraryOrStr] | None = None,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        aspect_ratio_min: float | None = None,
        aspect_ratio_max: float | None = None,
        aspect_ratio: float | None = None,
        added_date_end: Date | None = None,
        category: str | None = None,
        color: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None,
        fields: str | None = None,
        height: int | None = None,
        height_from: int | None = None,
        height_to: int | None = None,
        image_type: list[ImageType2OrStr] | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[LicenseOrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_model_released: bool | None = None,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity2OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        query: str | None = None,
        region: RegionModel | RegionModelDict | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        spellcheck_query: bool | None = True,
        view: View2OrStr | None = None,
        width: int | None = None,
        width_from: int | None = None,
        width_to: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ImageSearchResults, SearchImagesErrorBody]:
        """This endpoint searches for images. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter. You can also filter search terms out in the ``query``
        parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media,
        not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

        Args:
            library: Search within different Shutterstock owned libraries
            added_date: Show images added on the specified date
            added_date_start: Show images added on or after the specified date
            aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by
                the height, such as 1.7778 for a 16:9 image
            added_date_end: Show images added before the specified date
            category: Show images with the specified Shutterstock-defined category; specify a category name or ID
            color: Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that
                use similar colors
            contributor: Show images with the specified contributor names or IDs, allows multiple
            contributor_country: Show images from contributors in one or more specified countries, or start with NOT to
                exclude a country from the search
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            height: (Deprecated; use height_from and height_to instead) Show images with the specified height
            height_from: Show images with the specified height or larger, in pixels
            height_to: Show images with the specified height or smaller, in pixels
            image_type: Show images of the specified type
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only images with the specified license
            model: Show image results with the specified model IDs
            orientation: Show image results with horizontal or vertical orientation
            page: Page number
            per_page: Number of results per page
            people_model_released: Show images of people with a signed model release
            people_age: Show images that feature people of the specified age category
            people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images
                without those ethnicities
            people_gender: Show images with people of the specified gender
            people_number: Show images with the specified number of people
            query: One or more search terms separated by spaces; you can use NOT to filter out images that match a term
            region: Raise or lower search result rankings based on the result's relevance to a specified region; you can
                provide a country code or an IP address from which the API infers a country
            safe: Enable or disable safe search
            sort: Sort by
            spellcheck_query: Spellcheck the search query and return results on suggested spellings
            view: Amount of detail to render in the response
            width: (Deprecated; use width_from and width_to instead) Show images with the specified width
            width_from: Show images with the specified width or larger, in pixels
            width_to: Show images with the specified width or smaller, in pixels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/search"),
            query_params=[
                param[list[LibraryOrStr] | None]("library", library),
                param[Date | None]("added_date", added_date),
                param[Date | None]("added_date_start", added_date_start),
                param[float | None]("aspect_ratio_min", aspect_ratio_min),
                param[float | None]("aspect_ratio_max", aspect_ratio_max),
                param[float | None]("aspect_ratio", aspect_ratio),
                param[Date | None]("added_date_end", added_date_end),
                param[str | None]("category", category),
                param[str | None]("color", color),
                param[list[str] | None]("contributor", contributor),
                param[ContributorCountryModel | ContributorCountryModelDict | None](
                    "contributor_country", contributor_country
                ),
                param[str | None]("fields", fields),
                param[int | None]("height", height),
                param[int | None]("height_from", height_from),
                param[int | None]("height_to", height_to),
                param[list[ImageType2OrStr] | None]("image_type", image_type),
                param[bool | None]("keyword_safe_search", keyword_safe_search),
                param[LanguageOrStr | None]("language", language),
                param[list[LicenseOrStr] | None]("license", license),
                param[list[str] | None]("model", model),
                param[Orientation2OrStr | None]("orientation", orientation),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("people_model_released", people_model_released),
                param[PeopleAge2OrStr | None]("people_age", people_age),
                param[list[PeopleEthnicity2OrStr] | None]("people_ethnicity", people_ethnicity),
                param[PeopleGender2OrStr | None]("people_gender", people_gender),
                param[int | None]("people_number", people_number),
                param[str | None]("query", query),
                param[RegionModel | RegionModelDict | None]("region", region),
                param[bool | None]("safe", safe),
                param[Sort2OrStr | None]("sort", sort),
                param[bool | None]("spellcheck_query", spellcheck_query),
                param[View2OrStr | None]("view", view),
                param[int | None]("width", width),
                param[int | None]("width_from", width_from),
                param[int | None]("width_to", width_to),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ImageSearchResults],
            error_mapper=search_images_error_mapper,
            request_options=request_options,
        )


class AsyncImagesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_image_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddImageCollectionItemsErrorBody]:
        """This endpoint adds one or more images to a collection by image IDs.

        Args:
            id: Collection ID
            body: Array of image IDs to add to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionItemRequest | CollectionItemRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=add_image_collection_items_error_mapper,
            request_options=request_options,
        )

    async def bulk_search_images(
        self,
        body: list[SearchImage | SearchImageDict],
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        aspect_ratio_min: float | None = None,
        aspect_ratio_max: float | None = None,
        aspect_ratio: float | None = None,
        added_date_end: Date | None = None,
        category: str | None = None,
        color: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None,
        fields: str | None = None,
        height: int | None = None,
        height_from: int | None = None,
        height_to: int | None = None,
        image_type: list[ImageType2OrStr] | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[LicenseOrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_model_released: bool | None = None,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity2OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        region: RegionModel | RegionModelDict | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        spellcheck_query: bool | None = True,
        view: View2OrStr | None = None,
        width: int | None = None,
        width_from: int | None = None,
        width_to: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkImageSearchResults, BulkSearchImagesErrorBody]:
        """This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You
        can provide global search parameters in the query parameters and override them for each search in the body
        parameter. The query and body parameters are the same as in the ``GET /v2/images/search`` endpoint.

        Args:
            body: List of queries to request results for and filters to apply per query; these values override the
                defaults in the query parameters
            added_date: Show images added on the specified date
            added_date_start: Show images added on or after the specified date
            aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by
                the height, such as 1.7778 for a 16:9 image
            added_date_end: Show images added before the specified date
            category: Show images with the specified Shutterstock-defined category; specify a category name or ID
            color: Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that
                use similar colors
            contributor: Show images with the specified contributor names or IDs, allows multiple
            contributor_country: Show images from contributors in one or more specified countries, or start with NOT to
                exclude a country from the search
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            height: (Deprecated; use height_from and height_to instead) Show images with the specified height
            height_from: Show images with the specified height or larger, in pixels
            height_to: Show images with the specified height or smaller, in pixels
            image_type: Show images of the specified type
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only images with the specified license
            model: Show image results with the specified model IDs
            orientation: Show image results with horizontal or vertical orientation
            page: Page number
            per_page: Number of results per page
            people_model_released: Show images of people with a signed model release
            people_age: Show images that feature people of the specified age category
            people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images
                without those ethnicities
            people_gender: Show images with people of the specified gender
            people_number: Show images with the specified number of people
            region: Raise or lower search result rankings based on the result's relevance to a specified region; you can
                provide a country code or an IP address from which the API infers a country
            safe: Enable or disable safe search
            sort: Sort by
            spellcheck_query: Spellcheck the search query and return results on suggested spellings
            view: Amount of detail to render in the response
            width: (Deprecated; use width_from and width_to instead) Show images with the specified width
            width_from: Show images with the specified width or larger, in pixels
            width_to: Show images with the specified width or smaller, in pixels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bulk_search/images"),
            query_params=[
                param[Date | None]("added_date", added_date),
                param[Date | None]("added_date_start", added_date_start),
                param[float | None]("aspect_ratio_min", aspect_ratio_min),
                param[float | None]("aspect_ratio_max", aspect_ratio_max),
                param[float | None]("aspect_ratio", aspect_ratio),
                param[Date | None]("added_date_end", added_date_end),
                param[str | None]("category", category),
                param[str | None]("color", color),
                param[list[str] | None]("contributor", contributor),
                param[ContributorCountryModel | ContributorCountryModelDict | None](
                    "contributor_country", contributor_country
                ),
                param[str | None]("fields", fields),
                param[int | None]("height", height),
                param[int | None]("height_from", height_from),
                param[int | None]("height_to", height_to),
                param[list[ImageType2OrStr] | None]("image_type", image_type),
                param[bool | None]("keyword_safe_search", keyword_safe_search),
                param[LanguageOrStr | None]("language", language),
                param[list[LicenseOrStr] | None]("license", license),
                param[list[str] | None]("model", model),
                param[Orientation2OrStr | None]("orientation", orientation),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("people_model_released", people_model_released),
                param[PeopleAge2OrStr | None]("people_age", people_age),
                param[list[PeopleEthnicity2OrStr] | None]("people_ethnicity", people_ethnicity),
                param[PeopleGender2OrStr | None]("people_gender", people_gender),
                param[int | None]("people_number", people_number),
                param[RegionModel | RegionModelDict | None]("region", region),
                param[bool | None]("safe", safe),
                param[Sort2OrStr | None]("sort", sort),
                param[bool | None]("spellcheck_query", spellcheck_query),
                param[View2OrStr | None]("view", view),
                param[int | None]("width", width),
                param[int | None]("width_from", width_from),
                param[int | None]("width_to", width_to),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[SearchImage | SearchImageDict]](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[BulkImageSearchResults],
            error_mapper=bulk_search_images_error_mapper,
            request_options=request_options,
        )

    async def create_image_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionCreateResponse, CreateImageCollectionErrorBody]:
        """This endpoint creates one or more image collections (lightboxes). To add images to the collections, use
        ``POST /v2/images/collections/{id}/items``.

        Args:
            body: The names of the new collections
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/collections"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionCreateRequest | CollectionCreateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionCreateResponse],
            error_mapper=create_image_collection_error_mapper,
            request_options=request_options,
        )

    async def delete_image_collection(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteImageCollectionErrorBody]:
        """This endpoint deletes an image collection.

        Args:
            id: Collection ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/images/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_image_collection_error_mapper,
            request_options=request_options,
        )

    async def delete_image_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteImageCollectionItemsErrorBody]:
        """This endpoint removes one or more images from a collection.

        Args:
            id: Collection ID
            item_id: One or more image IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/images/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[str] | None]("item_id", item_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_image_collection_items_error_mapper,
            request_options=request_options,
        )

    async def download_image(
        self,
        id: str,
        body: RedownloadImage | RedownloadImageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Url, DownloadImageErrorBody]:
        """This endpoint redownloads images that you have already received a license for. The download links in the
        response are valid for 8 hours.

        Args:
            id: License ID
            body: Information about the images to redownload
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/licenses/{id}/downloads"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RedownloadImage | RedownloadImageDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Url],
            error_mapper=download_image_error_mapper,
            request_options=request_options,
        )

    async def get_image(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Image, GetImageErrorBody]:
        """This endpoint shows information about an image, including a URL to a preview image and the sizes that it is
        available in.

        Args:
            id: Image ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Image],
            error_mapper=get_image_error_mapper,
            request_options=request_options,
        )

    async def get_image_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Collection, GetImageCollectionErrorBody]:
        """This endpoint gets more detailed information about a collection, including its cover image and timestamps for
        its creation and most recent update. To get the images in collections, use ``GET
        /v2/images/collections/{id}/items``.

        Args:
            id: Collection ID
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/collections/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[EmbedOrStr] | None]("embed", embed), param[str | None]("share_code", share_code)],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Collection],
            error_mapper=get_image_collection_error_mapper,
            request_options=request_options,
        )

    async def get_image_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionItemDataList, GetImageCollectionItemsErrorBody]:
        """This endpoint lists the IDs of images in a collection and the date that each was added.

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
            url_template=self._server.default("/v2/images/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("share_code", share_code),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionItemDataList],
            error_mapper=get_image_collection_items_error_mapper,
            request_options=request_options,
        )

    async def get_image_collection_list(
        self,
        *,
        embed: list[EmbedOrStr] | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionDataList, GetImageCollectionListErrorBody]:
        """This endpoint lists your collections of images and their basic attributes.

        Args:
            embed: Which sharing information to include in the response, such as a URL to the collection
            page: Page number
            per_page: Number of results per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/collections"),
            query_params=[
                param[list[EmbedOrStr] | None]("embed", embed),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionDataList],
            error_mapper=get_image_collection_list_error_mapper,
            request_options=request_options,
        )

    async def get_image_keyword_suggestions(
        self,
        body: SearchEntitiesRequest | SearchEntitiesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchEntitiesResponse, GetImageKeywordSuggestionsErrorBody]:
        """This endpoint returns up to 10 important keywords from a block of plain text.

        Args:
            body: Plain text to extract keywords from
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/search/suggestions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchEntitiesRequest | SearchEntitiesRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[SearchEntitiesResponse],
            error_mapper=get_image_keyword_suggestions_error_mapper,
            request_options=request_options,
        )

    async def get_image_license_list(
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
    ) -> ApiResult[DownloadHistoryDataList, GetImageLicenseListErrorBody]:
        """This endpoint lists existing licenses.

        Args:
            image_id: Show licenses for the specified image ID
            license: Show images that are available with the specified license, such as ``standard`` or ``enhanced``
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
            url_template=self._server.default("/v2/images/licenses"),
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
            error_mapper=get_image_license_list_error_mapper,
            request_options=request_options,
        )

    async def get_image_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ImageDataList, GetImageListErrorBody]:
        """This endpoint lists information about one or more images, including the available sizes.

        Args:
            id: One or more image IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images"),
            query_params=[
                param[list[str]]("id", id),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ImageDataList],
            error_mapper=get_image_list_error_mapper,
            request_options=request_options,
        )

    async def get_image_recommendations(
        self,
        id: list[str],
        *,
        max_items: int | None = 20,
        safe: bool | None = True,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecommendationDataList, GetImageRecommendationsErrorBody]:
        """This endpoint returns images that customers put in the same collection as the specified image IDs.

        Args:
            id: Image IDs
            max_items: Maximum number of results returned in the response
            safe: Restrict results to safe images
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/recommendations"),
            query_params=[
                param[list[str]]("id", id), param[int | None]("max_items", max_items), param[bool | None]("safe", safe)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[RecommendationDataList],
            error_mapper=get_image_recommendations_error_mapper,
            request_options=request_options,
        )

    async def get_image_suggestions(
        self, query: str, *, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Suggestions, GetImageSuggestionsErrorBody]:
        """This endpoint provides autocomplete suggestions for partial search terms.

        Args:
            query: Search term for which you want keyword suggestions
            limit: Limit the number of suggestions
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/search/suggestions"),
            query_params=[param[str]("query", query), param[int | None]("limit", limit)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Suggestions],
            error_mapper=get_image_suggestions_error_mapper,
            request_options=request_options,
        )

    async def get_updated_images(
        self,
        *,
        type_: list[Type4OrStr] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str | None = "1 HOUR",
        page: int | None = 1,
        per_page: int | None = 100,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatedMediaDataList, RawError]:
        """This endpoint lists images that have been updated in the specified time period to update content management
        systems (CMS) or digital asset management (DAM) systems. In most cases, use the ``interval`` parameter to show
        images that were updated recently, but you can also use the ``start_date`` and ``end_date`` parameters to
        specify a range of no more than three days. Do not use the ``interval`` parameter with either ``start_date`` or
        ``end_date``.

        Args:
            type_: Show images that were added, deleted, or edited; by default, the endpoint returns images that were
                updated in any of these ways
            start_date: Show images updated on or after the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency.
            end_date: Show images updated before the specified date. The API will default to UTC (00:00:00) if no
                specific time is provided, ensuring consistency. Please note that the end date must be at least 5
                minutes after the start date.
            interval: Show images updated in the specified time period, where the time period is an interval (like SQL
                INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were
                updated in the hour preceding the request
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/updated"),
            query_params=[
                param[list[Type4OrStr] | None]("type", type_),
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

    async def license_images(
        self,
        body: LicenseImageRequest | LicenseImageRequestDict,
        *,
        subscription_id: str | None = None,
        format: Format15OrStr | None = None,
        size: Size12OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseImageResultDataList, LicenseImagesErrorBody]:
        """This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and
        other details like the format, size, and subscription ID either in the query parameter or with each image ID in
        the body parameter. Values in the body parameter override values in the query parameters. The download links in
        the response are valid for 8 hours.

        Args:
            body: List of images to request licenses for and information about each license transaction; these values
                override the defaults in the query parameters
            subscription_id: Subscription ID to use to license the image
            format: (Deprecated) Image format
            size: Image size
            search_id: Search ID that was provided in the results of an image search
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/licenses"),
            query_params=[
                param[str | None]("subscription_id", subscription_id),
                param[Format15OrStr | None]("format", format),
                param[Size12OrStr | None]("size", size),
                param[str | None]("search_id", search_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseImageRequest | LicenseImageRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseImageResultDataList],
            error_mapper=license_images_error_mapper,
            request_options=request_options,
        )

    async def list_image_categories(
        self, *, language: LanguageOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoryDataList, ListImageCategoriesErrorBody]:
        """This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

        Args:
            language: Language for the keywords and categories in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/categories"),
            query_params=[param[LanguageOrStr | None]("language", language)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[CategoryDataList],
            error_mapper=list_image_categories_error_mapper,
            request_options=request_options,
        )

    async def list_similar_images(
        self,
        id: str,
        *,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ImageSearchResults, ListSimilarImagesErrorBody]:
        """This endpoint returns images that are visually similar to an image that you specify.

        Args:
            id: Image ID
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/{id}/similar"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ImageSearchResults],
            error_mapper=list_similar_images_error_mapper,
            request_options=request_options,
        )

    async def rename_image_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RenameImageCollectionErrorBody]:
        """This endpoint sets a new name for an image collection.

        Args:
            id: Collection ID
            body: The new name for the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/images/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionUpdateRequest | CollectionUpdateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=rename_image_collection_error_mapper,
            request_options=request_options,
        )

    async def search_images(
        self,
        *,
        library: list[LibraryOrStr] | None = None,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        aspect_ratio_min: float | None = None,
        aspect_ratio_max: float | None = None,
        aspect_ratio: float | None = None,
        added_date_end: Date | None = None,
        category: str | None = None,
        color: str | None = None,
        contributor: list[str] | None = None,
        contributor_country: ContributorCountryModel | ContributorCountryModelDict | None = None,
        fields: str | None = None,
        height: int | None = None,
        height_from: int | None = None,
        height_to: int | None = None,
        image_type: list[ImageType2OrStr] | None = None,
        keyword_safe_search: bool | None = True,
        language: LanguageOrStr | None = None,
        license: list[LicenseOrStr] | None = None,
        model: list[str] | None = None,
        orientation: Orientation2OrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        people_model_released: bool | None = None,
        people_age: PeopleAge2OrStr | None = None,
        people_ethnicity: list[PeopleEthnicity2OrStr] | None = None,
        people_gender: PeopleGender2OrStr | None = None,
        people_number: int | None = None,
        query: str | None = None,
        region: RegionModel | RegionModelDict | None = None,
        safe: bool | None = True,
        sort: Sort2OrStr | None = None,
        spellcheck_query: bool | None = True,
        view: View2OrStr | None = None,
        width: int | None = None,
        width_from: int | None = None,
        width_to: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ImageSearchResults, SearchImagesErrorBody]:
        """This endpoint searches for images. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter. You can also filter search terms out in the ``query``
        parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media,
        not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

        Args:
            library: Search within different Shutterstock owned libraries
            added_date: Show images added on the specified date
            added_date_start: Show images added on or after the specified date
            aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the
                width divided by the height, such as 1.7778 for a 16:9 image
            aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by
                the height, such as 1.7778 for a 16:9 image
            added_date_end: Show images added before the specified date
            category: Show images with the specified Shutterstock-defined category; specify a category name or ID
            color: Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that
                use similar colors
            contributor: Show images with the specified contributor names or IDs, allows multiple
            contributor_country: Show images from contributors in one or more specified countries, or start with NOT to
                exclude a country from the search
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            height: (Deprecated; use height_from and height_to instead) Show images with the specified height
            height_from: Show images with the specified height or larger, in pixels
            height_to: Show images with the specified height or smaller, in pixels
            image_type: Show images of the specified type
            keyword_safe_search: Hide results with potentially unsafe keywords
            language: Set query and result language (uses Accept-Language header if not set)
            license: Show only images with the specified license
            model: Show image results with the specified model IDs
            orientation: Show image results with horizontal or vertical orientation
            page: Page number
            per_page: Number of results per page
            people_model_released: Show images of people with a signed model release
            people_age: Show images that feature people of the specified age category
            people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images
                without those ethnicities
            people_gender: Show images with people of the specified gender
            people_number: Show images with the specified number of people
            query: One or more search terms separated by spaces; you can use NOT to filter out images that match a term
            region: Raise or lower search result rankings based on the result's relevance to a specified region; you can
                provide a country code or an IP address from which the API infers a country
            safe: Enable or disable safe search
            sort: Sort by
            spellcheck_query: Spellcheck the search query and return results on suggested spellings
            view: Amount of detail to render in the response
            width: (Deprecated; use width_from and width_to instead) Show images with the specified width
            width_from: Show images with the specified width or larger, in pixels
            width_to: Show images with the specified width or smaller, in pixels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/images/search"),
            query_params=[
                param[list[LibraryOrStr] | None]("library", library),
                param[Date | None]("added_date", added_date),
                param[Date | None]("added_date_start", added_date_start),
                param[float | None]("aspect_ratio_min", aspect_ratio_min),
                param[float | None]("aspect_ratio_max", aspect_ratio_max),
                param[float | None]("aspect_ratio", aspect_ratio),
                param[Date | None]("added_date_end", added_date_end),
                param[str | None]("category", category),
                param[str | None]("color", color),
                param[list[str] | None]("contributor", contributor),
                param[ContributorCountryModel | ContributorCountryModelDict | None](
                    "contributor_country", contributor_country
                ),
                param[str | None]("fields", fields),
                param[int | None]("height", height),
                param[int | None]("height_from", height_from),
                param[int | None]("height_to", height_to),
                param[list[ImageType2OrStr] | None]("image_type", image_type),
                param[bool | None]("keyword_safe_search", keyword_safe_search),
                param[LanguageOrStr | None]("language", language),
                param[list[LicenseOrStr] | None]("license", license),
                param[list[str] | None]("model", model),
                param[Orientation2OrStr | None]("orientation", orientation),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("people_model_released", people_model_released),
                param[PeopleAge2OrStr | None]("people_age", people_age),
                param[list[PeopleEthnicity2OrStr] | None]("people_ethnicity", people_ethnicity),
                param[PeopleGender2OrStr | None]("people_gender", people_gender),
                param[int | None]("people_number", people_number),
                param[str | None]("query", query),
                param[RegionModel | RegionModelDict | None]("region", region),
                param[bool | None]("safe", safe),
                param[Sort2OrStr | None]("sort", sort),
                param[bool | None]("spellcheck_query", spellcheck_query),
                param[View2OrStr | None]("view", view),
                param[int | None]("width", width),
                param[int | None]("width_from", width_from),
                param[int | None]("width_to", width_to),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ImageSearchResults],
            error_mapper=search_images_error_mapper,
            request_options=request_options,
        )
