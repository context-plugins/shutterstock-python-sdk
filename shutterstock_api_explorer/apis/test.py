from __future__ import annotations

from ..core import ApiResult, AsyncRawClient, BaseRawResponse, RawClient, RequestOptionsOrDict, json_decoder, param
from ..errors.echo_error import EchoErrorBody, echo_error_mapper
from ..errors.validate_error import ValidateErrorBody, validate_error_mapper
from ..models.test_echo import TestEcho
from ..models.test_validate import TestValidate
from ..server.server import Server


class Test:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = TestWithRawResponse(client, server)

    def echo(self, *, text: str | None = "ok", request_options: RequestOptionsOrDict | None = None) -> TestEcho:
        """Send a ``GET`` request.

        Args:
            text: Text to echo
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.echo(text=text, request_options=request_options).unwrap()

    def validate(
        self,
        id: int,
        *,
        tag: list[str] | None = None,
        user_agent: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestValidate:
        """Send a ``GET`` request.

        Args:
            id: Integer ID
            tag: List of tags
            user_agent: User agent
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return self._with_raw_response.validate(
            id, tag=tag, user_agent=user_agent, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TestWithRawResponse:
        return self._with_raw_response


class AsyncTest:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncTestWithRawResponse(client, server)

    async def echo(self, *, text: str | None = "ok", request_options: RequestOptionsOrDict | None = None) -> TestEcho:
        """Send a ``GET`` request.

        Args:
            text: Text to echo
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (await self._with_raw_response.echo(text=text, request_options=request_options)).unwrap()

    async def validate(
        self,
        id: int,
        *,
        tag: list[str] | None = None,
        user_agent: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestValidate:
        """Send a ``GET`` request.

        Args:
            id: Integer ID
            tag: List of tags
            user_agent: User agent
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Forbidden ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.validate(id, tag=tag, user_agent=user_agent, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTestWithRawResponse:
        return self._with_raw_response


class TestWithRawResponse(BaseRawResponse[RawClient, Server]):
    def echo(
        self, *, text: str | None = "ok", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TestEcho, EchoErrorBody]:
        """Send a ``GET`` request.

        Args:
            text: Text to echo
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/test"),
            query_params=[param[str | None]("text", text)],
            decoder=json_decoder[TestEcho],
            error_mapper=echo_error_mapper,
            request_options=request_options,
        )

    def validate(
        self,
        id: int,
        *,
        tag: list[str] | None = None,
        user_agent: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestValidate, ValidateErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Integer ID
            tag: List of tags
            user_agent: User agent
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/test/validate"),
            query_params=[param[int]("id", id), param[list[str] | None]("tag", tag)],
            headers=[param[str | None]("user-agent", user_agent)],
            decoder=json_decoder[TestValidate],
            error_mapper=validate_error_mapper,
            request_options=request_options,
        )


class AsyncTestWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def echo(
        self, *, text: str | None = "ok", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TestEcho, EchoErrorBody]:
        """Send a ``GET`` request.

        Args:
            text: Text to echo
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/test"),
            query_params=[param[str | None]("text", text)],
            decoder=json_decoder[TestEcho],
            error_mapper=echo_error_mapper,
            request_options=request_options,
        )

    async def validate(
        self,
        id: int,
        *,
        tag: list[str] | None = None,
        user_agent: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestValidate, ValidateErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Integer ID
            tag: List of tags
            user_agent: User agent
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/test/validate"),
            query_params=[param[int]("id", id), param[list[str] | None]("tag", tag)],
            headers=[param[str | None]("user-agent", user_agent)],
            decoder=json_decoder[TestValidate],
            error_mapper=validate_error_mapper,
            request_options=request_options,
        )
