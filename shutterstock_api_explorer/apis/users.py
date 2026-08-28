from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder
from ..errors.get_access_token_error import GetAccessTokenErrorBody, get_access_token_error_mapper
from ..errors.get_user_error import GetUserErrorBody, get_user_error_mapper
from ..errors.get_user_subscription_list_error import (
    GetUserSubscriptionListErrorBody,
    get_user_subscription_list_error_mapper,
)
from ..models.access_token_details import AccessTokenDetails
from ..models.subscription_data_list import SubscriptionDataList
from ..models.user_details import UserDetails
from ..server.server import Server


class Users:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersWithRawResponse(client, server, auth)

    def get_access_token(self, *, request_options: RequestOptionsOrDict | None = None) -> AccessTokenDetails:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_access_token(request_options=request_options).unwrap()

    def get_user(self, *, request_options: RequestOptionsOrDict | None = None) -> UserDetails:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_user(request_options=request_options).unwrap()

    def get_user_subscription_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionDataList:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_subscription_list(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> UsersWithRawResponse:
        return self._with_raw_response


class AsyncUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersWithRawResponse(client, server, auth)

    async def get_access_token(self, *, request_options: RequestOptionsOrDict | None = None) -> AccessTokenDetails:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_access_token(request_options=request_options)).unwrap()

    async def get_user(self, *, request_options: RequestOptionsOrDict | None = None) -> UserDetails:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_user(request_options=request_options)).unwrap()

    async def get_user_subscription_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionDataList:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_user_subscription_list(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersWithRawResponse:
        return self._with_raw_response


class UsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_access_token(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccessTokenDetails, GetAccessTokenErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/user/access_token"),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[AccessTokenDetails],
            error_mapper=get_access_token_error_mapper,
            request_options=request_options,
        )

    def get_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserDetails, GetUserErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/user"),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[UserDetails],
            error_mapper=get_user_error_mapper,
            request_options=request_options,
        )

    def get_user_subscription_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionDataList, GetUserSubscriptionListErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/user/subscriptions"),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[SubscriptionDataList],
            error_mapper=get_user_subscription_list_error_mapper,
            request_options=request_options,
        )


class AsyncUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_access_token(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccessTokenDetails, GetAccessTokenErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/user/access_token"),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[AccessTokenDetails],
            error_mapper=get_access_token_error_mapper,
            request_options=request_options,
        )

    async def get_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserDetails, GetUserErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/user"),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[UserDetails],
            error_mapper=get_user_error_mapper,
            request_options=request_options,
        )

    async def get_user_subscription_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionDataList, GetUserSubscriptionListErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/user/subscriptions"),
            auth_scheme=self._auth.customer_access_code,
            decoder=json_decoder[SubscriptionDataList],
            error_mapper=get_user_subscription_list_error_mapper,
            request_options=request_options,
        )
