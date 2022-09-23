from dataclasses import dataclass, field
from typing import Optional

from desert import metadata
from marshmallow.fields import Float, Str, Nested, Int, Bool, List

from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class SalaryCap(Smore):
    is_enabled: Optional[bool] = field(metadata=metadata(Bool(attribute="is_enabled", missing=None)))
    max_value: Optional[float] = field(metadata=metadata(Float(attribute="max_value", missing=None)))
    min_value: Optional[float] = field(metadata=metadata(Float(attribute="min_value", missing=None)))


@dataclass(frozen=True)
class RosterSlot(Smore):
    description: Optional[str] = field(metadata=metadata(Int(attribute="roster_slot_id", missing=None)))
    name: Optional[str] = field(metadata=metadata(Str(attribute="description", missing=None)))
    roster_slot_id: Optional[int] = field(metadata=metadata(Str(attribute="name", missing=None)))


@dataclass(frozen=True)
class LineupTemplate(Smore):
    roster_slot: Optional[RosterSlot] = field(metadata=metadata(Nested(RosterSlot, attribute="roster_slot", missing=None)))


@dataclass(frozen=True)
class GameTypeRules(Smore):
    allow_late_swap: Optional[bool] = field(metadata=metadata(Bool(attribute="allow_late_swap", missing=None)))
    description: Optional[str] = field(metadata=metadata(Str(attribute="draft_type", missing=None)))
    draft_type: Optional[str] = field(metadata=metadata(Str(attribute="description", missing=None)))
    game_type_id: Optional[int] = field(metadata=metadata(Int(attribute="game_type_id", missing=None)))
    lineup_template: list[LineupTemplate] = field(metadata=metadata(Str(attribute="name", missing=None)))
    name: Optional[str] = field(metadata=metadata(List(Nested(LineupTemplate), attribute="lineup_template", missing=[])))
    salary_cap: Optional[SalaryCap] = field(metadata=metadata(Nested(SalaryCap, attribute="salary_cap", missing=None)))
    unique_players: Optional[bool] = field(metadata=metadata(Bool(attribute="unique_players", missing=None)))
