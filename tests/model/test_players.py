from datetime import datetime, timezone

import pytest

from draft_kings.model.players import (
    TeamSeries,
    Player,
    ExceptionalMessage,
    ExceptionalMessageType,
    Players,
    DraftDetails,
    Position,
    PlayerTeamSeries,
)
from tests.utilities import read_fixture


class TestSoccerPlayers:
    @pytest.fixture(autouse=True)
    def under_test(self) -> Players:
        return Players.model_validate_json(read_fixture("available_players/22831"))

    def test_deserialization(self, under_test: Players) -> None:
        assert under_test is not None

        assert under_test.players[0], Player.model_construct(
            draft_details=DraftDetails.model_construct(is_draftable=True, salary=10400.0, starts_at=None),
            exceptional_messages=[],
            first_name="Eden",
            last_name="Hazard",
            jersey_number=7,
            player_id=42786,
            points_per_game=0.0,
            position=Position.model_construct(id=182, name="M/F"),
            team_id=40551,
            team_series_details=PlayerTeamSeries.model_construct(
                away_team_id=40551,
                home_team_id=40813,
                opposition_rank=1,
                team_series_id=5527123,
            ),
        )

    def test_first_player_details(self, under_test: Players) -> None:
        pass

    def test_tottenham_and_chelesa_team_series_details(self, under_test: Players) -> None:
        assert next(
            (team_series for team_series in under_test.team_series if team_series.team_series_id == 5527123), None
        ), TeamSeries.model_construct(
            away_team_id=40551,
            home_team_id=40813,
            starts_at=datetime(2018, 11, 24, 17, 30, tzinfo=timezone.utc),
            status_description="Final",
            team_series_id=5527123,
            weather=None,
        )

    def test_west_ham_united_and_manchester_city_team_series_details(self, under_test: Players):
        assert TeamSeries.model_construct(
            away_team_id=40552,
            home_team_id=40819,
            starts_at=datetime(2018, 11, 24, 15, 0, tzinfo=timezone.utc),
            status_description="Final",
            team_series_id=5527125,
            weather=None,
        ), next((team_series for team_series in under_test.team_series if team_series.team_series_id == 5527125), None)

    def test_watford_and_liverpool_team_series_details(self, under_test: Players):
        assert TeamSeries.model_construct(
            away_team_id=40817,
            home_team_id=40824,
            starts_at=datetime(2018, 11, 24, 15, 0, tzinfo=timezone.utc),
            status_description="Final",
            team_series_id=5527124,
            weather=None,
        ), next((team_series for team_series in under_test.team_series if team_series.team_series_id == 5527124), None)

    def test_everton_and_cardiff_team_series_details(self, under_test: Players):
        assert TeamSeries.model_construct(
            away_team_id=53600,
            home_team_id=40815,
            starts_at=datetime(2018, 11, 24, 15, 0, tzinfo=timezone.utc),
            status_description="Final",
            team_series_id=5527120,
            weather=None,
        ), next((team_series for team_series in under_test.team_series if team_series.team_series_id == 5527120), None)

    def test_manchester_united_and_crystal_palace_team_series_details(self, under_test: Players):
        assert TeamSeries.model_construct(
            away_team_id=40820,
            home_team_id=40549,
            starts_at=datetime(2018, 11, 24, 15, 0, tzinfo=timezone.utc),
            status_description="Final",
            team_series_id=5527122,
            weather=None,
        ), next((team_series for team_series in under_test.team_series if team_series.team_series_id == 5527122), None)

    def test_birmingham_and_leicester_team_series_details(self, under_test: Players):
        assert TeamSeries.model_construct(
            away_team_id=40816,
            home_team_id=53563,
            starts_at=datetime(2018, 11, 24, 15, 0, tzinfo=timezone.utc),
            status_description="Final",
            team_series_id=5527118,
            weather=None,
        ), next((team_series for team_series in under_test.team_series if team_series.team_series_id == 5527118), None)

    def test_fulham_and_southampton_team_series_details(self, under_test: Players):
        assert TeamSeries.model_construct(
            away_team_id=40818,
            home_team_id=53577,
            starts_at=datetime(2018, 11, 24, 15, 0, tzinfo=timezone.utc),
            status_description="Final",
            team_series_id=5527121,
            weather=None,
        ), next((team_series for team_series in under_test.team_series if team_series.team_series_id == 5527121), None)


class TestNFLPlayersWithExceptionalMessages:
    @pytest.fixture(autouse=True)
    def under_test(self) -> Players:
        return Players.model_validate_json(read_fixture("available_players/41793"))

    def test_exceptional_messages(self, under_test: Players) -> None:
        assert under_test.players[3].exceptional_messages == [
            ExceptionalMessage.model_construct(
                message="The Ravens vs. Steelers game has been postponed. Players will NOT receive fantasy points "
                "in Thursday (11/26) MAIN and TIERS contests, please check your lineups!",
                priority_value=100,
                type_details=ExceptionalMessageType.model_construct(name="player"),
            )
        ]
