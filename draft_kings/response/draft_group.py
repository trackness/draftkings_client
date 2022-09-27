from dataclasses import dataclass
from datetime import datetime

from desert import field
from marshmallow.fields import Str, Int, AwareDateTime, Nested, List

from draft_kings.response.smore import Smore


@dataclass(frozen=True)
class ContestType(Smore):
    contest_type_id: int | None = field(Int(data_key="contestTypeId", missing=None))
    game_type: str | None = field(Str(data_key="gameType", missing=None))


@dataclass(frozen=True)
class League(Smore):
    league_abbreviation: str | None = field(Str(data_key="leagueAbbreviation", missing=None))
    league_id: int | None = field(Int(data_key="leagueId", missing=None))
    league_name: str | None = field(Str(data_key="leagueName", missing=None))


@dataclass(frozen=True)
class Game(Smore):
    away_team_id: int | None = field(Int(data_key="awayTeamId", missing=None))
    description: str | None = field(Str(data_key="description", missing=None))
    game_id: int | None = field(Int(data_key="gameId", missing=None))
    home_team_id: int | None = field(Int(data_key="homeTeamId", missing=None))
    location: str | None = field(Str(data_key="location", missing=None))
    name: str | None = field(Str(data_key="name", missing=None))
    start_date: datetime | None = field(AwareDateTime(data_key="startDate", missing=None))
    status: str | None = field(Str(data_key="status", missing=None))


@dataclass(frozen=True)
class DraftGroup(Smore):
    contest_type: ContestType = field(Nested(ContestType.schema(), data_key="contestType", required=True))
    draft_group_id: int | None = field(Int(data_key="draftGroupId", missing=None))
    draft_group_state: str | None = field(Str(data_key="draftGroupState", missing=None))
    games: list[Game] = field(List(Nested(Game.schema(), required=True), data_key="games", missing=[]))
    leagues: list[League] = field(List(Nested(League.schema(), required=True), data_key="leagues", missing=[]))
    max_start_time: datetime | None = field(AwareDateTime(data_key="maxStartTime", missing=None))
    min_start_time: datetime | None = field(AwareDateTime(data_key="minStartTime", missing=None))
    sport_id: int | None = field(Int(data_key="sportId", missing=None))
    start_time_type: str | None = field(Str(data_key="startTimeType", missing=None))


@dataclass(frozen=True)
class DraftGroupResponse(Smore):
    draft_group: DraftGroup = field(Nested(DraftGroup.schema(), data_key="draftGroup", required=True))
