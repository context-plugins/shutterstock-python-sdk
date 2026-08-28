from __future__ import annotations

from typing import TypeAlias

from ..license_image import LicenseImage, LicenseImageDict
from ..license_image_vector import LicenseImageVector, LicenseImageVectorDict

Image3: TypeAlias = LicenseImage | LicenseImageVector

Image3Dict: TypeAlias = LicenseImageDict | LicenseImageVectorDict
