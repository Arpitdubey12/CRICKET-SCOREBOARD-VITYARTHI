from player import Player


def get_players(team_name):
    print(f"\nEnter 11 players of {team_name}:")
    players = []

    for i in range(1, 12):
        while True:
            name = input(f"Player {i}: ").strip()
            if name:
                players.append(Player(name))
                break
            print("Name cannot be empty.")

    return players


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


def get_ball_result():
    valid = {"0", "1", "2", "3", "4", "6", "W", "WD"}

    while True:
        result = input(
            "\nEnter ball result (0, 1, 2, 3, 4, 6, W, WD): "
        ).strip().upper()

        if result in valid:
            return result

        print("Invalid input! Use only: 0, 1, 2, 3, 4, 6, W or WD.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than 0.")
        except ValueError:
            print("Enter a valid number.")
