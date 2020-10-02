import unittest
from src.anime import Recommendation
from src.main import newrec
from src.main import viewlist


class TestRecommendation(unittest.TestCase):

    def test_jikan(self):
        mal_id = jikan.search("Berserk")

        if result != 32379:
            raise Exception("You did not search Berserk")
