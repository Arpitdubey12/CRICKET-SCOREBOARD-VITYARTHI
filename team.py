class Team:
    """Stores team-level match information."""

    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0
        self.wickets = 0
        self.balls = 0
        self.extras = 0

    def overs(self):
        return f"{self.balls // 6}.{self.balls % 6}"

    def run_rate(self):
        if self.balls == 0:
            return 0
        return (self.score / self.balls) * 6
