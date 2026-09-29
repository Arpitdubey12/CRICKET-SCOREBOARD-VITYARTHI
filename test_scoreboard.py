import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import unittest
from player import Player
from team import Team
from utils import match_result


class TestScoreboardLogic(unittest.TestCase):
    def test_team_one_wins(self):
        team1 = Team("A", [])
        team2 = Team("B", [])
        team1.score = 100
        team2.score = 90
        self.assertEqual(match_result(team1, team2, 101), "A won by 10 runs!")

    def test_team_two_wins(self):
        team1 = Team("A", [])
        team2 = Team("B", [])
        team2.score = 101
        self.assertEqual(match_result(team1, team2, 101), "B won by 10 wickets!")


if __name__ == "__main__":
    unittest.main()
