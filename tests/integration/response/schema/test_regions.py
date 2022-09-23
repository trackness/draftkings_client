from unittest import TestCase

from draft_kings.response.objects.regions import Region, Regions
from tests.config import load_fixture


class TestUSRegions(TestCase):
    def setUp(self) -> None:
        with load_fixture('regions/us.json') as data_file:
            self.data = Regions.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_regions_length(self):
        self.assertEqual(62, len(self.data.regions))

    def test_first_region(self):
        self.assertEqual(
            Region(
                country_code="US",
                region_code="AL",
                iso_region_code="US-AL",
                name="Alabama"
            ),
            self.data.regions[0]
        )


class TestCanadianRegions(TestCase):
    def setUp(self) -> None:
        with load_fixture('regions/ca.json') as data_file:
            self.data = Regions.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_regions_length(self):
        self.assertEqual(13, len(self.data.regions))

    def test_first_region(self):
        self.assertEqual(
            Region(
                country_code="CA",
                region_code="AB",
                iso_region_code="CA-AB",
                name="Alberta"
            ),
            self.data.regions[0]
        )


class TestGBRegions(TestCase):
    def setUp(self) -> None:
        with load_fixture('regions/gb.json') as data_file:
            self.data = Regions.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_regions_length(self):
        self.assertEqual(225, len(self.data.regions))

    def test_first_region(self):
        self.assertEqual(
            Region(
                country_code="GB",
                region_code="ABE",
                iso_region_code="GB-ABE",
                name="Aberdeen City"
            ),
            self.data.regions[0]
        )
