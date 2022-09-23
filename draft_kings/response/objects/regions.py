from dataclasses import dataclass, field
from typing import Optional

from desert import metadata
from marshmallow.fields import Str, Nested, List

from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class Region(Smore):
    country_code: Optional[str] = field(metadata=metadata(Str(attribute="country_code", missing=None)))
    iso_region_code: Optional[str] = field(metadata=metadata(Str(attribute="iso_region_code", missing=None)))
    name: Optional[str] = field(metadata=metadata(Str(attribute="name", missing=None)))
    region_code: Optional[str] = field(metadata=metadata(Str(attribute="region_code", missing=None)))


@dataclass(frozen=True)
class Regions(Smore):
    regions: list[Region] = field(metadata=metadata(List(Nested(Region), attribute="regions", missing=[])))
