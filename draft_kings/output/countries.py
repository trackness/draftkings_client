from dataclasses import dataclass
from desert import field, schema

from draft_kings.response.smore import Smore

from marshmallow.fields import Int, Str, Bool, List, Nested


@dataclass(frozen=True)
class CountryDetails(Smore):
    code: str | None = field(Str(allow_none=True, required=True))
    country_id: int | None = field(Int(allow_none=True, required=True))
    is_licensed: bool | None = field(Bool(allow_none=True, required=True))
    name: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class CountriesDetails(Smore):
    countries: list[CountryDetails] = field(List(Nested(schema(CountryDetails), required=True), required=True))
