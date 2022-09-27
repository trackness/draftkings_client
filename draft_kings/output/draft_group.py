from dataclasses import dataclass
from datetime import datetime

from desert import field
from marshmallow.fields import Str, Int, Nested, List
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.fields import CustomAwareDateTime
from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class ContestDetails(Smore):
    game_type_description: str | None = field(Str(allow_none=True, required=True))
    type_id: int | None = field(Int(allow_none=True, required=True))


@dataclass(frozen=True)
class StartTimeDetails(Smore):
    maximum: datetime | None = field(CustomAwareDateTime(allow_none=True, required=True))
    minimum: datetime | None = field(CustomAwareDateTime(allow_none=True, required=True))
    type_description: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class LeagueDetails(Smore):
    abbreviation: str | None = field(Str(allow_none=True, required=True))
    league_id: int | None = field(Int(allow_none=True, required=True))
    name: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class GameDetails(Smore):
    away_team_id: int | None = field(Int(allow_none=True, required=True))
    description: str | None = field(Str(allow_none=True, required=True))
    game_id: int | None = field(Int(allow_none=True, required=True))
    home_team_id: int | None = field(Int(allow_none=True, required=True))
    location: str | None = field(Str(allow_none=True, required=True))
    name: str | None = field(Str(allow_none=True, required=True))
    starts_at: datetime | None = field(CustomAwareDateTime(allow_none=True, required=True))
    status_description: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class DraftGroupDetails(Smore):
    contest_details: ContestDetails = field(Nested(ContestDetails.schema(), required=True))
    draft_group_id: int | None = field(Int(allow_none=True, required=True))
    games: list[GameDetails] = field(List(Nested(GameDetails.schema(), required=True), required=True))
    leagues: list[LeagueDetails] = field(List(Nested(LeagueDetails.schema(), required=True), required=True))
    sport: Sport | None = field(EnumField(Sport, allow_none=True, required=True, by_value=True))
    start_time_details: StartTimeDetails = field(Nested(StartTimeDetails.schema(), required=True))
    state_description: str | None = field(Str(allow_none=True, required=True))
