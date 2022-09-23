from dataclasses import dataclass, field
from typing import Optional

from desert import metadata
from marshmallow.fields import Float, Str, Nested, Int, Bool, List

from draft_kings.response.objects.fields import DictField
from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class TeamSeries(Smore):
    away_team_id: Optional[int] = field(metadata=metadata(Int(data_key="away_team_id", missing=None)))
    home_team_id: Optional[int] = field(metadata=metadata(Int(data_key="home_team_id", missing=None)))
    starts_at: Optional[str] = field(metadata=metadata(Str(data_key="status", missing=None)))
    status: Optional[str] = field(metadata=metadata(Str(data_key="starts_at", missing=None)))
    weather: Optional[str] = field(metadata=metadata(Str(data_key="weather", missing=None)))


@dataclass(frozen=True)
class ExceptionalMessageType(Smore):
    name: Optional[str] = field(metadata=metadata(Str(data_key="name", missing=None)))


@dataclass(frozen=True)
class ExceptionalMessage(Smore):
    message: Optional[str] = field(metadata=metadata(Str(data_key="message", missing=None)))
    message_type: Optional[ExceptionalMessageType] = field(metadata=metadata(Nested(ExceptionalMessageType, data_key="message_type", missing=None)))
    priority: Optional[int] = field(metadata=metadata(Int(data_key="priority", missing=None)))


@dataclass(frozen=True)
class Player(Smore):
    away_team_id: Optional[int] = field(metadata=metadata(Int(data_key="away_team_id", missing=None)))
    draft_group_start_time: Optional[int] = field(metadata=metadata(Int(data_key="draft_group_start_time", missing=None)))
    exceptional_messages: list[ExceptionalMessage] = field(metadata=metadata(List(Nested(ExceptionalMessage), data_key="exceptional_messages", missing=None)))
    first_name: Optional[str] = field(metadata=metadata(Str(data_key="first_name", missing=None)))
    home_team_id: Optional[int] = field(metadata=metadata(Int(data_key="home_team_id", missing=None)))
    is_disabled_from_drafting: Optional[bool] = field(metadata=metadata(Bool(data_key="is_disabled_from_drafting", missing=None)))
    jersey_number: Optional[int] = field(metadata=metadata(Int(data_key="jersey_number", missing=None)))
    last_name: Optional[str] = field(metadata=metadata(Str(data_key="last_name", missing=None)))
    opposition_rank: Optional[int] = field(metadata=metadata(Int(data_key="opposition_rank", missing=None)))
    player_id: Optional[int] = field(metadata=metadata(Int(data_key="player_id", missing=None)))
    position_id: Optional[int] = field(metadata=metadata(Int(data_key="position_id", missing=None)))
    position_name: Optional[str] = field(metadata=metadata(Str(data_key="position_name", missing=None)))
    points_per_game: Optional[str] = field(metadata=metadata(Str(data_key="points_per_game", missing=None)))
    salary: Optional[float] = field(metadata=metadata(Float(data_key="salary", missing=None)))
    team_id: Optional[int] = field(metadata=metadata(Int(data_key="team_id", missing=None)))
    team_series_id: Optional[int] = field(metadata=metadata(Int(data_key="team_series_id", missing=None)))


@dataclass(frozen=True)
class PlayersDetails(Smore):
    players: list[Player] = field(metadata=metadata(List(Nested(Player), attribute="players", missing=[])))
    team_series: dict[str, TeamSeries] = field(metadata=metadata(DictField(Str(required=True), Nested(TeamSeries, required=True), attribute="team_series", missing=None)))
