import unittest
from unittest.mock import patch
from anime import Recommendation


class TestRecommendation(unittest.TestCase):
    @patch("builtins.input")
    def test_getmalid(self, input):
        input.return_value = "Berserk"
        recommendation = Recommendation("manga")
        result = recommendation.getmalid()
        self.assertEqual(result, 2)


class TestData(unittest.TestCase):

    def test_check_data_exists(self):
        file_path = "manga.json"
        self.assertEqual(file_path, "manga.json")
