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
from ..errors.download_sfx_error import DownloadSfxErrorBody, download_sfx_error_mapper
from ..errors.get_sfx_details_error import GetSfxDetailsErrorBody, get_sfx_details_error_mapper
from ..errors.get_sfx_license_list_error import GetSfxLicenseListErrorBody, get_sfx_license_list_error_mapper
from ..errors.get_sfx_list_details_error import GetSfxListDetailsErrorBody, get_sfx_list_details_error_mapper
from ..errors.licenses_sfx_error import LicensesSfxErrorBody, licenses_sfx_error_mapper
from ..errors.search_sfx_error import SearchSfxErrorBody, search_sfx_error_mapper
from ..models.download_history_data_list import DownloadHistoryDataList
from ..models.enums.download_availability import DownloadAvailabilityOrStr
from ..models.enums.language import LanguageOrStr
from ..models.enums.library2 import Library2OrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.enums.sort15 import Sort15OrStr
from ..models.enums.view2 import View2OrStr
from ..models.license_sfxrequest import LicenseSfxrequest, LicenseSfxrequestDict
from ..models.license_sfxresult_data_list import LicenseSfxresultDataList
from ..models.sfx import Sfx
from ..models.sfx_url import SfxUrl
from ..models.sfxdata_list import SfxdataList
from ..models.sfxsearch_results import SfxsearchResults
from ..server.server import Server


class SoundEffects:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoundEffectsWithRawResponse(client, server, auth)

    def download_sfx(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> SfxUrl:
        """This endpoint redownloads sound effects that you have already received a license for. The download links in
        the response are valid for 8 hours.

        Args:
            id: License ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.download_sfx(id, request_options=request_options).unwrap()

    def get_sfx_details(
        self,
        id: int,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        library: Library2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Sfx:
        """This endpoint shows information about a sound effect.

        Args:
            id: Audio track ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            library: Which library to fetch from
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Service Unavailable ``error`` is ``RawError``."""
        return self._with_raw_response.get_sfx_details(
            id, language=language, view=view, library=library, search_id=search_id, request_options=request_options
        ).unwrap()

    def get_sfx_license_list(
        self,
        *,
        sfx_id: str | None = None,
        license: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        username: str | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        license_id: str | None = None,
        download_availability: DownloadAvailabilityOrStr | None = None,
        team_history: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DownloadHistoryDataList:
        """This endpoint lists existing licenses.

        Args:
            sfx_id: Show licenses for the specified sound effects ID
            license: Show sound effects that are available with the specified license, such as ``standard`` or
                ``enhanced``
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            username: Filter licenses by username of licensee
            start_date: Show licenses created on or after the specified date
            end_date: Show licenses created before the specified date
            license_id: Filter by the license ID
            download_availability: Filter licenses by download availability
            team_history: Set to true to see license history for all members of your team.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_sfx_license_list(
            sfx_id=sfx_id,
            license=license,
            page=page,
            per_page=per_page,
            sort=sort,
            username=username,
            start_date=start_date,
            end_date=end_date,
            license_id=license_id,
            download_availability=download_availability,
            team_history=team_history,
            request_options=request_options,
        ).unwrap()

    def get_sfx_list_details(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        language: LanguageOrStr | None = None,
        library: Library2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SfxdataList:
        """This endpoint shows information about sound effects.

        Args:
            id: One or more sound effect IDs
            view: Amount of detail to render in the response
            language: Language for the keywords and categories in the response
            library: Which library to fetch from
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_sfx_list_details(
            id, view=view, language=language, library=library, search_id=search_id, request_options=request_options
        ).unwrap()

    def licenses_sfx(
        self, body: LicenseSfxrequest | LicenseSfxrequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> LicenseSfxresultDataList:
        """This endpoint licenses sounds effect assets.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.licenses_sfx(body, request_options=request_options).unwrap()

    def search_sfx(
        self,
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        added_date_end: Date | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        safe: bool | None = True,
        sort: Sort15OrStr | None = None,
        view: View2OrStr | None = None,
        language: LanguageOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SfxsearchResults:
        """This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND
        condition.

        Args:
            added_date: Show sound effects added on the specified date
            added_date_start: Show sound effects added on or after the specified date
            added_date_end: Show sound effects added before the specified date
            duration: Show sound effects with the specified duration in seconds
            duration_from: Show sound effects with the specified duration or longer in seconds
            duration_to: Show sound effects with the specified duration or shorter in seconds
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            safe: Enable or disable safe search
            sort: Sort by
            view: Amount of detail to render in the response
            language: Set query and result language (uses Accept-Language header if not set)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Service Unavailable ``error`` is ``RawError``."""
        return self._with_raw_response.search_sfx(
            added_date=added_date,
            added_date_start=added_date_start,
            added_date_end=added_date_end,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            page=page,
            per_page=per_page,
            query=query,
            safe=safe,
            sort=sort,
            view=view,
            language=language,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SoundEffectsWithRawResponse:
        return self._with_raw_response


class AsyncSoundEffects:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoundEffectsWithRawResponse(client, server, auth)

    async def download_sfx(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> SfxUrl:
        """This endpoint redownloads sound effects that you have already received a license for. The download links in
        the response are valid for 8 hours.

        Args:
            id: License ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.download_sfx(id, request_options=request_options)).unwrap()

    async def get_sfx_details(
        self,
        id: int,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        library: Library2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Sfx:
        """This endpoint shows information about a sound effect.

        Args:
            id: Audio track ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            library: Which library to fetch from
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Service Unavailable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_sfx_details(
                id, language=language, view=view, library=library, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def get_sfx_license_list(
        self,
        *,
        sfx_id: str | None = None,
        license: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        username: str | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        license_id: str | None = None,
        download_availability: DownloadAvailabilityOrStr | None = None,
        team_history: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DownloadHistoryDataList:
        """This endpoint lists existing licenses.

        Args:
            sfx_id: Show licenses for the specified sound effects ID
            license: Show sound effects that are available with the specified license, such as ``standard`` or
                ``enhanced``
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            username: Filter licenses by username of licensee
            start_date: Show licenses created on or after the specified date
            end_date: Show licenses created before the specified date
            license_id: Filter by the license ID
            download_availability: Filter licenses by download availability
            team_history: Set to true to see license history for all members of your team.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_sfx_license_list(
                sfx_id=sfx_id,
                license=license,
                page=page,
                per_page=per_page,
                sort=sort,
                username=username,
                start_date=start_date,
                end_date=end_date,
                license_id=license_id,
                download_availability=download_availability,
                team_history=team_history,
                request_options=request_options,
            )
        ).unwrap()

    async def get_sfx_list_details(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        language: LanguageOrStr | None = None,
        library: Library2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SfxdataList:
        """This endpoint shows information about sound effects.

        Args:
            id: One or more sound effect IDs
            view: Amount of detail to render in the response
            language: Language for the keywords and categories in the response
            library: Which library to fetch from
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_sfx_list_details(
                id, view=view, language=language, library=library, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def licenses_sfx(
        self, body: LicenseSfxrequest | LicenseSfxrequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> LicenseSfxresultDataList:
        """This endpoint licenses sounds effect assets.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.licenses_sfx(body, request_options=request_options)).unwrap()

    async def search_sfx(
        self,
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        added_date_end: Date | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        safe: bool | None = True,
        sort: Sort15OrStr | None = None,
        view: View2OrStr | None = None,
        language: LanguageOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SfxsearchResults:
        """This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND
        condition.

        Args:
            added_date: Show sound effects added on the specified date
            added_date_start: Show sound effects added on or after the specified date
            added_date_end: Show sound effects added before the specified date
            duration: Show sound effects with the specified duration in seconds
            duration_from: Show sound effects with the specified duration or longer in seconds
            duration_to: Show sound effects with the specified duration or shorter in seconds
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            safe: Enable or disable safe search
            sort: Sort by
            view: Amount of detail to render in the response
            language: Set query and result language (uses Accept-Language header if not set)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Service Unavailable ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_sfx(
                added_date=added_date,
                added_date_start=added_date_start,
                added_date_end=added_date_end,
                duration=duration,
                duration_from=duration_from,
                duration_to=duration_to,
                page=page,
                per_page=per_page,
                query=query,
                safe=safe,
                sort=sort,
                view=view,
                language=language,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoundEffectsWithRawResponse:
        return self._with_raw_response


class SoundEffectsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def download_sfx(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SfxUrl, DownloadSfxErrorBody]:
        """This endpoint redownloads sound effects that you have already received a license for. The download links in
        the response are valid for 8 hours.

        Args:
            id: License ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/sfx/licenses/{id}/downloads"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[SfxUrl],
            error_mapper=download_sfx_error_mapper,
            request_options=request_options,
        )

    def get_sfx_details(
        self,
        id: int,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        library: Library2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Sfx, GetSfxDetailsErrorBody]:
        """This endpoint shows information about a sound effect.

        Args:
            id: Audio track ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            library: Which library to fetch from
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sfx/{id}"),
            path_params=[param[int]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[View2OrStr | None]("view", view),
                param[Library2OrStr | None]("library", library),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Sfx],
            error_mapper=get_sfx_details_error_mapper,
            request_options=request_options,
        )

    def get_sfx_license_list(
        self,
        *,
        sfx_id: str | None = None,
        license: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        username: str | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        license_id: str | None = None,
        download_availability: DownloadAvailabilityOrStr | None = None,
        team_history: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DownloadHistoryDataList, GetSfxLicenseListErrorBody]:
        """This endpoint lists existing licenses.

        Args:
            sfx_id: Show licenses for the specified sound effects ID
            license: Show sound effects that are available with the specified license, such as ``standard`` or
                ``enhanced``
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            username: Filter licenses by username of licensee
            start_date: Show licenses created on or after the specified date
            end_date: Show licenses created before the specified date
            license_id: Filter by the license ID
            download_availability: Filter licenses by download availability
            team_history: Set to true to see license history for all members of your team.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sfx/licenses"),
            query_params=[
                param[str | None]("sfx_id", sfx_id),
                param[str | None]("license", license),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
                param[str | None]("username", username),
                param[RFC3339DateTime | None]("start_date", start_date),
                param[RFC3339DateTime | None]("end_date", end_date),
                param[str | None]("license_id", license_id),
                param[DownloadAvailabilityOrStr | None]("download_availability", download_availability),
                param[bool | None]("team_history", team_history),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[DownloadHistoryDataList],
            error_mapper=get_sfx_license_list_error_mapper,
            request_options=request_options,
        )

    def get_sfx_list_details(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        language: LanguageOrStr | None = None,
        library: Library2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SfxdataList, GetSfxListDetailsErrorBody]:
        """This endpoint shows information about sound effects.

        Args:
            id: One or more sound effect IDs
            view: Amount of detail to render in the response
            language: Language for the keywords and categories in the response
            library: Which library to fetch from
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sfx"),
            query_params=[
                param[list[str]]("id", id),
                param[View2OrStr | None]("view", view),
                param[LanguageOrStr | None]("language", language),
                param[Library2OrStr | None]("library", library),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[SfxdataList],
            error_mapper=get_sfx_list_details_error_mapper,
            request_options=request_options,
        )

    def licenses_sfx(
        self, body: LicenseSfxrequest | LicenseSfxrequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LicenseSfxresultDataList, LicensesSfxErrorBody]:
        """This endpoint licenses sounds effect assets.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/sfx/licenses"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseSfxrequest | LicenseSfxrequestDict](body),
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[LicenseSfxresultDataList],
            error_mapper=licenses_sfx_error_mapper,
            request_options=request_options,
        )

    def search_sfx(
        self,
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        added_date_end: Date | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        safe: bool | None = True,
        sort: Sort15OrStr | None = None,
        view: View2OrStr | None = None,
        language: LanguageOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SfxsearchResults, SearchSfxErrorBody]:
        """This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND
        condition.

        Args:
            added_date: Show sound effects added on the specified date
            added_date_start: Show sound effects added on or after the specified date
            added_date_end: Show sound effects added before the specified date
            duration: Show sound effects with the specified duration in seconds
            duration_from: Show sound effects with the specified duration or longer in seconds
            duration_to: Show sound effects with the specified duration or shorter in seconds
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            safe: Enable or disable safe search
            sort: Sort by
            view: Amount of detail to render in the response
            language: Set query and result language (uses Accept-Language header if not set)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sfx/search"),
            query_params=[
                param[Date | None]("added_date", added_date),
                param[Date | None]("added_date_start", added_date_start),
                param[Date | None]("added_date_end", added_date_end),
                param[int | None]("duration", duration),
                param[int | None]("duration_from", duration_from),
                param[int | None]("duration_to", duration_to),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("query", query),
                param[bool | None]("safe", safe),
                param[Sort15OrStr | None]("sort", sort),
                param[View2OrStr | None]("view", view),
                param[LanguageOrStr | None]("language", language),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[SfxsearchResults],
            error_mapper=search_sfx_error_mapper,
            request_options=request_options,
        )


class AsyncSoundEffectsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def download_sfx(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SfxUrl, DownloadSfxErrorBody]:
        """This endpoint redownloads sound effects that you have already received a license for. The download links in
        the response are valid for 8 hours.

        Args:
            id: License ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/sfx/licenses/{id}/downloads"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[SfxUrl],
            error_mapper=download_sfx_error_mapper,
            request_options=request_options,
        )

    async def get_sfx_details(
        self,
        id: int,
        *,
        language: LanguageOrStr | None = None,
        view: View2OrStr | None = None,
        library: Library2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Sfx, GetSfxDetailsErrorBody]:
        """This endpoint shows information about a sound effect.

        Args:
            id: Audio track ID
            language: Language for the keywords and categories in the response
            view: Amount of detail to render in the response
            library: Which library to fetch from
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sfx/{id}"),
            path_params=[param[int]("id", id)],
            query_params=[
                param[LanguageOrStr | None]("language", language),
                param[View2OrStr | None]("view", view),
                param[Library2OrStr | None]("library", library),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Sfx],
            error_mapper=get_sfx_details_error_mapper,
            request_options=request_options,
        )

    async def get_sfx_license_list(
        self,
        *,
        sfx_id: str | None = None,
        license: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: Sort5OrStr | None = None,
        username: str | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        license_id: str | None = None,
        download_availability: DownloadAvailabilityOrStr | None = None,
        team_history: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DownloadHistoryDataList, GetSfxLicenseListErrorBody]:
        """This endpoint lists existing licenses.

        Args:
            sfx_id: Show licenses for the specified sound effects ID
            license: Show sound effects that are available with the specified license, such as ``standard`` or
                ``enhanced``
            page: Page number
            per_page: Number of results per page
            sort: Sort order
            username: Filter licenses by username of licensee
            start_date: Show licenses created on or after the specified date
            end_date: Show licenses created before the specified date
            license_id: Filter by the license ID
            download_availability: Filter licenses by download availability
            team_history: Set to true to see license history for all members of your team.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sfx/licenses"),
            query_params=[
                param[str | None]("sfx_id", sfx_id),
                param[str | None]("license", license),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Sort5OrStr | None]("sort", sort),
                param[str | None]("username", username),
                param[RFC3339DateTime | None]("start_date", start_date),
                param[RFC3339DateTime | None]("end_date", end_date),
                param[str | None]("license_id", license_id),
                param[DownloadAvailabilityOrStr | None]("download_availability", download_availability),
                param[bool | None]("team_history", team_history),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[DownloadHistoryDataList],
            error_mapper=get_sfx_license_list_error_mapper,
            request_options=request_options,
        )

    async def get_sfx_list_details(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        language: LanguageOrStr | None = None,
        library: Library2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SfxdataList, GetSfxListDetailsErrorBody]:
        """This endpoint shows information about sound effects.

        Args:
            id: One or more sound effect IDs
            view: Amount of detail to render in the response
            language: Language for the keywords and categories in the response
            library: Which library to fetch from
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sfx"),
            query_params=[
                param[list[str]]("id", id),
                param[View2OrStr | None]("view", view),
                param[LanguageOrStr | None]("language", language),
                param[Library2OrStr | None]("library", library),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[SfxdataList],
            error_mapper=get_sfx_list_details_error_mapper,
            request_options=request_options,
        )

    async def licenses_sfx(
        self, body: LicenseSfxrequest | LicenseSfxrequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LicenseSfxresultDataList, LicensesSfxErrorBody]:
        """This endpoint licenses sounds effect assets.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/sfx/licenses"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseSfxrequest | LicenseSfxrequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[LicenseSfxresultDataList],
            error_mapper=licenses_sfx_error_mapper,
            request_options=request_options,
        )

    async def search_sfx(
        self,
        *,
        added_date: Date | None = None,
        added_date_start: Date | None = None,
        added_date_end: Date | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        safe: bool | None = True,
        sort: Sort15OrStr | None = None,
        view: View2OrStr | None = None,
        language: LanguageOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SfxsearchResults, SearchSfxErrorBody]:
        """This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND
        condition.

        Args:
            added_date: Show sound effects added on the specified date
            added_date_start: Show sound effects added on or after the specified date
            added_date_end: Show sound effects added before the specified date
            duration: Show sound effects with the specified duration in seconds
            duration_from: Show sound effects with the specified duration or longer in seconds
            duration_to: Show sound effects with the specified duration or shorter in seconds
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            safe: Enable or disable safe search
            sort: Sort by
            view: Amount of detail to render in the response
            language: Set query and result language (uses Accept-Language header if not set)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sfx/search"),
            query_params=[
                param[Date | None]("added_date", added_date),
                param[Date | None]("added_date_start", added_date_start),
                param[Date | None]("added_date_end", added_date_end),
                param[int | None]("duration", duration),
                param[int | None]("duration_from", duration_from),
                param[int | None]("duration_to", duration_to),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("query", query),
                param[bool | None]("safe", safe),
                param[Sort15OrStr | None]("sort", sort),
                param[View2OrStr | None]("view", view),
                param[LanguageOrStr | None]("language", language),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[SfxsearchResults],
            error_mapper=search_sfx_error_mapper,
            request_options=request_options,
        )
