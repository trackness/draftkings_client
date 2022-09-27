from dataclasses import dataclass

from desert import field
from marshmallow.fields import Str, Int, Bool, Nested, List, Float

from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class SalaryCapDetails(Smore):
    is_enabled: bool | None = field(Bool(allow_none=True, required=True))
    maximum_value: float | None = field(Float(allow_none=True, required=True))
    minimum_value: float | None = field(Float(allow_none=True, required=True))


@dataclass(frozen=True)
class RosterSlotDetails(Smore):
    description: str | None = field(Str(allow_none=True, required=True))
    name: str | None = field(Str(allow_none=True, required=True))
    roster_slot_id: int | None = field(Int(allow_none=True, required=True))


@dataclass(frozen=True)
class LineupTemplateDetails(Smore):
    roster_slot_details: RosterSlotDetails | None = field(Nested(RosterSlotDetails.schema(), allow_none=True, required=True))


@dataclass(frozen=True)
class GameTypeRulesDetails(Smore):
    allow_late_swaps: bool | None = field(Bool(allow_none=True, required=True))
    description: str | None = field(Str(allow_none=True, required=True))
    enforce_selecting_unique_players: bool | None = field(Bool(allow_none=True, required=True))
    draft_type_name: str | None = field(Str(allow_none=True, required=True))
    game_type_id: int | None = field(Int(allow_none=True, required=True))
    lineup_templates: list[LineupTemplateDetails] = field(List(Nested(LineupTemplateDetails.schema(), allow_none=False, required=True), allow_none=False, required=True))
    name: str | None = field(Str(allow_none=True, required=True))
    salary_cap_details: SalaryCapDetails | None = field(Nested(SalaryCapDetails.schema(), allow_none=True, required=True))
