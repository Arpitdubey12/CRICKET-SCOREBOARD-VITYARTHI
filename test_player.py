import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def test_player_defaults(self):
        player = Player("Test Player")
        self.assertEqual(player.runs, 0)
        self.assertEqual(player.balls, 0)
        self.assertFalse(player.out)

    def test_strike_rate(self):
        player = Player("Test Player")
        player.runs = 50
        player.balls = 25
        self.assertEqual(player.strike_rate(), 200)


if __name__ == "__main__":
    unittest.main()
