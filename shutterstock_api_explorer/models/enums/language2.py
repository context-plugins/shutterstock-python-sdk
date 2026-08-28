from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Language2(str, Enum):
    """Set query and result language (uses Accept-Language header if not set)"""

    AR = "ar"
    BG = "bg"
    BN = "bn"
    CS = "cs"
    DA = "da"
    DE = "de"
    EL = "el"
    EN = "en"
    ES = "es"
    FI = "fi"
    FR = "fr"
    GU = "gu"
    HE = "he"
    HI = "hi"
    HR = "hr"
    HU = "hu"
    ID = "id"
    IT = "it"
    JA = "ja"
    KN = "kn"
    KO = "ko"
    ML = "ml"
    MR = "mr"
    NB = "nb"
    NL = "nl"
    OR = "or"
    PL = "pl"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    SK = "sk"
    SL = "sl"
    SV = "sv"
    TA = "ta"
    TE = "te"
    TH = "th"
    TR = "tr"
    UK = "uk"
    UR = "ur"
    VI = "vi"
    ZH = "zh"
    ZH_HANT = "zh-Hant"

    __str__ = str.__str__


Language2OrStr: TypeAlias = Annotated[Language2 | str, open_enum_validator(Language2)]
