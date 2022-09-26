from dataclasses import dataclass

from desert import field
from marshmallow.fields import Float, Str, Nested, Int, Bool, List

from draft_kings.response.objects.fields import DictField
from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class TeamSeries(Smore):
    away_team_id: int | None = field(Int(data_key="away_team_id", missing=None))
    home_team_id: int | None = field(Int(data_key="home_team_id", missing=None))
    starts_at: str | None = field(Str(data_key="status", missing=None))
    status: str | None = field(Str(data_key="starts_at", missing=None))
    weather: str | None = field(Str(data_key="weather", missing=None))


@dataclass(frozen=True)
class ExceptionalMessageType(Smore):
    name: str | None = field(Str(data_key="name", missing=None))


@dataclass(frozen=True)
class ExceptionalMessage(Smore):
    message: str | None = field(Str(data_key="message", missing=None))
    message_type: ExceptionalMessageType | None = field(Smore.nest(ExceptionalMessageType, data_key="message_type", missing=None))
    priority: int | None = field(Int(data_key="priority", missing=None))


@dataclass(frozen=True)
class Player(Smore):
    away_team_id: int | None = field(Int(data_key="away_team_id", missing=None))
    draft_group_start_time: int | None = field(Int(data_key="draft_group_start_time", missing=None))
    exceptional_messages: list[ExceptionalMessage] = field(Smore.list_nest(ExceptionalMessage, data_key="exceptional_messages", missing=None))
    first_name: str | None = field(Str(data_key="first_name", missing=None))
    home_team_id: int | None = field(Int(data_key="home_team_id", missing=None))
    is_disabled_from_drafting: bool | None = field(Bool(data_key="is_disabled_from_drafting", missing=None))
    jersey_number: int | None = field(Int(data_key="jersey_number", missing=None))
    last_name: str | None = field(Str(data_key="last_name", missing=None))
    opposition_rank: int | None = field(Int(data_key="opposition_rank", missing=None))
    player_id: int | None = field(Int(data_key="player_id", missing=None))
    position_id: int | None = field(Int(data_key="position_id", missing=None))
    position_name: str | None = field(Str(data_key="position_name", missing=None))
    points_per_game: str | None = field(Str(data_key="points_per_game", missing=None))
    salary: float | None = field(Float(data_key="salary", missing=None))
    team_id: int | None = field(Int(data_key="team_id", missing=None))
    team_series_id: int | None = field(Int(data_key="team_series_id", missing=None))


@dataclass(frozen=True)
class PlayersDetails(Smore):
    players: list[Player] = field(List(Nested(Player), attribute="players", missing=[]))
    team_series: dict[str, TeamSeries] = field(Smore.dict_nest(TeamSeries, attribute="team_series", missing=None))
