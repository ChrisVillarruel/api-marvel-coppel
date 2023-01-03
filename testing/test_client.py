import unittest

from api_marvel.client import APICharacterSearch


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


unittest.main()
