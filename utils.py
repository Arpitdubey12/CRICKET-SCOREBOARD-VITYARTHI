def match_result(team1, team2, target):
    """Returns a human-readable result for the completed match."""

    if team2.score >= target:
        wickets_left = 10 - team2.wickets
        return f"{team2.name} won by {wickets_left} wickets!"

    if team1.score > team2.score:
        runs = team1.score - team2.score
        return f"{team1.name} won by {runs} runs!"

    return "MATCH TIED!"
