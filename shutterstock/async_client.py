from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.audio_api import AsyncAudioApi
from .apis.catalog import AsyncCatalog
from .apis.computer_vision import AsyncComputerVision
from .apis.contributors import AsyncContributors
from .apis.editorial_images import AsyncEditorialImages
from .apis.editorial_video import AsyncEditorialVideo
from .apis.images import AsyncImages
from .apis.oauth import AsyncOauth
from .apis.sound_effects import AsyncSoundEffects
from .apis.test import AsyncTest
from .apis.users import AsyncUsers
from .apis.videos import AsyncVideos
from .auth import AsyncAuthSchemes, CustomerAccessCodeScope
from .base_client import DEFAULT_TIMEOUT, BaseShutterstockClient
from .core import (
    AsyncAuthorizationCodeCredentials,
    AsyncAuthorizationCodeCredentialsOrDict,
    AsyncAuthorizationCodeTokenSource,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncOAuth2RefreshableScheme,
    AsyncRawClient,
    AsyncRefreshableTokenSource,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    client_secret_basic,
    no_auth,
)
from .server.environment import Environment
from .server.server_config import ServerConfigOrDict


class AsyncShutterstockClient(BaseShutterstockClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        basic: BasicAuthCredentialsOrDict | None = None,
        customer_access_code: AsyncAuthorizationCodeCredentialsOrDict[CustomerAccessCodeScope] | None = None,
        customer_access_code_token_source: (
            AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[CustomerAccessCodeScope]] | None
        ) = None,
    ) -> None:
        super().__init__(environment=environment, timeout=timeout, server_config=server_config)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
        )
        self._auth = AsyncAuthSchemes(
            basic=BasicAuthScheme(BasicAuthCredentials.coerce(basic)) if basic is not None else no_auth,
            customer_access_code=(
                AsyncOAuth2RefreshableScheme(
                    credentials=AsyncAuthorizationCodeCredentials[CustomerAccessCodeScope].coerce(customer_access_code),
                    source=(
                        customer_access_code_token_source
                        if customer_access_code_token_source is not None
                        else AsyncAuthorizationCodeTokenSource[CustomerAccessCodeScope](
                            client=self._raw_client,
                            authorization_url=self._server.auth_server("/authorize"),
                            token_url=self._server.default("/v2/oauth/access_token"),
                            refresh_url=self._server.default("/v2/oauth/access_token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if customer_access_code is not None
                else no_auth
            ),
        )

    @cached_property
    def audio_api(self) -> AsyncAudioApi:
        return AsyncAudioApi(self._raw_client, self._server, self._auth)

    @cached_property
    def catalog(self) -> AsyncCatalog:
        return AsyncCatalog(self._raw_client, self._server, self._auth)

    @cached_property
    def computer_vision(self) -> AsyncComputerVision:
        return AsyncComputerVision(self._raw_client, self._server, self._auth)

    @cached_property
    def contributors(self) -> AsyncContributors:
        return AsyncContributors(self._raw_client, self._server, self._auth)

    @cached_property
    def editorial_images(self) -> AsyncEditorialImages:
        return AsyncEditorialImages(self._raw_client, self._server, self._auth)

    @cached_property
    def editorial_video(self) -> AsyncEditorialVideo:
        return AsyncEditorialVideo(self._raw_client, self._server, self._auth)

    @cached_property
    def images(self) -> AsyncImages:
        return AsyncImages(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth(self) -> AsyncOauth:
        return AsyncOauth(self._raw_client, self._server)

    @cached_property
    def sound_effects(self) -> AsyncSoundEffects:
        return AsyncSoundEffects(self._raw_client, self._server, self._auth)

    @cached_property
    def test(self) -> AsyncTest:
        return AsyncTest(self._raw_client, self._server)

    @cached_property
    def users(self) -> AsyncUsers:
        return AsyncUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def videos(self) -> AsyncVideos:
        return AsyncVideos(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncShutterstockClient
