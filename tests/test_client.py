import pytest
from pytest import param
from requests_mock import mock

from draft_kings import Client
from draft_kings.data import Sport
from draft_kings.model.contests import Contests
from draft_kings.model.countries import Countries
from draft_kings.model.draft_group import Game, DraftGroup
from draft_kings.model.draftables import Player as DraftPlayer, Competition, Draftables
from draft_kings.model.game_type_rules import LineupTemplate, GameTypeRules
from draft_kings.model.players import TeamSeries, Players, Player
from draft_kings.model.regions import Region, Regions
from draft_kings.url_builder import URLBuilder
from tests.utilities import read_fixture


class TestClient:
    @pytest.fixture(autouse=True)
    def under_test(self) -> Client:
        return Client()

    def test_tmp(self) -> None:
        pass

    class TestAvailablePlayers:
        def test_integration(self, under_test: Client) -> None:
            result: Players = under_test.available_players(draft_group_id=42463)

            assert result is not None
            assert isinstance(result, Players)

            assert result.players is not None
            assert len(result.players) == 75
            assert isinstance(result.players[0], Player)
            assert result.players[0].player_id == 603096

            assert result.team_series is not None
            assert len(result.team_series) == 2
            assert isinstance(result.team_series[0], TeamSeries)
            assert result.team_series[0].team_series_id == 5713406

        def test_unit(self, under_test: Client, requests_mock: mock) -> None:
            fixture: str = read_fixture("available_players/41793")
            expected: Players = Players.model_validate_json(fixture)
            requests_mock.get(f"{URLBuilder.available_players()}?draftGroupId=41793", text=fixture)
            actual: Players = under_test.available_players(draft_group_id=41793)
            assert actual is not None
            assert expected.players[3].exceptional_messages == actual.players[3].exceptional_messages

    class TestContests:
        @pytest.mark.parametrize("sport", [param(sport) for sport in Sport])
        def test_integration(self, under_test: Client, sport: Sport) -> None:
            result: Contests = under_test.contests(sport=sport)
            assert result is not None
            assert result.contests is not None
            assert result.draft_groups is not None

        def test_unit(self, under_test: Client, requests_mock: mock) -> None:
            fixture: str = read_fixture("contests/golf/2020_10_22")
            expected: Contests = Contests.model_validate_json(fixture)
            requests_mock.get(f"{URLBuilder.contests()}?sport=GOLF", text=fixture)
            actual: Contests = under_test.contests(Sport.GOLF)
            assert actual is not None
            assert actual == expected

    class TestCountries:
        def test_integration(self, under_test: Client) -> None:
            result = under_test.countries()
            assert result is not None
            assert len(result.countries) > 0

        def test_unit(self, under_test: Client, requests_mock: mock) -> None:
            fixture: str = read_fixture("countries")
            expected = Countries.model_validate_json(fixture)
            requests_mock.get(URLBuilder.countries(), text=fixture)
            actual: Countries = under_test.countries()
            assert actual is not None
            assert actual == expected

    class TestDraftGroupDetails:
        def test_integration(self, under_test: Client) -> None:
            result: DraftGroup = under_test.draft_group_details(draft_group_id=11513)

            assert result is not None
            assert isinstance(result, DraftGroup)
            assert result.draft_group_id == 11513
            assert result.sport == Sport.NBA

            assert result.games is not None
            assert len(result.games) == 5
            assert isinstance(result.games[0], Game)

        def test_unit(self, under_test: Client, requests_mock: mock) -> None:
            fixture: str = read_fixture("draft_group_details/11513")
            expected: DraftGroup = DraftGroup.model_validate_json(fixture)
            requests_mock.get(f"{URLBuilder.draft_groups(draft_group_id=11513)}", text=fixture)
            actual: DraftGroup = under_test.draft_group_details(draft_group_id=11513)
            assert actual is not None
            assert expected == actual

    class TestDraftables:
        def test_integration(self, under_test: Client) -> None:
            result: Draftables = under_test.draftables(draft_group_id=41793)

            assert result is not None
            assert isinstance(result, Draftables)

            assert result.players is not None
            assert len(result.players) == 213
            assert isinstance(result.players[0], DraftPlayer)

            assert result.competitions is not None
            assert len(result.competitions) == 3
            assert isinstance(result.competitions[0], Competition)

        def test_unit(self, under_test: Client, requests_mock: mock) -> None:
            fixture: str = read_fixture("draftables/41793/upcoming")  # add draftables/41793/postponed too
            expected: Draftables = Draftables.model_validate_json(fixture)
            requests_mock.get(f"{URLBuilder.draftables(draft_group_id=41793)}", text=fixture)
            actual: Draftables = under_test.draftables(draft_group_id=41793)
            assert actual is not None
            assert expected == actual

    class TestGameTypeRules:
        def test_integration(self, under_test: Client) -> None:
            result: GameTypeRules = under_test.game_type_rules(game_type_id=1)

            assert result is not None
            assert isinstance(result, GameTypeRules)
            assert result.name == "Classic"

            assert result.lineup_templates is not None
            assert len(result.lineup_templates) == 9
            assert isinstance(result.lineup_templates[0], LineupTemplate)

        def test_unit(self, under_test: Client, requests_mock: mock) -> None:
            fixture: str = read_fixture("game_type_rules/1")
            expected: GameTypeRules = GameTypeRules.model_validate_json(fixture)
            requests_mock.get(f"{URLBuilder.game_type_rules(1)}", text=fixture)
            actual: GameTypeRules = under_test.game_type_rules(game_type_id=1)
            assert actual is not None
            assert expected == actual

    class TestRegions:
        @pytest.mark.parametrize(
            "region, first_region",
            [
                param("US", Region.model_construct(code="AL", country_code="US", iso_code="US-AL", name="Alabama"), id="US"),
                param("GB", Region.model_construct(code="ABE", country_code="GB", iso_code="GB-ABE", name="Aberdeen City"), id="GB"),
                param("CA", Region.model_construct(code="AB", country_code="CA", iso_code="CA-AB", name="Alberta"), id="CA"),
            ],
        )
        def test_integration(self, under_test: Client, region: str, first_region: Region) -> None:
            response = under_test.regions(region)
            assert response is not None
            assert len(response.regions) > 0
            assert response.regions[0] == first_region

        @pytest.mark.parametrize("region", [param("US"), param("GB"), param("CA")])
        def test_unit(self, under_test: Client, region: str, requests_mock: mock) -> None:
            fixture: str = read_fixture(f"regions/{region.lower()}")
            expected = Regions.model_validate_json(fixture)
            requests_mock.get(URLBuilder.regions(region), text=fixture)
            actual: Regions = under_test.regions(region)
            assert actual is not None
            assert actual == expected
