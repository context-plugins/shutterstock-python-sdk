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
    json_body,
    json_decoder,
    param,
)
from ..errors.get_keywords_error import GetKeywordsErrorBody, get_keywords_error_mapper
from ..errors.get_similar_images_error import GetSimilarImagesErrorBody, get_similar_images_error_mapper
from ..errors.get_similar_videos_error import GetSimilarVideosErrorBody, get_similar_videos_error_mapper
from ..errors.upload_image_error import UploadImageErrorBody, upload_image_error_mapper
from ..models.computer_vision_image_create_response import ComputerVisionImageCreateResponse
from ..models.enums.language import LanguageOrStr
from ..models.enums.license9 import License9OrStr
from ..models.enums.view2 import View2OrStr
from ..models.image_create_request import ImageCreateRequest, ImageCreateRequestDict
from ..models.image_search_results import ImageSearchResults
from ..models.keyword_data_list import KeywordDataList
from ..models.unions.asset_id import AssetId, AssetIdDict
from ..models.video_search_results import VideoSearchResults
from ..server.server import Server


class ComputerVision:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ComputerVisionWithRawResponse(client, server, auth)

    def get_keywords(
        self, asset_id: AssetId | AssetIdDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> KeywordDataList:
        """This endpoint returns a list of suggested keywords for a media item that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to suggest keywords for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Unsupported Media Type ``error`` is ``RawError``."""
        return self._with_raw_response.get_keywords(asset_id, request_options=request_options).unwrap()

    def get_similar_images(
        self,
        asset_id: str,
        *,
        license: list[License9OrStr] | None = None,
        safe: bool | None = True,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ImageSearchResults:
        """This endpoint returns images that are visually similar to an image that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to find similar images for
            license: Show only images with the specified license
            safe: Enable or disable safe search
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_similar_images(
            asset_id,
            license=license,
            safe=safe,
            language=language,
            page=page,
            per_page=per_page,
            view=view,
            request_options=request_options,
        ).unwrap()

    def get_similar_videos(
        self,
        asset_id: str,
        *,
        license: list[License9OrStr] | None = None,
        safe: bool | None = True,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoSearchResults:
        """This endpoint returns videos that are visually similar to an image that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to find similar videos for
            license: Show only videos with the specified license
            safe: Enable or disable safe search
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_similar_videos(
            asset_id,
            license=license,
            safe=safe,
            language=language,
            page=page,
            per_page=per_page,
            view=view,
            request_options=request_options,
        ).unwrap()

    def upload_image(
        self, body: ImageCreateRequest | ImageCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComputerVisionImageCreateResponse:
        """This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To
        get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET
        /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

        Args:
            body: A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000
                pixels in width or height
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Payload Too Large Unsupported Media Type ``error`` is
                ``RawError``."""
        return self._with_raw_response.upload_image(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ComputerVisionWithRawResponse:
        return self._with_raw_response


class AsyncComputerVision:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncComputerVisionWithRawResponse(client, server, auth)

    async def get_keywords(
        self, asset_id: AssetId | AssetIdDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> KeywordDataList:
        """This endpoint returns a list of suggested keywords for a media item that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to suggest keywords for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Unsupported Media Type ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_keywords(asset_id, request_options=request_options)).unwrap()

    async def get_similar_images(
        self,
        asset_id: str,
        *,
        license: list[License9OrStr] | None = None,
        safe: bool | None = True,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ImageSearchResults:
        """This endpoint returns images that are visually similar to an image that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to find similar images for
            license: Show only images with the specified license
            safe: Enable or disable safe search
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
            await self._with_raw_response.get_similar_images(
                asset_id,
                license=license,
                safe=safe,
                language=language,
                page=page,
                per_page=per_page,
                view=view,
                request_options=request_options,
            )
        ).unwrap()

    async def get_similar_videos(
        self,
        asset_id: str,
        *,
        license: list[License9OrStr] | None = None,
        safe: bool | None = True,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoSearchResults:
        """This endpoint returns videos that are visually similar to an image that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to find similar videos for
            license: Show only videos with the specified license
            safe: Enable or disable safe search
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
            await self._with_raw_response.get_similar_videos(
                asset_id,
                license=license,
                safe=safe,
                language=language,
                page=page,
                per_page=per_page,
                view=view,
                request_options=request_options,
            )
        ).unwrap()

    async def upload_image(
        self, body: ImageCreateRequest | ImageCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComputerVisionImageCreateResponse:
        """This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To
        get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET
        /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

        Args:
            body: A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000
                pixels in width or height
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Payload Too Large Unsupported Media Type ``error`` is
                ``RawError``."""
        return (await self._with_raw_response.upload_image(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncComputerVisionWithRawResponse:
        return self._with_raw_response


class ComputerVisionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_keywords(
        self, asset_id: AssetId | AssetIdDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[KeywordDataList, GetKeywordsErrorBody]:
        """This endpoint returns a list of suggested keywords for a media item that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to suggest keywords for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cv/keywords"),
            query_params=[param[AssetId | AssetIdDict]("asset_id", asset_id)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[KeywordDataList],
            error_mapper=get_keywords_error_mapper,
            request_options=request_options,
        )

    def get_similar_images(
        self,
        asset_id: str,
        *,
        license: list[License9OrStr] | None = None,
        safe: bool | None = True,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ImageSearchResults, GetSimilarImagesErrorBody]:
        """This endpoint returns images that are visually similar to an image that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to find similar images for
            license: Show only images with the specified license
            safe: Enable or disable safe search
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cv/similar/images"),
            query_params=[
                param[str]("asset_id", asset_id),
                param[list[License9OrStr] | None]("license", license),
                param[bool | None]("safe", safe),
                param[LanguageOrStr | None]("language", language),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ImageSearchResults],
            error_mapper=get_similar_images_error_mapper,
            request_options=request_options,
        )

    def get_similar_videos(
        self,
        asset_id: str,
        *,
        license: list[License9OrStr] | None = None,
        safe: bool | None = True,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoSearchResults, GetSimilarVideosErrorBody]:
        """This endpoint returns videos that are visually similar to an image that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to find similar videos for
            license: Show only videos with the specified license
            safe: Enable or disable safe search
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cv/similar/videos"),
            query_params=[
                param[str]("asset_id", asset_id),
                param[list[License9OrStr] | None]("license", license),
                param[bool | None]("safe", safe),
                param[LanguageOrStr | None]("language", language),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[VideoSearchResults],
            error_mapper=get_similar_videos_error_mapper,
            request_options=request_options,
        )

    def upload_image(
        self, body: ImageCreateRequest | ImageCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComputerVisionImageCreateResponse, UploadImageErrorBody]:
        """This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To
        get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET
        /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

        Args:
            body: A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000
                pixels in width or height
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/cv/images"),
            body=json_body[ImageCreateRequest | ImageCreateRequestDict](body),
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ComputerVisionImageCreateResponse],
            error_mapper=upload_image_error_mapper,
            request_options=request_options,
        )


class AsyncComputerVisionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_keywords(
        self, asset_id: AssetId | AssetIdDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[KeywordDataList, GetKeywordsErrorBody]:
        """This endpoint returns a list of suggested keywords for a media item that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to suggest keywords for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cv/keywords"),
            query_params=[param[AssetId | AssetIdDict]("asset_id", asset_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[KeywordDataList],
            error_mapper=get_keywords_error_mapper,
            request_options=request_options,
        )

    async def get_similar_images(
        self,
        asset_id: str,
        *,
        license: list[License9OrStr] | None = None,
        safe: bool | None = True,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ImageSearchResults, GetSimilarImagesErrorBody]:
        """This endpoint returns images that are visually similar to an image that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to find similar images for
            license: Show only images with the specified license
            safe: Enable or disable safe search
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cv/similar/images"),
            query_params=[
                param[str]("asset_id", asset_id),
                param[list[License9OrStr] | None]("license", license),
                param[bool | None]("safe", safe),
                param[LanguageOrStr | None]("language", language),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ImageSearchResults],
            error_mapper=get_similar_images_error_mapper,
            request_options=request_options,
        )

    async def get_similar_videos(
        self,
        asset_id: str,
        *,
        license: list[License9OrStr] | None = None,
        safe: bool | None = True,
        language: LanguageOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        view: View2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoSearchResults, GetSimilarVideosErrorBody]:
        """This endpoint returns videos that are visually similar to an image that you specify or upload.

        Args:
            asset_id: The asset ID or upload ID to find similar videos for
            license: Show only videos with the specified license
            safe: Enable or disable safe search
            language: Language for the keywords and categories in the response
            page: Page number
            per_page: Number of results per page
            view: Amount of detail to render in the response
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cv/similar/videos"),
            query_params=[
                param[str]("asset_id", asset_id),
                param[list[License9OrStr] | None]("license", license),
                param[bool | None]("safe", safe),
                param[LanguageOrStr | None]("language", language),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[View2OrStr | None]("view", view),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[VideoSearchResults],
            error_mapper=get_similar_videos_error_mapper,
            request_options=request_options,
        )

    async def upload_image(
        self, body: ImageCreateRequest | ImageCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComputerVisionImageCreateResponse, UploadImageErrorBody]:
        """This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To
        get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET
        /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

        Args:
            body: A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000
                pixels in width or height
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/cv/images"),
            body=json_body[ImageCreateRequest | ImageCreateRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[ComputerVisionImageCreateResponse],
            error_mapper=upload_image_error_mapper,
            request_options=request_options,
        )
