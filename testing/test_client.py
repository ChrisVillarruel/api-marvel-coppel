import unittest

from api_marvel.client import APICharacterSearch, APIComicsSearch


class TestCaseAPICharacterSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.api_character_search = APICharacterSearch

    def test_api_character_search(self):
        test: APICharacterSearch = self.api_character_search(
            nameStartsWith="wol",
        )

        self.assertEqual(test.name_starts_with, "wol")
        self.assertIsInstance(test.name_starts_with, str)
        self.assertEqual(test.name, "None")
        self.assertIsInstance(test.query_params, dict)
        self.assertEqual(test.query_params.get("name"), None)
        self.assertNotEqual(test.query_params.get("nameStartsWith"), None)
        self.assertIsInstance(test.response, list)


class TestCaseAPIComicsSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.api_comics_search = APIComicsSearch

    def test_api_character_search(self):
        test: APIComicsSearch = self.api_comics_search(
            title="Avengers",
        )

        self.assertEqual(test.title_starts_with, "None")
        self.assertIsInstance(test.title_starts_with, str)
        self.assertEqual(test.title, "Avengers")
        self.assertIsInstance(test.query_params, dict)
        self.assertEqual(test.query_params.get("title"), 'Avengers')
        self.assertEqual(test.query_params.get("titleStartsWith"), None)
        self.assertIsInstance(test.response, list)
        self.assertIsInstance(test.response[0], dict)


unittest.main()
