class Player:
    """Stores batting and bowling statistics for one player."""

    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls = 0
        self.fours = 0
        self.sixes = 0
        self.out = False
        self.dismissal = "Not Out"

        self.balls_bowled = 0
        self.runs_conceded = 0
        self.wickets = 0

    def strike_rate(self):
        if self.balls == 0:
            return 0
        return (self.runs / self.balls) * 100

    def bowling_overs(self):
        return f"{self.balls_bowled // 6}.{self.balls_bowled % 6}"

    def economy_rate(self):
        if self.balls_bowled == 0:
            return 0
        return (self.runs_conceded / self.balls_bowled) * 6
