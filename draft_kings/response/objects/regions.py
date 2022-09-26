from dataclasses import dataclass
from typing import Optional

from desert import field
from marshmallow.fields import Str, List

from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class Region(Smore):
    country_code: Optional[str] = field(Str(data_key="countryCode", missing=None))
    iso_region_code: Optional[str] = field(Str(data_key="isoRegionCode", missing=None))
    name: Optional[str] = field(Str(data_key="name", missing=None))
    region_code: Optional[str] = field(Str(data_key="regionCode", missing=None))


@dataclass(frozen=True)
class Regions(Smore):
    regions: list[Region] = field(List(Smore.nest(Region), data_key="regions", missing=[]))

