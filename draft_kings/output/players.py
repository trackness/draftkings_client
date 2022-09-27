from dataclasses import dataclass
from datetime import datetime

from desert import field
from marshmallow.fields import Str, Int, Bool, Nested, List, Float

from draft_kings.fields import CustomDateTime
from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class TeamSeriesDetails(Smore):
    away_team_id: int | None = field(Int(allow_none=True, required=True))
    home_team_id: int | None = field(Int(allow_none=True, required=True))
    starts_at: datetime | None = field(CustomDateTime(allow_none=True, required=True))
    status_description: str | None = field(Str(allow_none=True, required=True))
    team_series_id: int | None = field(Int(allow_none=True, required=True))
    weather_description: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class DraftDetails(Smore):
    is_draftable: bool | None = field(Bool(allow_none=True, required=True))
    salary: float | None = field(Float(allow_none=True, required=True))
    starts_at: datetime | None = field(CustomDateTime(allow_none=True, required=True))


@dataclass(frozen=True)
class PlayerTeamSeriesDetails(Smore):
    away_team_id: int | None = field(Int(allow_none=True, required=True))
    home_team_id: int | None = field(Int(allow_none=True, required=True))
    opposition_rank: int | None = field(Int(allow_none=True, required=True))
    team_series_id: int | None = field(Int(allow_none=True, required=True))


@dataclass(frozen=True)
class PositionDetails(Smore):
    name: str | None = field(Str(allow_none=True, required=True))
    position_id: int | None = field(Int(allow_none=True, required=True))


@dataclass(frozen=True)
class ExceptionalMessageTypeDetails(Smore):
    name: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class ExceptionalMessageDetails(Smore):
    message: str | None = field(Str(allow_none=True, required=True))
    priority_value: int | None = field(Int(allow_none=True, required=True))
    type_details: ExceptionalMessageTypeDetails | None = field(Nested(ExceptionalMessageTypeDetails.schema(), allow_none=True, required=True))


@dataclass(frozen=True)
class PlayerDetails(Smore):
    draft_details: DraftDetails = field(Nested(DraftDetails.schema(), required=True))
    exceptional_messages: list[ExceptionalMessageDetails] = field(List(Nested(ExceptionalMessageDetails.schema(), required=True), required=True))
    first_name: str | None = field(Str(allow_none=True, required=True))
    jersey_number: int | None = field(Int(allow_none=True, required=True))
    last_name: str | None = field(Str(allow_none=True, required=True))
    player_id: int | None = field(Int(allow_none=True, required=True))
    points_per_game: float | None = field(Float(allow_none=True, required=True))
    position_details: PositionDetails = field(Nested(PositionDetails.schema(), required=True))
    team_id: int | None = field(Int(allow_none=True, required=True))
    team_series_details: PlayerTeamSeriesDetails = field(Nested(PlayerTeamSeriesDetails.schema(), required=True))


@dataclass(frozen=True)
class PlayersDetails(Smore):
    players: list[PlayerDetails] = field(List(Nested(PlayerDetails.schema(), required=True), required=True))
    team_series: list[TeamSeriesDetails] = field(List(Nested(TeamSeriesDetails.schema(), required=True), required=True))
