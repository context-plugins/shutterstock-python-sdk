from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.audio_api import AudioApi
from .apis.catalog import Catalog
from .apis.computer_vision import ComputerVision
from .apis.contributors import Contributors
from .apis.editorial_images import EditorialImages
from .apis.editorial_video import EditorialVideo
from .apis.images import Images
from .apis.oauth import Oauth
from .apis.sound_effects import SoundEffects
from .apis.test import Test
from .apis.users import Users
from .apis.videos import Videos
from .auth import AuthSchemes, CustomerAccessCodeScope
from .base_client import DEFAULT_TIMEOUT, BaseShutterstockApiExplorerClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AuthorizationCodeCredentials,
    AuthorizationCodeCredentialsOrDict,
    AuthorizationCodeTokenSource,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    HttpClient,
    HttpxClient,
    OAuth2RefreshableScheme,
    RawClient,
    RefreshableTokenSource,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment
from .server.server_config import ServerConfigOrDict


class ShutterstockApiExplorerClient(BaseShutterstockApiExplorerClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        basic: BasicAuthCredentialsOrDict | None = None,
        customer_access_code: AuthorizationCodeCredentialsOrDict[CustomerAccessCodeScope] | None = None,
        customer_access_code_token_source: (
            RefreshableTokenSource[AuthorizationCodeCredentials[CustomerAccessCodeScope]] | None
        ) = None,
    ) -> None:
        super().__init__(environment=environment, timeout=timeout, server_config=server_config)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "ShutterstockApiExplorerClient/1.2.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.2.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            basic=BasicAuthScheme(BasicAuthCredentials.coerce(basic)) if basic is not None else no_auth,
            customer_access_code=(
                OAuth2RefreshableScheme(
                    credentials=AuthorizationCodeCredentials[CustomerAccessCodeScope].coerce(customer_access_code),
                    source=(
                        customer_access_code_token_source
                        if customer_access_code_token_source is not None
                        else AuthorizationCodeTokenSource[CustomerAccessCodeScope](
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
    def audio_api(self) -> AudioApi:
        return AudioApi(self._raw_client, self._server, self._auth)

    @cached_property
    def catalog(self) -> Catalog:
        return Catalog(self._raw_client, self._server, self._auth)

    @cached_property
    def computer_vision(self) -> ComputerVision:
        return ComputerVision(self._raw_client, self._server, self._auth)

    @cached_property
    def contributors(self) -> Contributors:
        return Contributors(self._raw_client, self._server, self._auth)

    @cached_property
    def editorial_images(self) -> EditorialImages:
        return EditorialImages(self._raw_client, self._server, self._auth)

    @cached_property
    def editorial_video(self) -> EditorialVideo:
        return EditorialVideo(self._raw_client, self._server, self._auth)

    @cached_property
    def images(self) -> Images:
        return Images(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth(self) -> Oauth:
        return Oauth(self._raw_client, self._server)

    @cached_property
    def sound_effects(self) -> SoundEffects:
        return SoundEffects(self._raw_client, self._server, self._auth)

    @cached_property
    def test(self) -> Test:
        return Test(self._raw_client, self._server)

    @cached_property
    def users(self) -> Users:
        return Users(self._raw_client, self._server, self._auth)

    @cached_property
    def videos(self) -> Videos:
        return Videos(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = ShutterstockApiExplorerClient
