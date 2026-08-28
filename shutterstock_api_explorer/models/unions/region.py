from __future__ import annotations

from typing import TypeAlias

Region: TypeAlias = str | str
"""Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a
country code or an IP address from which the API infers a country"""

RegionDict: TypeAlias = str | str
