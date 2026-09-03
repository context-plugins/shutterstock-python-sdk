from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    basic: AuthScheme
    customer_access_code: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    basic: AsyncAuthScheme
    customer_access_code: AsyncAuthScheme


CustomerAccessCodeScope: TypeAlias = Literal[
    "licenses.create", "purchases.view", "licenses.view", "collections.edit", "collections.view", "user.view"
]
"""``licenses.create``: Grant the ability to download and license media on behalf of the user. ``purchases.view``: Grant
read-only access to a user's purchase history. ``licenses.view``: Grant read-only access to a user's licenses.
``collections.edit``: Grant the ability to create new collections, edit a collection, and modify the contents of a
collection. ``collections.view``: Grant read-only access to a collection and its contents. ``user.view``."""
