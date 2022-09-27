from dataclasses import dataclass

from desert import field
from marshmallow.fields import Str, Int, Bool

from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class SalaryCap(Smore):
    is_enabled: bool | None = field(Bool(data_key="isEnabled", missing=None))
    max_value: int | None = field(Int(data_key="maxValue", missing=None))
    min_value: int | None = field(Int(data_key="minValue", missing=None))


@dataclass(frozen=True)
class RosterSlot(Smore):
    description: str | None = field(Str(data_key="description", missing=None))
    name: str | None = field(Str(data_key="name", missing=None))
    roster_slot_id: int | None = field(Int(data_key="id", missing=None))


@dataclass(frozen=True)
class LineupTemplate(Smore):
    roster_slot: RosterSlot | None = field(Smore.nest(RosterSlot, data_key="rosterSlot", missing=None))


@dataclass(frozen=True)
class GameTypeRules(Smore):
    allow_late_swap: bool | None = field(Bool(data_key="allowLateSwap", missing=None))
    draft_type: str | None = field(Str(data_key="draftType", missing=None))
    description: str | None = field(Str(data_key="gameTypeDescription", missing=None))
    game_type_id: int | None = field(Int(data_key="gameTypeId", missing=None))
    name: str | None = field(Str(data_key="gameTypeName", missing=None))
    lineup_template: list[LineupTemplate] = field(Smore.list_nest(LineupTemplate, data_key="lineupTemplate", missing=[]))
    salary_cap: SalaryCap | None = field(Smore.nest(SalaryCap, data_key="salaryCap", missing=None))
    unique_players: bool | None = field(Bool(data_key="uniquePlayers", missing=None))
