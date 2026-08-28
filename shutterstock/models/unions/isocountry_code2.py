from __future__ import annotations

from typing import TypeAlias

from ..enums.isocountry_code import IsocountryCodeOrStr
from ..enums.isocountry_code1 import IsocountryCode1OrStr

IsocountryCode2: TypeAlias = IsocountryCodeOrStr | IsocountryCode1OrStr
"""A valid ISO 3166-1 Alpha-2 or ISO 3166-1 Alpha-3 code."""

IsocountryCode2Dict: TypeAlias = IsocountryCodeOrStr | IsocountryCode1OrStr
