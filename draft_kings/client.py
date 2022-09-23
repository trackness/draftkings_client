# pylint: disable=too-many-instance-attributes
from typing import AnyStr

from requests import Response

from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.contests import ContestsDetails
from draft_kings.output.objects.countries import CountriesDetails
from draft_kings.output.objects.draft_group import DraftGroupDetails
from draft_kings.output.objects.draftables import DraftablesDetails
from draft_kings.output.objects.game_type_rules import GameTypeRulesDetails
from draft_kings.output.objects.players import PlayersDetails
from draft_kings.output.objects.regions import RegionsDetails
from draft_kings.output.transformers.contests import ContestsDetailsTransformer, DraftGroupTransformer, \
    ContestTransformer
from draft_kings.output.transformers.countries import CountriesTransformer, transform_country
from draft_kings.output.transformers.draft_group import transform_contest as transform_draft_group_contest, \
    transform_draft_group_start_time_details, transform_game, transform_league, DraftGroupDetailsTransformer
from draft_kings.output.transformers.draftables import transform_competition_team_details, \
    transform_competition_weather_details, transform_player_competition_details, transform_player_image_details, \
    transform_player_name_details, transform_player_team_details, PlayerTransformer, CompetitionTransformer, \
    DraftablesTransformer, transform_draft_alert
from draft_kings.output.transformers.game_type_rules import transform_roster_slot, transform_salary_cap, \
    LineupTemplateTransformer, GameTypeRulesTransformer
from draft_kings.output.transformers.players import TeamSeriesTransformer, DraftDetailsTransformer, \
    transform_player_position, transform_player_team_series_details, PlayerDetailsTransformer, \
    PlayersDetailsTransformer, ExceptionalMessageTransformer, transform_exceptional_message_type
from draft_kings.output.transformers.regions import RegionsTransformer, transform_region
from draft_kings.output.transformers.sports import transform_sport_id, transform_sport_abbreviation
from draft_kings.response.objects.contests import Contests as ResponseContests
from draft_kings.response.objects.countries import Countries as ResponseCountries
from draft_kings.response.objects.draftables import Draftables as ResponseDraftables
from draft_kings.response.objects.game_type_rules import GameTypeRules as ResponseGameTypeRules
from draft_kings.response.objects.players import PlayersDetails as ResponsePlayersDetails
from draft_kings.response.objects.regions import Regions as ResponseRegions
from draft_kings.url_builder import URLBuilder
from draft_kings.utilities import translate_formatted_datetime, from_unix_milliseconds_to_datetime


class Client:
    def __init__(self):
        self.contest_details_transformer: ContestsDetailsTransformer = ContestsDetailsTransformer(
            contest_transformer=ContestTransformer(
                formatted_datetime_transformer=translate_formatted_datetime,
                sport_id_transformer=transform_sport_id,
            ),
            draft_group_transformer=DraftGroupTransformer(
                sport_abbreviation_transformer=transform_sport_abbreviation,
            )
        )
        self.players_details_transformer: PlayersDetailsTransformer = PlayersDetailsTransformer(
            team_series_transformer=TeamSeriesTransformer(
                formatted_datetime_translator=translate_formatted_datetime
            ),
            player_details_transformer=PlayerDetailsTransformer(
                draft_details_transformer=DraftDetailsTransformer(
                    unix_milliseconds_translator=from_unix_milliseconds_to_datetime
                ),
                player_team_series_details_transformer=transform_player_team_series_details,
                player_position_transformer=transform_player_position,
                exceptional_message_transformer=ExceptionalMessageTransformer(
                    message_type_transformer=transform_exceptional_message_type
                )
            )
        )
        self.draft_group_details_transformer: DraftGroupDetailsTransformer = DraftGroupDetailsTransformer(
            contest_transformer=transform_draft_group_contest,
            game_transformer=transform_game,
            league_transformer=transform_league,
            sport_id_transformer=transform_sport_id,
            start_time_details_transformer=transform_draft_group_start_time_details
        )
        self.countries_transformer: CountriesTransformer = CountriesTransformer(country_transformer=transform_country)
        self.regions_transformer: RegionsTransformer = RegionsTransformer(region_transformer=transform_region)
        self.draftables_transformer: DraftablesTransformer = DraftablesTransformer(
            competition_transformer=CompetitionTransformer(
                team_details_transformer=transform_competition_team_details,
                weather_details_transformer=transform_competition_weather_details,
                sport_abbreviation_transformer=transform_sport_abbreviation,
            ),
            player_transformer=PlayerTransformer(
                competition_details_transformer=transform_player_competition_details,
                name_details_transformer=transform_player_name_details,
                image_details_transformer=transform_player_image_details,
                team_details_transformer=transform_player_team_details,
                draft_alert_transformer=transform_draft_alert,
            )
        )
        self.game_type_rules_transformer: GameTypeRulesTransformer = GameTypeRulesTransformer(
            salary_cap_transformer=transform_salary_cap,
            lineup_template_transformer=LineupTemplateTransformer(
                roster_slot_transformer=transform_roster_slot,
            )
        )

        self.http_client: HTTPClient = HTTPClient(url_builder=URLBuilder())

    def contests(self, sport: Sport) -> ContestsDetails:
        response: Response = self.http_client.contests(sport=sport)
        deserialized_response: ResponseContests = ResponseContests.loads(response.text)
        return self.contest_details_transformer.transform(deserialized_response)

    def available_players(self, draft_group_id: int) -> PlayersDetails:
        response: Response = self.http_client.available_players(draft_group_id=draft_group_id)
        deserialized_response: ResponsePlayersDetails = ResponsePlayersDetails.loads(response.text)
        return self.players_details_transformer.transform(deserialized_response)

    def draft_group_details(self, draft_group_id: int) -> DraftGroupDetails:
        response: Response = self.http_client.draft_group_details(draft_group_id=draft_group_id)
        deserialized_response = ResponseDraftables.loads(response.text)
        return self.draft_group_details_transformer.transform(deserialized_response.draft_group)

    def countries(self) -> CountriesDetails:
        response: Response = self.http_client.countries()
        deserialized_response: ResponseCountries = ResponseCountries.loads(response.text)
        return self.countries_transformer.transform(deserialized_response)

    def regions(self, country_code: AnyStr) -> RegionsDetails:
        response: Response = self.http_client.regions(country_code=country_code)
        deserialized_response: ResponseRegions = ResponseRegions.loads(response.text)
        return self.regions_transformer.transform(deserialized_response)

    def draftables(self, draft_group_id: int) -> DraftablesDetails:
        response: Response = self.http_client.draftables(draft_group_id=draft_group_id)
        deserialized_response: ResponseDraftables = ResponseDraftables.loads(response.text)
        return self.draftables_transformer.transform(deserialized_response)

    def game_type_rules(self, game_type_id: int) -> GameTypeRulesDetails:
        response: Response = self.http_client.game_type_rules(game_type_id=game_type_id)
        deserialized_response: ResponseGameTypeRules = ResponseGameTypeRules.loads(response.text)
        return self.game_type_rules_transformer.transform(deserialized_response)

# pylint: enable=too-many-instance-attributes
