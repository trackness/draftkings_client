from dataclasses import dataclass

from desert import field
from marshmallow.fields import Str, Nested, List

from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class RegionDetails(Smore):
    code: str | None = field(Str(allow_none=True, required=True))
    country_code: str | None = field(Str(allow_none=True, required=True))
    iso_code: str | None = field(Str(allow_none=True, required=True))
    name: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class RegionsDetails(Smore):
    regions: list[RegionDetails] = field(List(Nested(RegionDetails.schema(), required=True), required=True))
