from dataclasses import dataclass

from desert import field
from marshmallow.fields import Float, Str, Int, Bool

from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class TeamSeries(Smore):
    away_team_id: int | None = field(Int(data_key="atid", missing=None))
    home_team_id: int | None = field(Int(data_key="htid", missing=None))
    starts_at: str | None = field(Str(data_key="tz", missing=None))
    status: str | None = field(Str(data_key="status", missing=None))
    weather: str | None = field(Str(data_key="wthr", missing=None))


@dataclass(frozen=True)
class ExceptionalMessageType(Smore):
    name: str | None = field(Str(data_key="Name", missing=None))


@dataclass(frozen=True)
class ExceptionalMessage(Smore):
    message: str | None = field(Str(data_key="Message", missing=None))
    message_type: ExceptionalMessageType | None = field(Smore.nest(ExceptionalMessageType, data_key="MessageType", missing=None))
    priority: int | None = field(Int(data_key="Priority", missing=None))


@dataclass(frozen=True)
class Player(Smore):
    away_team_id: int | None = field(Int(data_key="atid", missing=None))
    draft_group_start_time: int | None = field(Int(data_key="dgst", missing=None))
    exceptional_messages: list[ExceptionalMessage] = field(Smore.list_nest(ExceptionalMessage, data_key="ExceptionalMessages", missing=None))
    first_name: str | None = field(Str(data_key="fn", missing=None))
    home_team_id: int | None = field(Int(data_key="htid", missing=None))
    is_disabled_from_drafting: bool | None = field(Bool(data_key="IsDisabledFromDrafting", missing=None))
    jersey_number: int | None = field(Int(data_key="jn", missing=None))
    last_name: str | None = field(Str(data_key="ln", missing=None))
    opposition_rank: int | None = field(Int(data_key="or", missing=None))
    player_id: int | None = field(Int(data_key="pid", missing=None))
    position_id: int | None = field(Int(data_key="posid", missing=None))
    position_name: str | None = field(Str(data_key="pn", missing=None))
    points_per_game: str | None = field(Str(data_key="ppg", missing=None))
    salary: float | None = field(Float(data_key="s", missing=None))
    team_id: int | None = field(Int(data_key="tid", missing=None))
    team_series_id: int | None = field(Int(data_key="tsid", missing=None))


@dataclass(frozen=True)
class PlayersDetails(Smore):
    players: list[Player] = field(Smore.list_nest(Player, data_key="playerList", missing=[]))
    team_series: dict[str, TeamSeries] = field(Smore.dict_nest(TeamSeries, data_key="teamList", missing=None))
