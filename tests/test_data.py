from unittest import TestCase
from unittest.mock import MagicMock

from draft_kings.data import CountryData


class TestCountryData(TestCase):
    def test_asdict(self):
        self.assertEqual(
            {
                "id": 1,
                "code": "some code",
                "name": "some name",
                "licensed": True
            },
            CountryData(1, "some code", "some name", True).asdict()
        )

    def test_equal_when_same_class_and_same_exact_values(self):
        self.assertEqual(
            CountryData(1, "2", "3", True),
            CountryData(1, "2", "3", True)
        )

    def test_not_equal_when_not_same_class_but_same_values(self):
        self.assertNotEqual(
            CountryData(1, "2", "3", True),
            MagicMock(country_id=1, code="2", name="3", licensed=True)
        )

    def test_not_equal_when_same_class_but_not_same_values(self):
        self.assertNotEqual(
            CountryData(1, "2", "3", True),
            CountryData(2, "2", "3", True)
        )

    def test_not_equal_when_not_same_class_and_not_same_values(self):
        self.assertNotEqual(
            CountryData(1, "2", "3", True),
            MagicMock(country_id=2, code="2", name="3", licensed=True)
        )