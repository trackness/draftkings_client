# pylint: disable=too-many-instance-attributes
from typing import AnyStr

from requests import Response

from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output import ContestsDetails, CountriesDetails, DraftGroupDetails, DraftablesDetails, \
    GameTypeRulesDetails, PlayersDetails, RegionsDetails
from draft_kings.response import ResponseContests, ResponseDraftables, ResponsePlayersDetails, ResponseGameTypeRules, \
    ResponseRegions, DraftGroupResponse, ResponseCountries
from draft_kings.transformers import ContestsDetailsTransformer, PlayersDetailsTransformer, \
    DraftGroupDetailsTransformer, CountriesTransformer, RegionsTransformer, DraftablesTransformer, \
    GameTypeRulesTransformer
from draft_kings.url_builder import URLBuilder


class Client:
    def __init__(self):
        self.http_client: HTTPClient = HTTPClient(url_builder=URLBuilder())

    def contests(self, sport: Sport) -> ContestsDetails:
        response: Response = self.http_client.contests(sport=sport)
        deserialized_response: ResponseContests = ResponseContests.loads(response.text)
        return ContestsDetailsTransformer().transform(deserialized_response)

    def available_players(self, draft_group_id: int) -> PlayersDetails:
        response: Response = self.http_client.available_players(draft_group_id=draft_group_id)
        deserialized_response: ResponsePlayersDetails = ResponsePlayersDetails.loads(response.text)
        return PlayersDetailsTransformer().transform(deserialized_response)

    def draft_group_details(self, draft_group_id: int) -> DraftGroupDetails:
        response: Response = self.http_client.draft_group_details(draft_group_id=draft_group_id)
        deserialized_response = DraftGroupResponse.loads(response.text)
        return DraftGroupDetailsTransformer().transform(deserialized_response.draft_group)

    def countries(self) -> CountriesDetails:
        response: Response = self.http_client.countries()
        deserialized_response: ResponseCountries = ResponseCountries.loads(response.text)
        return CountriesTransformer().transform(deserialized_response)

    def regions(self, country_code: AnyStr) -> RegionsDetails:
        response: Response = self.http_client.regions(country_code=country_code)
        deserialized_response: ResponseRegions = ResponseRegions.loads(response.text)
        return RegionsTransformer().transform(deserialized_response)

    def draftables(self, draft_group_id: int) -> DraftablesDetails:
        response: Response = self.http_client.draftables(draft_group_id=draft_group_id)
        deserialized_response: ResponseDraftables = ResponseDraftables.loads(response.text)
        return DraftablesTransformer().transform(deserialized_response)

    def game_type_rules(self, game_type_id: int) -> GameTypeRulesDetails:
        response: Response = self.http_client.game_type_rules(game_type_id=game_type_id)
        deserialized_response: ResponseGameTypeRules = ResponseGameTypeRules.loads(response.text)
        return GameTypeRulesTransformer().transform(deserialized_response)

# pylint: enable=too-many-instance-attributes
