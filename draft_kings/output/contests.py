from dataclasses import dataclass
from datetime import datetime

from desert import field
from marshmallow.fields import Str, Int, Bool, Nested, Number, List
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.fields import CustomAwareDateTime, CustomDateTime
from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class EntriesDetails(Smore):
    fee: float | None = field(Number(allow_none=True, required=True))
    maximum: int | None = field(Int(allow_none=True, required=True))
    total: int | None = field(Int(allow_none=True, required=True))


@dataclass(frozen=True)
class ContestDetails(Smore):
    contest_id: int | None = field(Int(allow_none=True, required=True))
    draft_group_id: int | None = field(Int(allow_none=True, required=True))
    entries_details: EntriesDetails = field(Nested(EntriesDetails.schema(), required=True))
    fantasy_player_points: float | None = field(Number(allow_none=True, required=True))
    is_double_up: bool = field(Bool(allow_none=False, required=True))
    is_fifty_fifty: bool = field(Bool(allow_none=False, required=True))
    is_guaranteed: bool = field(Bool(allow_none=False, required=True))
    is_head_to_head: bool = field(Bool(allow_none=False, required=True))
    is_starred: bool = field(Bool(allow_none=False, required=True))
    name: str | None = field(Str(allow_none=True, required=True))
    payout: float | None = field(Number(allow_none=True, required=True))
    sport: Sport | None = field(EnumField(Sport, by_value=True, allow_none=True, required=True))
    starts_at: datetime | None = field(CustomDateTime(allow_none=True, required=True))


@dataclass(frozen=True)
class DraftGroupDetails(Smore):
    contest_type_id: int | None = field(Int(allow_none=True, required=True))
    draft_group_id: int | None = field(Int(allow_none=True, required=True))
    games_count: int | None = field(Int(allow_none=True, required=True))
    series_id: int | None = field(Int(allow_none=True, required=True))
    sport: Sport | None = field(EnumField(Sport, allow_none=True, required=True, by_value=True))
    starts_at: datetime | None = field(CustomAwareDateTime(allow_none=True, required=True))


@dataclass(frozen=True)
class ContestsDetails(Smore):
    contests: list[ContestDetails] = field(List(Nested(ContestDetails.schema(), required=True), required=True))
    draft_groups: list[DraftGroupDetails] = field(List(Nested(DraftGroupDetails.schema(), required=True), required=True))
