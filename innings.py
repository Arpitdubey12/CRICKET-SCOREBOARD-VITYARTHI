from input_handler import get_bowler, get_ball_result


def play_innings(batting_team, bowling_team, overs, target=None):
    """Runs one innings using ball-by-ball user input."""

    print("\n" + "=" * 60)
    print(f"{batting_team.name.upper()} INNINGS")
    print("=" * 60)

    striker = batting_team.players[0]
    non_striker = batting_team.players[1]
    next_batter = 2

    for over in range(overs):
        if batting_team.wickets == 10:
            break
        if target is not None and batting_team.score >= target:
            break

        print("\n" + "-" * 60)
        print(f"OVER {over + 1}")
        print(f"Striker: {striker.name}")
        print(f"Non-Striker: {non_striker.name}")

        bowler = get_bowler(bowling_team)
        legal_balls = 0

        while legal_balls < 6:
            if batting_team.wickets == 10:
                break
            if target is not None and batting_team.score >= target:
                break

            print(f"\nScore: {batting_team.score}/{batting_team.wickets}")
            print(f"Ball: {legal_balls + 1}/6")
            print(f"Bowler: {bowler.name}")

            result = get_ball_result()

            if result == "WD":
                batting_team.score += 1
                batting_team.extras += 1
                bowler.runs_conceded += 1
                print("Wide! +1 run")
                continue

            legal_balls += 1
            batting_team.balls += 1
            bowler.balls_bowled += 1
            striker.balls += 1

            if result == "W":
                batting_team.wickets += 1
                bowler.wickets += 1
                striker.out = True
                striker.dismissal = f"b {bowler.name}"
                print(f"WICKET! {striker.name} is OUT!")

                if next_batter < 11:
                    striker = batting_team.players[next_batter]
                    next_batter += 1
                    print(f"New batter: {striker.name}")
                else:
                    print("All out!")
                continue

            runs = int(result)
            batting_team.score += runs
            striker.runs += runs
            bowler.runs_conceded += runs

            if runs == 4:
                striker.fours += 1
                print("FOUR!")
            elif runs == 6:
                striker.sixes += 1
                print("SIX!")
            else:
                print(f"{runs} run(s)")

            if runs % 2 == 1:
                striker, non_striker = non_striker, striker

        striker, non_striker = non_striker, striker

        print(
            f"\nEnd of over {over + 1}: "
            f"{batting_team.score}/{batting_team.wickets}"
        )

    print("\nInnings finished!")
