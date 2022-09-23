from dataclasses import dataclass, field
from typing import Optional

from desert import metadata
from marshmallow.fields import Str, Int, Bool, List, Nested

from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class Country(Smore):
    country_code: Optional[str] = field(metadata=metadata(Str(data_key="country_code", missing=None)))
    country_id: Optional[int] = field(metadata=metadata(Int(data_key="country_id", missing=None)))
    is_licensed: Optional[bool] = field(metadata=metadata(Bool(data_key="is_licensed", missing=None)))
    name: Optional[str] = field(metadata=metadata(Str(data_key="name", missing=None)))


@dataclass(frozen=True)
class Countries(Smore):
    countries: list[Country] = field(metadata=metadata(List(Nested(Country), missing=[])))
