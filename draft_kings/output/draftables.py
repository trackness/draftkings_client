from dataclasses import dataclass
from datetime import datetime

from desert import field
from marshmallow.fields import Int, Nested, List, Bool, Str, Float
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.fields import CustomAwareDateTime
from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class PlayerNameDetails(Smore):
    display: str | None = field(Str(allow_none=True, required=True))
    first: str | None = field(Str(allow_none=True, required=True))
    last: str | None = field(Str(allow_none=True, required=True))
    short: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class PlayerImageDetails(Smore):
    fifty_pixels_by_fifty_pixels_url: str | None = field(Str(allow_none=True, required=True))
    one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url: str | None = field(Str(allow_none=True, required=True))


@dataclass(frozen=True)
class PlayerCompetitionDetails(Smore):
    competition_id: int | None = field(Int(allow_none=True, required=True))
    name: str | None = field(Str(allow_none=True, required=True))
    starts_at: datetime | None = field(CustomAwareDateTime(allow_none=True, required=True))


@dataclass(frozen=True)
class PlayerTeamDetails(Smore):
    abbreviation: str | None = field(Str(allow_none=True, required=True))
    team_id: int | None = field(Int(allow_none=True, required=True))


@dataclass(frozen=True)
class PlayerDraftAlertDetails(Smore):
    alert_description: str | None = field(Str(allow_none=True, required=True))
    message: str | None = field(Str(allow_none=True, required=True))
    priority_value: int | None = field(Int(allow_none=True, required=True))
    updated_at: datetime | None = field(CustomAwareDateTime(allow_none=True, required=True))


@dataclass(frozen=True)
class PlayerDetails(Smore):
    competition_details: PlayerCompetitionDetails | None = field(Nested(PlayerCompetitionDetails.schema(), allow_none=True, required=True))
    draftable_id: int | None = field(Int(allow_none=True, required=True))
    draft_alerts: list[PlayerDraftAlertDetails] = field(List(Nested(PlayerDraftAlertDetails.schema(), required=True), required=True))
    image_details: PlayerImageDetails = field(Nested(PlayerImageDetails.schema(), required=True))
    is_disabled: bool | None = field(Bool(allow_none=True, required=True))
    is_swappable: bool | None = field(Bool(allow_none=True, required=True))
    name_details: PlayerNameDetails = field(Nested(PlayerNameDetails.schema(), required=True))
    news_status_description: str | None = field(Str(allow_none=True, required=True))
    player_id: int | None = field(Int(allow_none=True, required=True))
    position_name: str | None = field(Str(allow_none=True, required=True))
    roster_slot_id: int | None = field(Int(allow_none=True, required=True))
    salary: float | None = field(Float(allow_none=True, required=True))
    team_details: PlayerTeamDetails = field(Nested(PlayerTeamDetails.schema(), required=True))


@dataclass(frozen=True)
class CompetitionTeamDetails(Smore):
    abbreviation: str | None = field(Str(allow_none=True, required=True))
    city: str | None = field(Str(allow_none=True, required=True))
    name: str | None = field(Str(allow_none=True, required=True))
    team_id: int | None = field(Int(allow_none=True, required=True))


@dataclass(frozen=True)
class CompetitionWeatherDetails(Smore):
    description: str | None = field(Str(allow_none=True, required=True))
    is_in_a_dome: bool | None = field(Bool(allow_none=True, required=True))


@dataclass(frozen=True)
class CompetitionDetails(Smore):
    are_depth_charts_available: bool | None = field(Bool(allow_none=True, required=True))
    are_starting_lineups_available: bool | None = field(Bool(allow_none=True, required=True))
    away_team: CompetitionTeamDetails | None = field(Nested(CompetitionTeamDetails.schema(), allow_none=True, required=True))
    competition_id: int | None = field(Int(allow_none=True, required=True))
    home_team: CompetitionTeamDetails | None = field(Nested(CompetitionTeamDetails.schema(), allow_none=True, required=True))
    name: str | None = field(Str(allow_none=True, required=True))
    sport: Sport | None = field(EnumField(Sport, by_value=True, allow_none=True, required=True))
    starts_at: datetime | None = field(CustomAwareDateTime(allow_none=True, required=True))
    state_description: str | None = field(Str(allow_none=True, required=True))
    venue: str | None = field(Str(allow_none=True, required=True))
    weather: CompetitionWeatherDetails | None = field(Nested(CompetitionWeatherDetails.schema(), allow_none=True, required=True))


@dataclass(frozen=True)
class DraftablesDetails(Smore):
    competitions: list[CompetitionDetails] = field(List(Nested(PlayerDetails.schema(), required=True), required=True))
    players: list[PlayerDetails] = field(List(Nested(CompetitionDetails.schema(), required=True), required=True))
