from datetime import datetime, timezone
from unittest import TestCase

from draft_kings.response.contests import Contest, ContestAttributes, DraftGroup, Contests
from tests.config import load_fixture


class TestUpcomingNFLContests(TestCase):
    def setUp(self) -> None:
        with load_fixture('contests/nfl/2020_10_22.json') as data_file:
            self.data: Contests = Contests.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_contests_exist(self) -> None:
        self.assertIsNotNone(self.data.contests)

    def test_contests_have_a_length_greater_than_0(self) -> None:
        self.assertGreater(len(self.data.contests), 0)

    def test_first_contest(self):
        self.assertEqual(
            Contest(
                attributes=ContestAttributes(
                    is_double_up=None,
                    is_fifty_fifty=None,
                    is_guaranteed=True,
                    is_h2h=None,
                    is_starred=True
                ),
                contest_id=96625286,
                draft_group_id=41643,
                entry_fee=20,
                entry_maximum=205882,
                entry_total=144081,
                fantasy_player_points=20,
                name="NFL $3.5M Fantasy Football Millionaire [$1M to 1st]",
                payout=3500000,
                sport_id=1,
                starts_at="/Date(1606068000000)/"
            ),
            self.data.contests[0]
        )

    def test_draft_groups_exist(self):
        self.assertIsNotNone(self.data.draft_groups)

    def test_draft_groups_have_a_length_greater_than_0(self):
        self.assertGreater(len(self.data.draft_groups), 0)

    def test_first_draft_group(self):
        self.assertEqual(
            DraftGroup(
                draft_group_id=41643,
                series_id=2,
                contest_type_id=21,
                game_count=11,
                sport="NFL",
                starts_at=datetime(year=2020, month=11, day=22, hour=18, minute=0, second=0, microsecond=0,
                                    tzinfo=timezone.utc)
            ),
            self.data.draft_groups[0]
        )
