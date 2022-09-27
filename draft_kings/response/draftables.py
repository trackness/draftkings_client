from dataclasses import dataclass
from datetime import datetime

from desert import field
from marshmallow.fields import Float, Str, Int, Bool, AwareDateTime, Nested, List

from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class PlayerCompetitionDetails(Smore):
    competition_id: int | None = field(Int(data_key="competitionId", missing=None))
    name: str | None = field(Str(data_key="name", missing=None))
    start_time: datetime | None = field(AwareDateTime(data_key="startTime", missing=None))


@dataclass(frozen=True)
class DraftAlert(Smore):
    alert_type: str | None = field(Str(data_key="alertType", missing=None))
    message: str | None = field(Str(data_key="message", missing=None))
    priority: int | None = field(Int(data_key="priority", missing=None))
    updated_date: datetime | None = field(AwareDateTime(data_key="updatedDate", missing=None))


@dataclass(frozen=True)
class Player(Smore):
    competition: PlayerCompetitionDetails | None = field(Nested(PlayerCompetitionDetails.schema(), data_key="competition", missing=None))
    display_name: str | None = field(Str(data_key="displayName", missing=None))
    draftable_id: int | None = field(Int(data_key="draftableId", missing=None))
    draft_alerts: list[DraftAlert] = field(List(Nested(DraftAlert.schema()), data_key="draftAlerts", missing=[]))
    first_name: str | None = field(Str(data_key="firstName", missing=None))
    is_disabled: bool | None = field(Bool(data_key="isDisabled", missing=None))
    is_swappable: bool | None = field(Bool(data_key="isSwappable", missing=None))
    last_name: str | None = field(Str(data_key="lastName", missing=None))
    news_status: str | None = field(Str(data_key="newsStatus", missing=None))
    player_id: int | None = field(Int(data_key="playerId", missing=None))
    player_image_50: str | None = field(Str(data_key="playerImage50", missing=None))
    player_image_160: str | None = field(Str(data_key="playerImage160", missing=None))
    position: str | None = field(Str(data_key="position", missing=None))
    roster_slot_id: int | None = field(Int(data_key="rosterSlotId", missing=None))
    salary: float | None = field(Float(data_key="salary", missing=None))
    short_name: str | None = field(Str(data_key="shortName", missing=None))
    team_abbreviation: str | None = field(Str(data_key="teamAbbreviation", missing=None))
    team_id: int | None = field(Int(data_key="teamId", missing=None))


@dataclass(frozen=True)
class CompetitionTeam(Smore):
    abbreviation: str | None = field(Str(data_key="abbreviation", missing=None))
    city: str | None = field(Str(data_key="city", missing=None))
    team_id: int | None = field(Int(data_key="teamId", missing=None))
    team_name: str | None = field(Str(data_key="teamName", missing=None))


@dataclass(frozen=True)
class CompetitionWeather(Smore):
    icon: str | None = field(Str(data_key="icon", missing=None))
    is_dome: bool | None = field(Bool(data_key="isDome", missing=None))


@dataclass(frozen=True)
class Competition(Smore):
    are_depth_charts_available: bool | None = field(Bool(data_key="depthChartsAvailable", missing=None))
    are_starting_lineups_available: bool | None = field(Bool(data_key="startingLineupsAvailable", missing=None))
    away_team: CompetitionTeam | None = field(Nested(CompetitionTeam.schema(), data_key="awayTeam", missing=None))
    competition_id: int | None = field(Int(data_key="competitionId", missing=None))
    competition_state: str | None = field(Str(data_key="competitionState", missing=None))
    home_team: CompetitionTeam | None = field(Nested(CompetitionTeam.schema(), data_key="homeTeam", missing=None))
    name: str | None = field(Str(data_key="name", missing=None))
    sport: str | None = field(Str(data_key="sport", missing=None))
    sport_id: int | None = field(Int(data_key="sportId", missing=None))
    start_time: datetime | None = field(AwareDateTime(data_key="startTime", missing=None))
    venue: str | None = field(Str(data_key="venue", missing=None))
    weather: CompetitionWeather | None = field(Nested(CompetitionWeather.schema(), data_key="weather", missing=None))


@dataclass(frozen=True)
class Draftables(Smore):
    competitions: list[Competition] = field(List(Nested(Competition.schema()), data_key="competitions", missing=[]))
    draftables: list[Player] = field(List(Nested(Player.schema()), data_key="draftables", missing=[]))
