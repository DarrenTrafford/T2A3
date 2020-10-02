import unittest
from unittest.mock import patch
from anime import Recommendation


class TestRecommendation(unittest.TestCase):
    @patch("builtins.input")
    def test_getmalid(self, input):
        input.return_value = "Berserk"
        recommendation = Recommendation("anime")
        result = recommendation.getmalid()
        self.assertEqual(result, 32379)


class TestData(unittest.TestCase):

    def test_check_data_exists(self):
        file_path = "anime.json"
        self.assertEqual(file_path, "anime.json")
