def show_scorecard(team, bowling_team):
    """Prints batting and bowling scorecards."""

    print("\n" + "=" * 75)
    print(f"{team.name.upper()} SCORECARD")
    print("=" * 75)

    print(
        f"{'Batter':<20}{'Status':<25}"
        f"{'R':>5}{'B':>5}{'4s':>5}{'6s':>5}{'SR':>8}"
    )
    print("-" * 75)

    for player in team.players:
        if player.balls > 0 or player.out:
            print(
                f"{player.name:<20}{player.dismissal:<25}"
                f"{player.runs:>5}{player.balls:>5}"
                f"{player.fours:>5}{player.sixes:>5}"
                f"{player.strike_rate():>8.1f}"
            )

    print("-" * 75)
    print(f"Extras: {team.extras}")
    print(f"TOTAL: {team.score}/{team.wickets} ({team.overs()} overs)")
    print(f"Run Rate: {team.run_rate():.2f}")

    print("\nBOWLING - " + bowling_team.name)
    print("-" * 75)
    print(f"{'Bowler':<20}{'O':>8}{'R':>8}{'W':>8}{'Econ':>10}")
    print("-" * 75)

    for player in bowling_team.players:
        if player.balls_bowled > 0:
            print(
                f"{player.name:<20}{player.bowling_overs():>8}"
                f"{player.runs_conceded:>8}{player.wickets:>8}"
                f"{player.economy_rate():>10.2f}"
            )
