def update_bowler_for_runs(bowler, runs):
    """Adds runs conceded to a bowler."""
    bowler.runs_conceded += runs


def update_bowler_for_wicket(bowler):
    """Adds one wicket to a bowler."""
    bowler.wickets += 1


def bowling_summary(bowler):
    return {
        "overs": bowler.bowling_overs(),
        "runs": bowler.runs_conceded,
        "wickets": bowler.wickets,
        "economy": bowler.economy_rate(),
    }
