from __future__ import annotations

from typing import TypeAlias

from ..enums.country import CountryOrStr
from ..enums.country1 import Country1OrStr

Country2: TypeAlias = CountryOrStr | Country1OrStr
"""Mandatory country code for where the editorial content will be distributed; this value is used for rights checks"""

Country2Dict: TypeAlias = CountryOrStr | Country1OrStr
