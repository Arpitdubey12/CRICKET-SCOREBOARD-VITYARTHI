"""User Input Cricket Scoreboard"""

# ---------- PLAYER CLASS ----------

class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls = 0
        self.fours = 0
        self.sixes = 0
        self.out = False
        self.dismissal = "Not Out"

        # Bowling statistics
        self.balls_bowled = 0
        self.runs_conceded = 0
        self.wickets = 0

    def bowling_overs(self):
        return f"{self.balls_bowled // 6}.{self.balls_bowled % 6}"


# ---------- TEAM CLASS ----------

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0
        self.wickets = 0
        self.balls = 0
        self.extras = 0


# ---------- GET PLAYERS ----------

def get_players(team_name):
    print(f"\nEnter 11 players of {team_name}:")

    players = []

    for i in range(1, 12):
        while True:
            name = input(f"Player {i}: ").strip()

            if name:
                players.append(Player(name))
                break
            else:
                print("Name cannot be empty.")

    return players


# ---------- GET BOWLER ----------

def get_bowler(team):
    print("\nAvailable bowlers:")

    for i, player in enumerate(team.players, 1):
        print(f"{i}. {player.name}")

    while True:
        try:
            choice = int(input("Choose bowler number: "))

            if 1 <= choice <= 11:
                return team.players[choice - 1]

            print("Please enter a number from 1 to 11.")

        except ValueError:
            print("Please enter a valid number.")


# ---------- GET BALL RESULT ----------

def get_ball_result():

    while True:
        result = input(
            "\nEnter ball result "
            "(0, 1, 2, 3, 4, 6, W, WD): "
        ).strip().upper()

        if result in ["0", "1", "2", "3", "4", "6", "W", "WD"]:
            return result

        print("Invalid input!")
        print("Use only: 0, 1, 2, 3, 4, 6, W or WD")


# ---------- PLAY INNINGS ----------

def play_innings(batting_team, bowling_team, overs, target=None):

    print("\n" + "=" * 60)
    print(f"{batting_team.name.upper()} INNINGS")
    print("=" * 60)

    striker = batting_team.players[0]
    non_striker = batting_team.players[1]

    next_batter = 2

    striker_out = False

    for over in range(overs):

        if batting_team.wickets == 10:
            break

        if target and batting_team.score >= target:
            break

        print("\n" + "-" * 60)
        print(f"OVER {over + 1}")
        print(f"Striker     : {striker.name}")
        print(f"Non-Striker : {non_striker.name}")

        bowler = get_bowler(bowling_team)

        legal_balls = 0

        while legal_balls < 6:

            if batting_team.wickets == 10:
                break

            if target and batting_team.score >= target:
                break

            print(
                f"\nScore: {batting_team.score}/"
                f"{batting_team.wickets}"
            )

            print(
                f"Ball: {legal_balls + 1}/6"
            )

            print(f"Bowler: {bowler.name}")

            result = get_ball_result()

            # ---------- WIDE ----------

            if result == "WD":

                batting_team.score += 1
                batting_team.extras += 1

                bowler.runs_conceded += 1

                print("Wide! +1 run")

                continue

            # ---------- LEGAL BALL ----------

            legal_balls += 1
            batting_team.balls += 1

            bowler.balls_bowled += 1
            striker.balls += 1

            # ---------- WICKET ----------

            if result == "W":

                batting_team.wickets += 1
                bowler.wickets += 1

                striker.out = True
                striker.dismissal = f"b {bowler.name}"

                print(
                    f"WICKET! {striker.name} is OUT!"
                )

                # New batter
                if next_batter < 11:

                    striker = batting_team.players[next_batter]

                    striker.out = False
                    striker.dismissal = "Not Out"

                    print(
                        f"New batter: {striker.name}"
                    )

                    next_batter += 1

                else:
                    print("All out!")

                continue

            # ---------- RUNS ----------

            runs = int(result)

            batting_team.score += runs
            striker.runs += runs
            bowler.runs_conceded += runs

            # Fours and sixes
            if runs == 4:
                striker.fours += 1
                print("FOUR!")

            elif runs == 6:
                striker.sixes += 1
                print("SIX!")

            else:
                print(f"{runs} run(s)")

            # Change strike for odd runs
            if runs % 2 == 1:
                striker, non_striker = non_striker, striker

        # End of over -> change strike
        striker, non_striker = non_striker, striker

        print(
            f"\nEnd of over {over + 1}: "
            f"{batting_team.score}/{batting_team.wickets}"
        )

    print("\nInnings finished!")


# ---------- SHOW SCORECARD ----------

def show_scorecard(team, bowling_team):

    print("\n")
    print("=" * 75)
    print(f"{team.name.upper()} SCORECARD")
    print("=" * 75)

    print(
        f"{'Batter':<20}"
        f"{'Status':<25}"
        f"{'R':>5}"
        f"{'B':>5}"
        f"{'4s':>5}"
        f"{'6s':>5}"
        f"{'SR':>8}"
    )

    print("-" * 75)

    for player in team.players:

        # Show players who batted
        if player.balls > 0 or player.out:

            if player.balls > 0:
                strike_rate = (
                    player.runs / player.balls * 100
                )
            else:
                strike_rate = 0

            print(
                f"{player.name:<20}"
                f"{player.dismissal:<25}"
                f"{player.runs:>5}"
                f"{player.balls:>5}"
                f"{player.fours:>5}"
                f"{player.sixes:>5}"
                f"{strike_rate:>8.1f}"
            )

    print("-" * 75)

    print(f"Extras: {team.extras}")

    overs = f"{team.balls // 6}.{team.balls % 6}"

    run_rate = (
        team.score / team.balls * 6
        if team.balls > 0
        else 0
    )

    print(
        f"TOTAL: {team.score}/{team.wickets} "
        f"({overs} overs)"
    )

    print(f"Run Rate: {run_rate:.2f}")

    # ---------- BOWLING SCORECARD ----------

    print("\n")
    print(f"BOWLING - {bowling_team.name}")

    print("-" * 75)

    print(
        f"{'Bowler':<20}"
        f"{'O':>8}"
        f"{'R':>8}"
        f"{'W':>8}"
        f"{'Econ':>10}"
    )

    print("-" * 75)

    for player in bowling_team.players:

        if player.balls_bowled > 0:

            economy = (
                player.runs_conceded /
                player.balls_bowled * 6
            )

            print(
                f"{player.name:<20}"
                f"{player.bowling_overs():>8}"
                f"{player.runs_conceded:>8}"
                f"{player.wickets:>8}"
                f"{economy:>10.2f}"
            )


# ---------- MAIN PROGRAM ----------

def main():

    print("=" * 60)
    print("        USER INPUT CRICKET SCOREBOARD")
    print("=" * 60)

    # Team names
    team1_name = input("\nEnter Team 1 name: ").strip()
    team2_name = input("Enter Team 2 name: ").strip()

    # Players
    team1_players = get_players(team1_name)
    team2_players = get_players(team2_name)

    team1 = Team(team1_name, team1_players)
    team2 = Team(team2_name, team2_players)

    # Overs
    while True:
        try:
            overs = int(input("\nEnter number of overs: "))

            if overs > 0:
                break

            print("Overs must be greater than 0.")

        except ValueError:
            print("Enter a valid number.")

    # ---------- FIRST INNINGS ----------

    print("\n")
    print("=" * 60)
    print("FIRST INNINGS")
    print("=" * 60)

    play_innings(
        team1,
        team2,
        overs
    )

    show_scorecard(team1, team2)

    # ---------- SECOND INNINGS ----------

    target = team1.score + 1

    print("\n")
    print("=" * 60)
    print("SECOND INNINGS")
    print("=" * 60)

    print(
        f"{team2.name} needs "
        f"{target} runs to win."
    )

    play_innings(
        team2,
        team1,
        overs,
        target
    )

    show_scorecard(team2, team1)

    # ---------- RESULT ----------

    print("\n")
    print("*" * 60)
    print("                    RESULT")
    print("*" * 60)

    if team2.score >= target:

        wickets_left = 10 - team2.wickets

        print(
            f"{team2.name} won by "
            f"{wickets_left} wickets!"
        )

    elif team1.score > team2.score:

        runs = team1.score - team2.score

        print(
            f"{team1.name} won by "
            f"{runs} runs!"
        )

    else:

        print("MATCH TIED!")

    print("*" * 60)


# ---------- START PROGRAM ----------

if __name__ == "__main__":
    main()
    
