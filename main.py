from team import Team
from input_handler import get_players, get_positive_integer
from innings import play_innings
from scoreboard import show_scorecard
from utils import match_result


def main():
    print("=" * 60)
    print("        USER INPUT CRICKET SCOREBOARD")
    print("=" * 60)

    team1_name = input("\nEnter Team 1 name: ").strip()
    team2_name = input("Enter Team 2 name: ").strip()

    team1 = Team(team1_name, get_players(team1_name))
    team2 = Team(team2_name, get_players(team2_name))

    overs = get_positive_integer("\nEnter number of overs: ")

    print("\nFIRST INNINGS")
    play_innings(team1, team2, overs)
    show_scorecard(team1, team2)

    target = team1.score + 1

    print("\nSECOND INNINGS")
    print(f"{team2.name} needs {target} runs to win.")
    play_innings(team2, team1, overs, target)
    show_scorecard(team2, team1)

    print("\n" + "*" * 60)
    print("RESULT")
    print("*" * 60)
    print(match_result(team1, team2, target))
    print("*" * 60)


if __name__ == "__main__":
    main()
