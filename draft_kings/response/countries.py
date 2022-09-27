from dataclasses import dataclass
from typing import Optional

from desert import field
from marshmallow.fields import Str, Int, Bool, List, Nested

from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class Country(Smore):
    country_code: Optional[str] = field(Str(data_key="countryCode", missing=None))
    country_id: Optional[int] = field(Int(data_key="countryId", missing=None))
    is_licensed: Optional[bool] = field(Bool(data_key="isLicensed", missing=None))
    name: Optional[str] = field(Str(data_key="name", missing=None))


@dataclass(frozen=True)
class Countries(Smore):
    countries: list[Country] = field(List(Nested(Country.schema()), missing=[]))
