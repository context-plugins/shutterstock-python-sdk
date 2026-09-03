from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    empty_response,
    form_body,
    json_decoder,
    param,
)
from ..errors.authorize_error import AuthorizeErrorBody, authorize_error_mapper
from ..errors.create_access_token_error import CreateAccessTokenErrorBody, create_access_token_error_mapper
from ..models.enums.expires import ExpiresOrStr
from ..models.enums.grant_type import GrantTypeOrStr
from ..models.enums.realm2 import Realm2OrStr
from ..models.enums.realm3 import Realm3OrStr
from ..models.enums.response_type import ResponseTypeOrStr
from ..models.oauth_access_token_response import OauthAccessTokenResponse
from ..server.server import Server


class Oauth:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = OauthWithRawResponse(client, server)

    def authorize(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: ResponseTypeOrStr,
        state: str,
        *,
        realm: Realm2OrStr | None = None,
        scope: str | None = "user.view",
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint returns a redirect URI (in the 'Location' header) that the customer uses to authorize your
        application and, together with POST /v2/oauth/access_token, generate an access token that represents that
        authorization.

        Args:
            client_id: Client ID (Consumer Key) of your application
            redirect_uri: The callback URI to send the request to after authorization; must use a host name that is
                registered with your application
            response_type: Type of temporary authorization code that will be used to generate an access code; the only
                valid value is 'code'
            state: Unique value used by the calling app to verify the request
            realm: User type to be authorized (usually 'customer')
            scope: Space-separated list of scopes to be authorized
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.authorize(
            client_id, redirect_uri, response_type, state, realm=realm, scope=scope, request_options=request_options
        ).unwrap()

    def create_access_token(
        self,
        client_id: str,
        grant_type: GrantTypeOrStr,
        *,
        client_secret: str | None = None,
        code: str | None = None,
        realm: Realm3OrStr | None = None,
        expires: ExpiresOrStr | None = None,
        refresh_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OauthAccessTokenResponse:
        """This endpoint returns an access token for the specified user and with the specified scopes. The token does
        not expire until the user changes their password. The body parameters must be encoded as form data.

        Args:
            client_id: Client ID (Consumer Key) of your application
            grant_type: Grant type: authorization_code generates user tokens, client_credentials generates short-lived
                client grants
            client_secret: Client Secret (Consumer Secret) of your application
            code: Response code from the /oauth/authorize flow; required if grant_type=authorization_code
            realm: User type to be authorized (usually 'customer')
            expires: Whether or not the token expires, expiring tokens come with a refresh_token to renew the
                access_token
            refresh_token: Pass this along with grant_type=refresh_token to get a fresh access token
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.create_access_token(
            client_id,
            grant_type,
            client_secret=client_secret,
            code=code,
            realm=realm,
            expires=expires,
            refresh_token=refresh_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> OauthWithRawResponse:
        return self._with_raw_response


class AsyncOauth:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncOauthWithRawResponse(client, server)

    async def authorize(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: ResponseTypeOrStr,
        state: str,
        *,
        realm: Realm2OrStr | None = None,
        scope: str | None = "user.view",
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint returns a redirect URI (in the 'Location' header) that the customer uses to authorize your
        application and, together with POST /v2/oauth/access_token, generate an access token that represents that
        authorization.

        Args:
            client_id: Client ID (Consumer Key) of your application
            redirect_uri: The callback URI to send the request to after authorization; must use a host name that is
                registered with your application
            response_type: Type of temporary authorization code that will be used to generate an access code; the only
                valid value is 'code'
            state: Unique value used by the calling app to verify the request
            realm: User type to be authorized (usually 'customer')
            scope: Space-separated list of scopes to be authorized
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.authorize(
                client_id, redirect_uri, response_type, state, realm=realm, scope=scope, request_options=request_options
            )
        ).unwrap()

    async def create_access_token(
        self,
        client_id: str,
        grant_type: GrantTypeOrStr,
        *,
        client_secret: str | None = None,
        code: str | None = None,
        realm: Realm3OrStr | None = None,
        expires: ExpiresOrStr | None = None,
        refresh_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OauthAccessTokenResponse:
        """This endpoint returns an access token for the specified user and with the specified scopes. The token does
        not expire until the user changes their password. The body parameters must be encoded as form data.

        Args:
            client_id: Client ID (Consumer Key) of your application
            grant_type: Grant type: authorization_code generates user tokens, client_credentials generates short-lived
                client grants
            client_secret: Client Secret (Consumer Secret) of your application
            code: Response code from the /oauth/authorize flow; required if grant_type=authorization_code
            realm: User type to be authorized (usually 'customer')
            expires: Whether or not the token expires, expiring tokens come with a refresh_token to renew the
                access_token
            refresh_token: Pass this along with grant_type=refresh_token to get a fresh access token
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_access_token(
                client_id,
                grant_type,
                client_secret=client_secret,
                code=code,
                realm=realm,
                expires=expires,
                refresh_token=refresh_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOauthWithRawResponse:
        return self._with_raw_response


class OauthWithRawResponse(BaseRawResponse[RawClient, Server]):
    def authorize(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: ResponseTypeOrStr,
        state: str,
        *,
        realm: Realm2OrStr | None = None,
        scope: str | None = "user.view",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AuthorizeErrorBody]:
        """This endpoint returns a redirect URI (in the 'Location' header) that the customer uses to authorize your
        application and, together with POST /v2/oauth/access_token, generate an access token that represents that
        authorization.

        Args:
            client_id: Client ID (Consumer Key) of your application
            redirect_uri: The callback URI to send the request to after authorization; must use a host name that is
                registered with your application
            response_type: Type of temporary authorization code that will be used to generate an access code; the only
                valid value is 'code'
            state: Unique value used by the calling app to verify the request
            realm: User type to be authorized (usually 'customer')
            scope: Space-separated list of scopes to be authorized
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/oauth/authorize"),
            query_params=[
                param[str]("client_id", client_id),
                param[str]("redirect_uri", redirect_uri),
                param[ResponseTypeOrStr]("response_type", response_type),
                param[str]("state", state),
                param[Realm2OrStr | None]("realm", realm),
                param[str | None]("scope", scope),
            ],
            decoder=empty_response,
            error_mapper=authorize_error_mapper,
            request_options=request_options,
        )

    def create_access_token(
        self,
        client_id: str,
        grant_type: GrantTypeOrStr,
        *,
        client_secret: str | None = None,
        code: str | None = None,
        realm: Realm3OrStr | None = None,
        expires: ExpiresOrStr | None = None,
        refresh_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OauthAccessTokenResponse, CreateAccessTokenErrorBody]:
        """This endpoint returns an access token for the specified user and with the specified scopes. The token does
        not expire until the user changes their password. The body parameters must be encoded as form data.

        Args:
            client_id: Client ID (Consumer Key) of your application
            grant_type: Grant type: authorization_code generates user tokens, client_credentials generates short-lived
                client grants
            client_secret: Client Secret (Consumer Secret) of your application
            code: Response code from the /oauth/authorize flow; required if grant_type=authorization_code
            realm: User type to be authorized (usually 'customer')
            expires: Whether or not the token expires, expiring tokens come with a refresh_token to renew the
                access_token
            refresh_token: Pass this along with grant_type=refresh_token to get a fresh access token
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/oauth/access_token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("client_id", client_id),
                    param[GrantTypeOrStr]("grant_type", grant_type),
                    param[str | None]("client_secret", client_secret),
                    param[str | None]("code", code),
                    param[Realm3OrStr | None]("realm", realm),
                    param[ExpiresOrStr | None]("expires", expires),
                    param[str | None]("refresh_token", refresh_token),
                ],
            ),
            decoder=json_decoder[OauthAccessTokenResponse],
            error_mapper=create_access_token_error_mapper,
            request_options=request_options,
        )


class AsyncOauthWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def authorize(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: ResponseTypeOrStr,
        state: str,
        *,
        realm: Realm2OrStr | None = None,
        scope: str | None = "user.view",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AuthorizeErrorBody]:
        """This endpoint returns a redirect URI (in the 'Location' header) that the customer uses to authorize your
        application and, together with POST /v2/oauth/access_token, generate an access token that represents that
        authorization.

        Args:
            client_id: Client ID (Consumer Key) of your application
            redirect_uri: The callback URI to send the request to after authorization; must use a host name that is
                registered with your application
            response_type: Type of temporary authorization code that will be used to generate an access code; the only
                valid value is 'code'
            state: Unique value used by the calling app to verify the request
            realm: User type to be authorized (usually 'customer')
            scope: Space-separated list of scopes to be authorized
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/oauth/authorize"),
            query_params=[
                param[str]("client_id", client_id),
                param[str]("redirect_uri", redirect_uri),
                param[ResponseTypeOrStr]("response_type", response_type),
                param[str]("state", state),
                param[Realm2OrStr | None]("realm", realm),
                param[str | None]("scope", scope),
            ],
            decoder=empty_response,
            error_mapper=authorize_error_mapper,
            request_options=request_options,
        )

    async def create_access_token(
        self,
        client_id: str,
        grant_type: GrantTypeOrStr,
        *,
        client_secret: str | None = None,
        code: str | None = None,
        realm: Realm3OrStr | None = None,
        expires: ExpiresOrStr | None = None,
        refresh_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OauthAccessTokenResponse, CreateAccessTokenErrorBody]:
        """This endpoint returns an access token for the specified user and with the specified scopes. The token does
        not expire until the user changes their password. The body parameters must be encoded as form data.

        Args:
            client_id: Client ID (Consumer Key) of your application
            grant_type: Grant type: authorization_code generates user tokens, client_credentials generates short-lived
                client grants
            client_secret: Client Secret (Consumer Secret) of your application
            code: Response code from the /oauth/authorize flow; required if grant_type=authorization_code
            realm: User type to be authorized (usually 'customer')
            expires: Whether or not the token expires, expiring tokens come with a refresh_token to renew the
                access_token
            refresh_token: Pass this along with grant_type=refresh_token to get a fresh access token
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/oauth/access_token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("client_id", client_id),
                    param[GrantTypeOrStr]("grant_type", grant_type),
                    param[str | None]("client_secret", client_secret),
                    param[str | None]("code", code),
                    param[Realm3OrStr | None]("realm", realm),
                    param[ExpiresOrStr | None]("expires", expires),
                    param[str | None]("refresh_token", refresh_token),
                ],
            ),
            decoder=json_decoder[OauthAccessTokenResponse],
            error_mapper=create_access_token_error_mapper,
            request_options=request_options,
        )
