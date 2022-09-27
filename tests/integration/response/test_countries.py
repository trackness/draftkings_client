from unittest import TestCase

from draft_kings.response.countries import Country, Countries
from tests.config import load_fixture


class TestCountries(TestCase):
    def setUp(self) -> None:
        with load_fixture('countries.json') as data_file:
            self.data = Countries.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_countries_data(self) -> None:
        self.assertEqual(
            Countries(
                countries=[
                    Country(
                        country_id=1,
                        country_code="US",
                        name="United States",
                        is_licensed=True
                    ),
                    Country(
                        country_id=14,
                        country_code="AU",
                        name="Australia",
                        is_licensed=True
                    ),
                    Country(
                        country_id=15,
                        country_code="AT",
                        name="Austria",
                        is_licensed=True
                    ),
                    Country(
                        country_id=2,
                        country_code="CA",
                        name="Canada",
                        is_licensed=True
                    ),
                    Country(
                        country_id=4,
                        country_code="DE",
                        name="Germany",
                        is_licensed=True
                    ),
                    Country(
                        country_id=89,
                        country_code="IE",
                        name="Ireland",
                        is_licensed=True
                    ),
                    Country(
                        country_id=117,
                        country_code="MT",
                        name="Malta",
                        is_licensed=True
                    ),
                    Country(
                        country_id=132,
                        country_code="NL",
                        name="Netherlands",
                        is_licensed=True
                    ),
                    Country(
                        country_id=3,
                        country_code="GB",
                        name="United Kingdom",
                        is_licensed=True
                    )
                ]
            ),
            self.data
        )
