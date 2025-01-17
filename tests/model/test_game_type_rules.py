import pytest

from draft_kings.model.game_type_rules import SalaryCap, RosterSlot, LineupTemplate, GameTypeRules
from tests.utilities import read_fixture


class TestClassicNFLGameTypeRules:
    @pytest.fixture(autouse=True)
    def under_test(self) -> GameTypeRules:
        return GameTypeRules.model_validate_json(read_fixture("game_type_rules/1"))

    def test_deserialization(self, under_test: GameTypeRules) -> None:
        assert under_test is not None

    def test_game_type_rules(self, under_test: GameTypeRules) -> None:
        assert under_test, GameTypeRules.model_construct(
            allow_late_swap=True,
            description="Create a 9-player lineup while staying under the $50,000 salary cap",
            draft_type_name="SalaryCap",
            name="Classic",
            game_type_id=1,
            lineup_templates=[
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Quarterback",
                        name="QB",
                        roster_slot_id=66,
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Running Back",
                        name="RB",
                        roster_slot_id=67,
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Running Back",
                        name="RB",
                        roster_slot_id=67,
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Wide Receiver",
                        name="WR",
                        roster_slot_id=68,
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Wide Receiver",
                        name="WR",
                        roster_slot_id=68,
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Wide Receiver",
                        name="WR",
                        roster_slot_id=68,
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Tight End",
                        name="TE",
                        roster_slot_id=69,
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(description="Flex", name="FLEX", roster_slot_id=70)
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Defense/Special Teams", name="DST", roster_slot_id=71
                    )
                ),
            ],
            salary_cap_details=SalaryCap.model_construct(
                is_enabled=True,
                maximum_value=50000.0,
                minimum_value=0.0,
            ),
            enforce_selecting_unique_players=True,
        )
