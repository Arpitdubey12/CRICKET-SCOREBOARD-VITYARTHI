import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import unittest
from player import Player
from team import Team


class TestTeam(unittest.TestCase):
    def test_team_defaults(self):
        team = Team("Test Team", [Player("A"), Player("B")])
        self.assertEqual(team.score, 0)
        self.assertEqual(team.wickets, 0)

    def test_overs(self):
        team = Team("Test Team", [])
        team.balls = 8
        self.assertEqual(team.overs(), "1.2")


if __name__ == "__main__":
    unittest.main()
