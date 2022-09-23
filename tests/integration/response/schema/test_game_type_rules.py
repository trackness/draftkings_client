from unittest import TestCase

from draft_kings.response.objects.game_type_rules import SalaryCap, RosterSlot, LineupTemplate, GameTypeRules
from tests.config import load_fixture


class TestClassicNFLGameTypeRules(TestCase):
    def setUp(self) -> None:
        with load_fixture('game_type_rules/1.json') as data_file:
            self.data = GameTypeRules.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_game_type_rules(self) -> None:
        self.assertEqual(
            GameTypeRules(
                allow_late_swap=True,
                description="Create a 9-player lineup while staying under the $50,000 salary cap",
                draft_type="SalaryCap",
                name="Classic",
                game_type_id=1,
                lineup_template=[
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Quarterback",
                            name="QB",
                            roster_slot_id=66,
                        )
                    ),
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Running Back",
                            name="RB",
                            roster_slot_id=67,
                        )
                    ),
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Running Back",
                            name="RB",
                            roster_slot_id=67,
                        )
                    ),
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Tight End",
                            name="TE",
                            roster_slot_id=69,
                        )
                    ),
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Flex",
                            name="FLEX",
                            roster_slot_id=70
                        )
                    ),
                    LineupTemplate(
                        roster_slot=RosterSlot(
                            description="Defense/Special Teams",
                            name="DST",
                            roster_slot_id=71
                        )
                    )
                ],
                salary_cap=SalaryCap(
                    is_enabled=True,
                    min_value=0,
                    max_value=50000,
                ),
                unique_players=True,
            ),
            self.data
        )
