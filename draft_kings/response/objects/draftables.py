from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from desert import metadata
from marshmallow.fields import Float, Str, Nested, Int, Bool, AwareDateTime, List

from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class PlayerCompetitionDetails(Smore):
    competition_id: Optional[int] = field(metadata=metadata(Int(attribute="competition_id", missing=None)))
    name: Optional[str] = field(metadata=metadata(Str(attribute="name", missing=None)))
    start_time: Optional[datetime] = field(metadata=metadata(AwareDateTime(attribute="start_time", missing=None)))


@dataclass(frozen=True)
class DraftAlert(Smore):
    alert_type: Optional[str] = field(metadata=metadata(Str(attribute="alert_type", missing=None)))
    message: Optional[str] = field(metadata=metadata(Str(attribute="message", missing=None)))
    priority: Optional[int] = field(metadata=metadata(Int(attribute="priority", missing=None)))
    updated_date: Optional[datetime] = field(metadata=metadata(AwareDateTime(attribute="updated_date", missing=None)))


@dataclass(frozen=True)
class Player(Smore):
    competition: Optional[PlayerCompetitionDetails] = field(metadata=metadata(Nested(PlayerCompetitionDetails, attribute="competition", missing=None)))
    display_name: Optional[str] = field(metadata=metadata(Str(attribute="display_name", missing=None)))
    draftable_id: Optional[int] = field(metadata=metadata(Int(attribute="draftable_id", missing=None)))
    draft_alerts: list[DraftAlert] = field(metadata=metadata(List(Nested(DraftAlert), attribute="draft_alerts", missing=[])))
    first_name: Optional[str] = field(metadata=metadata(Str(attribute="first_name", missing=None)))
    is_disabled: Optional[bool] = field(metadata=metadata(Bool(attribute="is_disabled", missing=None)))
    is_swappable: Optional[bool] = field(metadata=metadata(Bool(attribute="is_swappable", missing=None)))
    last_name: Optional[str] = field(metadata=metadata(Str(attribute="last_name", missing=None)))
    news_status: Optional[str] = field(metadata=metadata(Str(attribute="news_status", missing=None)))
    player_id: Optional[int] = field(metadata=metadata(Int(attribute="player_id", missing=None)))
    player_image_50: Optional[str] = field(metadata=metadata(Str(attribute="player_image_50", missing=None)))
    player_image_160: Optional[str] = field(metadata=metadata(Str(attribute="player_image_160", missing=None)))
    position: Optional[str] = field(metadata=metadata(Str(attribute="position", missing=None)))
    roster_slot_id: Optional[int] = field(metadata=metadata(Int(attribute="roster_slot_id", missing=None)))
    salary: Optional[float] = field(metadata=metadata(Float(attribute="salary", missing=None)))
    short_name: Optional[str] = field(metadata=metadata(Str(attribute="short_name", missing=None)))
    team_abbreviation: Optional[str] = field(metadata=metadata(Str(attribute="team_abbreviation", missing=None)))
    team_id: Optional[int] = field(metadata=metadata(Int(attribute="team_id", missing=None)))


@dataclass(frozen=True)
class CompetitionTeam(Smore):
    abbreviation: Optional[str] = field(metadata=metadata(Str(attribute="abbreviation", missing=None)))
    city: Optional[str] = field(metadata=metadata(Str(attribute="city", missing=None)))
    team_id: Optional[int] = field(metadata=metadata(Int(attribute="team_id", missing=None)))
    team_name: Optional[str] = field(metadata=metadata(Str(attribute="team_name", missing=None)))


@dataclass(frozen=True)
class CompetitionWeather(Smore):
    icon: Optional[str] = field(metadata=metadata(Str(attribute="icon", missing=None)))
    is_dome: Optional[bool] = field(metadata=metadata(Bool(attribute="is_dome", missing=None)))


@dataclass(frozen=True)
class Competition(Smore):
    are_depth_charts_available: Optional[bool] = field(metadata=metadata(Nested(CompetitionTeam, attribute="away_team", missing=None)))
    are_starting_lineups_available: Optional[bool] = field(metadata=metadata(Int(attribute="competition_id", missing=None)))
    away_team: Optional[CompetitionTeam] = field(metadata=metadata(Str(attribute="competition_state", missing=None)))
    competition_id: Optional[int] = field(metadata=metadata(Bool(attribute="are_depth_charts_available", missing=None)))
    competition_state: Optional[str] = field(metadata=metadata(Nested(CompetitionTeam, attribute="home_team", missing=None)))
    home_team: Optional[CompetitionTeam] = field(metadata=metadata(Str(attribute="name", missing=None)))
    name: Optional[str] = field(metadata=metadata(Str(attribute="sport", missing=None)))
    sport: Optional[str] = field(metadata=metadata(Bool(attribute="are_starting_lineups_available", missing=None)))
    start_time: Optional[datetime] = field(metadata=metadata(AwareDateTime(attribute="start_time", missing=None)))
    venue: Optional[str] = field(metadata=metadata(Str(attribute="venue", missing=None)))
    weather: Optional[CompetitionWeather] = field(metadata=metadata(Nested(CompetitionWeather, attribute="weather", missing=None)))


@dataclass(frozen=True)
class Draftables(Smore):
    competitions: list[Competition] = field(metadata=metadata(List(Nested(Player), data_key="draftables", missing=[])))
    draftables: list[Player] = field(metadata=metadata(List(Nested(Competition), attribute="competitions", missing=[])))
