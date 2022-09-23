from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from desert import metadata
from marshmallow.fields import Str, Int, AwareDateTime, List, Nested

from draft_kings.response.objects.smore import Smore


@dataclass(frozen=True)
class ContestType(Smore):
    contest_type_id: Optional[int] = field(metadata=metadata(Int(data_key="contest_type_id", missing=None)))
    game_type: Optional[str] = field(metadata=metadata(Str(data_key="game_type", missing=None)))


@dataclass(frozen=True)
class League(Smore):
    league_abbreviation: Optional[str] = field(metadata=metadata(Str(data_key="league_abbreviation", missing=None)))
    league_id: Optional[int] = field(metadata=metadata(Int(data_key="league_id", missing=None)))
    league_name: Optional[str] = field(metadata=metadata(Str(data_key="league_name", missing=None)))


@dataclass(frozen=True)
class Game(Smore):
    away_team_id: Optional[int] = field(metadata=metadata(Int(data_key="away_team_id", missing=None)))
    description: Optional[str] = field(metadata=metadata(Str(data_key="description", missing=None)))
    game_id: Optional[int] = field(metadata=metadata(Int(data_key="game_id", missing=None)))
    home_team_id: Optional[int] = field(metadata=metadata(Int(data_key="home_team_id", missing=None)))
    location: Optional[str] = field(metadata=metadata(Str(data_key="location", missing=None)))
    name: Optional[str] = field(metadata=metadata(Str(data_key="name", missing=None)))
    start_date: Optional[datetime] = field(metadata=metadata(AwareDateTime(data_key="start_date", missing=None)))
    status: Optional[str] = field(metadata=metadata(Str(data_key="status", missing=None)))


@dataclass(frozen=True)
class DraftGroup(Smore):
    contest_type: ContestType = field(metadata=metadata(Nested(ContestType, data_key="contest_type", required=True)))
    draft_group_id: Optional[int] = field(metadata=metadata(Int(data_key="draft_group_id", missing=None)))
    draft_group_state: Optional[str] = field(metadata=metadata(Str(data_key="draft_group_state", missing=None)))
    games: list[Game] = field(metadata=metadata(List(Nested(Game, required=True), data_key="games", missing=[])))
    leagues: list[League] = field(metadata=metadata(List(Nested(League, required=True), data_key="leagues", missing=[])))
    max_start_time: Optional[datetime] = field(metadata=metadata(AwareDateTime(data_key="max_start_time", missing=None)))
    min_start_time: Optional[datetime] = field(metadata=metadata(AwareDateTime(data_key="min_start_time", missing=None)))
    sport_id: Optional[int] = field(metadata=metadata(Int(data_key="sport_id", missing=None)))
    start_time_type: Optional[str] = field(metadata=metadata(Str(data_key="start_time_type", missing=None)))


@dataclass(frozen=True)
class DraftGroupResponse(Smore):
    draft_group: DraftGroup = field(metadata=metadata(Nested(DraftGroup, data_key="draft_group", required=True)))
