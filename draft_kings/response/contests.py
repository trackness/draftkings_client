from dataclasses import dataclass
from datetime import datetime

from desert import field
from marshmallow.fields import Float, Str, Int, Bool, AwareDateTime

from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class ContestAttributes(Smore):
    is_double_up: bool | None = field(Bool(data_key="IsDoubleUp", missing=None))
    is_fifty_fifty: bool | None = field(Bool(data_key="IsFiftyFifty", missing=None))
    is_guaranteed: bool | None = field(Bool(data_key="IsGuaranteed", missing=None))
    is_h2h: bool | None = field(Bool(data_key="IsH2h", missing=None))
    is_starred: bool | None = field(Bool(data_key="IsStarred", missing=None))


@dataclass(frozen=True)
class Contest(Smore):
    attributes: ContestAttributes | None = field(Smore.nest(ContestAttributes, data_key="attr", missing=None))
    contest_id: int | None = field(Int(data_key="id", missing=None))
    draft_group_id: int | None = field(Int(data_key="dg", missing=None))
    entry_fee: float | None = field(Float(data_key="a", missing=None))
    entry_maximum: int | None = field(Int(data_key="m", missing=None))
    entry_total: int | None = field(Int(data_key="nt", missing=None))
    fantasy_player_points: float | None = field(Float(data_key="fpp", missing=None))
    name: str | None = field(Str(data_key="n", missing=None))
    payout: float | None = field(Float(data_key="po", missing=None))
    sport_id: int | None = field(Int(data_key="s", missing=None))
    starts_at: str | None = field(Str(data_key="sd", missing=None))


@dataclass(frozen=True)
class DraftGroup(Smore):
    draft_group_id: int | None = field(Int(data_key="DraftGroupId", missing=None))
    draft_group_series_id: int | None = field(Int(data_key="DraftGroupSeriesId", missing=None))
    contest_type_id: int | None = field(Int(data_key="ContestTypeId", missing=None))
    game_count: int | None = field(Int(data_key="GameCount", missing=None))
    sport: str | None = field(Str(data_key="Sport", missing=None))
    start_date: datetime | None = field(AwareDateTime(data_key="StartDate", missing=None))


@dataclass(frozen=True)
class Contests(Smore):
    contests: list[Contest] = field(Smore.list_nest(Contest, data_key="Contests", missing=[]))
    draft_groups: list[DraftGroup] = field(Smore.list_nest(DraftGroup, data_key="DraftGroups", missing=[]))


