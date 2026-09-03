from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
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
from ..errors.add_track_collection_items_error import (
    AddTrackCollectionItemsErrorBody,
    add_track_collection_items_error_mapper,
)
from ..errors.create_track_collection_error import CreateTrackCollectionErrorBody, create_track_collection_error_mapper
from ..errors.delete_track_collection_error import DeleteTrackCollectionErrorBody, delete_track_collection_error_mapper
from ..errors.delete_track_collection_items_error import (
    DeleteTrackCollectionItemsErrorBody,
    delete_track_collection_items_error_mapper,
)
from ..errors.download_tracks_error import DownloadTracksErrorBody, download_tracks_error_mapper
from ..errors.get_track_collection_error import GetTrackCollectionErrorBody, get_track_collection_error_mapper
from ..errors.get_track_collection_items_error import (
    GetTrackCollectionItemsErrorBody,
    get_track_collection_items_error_mapper,
)
from ..errors.get_track_collection_list_error import (
    GetTrackCollectionListErrorBody,
    get_track_collection_list_error_mapper,
)
from ..errors.get_track_error import GetTrackErrorBody, get_track_error_mapper
from ..errors.get_track_license_list_error import GetTrackLicenseListErrorBody, get_track_license_list_error_mapper
from ..errors.get_track_list_error import GetTrackListErrorBody, get_track_list_error_mapper
from ..errors.license_track_error import LicenseTrackErrorBody, license_track_error_mapper
from ..errors.rename_track_collection_error import RenameTrackCollectionErrorBody, rename_track_collection_error_mapper
from ..errors.search_tracks_error import SearchTracksErrorBody, search_tracks_error_mapper
from ..models.audio import Audio
from ..models.audio_data_list import AudioDataList
from ..models.audio_search_results import AudioSearchResults
from ..models.audio_url import AudioUrl
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
from ..models.enums.library1 import Library1OrStr
from ..models.enums.license10 import License10OrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.enums.sort12 import Sort12OrStr
from ..models.enums.sort_order import SortOrderOrStr
from ..models.enums.view2 import View2OrStr
from ..models.genre_list import GenreList
from ..models.instrument_list import InstrumentList
from ..models.license_audio_request import LicenseAudioRequest, LicenseAudioRequestDict
from ..models.license_audio_result_data_list import LicenseAudioResultDataList
from ..models.mood_list import MoodList
from ..server.server import Server


class AudioApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AudioApiWithRawResponse(client, server, auth)

    def add_track_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint adds one or more tracks to a collection by track IDs.

        Args:
            id: Collection ID
            body: List of items to add to collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully added collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.add_track_collection_items(id, body, request_options=request_options).unwrap()

    def create_track_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionCreateResponse:
        """This endpoint creates one or more collections (soundboxes). To add tracks, use ``POST
        /v2/audio/collections/{id}/items``.

        Args:
            body: Collection metadata
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully created audio collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.create_track_collection(body, request_options=request_options).unwrap()

    def delete_track_collection(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This endpoint deletes a collection.

        Args:
            id: Collection ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully deleted collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_track_collection(id, request_options=request_options).unwrap()

    def delete_track_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint removes one or more tracks from a collection.

        Args:
            id: Collection ID
            item_id: One or more item IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully removed collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_track_collection_items(
            id, item_id=item_id, request_options=request_options
        ).unwrap()

    def download_tracks(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> AudioUrl:
        """This endpoint redownloads tracks that you have already received a license for. The download links in the
        response are valid for 8 hours.

        Args:
            id: License ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.download_tracks(id, request_options=request_options).unwrap()

    def get_track(
        self,
        id: int,
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Audio:
        """This endpoint shows information about a track, including its genres, instruments, and other attributes.

        Args:
            id: Audio track ID
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_track(
            id, view=view, search_id=search_id, request_options=request_options
        ).unwrap()

    def get_track_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Collection:
        """This endpoint gets more detailed information about a collection, including the number of items in it and when
        it was last updated. To get the tracks in collections, use ``GET /v2/audio/collections/{id}/items``.

        Args:
            id: Collection ID
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_track_collection(
            id, embed=embed, share_code=share_code, request_options=request_options
        ).unwrap()

    def get_track_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionItemDataList:
        """This endpoint lists the IDs of tracks in a collection and the date that each was added.

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
        return self._with_raw_response.get_track_collection_items(
            id, page=page, per_page=per_page, share_code=share_code, sort=sort, request_options=request_options
        ).unwrap()

    def get_track_collection_list(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        embed: list[EmbedOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionDataList:
        """This endpoint lists your collections of audio tracks and their basic attributes.

        Args:
            page: Page number
            per_page: Number of results per page
            embed: Which sharing information to include in the response, such as a URL to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_track_collection_list(
            page=page, per_page=per_page, embed=embed, request_options=request_options
        ).unwrap()

    def get_track_license_list(
        self,
        *,
        audio_id: str | None = None,
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
        """This endpoint lists existing licenses. You can filter the results according to the track ID to see if you
        have an existing license for a specific track.

        Args:
            audio_id: Show licenses for the specified track ID
            license: Restrict results by license.
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
        return self._with_raw_response.get_track_license_list(
            audio_id=audio_id,
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

    def get_track_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AudioDataList:
        """This endpoint lists information about one or more audio tracks, including the description and publication
        date.

        Args:
            id: One or more audio IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_track_list(
            id, view=view, search_id=search_id, request_options=request_options
        ).unwrap()

    def license_track(
        self,
        body: LicenseAudioRequest | LicenseAudioRequestDict,
        *,
        license: License10OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseAudioResultDataList:
        """This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

        Args:
            body: Tracks to license
            license: License type
            search_id: The ID of the search that led to licensing this track
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.license_track(
            body, license=license, search_id=search_id, request_options=request_options
        ).unwrap()

    def list_genres(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GenreList:
        """This endpoint returns a list of all audio genres.

        Args:
            language: Which language the genres will be returned
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_genres(language=language, request_options=request_options).unwrap()

    def list_instruments(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InstrumentList:
        """This endpoint returns a list of all audio instruments.

        Args:
            language: Which language the instruments will be returned in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_instruments(language=language, request_options=request_options).unwrap()

    def list_moods(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> MoodList:
        """This endpoint returns a list of all audio moods.

        Args:
            language: Which language the moods will be returned in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_moods(language=language, request_options=request_options).unwrap()

    def rename_track_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint sets a new name for a collection.

        Args:
            id: Collection ID
            body: Collection changes
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully updated collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return self._with_raw_response.rename_track_collection(id, body, request_options=request_options).unwrap()

    def search_tracks(
        self,
        *,
        artists: list[str] | None = None,
        bpm: int | None = None,
        bpm_from: int | None = None,
        bpm_to: int | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        genre: list[str] | None = None,
        is_instrumental: bool | None = None,
        instruments: list[str] | None = None,
        moods: list[str] | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        sort: Sort12OrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        vocal_description: str | None = None,
        view: View2OrStr | None = None,
        fields: str | None = None,
        library: Library1OrStr | None = None,
        language: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AudioSearchResults:
        """This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter.

        Args:
            artists: Show tracks with one of the specified artist names or IDs
            bpm: (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute
            bpm_from: Show tracks with the specified beats per minute or faster
            bpm_to: Show tracks with the specified beats per minute or slower
            duration: Show tracks with the specified duration in seconds
            duration_from: Show tracks with the specified duration or longer in seconds
            duration_to: Show tracks with the specified duration or shorter in seconds
            genre: Show tracks with each of the specified genres; to get the list of genres, use ``GET
                /v2/audio/genres``
            is_instrumental: Show instrumental music only
            instruments: Show tracks with each of the specified instruments; to get the list of instruments, use ``GET
                /v2/audio/instruments``
            moods: Show tracks with each of the specified moods; to get the list of moods, use ``GET /v2/audio/moods``
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            sort: Sort by
            sort_order: Sort order
            vocal_description: Show tracks with the specified vocal description (male, female)
            view: Amount of detail to render in the response
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            library: Which library to search
            language: Which language to search in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.search_tracks(
            artists=artists,
            bpm=bpm,
            bpm_from=bpm_from,
            bpm_to=bpm_to,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            genre=genre,
            is_instrumental=is_instrumental,
            instruments=instruments,
            moods=moods,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            sort_order=sort_order,
            vocal_description=vocal_description,
            view=view,
            fields=fields,
            library=library,
            language=language,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> AudioApiWithRawResponse:
        return self._with_raw_response


class AsyncAudioApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAudioApiWithRawResponse(client, server, auth)

    async def add_track_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint adds one or more tracks to a collection by track IDs.

        Args:
            id: Collection ID
            body: List of items to add to collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully added collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_track_collection_items(id, body, request_options=request_options)
        ).unwrap()

    async def create_track_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionCreateResponse:
        """This endpoint creates one or more collections (soundboxes). To add tracks, use ``POST
        /v2/audio/collections/{id}/items``.

        Args:
            body: Collection metadata
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully created audio collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_track_collection(body, request_options=request_options)).unwrap()

    async def delete_track_collection(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This endpoint deletes a collection.

        Args:
            id: Collection ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully deleted collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_track_collection(id, request_options=request_options)).unwrap()

    async def delete_track_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint removes one or more tracks from a collection.

        Args:
            id: Collection ID
            item_id: One or more item IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully removed collection items

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_track_collection_items(
                id, item_id=item_id, request_options=request_options
            )
        ).unwrap()

    async def download_tracks(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> AudioUrl:
        """This endpoint redownloads tracks that you have already received a license for. The download links in the
        response are valid for 8 hours.

        Args:
            id: License ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.download_tracks(id, request_options=request_options)).unwrap()

    async def get_track(
        self,
        id: int,
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Audio:
        """This endpoint shows information about a track, including its genres, instruments, and other attributes.

        Args:
            id: Audio track ID
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_track(id, view=view, search_id=search_id, request_options=request_options)
        ).unwrap()

    async def get_track_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Collection:
        """This endpoint gets more detailed information about a collection, including the number of items in it and when
        it was last updated. To get the tracks in collections, use ``GET /v2/audio/collections/{id}/items``.

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
            await self._with_raw_response.get_track_collection(
                id, embed=embed, share_code=share_code, request_options=request_options
            )
        ).unwrap()

    async def get_track_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionItemDataList:
        """This endpoint lists the IDs of tracks in a collection and the date that each was added.

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
            await self._with_raw_response.get_track_collection_items(
                id, page=page, per_page=per_page, share_code=share_code, sort=sort, request_options=request_options
            )
        ).unwrap()

    async def get_track_collection_list(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        embed: list[EmbedOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CollectionDataList:
        """This endpoint lists your collections of audio tracks and their basic attributes.

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
            await self._with_raw_response.get_track_collection_list(
                page=page, per_page=per_page, embed=embed, request_options=request_options
            )
        ).unwrap()

    async def get_track_license_list(
        self,
        *,
        audio_id: str | None = None,
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
        """This endpoint lists existing licenses. You can filter the results according to the track ID to see if you
        have an existing license for a specific track.

        Args:
            audio_id: Show licenses for the specified track ID
            license: Restrict results by license.
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
            await self._with_raw_response.get_track_license_list(
                audio_id=audio_id,
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

    async def get_track_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AudioDataList:
        """This endpoint lists information about one or more audio tracks, including the description and publication
        date.

        Args:
            id: One or more audio IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_track_list(
                id, view=view, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def license_track(
        self,
        body: LicenseAudioRequest | LicenseAudioRequestDict,
        *,
        license: License10OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LicenseAudioResultDataList:
        """This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

        Args:
            body: Tracks to license
            license: License type
            search_id: The ID of the search that led to licensing this track
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.license_track(
                body, license=license, search_id=search_id, request_options=request_options
            )
        ).unwrap()

    async def list_genres(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GenreList:
        """This endpoint returns a list of all audio genres.

        Args:
            language: Which language the genres will be returned
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_genres(language=language, request_options=request_options)).unwrap()

    async def list_instruments(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InstrumentList:
        """This endpoint returns a list of all audio instruments.

        Args:
            language: Which language the instruments will be returned in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_instruments(language=language, request_options=request_options)
        ).unwrap()

    async def list_moods(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> MoodList:
        """This endpoint returns a list of all audio moods.

        Args:
            language: Which language the moods will be returned in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_moods(language=language, request_options=request_options)).unwrap()

    async def rename_track_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint sets a new name for a collection.

        Args:
            id: Collection ID
            body: Collection changes
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully updated collection

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Collection not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.rename_track_collection(id, body, request_options=request_options)
        ).unwrap()

    async def search_tracks(
        self,
        *,
        artists: list[str] | None = None,
        bpm: int | None = None,
        bpm_from: int | None = None,
        bpm_to: int | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        genre: list[str] | None = None,
        is_instrumental: bool | None = None,
        instruments: list[str] | None = None,
        moods: list[str] | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        sort: Sort12OrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        vocal_description: str | None = None,
        view: View2OrStr | None = None,
        fields: str | None = None,
        library: Library1OrStr | None = None,
        language: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AudioSearchResults:
        """This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter.

        Args:
            artists: Show tracks with one of the specified artist names or IDs
            bpm: (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute
            bpm_from: Show tracks with the specified beats per minute or faster
            bpm_to: Show tracks with the specified beats per minute or slower
            duration: Show tracks with the specified duration in seconds
            duration_from: Show tracks with the specified duration or longer in seconds
            duration_to: Show tracks with the specified duration or shorter in seconds
            genre: Show tracks with each of the specified genres; to get the list of genres, use ``GET
                /v2/audio/genres``
            is_instrumental: Show instrumental music only
            instruments: Show tracks with each of the specified instruments; to get the list of instruments, use ``GET
                /v2/audio/instruments``
            moods: Show tracks with each of the specified moods; to get the list of moods, use ``GET /v2/audio/moods``
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            sort: Sort by
            sort_order: Sort order
            vocal_description: Show tracks with the specified vocal description (male, female)
            view: Amount of detail to render in the response
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            library: Which library to search
            language: Which language to search in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_tracks(
                artists=artists,
                bpm=bpm,
                bpm_from=bpm_from,
                bpm_to=bpm_to,
                duration=duration,
                duration_from=duration_from,
                duration_to=duration_to,
                genre=genre,
                is_instrumental=is_instrumental,
                instruments=instruments,
                moods=moods,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                sort_order=sort_order,
                vocal_description=vocal_description,
                view=view,
                fields=fields,
                library=library,
                language=language,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAudioApiWithRawResponse:
        return self._with_raw_response


class AudioApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_track_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddTrackCollectionItemsErrorBody]:
        """This endpoint adds one or more tracks to a collection by track IDs.

        Args:
            id: Collection ID
            body: List of items to add to collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionItemRequest | CollectionItemRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=add_track_collection_items_error_mapper,
            request_options=request_options,
        )

    def create_track_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionCreateResponse, CreateTrackCollectionErrorBody]:
        """This endpoint creates one or more collections (soundboxes). To add tracks, use ``POST
        /v2/audio/collections/{id}/items``.

        Args:
            body: Collection metadata
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/collections"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionCreateRequest | CollectionCreateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionCreateResponse],
            error_mapper=create_track_collection_error_mapper,
            request_options=request_options,
        )

    def delete_track_collection(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTrackCollectionErrorBody]:
        """This endpoint deletes a collection.

        Args:
            id: Collection ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/audio/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_track_collection_error_mapper,
            request_options=request_options,
        )

    def delete_track_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTrackCollectionItemsErrorBody]:
        """This endpoint removes one or more tracks from a collection.

        Args:
            id: Collection ID
            item_id: One or more item IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/audio/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[str] | None]("item_id", item_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_track_collection_items_error_mapper,
            request_options=request_options,
        )

    def download_tracks(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AudioUrl, DownloadTracksErrorBody]:
        """This endpoint redownloads tracks that you have already received a license for. The download links in the
        response are valid for 8 hours.

        Args:
            id: License ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/licenses/{id}/downloads"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[AudioUrl],
            error_mapper=download_tracks_error_mapper,
            request_options=request_options,
        )

    def get_track(
        self,
        id: int,
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Audio, GetTrackErrorBody]:
        """This endpoint shows information about a track, including its genres, instruments, and other attributes.

        Args:
            id: Audio track ID
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/{id}"),
            path_params=[param[int]("id", id)],
            query_params=[param[View2OrStr | None]("view", view), param[str | None]("search_id", search_id)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Audio],
            error_mapper=get_track_error_mapper,
            request_options=request_options,
        )

    def get_track_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Collection, GetTrackCollectionErrorBody]:
        """This endpoint gets more detailed information about a collection, including the number of items in it and when
        it was last updated. To get the tracks in collections, use ``GET /v2/audio/collections/{id}/items``.

        Args:
            id: Collection ID
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/collections/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[EmbedOrStr] | None]("embed", embed), param[str | None]("share_code", share_code)],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Collection],
            error_mapper=get_track_collection_error_mapper,
            request_options=request_options,
        )

    def get_track_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionItemDataList, GetTrackCollectionItemsErrorBody]:
        """This endpoint lists the IDs of tracks in a collection and the date that each was added.

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
            url_template=self._server.default("/v2/audio/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("share_code", share_code),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionItemDataList],
            error_mapper=get_track_collection_items_error_mapper,
            request_options=request_options,
        )

    def get_track_collection_list(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        embed: list[EmbedOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionDataList, GetTrackCollectionListErrorBody]:
        """This endpoint lists your collections of audio tracks and their basic attributes.

        Args:
            page: Page number
            per_page: Number of results per page
            embed: Which sharing information to include in the response, such as a URL to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/collections"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[list[EmbedOrStr] | None]("embed", embed),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionDataList],
            error_mapper=get_track_collection_list_error_mapper,
            request_options=request_options,
        )

    def get_track_license_list(
        self,
        *,
        audio_id: str | None = None,
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
    ) -> ApiResult[DownloadHistoryDataList, GetTrackLicenseListErrorBody]:
        """This endpoint lists existing licenses. You can filter the results according to the track ID to see if you
        have an existing license for a specific track.

        Args:
            audio_id: Show licenses for the specified track ID
            license: Restrict results by license.
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
            url_template=self._server.default("/v2/audio/licenses"),
            query_params=[
                param[str | None]("audio_id", audio_id),
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
            error_mapper=get_track_license_list_error_mapper,
            request_options=request_options,
        )

    def get_track_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AudioDataList, GetTrackListErrorBody]:
        """This endpoint lists information about one or more audio tracks, including the description and publication
        date.

        Args:
            id: One or more audio IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio"),
            query_params=[
                param[list[str]]("id", id),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[AudioDataList],
            error_mapper=get_track_list_error_mapper,
            request_options=request_options,
        )

    def license_track(
        self,
        body: LicenseAudioRequest | LicenseAudioRequestDict,
        *,
        license: License10OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseAudioResultDataList, LicenseTrackErrorBody]:
        """This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

        Args:
            body: Tracks to license
            license: License type
            search_id: The ID of the search that led to licensing this track
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/licenses"),
            query_params=[param[License10OrStr | None]("license", license), param[str | None]("search_id", search_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseAudioRequest | LicenseAudioRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseAudioResultDataList],
            error_mapper=license_track_error_mapper,
            request_options=request_options,
        )

    def list_genres(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenreList, RawError]:
        """This endpoint returns a list of all audio genres.

        Args:
            language: Which language the genres will be returned
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/genres"),
            query_params=[param[str | None]("language", language)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[GenreList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_instruments(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InstrumentList, RawError]:
        """This endpoint returns a list of all audio instruments.

        Args:
            language: Which language the instruments will be returned in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/instruments"),
            query_params=[param[str | None]("language", language)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[InstrumentList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_moods(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MoodList, RawError]:
        """This endpoint returns a list of all audio moods.

        Args:
            language: Which language the moods will be returned in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/moods"),
            query_params=[param[str | None]("language", language)],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[MoodList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def rename_track_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RenameTrackCollectionErrorBody]:
        """This endpoint sets a new name for a collection.

        Args:
            id: Collection ID
            body: Collection changes
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionUpdateRequest | CollectionUpdateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=rename_track_collection_error_mapper,
            request_options=request_options,
        )

    def search_tracks(
        self,
        *,
        artists: list[str] | None = None,
        bpm: int | None = None,
        bpm_from: int | None = None,
        bpm_to: int | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        genre: list[str] | None = None,
        is_instrumental: bool | None = None,
        instruments: list[str] | None = None,
        moods: list[str] | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        sort: Sort12OrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        vocal_description: str | None = None,
        view: View2OrStr | None = None,
        fields: str | None = None,
        library: Library1OrStr | None = None,
        language: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AudioSearchResults, SearchTracksErrorBody]:
        """This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter.

        Args:
            artists: Show tracks with one of the specified artist names or IDs
            bpm: (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute
            bpm_from: Show tracks with the specified beats per minute or faster
            bpm_to: Show tracks with the specified beats per minute or slower
            duration: Show tracks with the specified duration in seconds
            duration_from: Show tracks with the specified duration or longer in seconds
            duration_to: Show tracks with the specified duration or shorter in seconds
            genre: Show tracks with each of the specified genres; to get the list of genres, use ``GET
                /v2/audio/genres``
            is_instrumental: Show instrumental music only
            instruments: Show tracks with each of the specified instruments; to get the list of instruments, use ``GET
                /v2/audio/instruments``
            moods: Show tracks with each of the specified moods; to get the list of moods, use ``GET /v2/audio/moods``
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            sort: Sort by
            sort_order: Sort order
            vocal_description: Show tracks with the specified vocal description (male, female)
            view: Amount of detail to render in the response
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            library: Which library to search
            language: Which language to search in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/search"),
            query_params=[
                param[list[str] | None]("artists", artists),
                param[int | None]("bpm", bpm),
                param[int | None]("bpm_from", bpm_from),
                param[int | None]("bpm_to", bpm_to),
                param[int | None]("duration", duration),
                param[int | None]("duration_from", duration_from),
                param[int | None]("duration_to", duration_to),
                param[list[str] | None]("genre", genre),
                param[bool | None]("is_instrumental", is_instrumental),
                param[list[str] | None]("instruments", instruments),
                param[list[str] | None]("moods", moods),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort12OrStr | None]("sort", sort),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("vocal_description", vocal_description),
                param[View2OrStr | None]("view", view),
                param[str | None]("fields", fields),
                param[Library1OrStr | None]("library", library),
                param[str | None]("language", language),
            ],
            auth_scheme=AnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[AudioSearchResults],
            error_mapper=search_tracks_error_mapper,
            request_options=request_options,
        )


class AsyncAudioApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_track_collection_items(
        self,
        id: str,
        body: CollectionItemRequest | CollectionItemRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddTrackCollectionItemsErrorBody]:
        """This endpoint adds one or more tracks to a collection by track IDs.

        Args:
            id: Collection ID
            body: List of items to add to collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionItemRequest | CollectionItemRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=add_track_collection_items_error_mapper,
            request_options=request_options,
        )

    async def create_track_collection(
        self,
        body: CollectionCreateRequest | CollectionCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionCreateResponse, CreateTrackCollectionErrorBody]:
        """This endpoint creates one or more collections (soundboxes). To add tracks, use ``POST
        /v2/audio/collections/{id}/items``.

        Args:
            body: Collection metadata
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/collections"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionCreateRequest | CollectionCreateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionCreateResponse],
            error_mapper=create_track_collection_error_mapper,
            request_options=request_options,
        )

    async def delete_track_collection(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTrackCollectionErrorBody]:
        """This endpoint deletes a collection.

        Args:
            id: Collection ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/audio/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_track_collection_error_mapper,
            request_options=request_options,
        )

    async def delete_track_collection_items(
        self, id: str, *, item_id: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTrackCollectionItemsErrorBody]:
        """This endpoint removes one or more tracks from a collection.

        Args:
            id: Collection ID
            item_id: One or more item IDs to remove from the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/audio/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[str] | None]("item_id", item_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=delete_track_collection_items_error_mapper,
            request_options=request_options,
        )

    async def download_tracks(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AudioUrl, DownloadTracksErrorBody]:
        """This endpoint redownloads tracks that you have already received a license for. The download links in the
        response are valid for 8 hours.

        Args:
            id: License ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/licenses/{id}/downloads"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[AudioUrl],
            error_mapper=download_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_track(
        self,
        id: int,
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Audio, GetTrackErrorBody]:
        """This endpoint shows information about a track, including its genres, instruments, and other attributes.

        Args:
            id: Audio track ID
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/{id}"),
            path_params=[param[int]("id", id)],
            query_params=[param[View2OrStr | None]("view", view), param[str | None]("search_id", search_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[Audio],
            error_mapper=get_track_error_mapper,
            request_options=request_options,
        )

    async def get_track_collection(
        self,
        id: str,
        *,
        embed: list[EmbedOrStr] | None = None,
        share_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Collection, GetTrackCollectionErrorBody]:
        """This endpoint gets more detailed information about a collection, including the number of items in it and when
        it was last updated. To get the tracks in collections, use ``GET /v2/audio/collections/{id}/items``.

        Args:
            id: Collection ID
            embed: Which sharing information to include in the response, such as a URL to the collection
            share_code: Code to retrieve a shared collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/collections/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[list[EmbedOrStr] | None]("embed", embed), param[str | None]("share_code", share_code)],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[Collection],
            error_mapper=get_track_collection_error_mapper,
            request_options=request_options,
        )

    async def get_track_collection_items(
        self,
        id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        share_code: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionItemDataList, GetTrackCollectionItemsErrorBody]:
        """This endpoint lists the IDs of tracks in a collection and the date that each was added.

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
            url_template=self._server.default("/v2/audio/collections/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("share_code", share_code),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionItemDataList],
            error_mapper=get_track_collection_items_error_mapper,
            request_options=request_options,
        )

    async def get_track_collection_list(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 100,
        embed: list[EmbedOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CollectionDataList, GetTrackCollectionListErrorBody]:
        """This endpoint lists your collections of audio tracks and their basic attributes.

        Args:
            page: Page number
            per_page: Number of results per page
            embed: Which sharing information to include in the response, such as a URL to the collection
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/collections"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[list[EmbedOrStr] | None]("embed", embed),
            ],
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[CollectionDataList],
            error_mapper=get_track_collection_list_error_mapper,
            request_options=request_options,
        )

    async def get_track_license_list(
        self,
        *,
        audio_id: str | None = None,
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
    ) -> ApiResult[DownloadHistoryDataList, GetTrackLicenseListErrorBody]:
        """This endpoint lists existing licenses. You can filter the results according to the track ID to see if you
        have an existing license for a specific track.

        Args:
            audio_id: Show licenses for the specified track ID
            license: Restrict results by license.
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
            url_template=self._server.default("/v2/audio/licenses"),
            query_params=[
                param[str | None]("audio_id", audio_id),
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
            error_mapper=get_track_license_list_error_mapper,
            request_options=request_options,
        )

    async def get_track_list(
        self,
        id: list[str],
        *,
        view: View2OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AudioDataList, GetTrackListErrorBody]:
        """This endpoint lists information about one or more audio tracks, including the description and publication
        date.

        Args:
            id: One or more audio IDs
            view: Amount of detail to render in the response
            search_id: The ID of the search that is related to this request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio"),
            query_params=[
                param[list[str]]("id", id),
                param[View2OrStr | None]("view", view),
                param[str | None]("search_id", search_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[AudioDataList],
            error_mapper=get_track_list_error_mapper,
            request_options=request_options,
        )

    async def license_track(
        self,
        body: LicenseAudioRequest | LicenseAudioRequestDict,
        *,
        license: License10OrStr | None = None,
        search_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LicenseAudioResultDataList, LicenseTrackErrorBody]:
        """This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

        Args:
            body: Tracks to license
            license: License type
            search_id: The ID of the search that led to licensing this track
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/licenses"),
            query_params=[param[License10OrStr | None]("license", license), param[str | None]("search_id", search_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LicenseAudioRequest | LicenseAudioRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[LicenseAudioResultDataList],
            error_mapper=license_track_error_mapper,
            request_options=request_options,
        )

    async def list_genres(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenreList, RawError]:
        """This endpoint returns a list of all audio genres.

        Args:
            language: Which language the genres will be returned
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/genres"),
            query_params=[param[str | None]("language", language)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[GenreList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_instruments(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InstrumentList, RawError]:
        """This endpoint returns a list of all audio instruments.

        Args:
            language: Which language the instruments will be returned in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/instruments"),
            query_params=[param[str | None]("language", language)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[InstrumentList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_moods(
        self, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MoodList, RawError]:
        """This endpoint returns a list of all audio moods.

        Args:
            language: Which language the moods will be returned in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/moods"),
            query_params=[param[str | None]("language", language)],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[MoodList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def rename_track_collection(
        self,
        id: str,
        body: CollectionUpdateRequest | CollectionUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RenameTrackCollectionErrorBody]:
        """This endpoint sets a new name for a collection.

        Args:
            id: Collection ID
            body: Collection changes
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/audio/collections/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CollectionUpdateRequest | CollectionUpdateRequestDict](body),
            auth_scheme=self._auth.customer_access_code,
            decoder=empty_response,
            error_mapper=rename_track_collection_error_mapper,
            request_options=request_options,
        )

    async def search_tracks(
        self,
        *,
        artists: list[str] | None = None,
        bpm: int | None = None,
        bpm_from: int | None = None,
        bpm_to: int | None = None,
        duration: int | None = None,
        duration_from: int | None = None,
        duration_to: int | None = None,
        genre: list[str] | None = None,
        is_instrumental: bool | None = None,
        instruments: list[str] | None = None,
        moods: list[str] | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        query: str | None = None,
        sort: Sort12OrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        vocal_description: str | None = None,
        view: View2OrStr | None = None,
        fields: str | None = None,
        library: Library1OrStr | None = None,
        language: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AudioSearchResults, SearchTracksErrorBody]:
        """This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND
        condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR
        condition with those values, depending on the parameter.

        Args:
            artists: Show tracks with one of the specified artist names or IDs
            bpm: (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute
            bpm_from: Show tracks with the specified beats per minute or faster
            bpm_to: Show tracks with the specified beats per minute or slower
            duration: Show tracks with the specified duration in seconds
            duration_from: Show tracks with the specified duration or longer in seconds
            duration_to: Show tracks with the specified duration or shorter in seconds
            genre: Show tracks with each of the specified genres; to get the list of genres, use ``GET
                /v2/audio/genres``
            is_instrumental: Show instrumental music only
            instruments: Show tracks with each of the specified instruments; to get the list of instruments, use ``GET
                /v2/audio/instruments``
            moods: Show tracks with each of the specified moods; to get the list of moods, use ``GET /v2/audio/moods``
            page: Page number
            per_page: Number of results per page
            query: One or more search terms separated by spaces
            sort: Sort by
            sort_order: Sort order
            vocal_description: Show tracks with the specified vocal description (male, female)
            view: Amount of detail to render in the response
            fields: Fields to display in the response; see the documentation for the fields parameter in the overview
                section
            library: Which library to search
            language: Which language to search in
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/audio/search"),
            query_params=[
                param[list[str] | None]("artists", artists),
                param[int | None]("bpm", bpm),
                param[int | None]("bpm_from", bpm_from),
                param[int | None]("bpm_to", bpm_to),
                param[int | None]("duration", duration),
                param[int | None]("duration_from", duration_from),
                param[int | None]("duration_to", duration_to),
                param[list[str] | None]("genre", genre),
                param[bool | None]("is_instrumental", is_instrumental),
                param[list[str] | None]("instruments", instruments),
                param[list[str] | None]("moods", moods),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort12OrStr | None]("sort", sort),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("vocal_description", vocal_description),
                param[View2OrStr | None]("view", view),
                param[str | None]("fields", fields),
                param[Library1OrStr | None]("library", library),
                param[str | None]("language", language),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic, self._auth.customer_access_code),
            decoder=json_decoder[AudioSearchResults],
            error_mapper=search_tracks_error_mapper,
            request_options=request_options,
        )
