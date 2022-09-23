from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from desert import metadata
from marshmallow.fields import Float, Str, Nested, Int, Bool, AwareDateTime

from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class ContestAttributes(Smore):
    # is_double_up: Optional[bool] = field(metadata=metadata(Bool(missing=None, data_key="is_double_up")))
    # is_fifty_fifty: Optional[bool] = field(metadata=metadata(Bool(missing=None, data_key="is_fifty_fifty")))
    # is_guaranteed: Optional[bool] = field(metadata=metadata(Bool(missing=None, data_key="is_guaranteed")))
    # is_h2h: Optional[bool] = field(metadata=metadata(Bool(missing=None, data_key="is_h2h")))
    # is_starred: Optional[bool] = field(metadata=metadata(Bool(missing=None, data_key="is_starred")))
    is_double_up: Optional[bool] = Smore.field(Bool(missing=None, data_key="is_double_up"))
    is_fifty_fifty: Optional[bool] = Smore.field(Bool(missing=None, data_key="is_fifty_fifty"))
    is_guaranteed: Optional[bool] = Smore.field(Bool(missing=None, data_key="is_guaranteed"))
    is_h2h: Optional[bool] = Smore.field(Bool(missing=None, data_key="is_h2h"))
    is_starred: Optional[bool] = Smore.field(Bool(missing=None, data_key="is_starred"))


@dataclass(frozen=True)
class Contest(Smore):
    attributes: Optional[ContestAttributes] = field(metadata=metadata(Nested(ContestAttributes, missing=None, data_key="attributes")))
    contest_id: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="contest_id")))
    draft_group_id: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="draft_group_id")))
    entry_fee: Optional[float] = field(metadata=metadata(Float(missing=None, data_key="entry_fee")))
    entry_maximum: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="entry_maximum")))
    entry_total: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="entry_total")))
    fantasy_player_points: Optional[float] = field(metadata=metadata(Float(missing=None, data_key="fantasy_player_points")))
    name: Optional[str] = field(metadata=metadata(Str(missing=None, data_key="name")))
    payout: Optional[float] = field(metadata=metadata(Float(missing=None, data_key="payout")))
    sport_id: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="sport_id")))
    starts_at: Optional[str] = field(metadata=metadata(Str(missing=None, data_key="starts_at")))


@dataclass(frozen=True)
class DraftGroup(Smore):
    draft_group_id: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="draft_group_id")))
    draft_group_series_id: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="draft_group_series_id")))
    contest_type_id: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="contest_type_id")))
    game_count: Optional[int] = field(metadata=metadata(Int(missing=None, data_key="game_count")))
    sport: Optional[str] = field(metadata=metadata(Str(missing=None, data_key="sport")))
    start_date: Optional[datetime] = field(metadata=metadata(AwareDateTime(missing=None, data_key="start_date")))


@dataclass(frozen=True)
class Contests(Smore):
    contests: list[Contest] = field(metadata=metadata(Nested(Contest, missing=[], data_key="contests")))
    draft_groups: list[DraftGroup] = field(metadata=metadata(Nested(DraftGroup, missing=[], data_key="draft_groups")))
