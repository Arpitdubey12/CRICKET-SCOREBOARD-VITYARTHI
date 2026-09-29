# User Input Cricket Scoreboard

## Project Overview

User Input Cricket Scoreboard is a Python command-line project that simulates a basic cricket match using user-entered team, player, and ball-by-ball information.

The project was designed as a practical application of Python programming concepts. Instead of storing only a final score, the system keeps track of individual player statistics, team totals, wickets, legal deliveries, wides, batting strike rates, bowling economy rates, and the match result.

## Problem It Solves

Manual scorekeeping requires the scorer to continuously calculate runs, wickets, overs, strike rotation, and player statistics. Small calculation mistakes can affect the final scorecard.

This project automates those calculations through a simple text-based interface.

## Main Features

- Create two teams with 11 players each
- Set the number of overs
- Enter ball-by-ball results
- Handle runs from 0 to 6
- Handle wickets
- Handle wide balls
- Track striker and non-striker
- Track batter runs, balls, fours and sixes
- Calculate batting strike rate
- Track bowler overs, runs and wickets
- Calculate bowling economy
- Generate batting and bowling scorecards
- Calculate the target for the second innings
- Display the final match result
- Validate user input

## Functional Modules

### 1. Team and Player Management
Creates teams and stores player-level statistics.

### 2. Match and Innings Management
Controls innings, overs, deliveries, wickets, runs, wides and strike rotation.

### 3. Scorecard and Result
Calculates and displays batting/bowling statistics and the final result.

## Non-Functional Requirements

- **Usability:** Prompts are kept simple so a beginner can follow the match flow.
- **Reliability:** Score, wicket and ball counters are updated consistently for each accepted delivery.
- **Error Handling:** Invalid player names, numbers and ball results are rejected and requested again.
- **Maintainability:** Classes and match functions are separated into meaningful Python modules.
- **Resource Efficiency:** The application uses in-memory data and has no unnecessary external dependencies.

## Technologies

- Python 3
- Object-Oriented Programming
- Command Line Interface
- Git
- GitHub
- Python unittest

## Repository Structure

```text
cricket-scoreboard/
├── README.md
├── statement.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── player.py
│   ├── team.py
│   ├── innings.py
│   ├── scoreboard.py
│   ├── bowling.py
│   ├── input_handler.py
│   └── utils.py
├── tests/
│   ├── test_player.py
│   ├── test_team.py
│   └── test_scoreboard.py
├── docs/
└── screenshots/
```

## Installation and Run

1. Install Python 3.x.
2. Clone this repository.
3. Open the project folder in a terminal.
4. Run:

```bash
python src/main.py
```

No external Python package is required for the core application.

## Testing

The project contains unit tests for basic player, team and result-calculation logic.

Run:

```bash
python -m unittest discover tests
```

## Input Format

Accepted ball results:

```text
0, 1, 2, 3, 4, 6, W, WD
```

- `W` = wicket
- `WD` = wide

## Documentation

The `docs` folder contains the project's architecture, workflow and UML-related documentation. The final project report contains the detailed design diagrams, implementation explanation, testing approach, challenges, learnings and future enhancements.

## Future Enhancements

- GUI version
- Match history
- Database storage
- Player statistics across multiple matches
- Tournament mode
- Additional cricket formats
- Save/load match functionality

## Academic Purpose

This project is intended as a student-built application for demonstrating programming, modular design, input validation, data processing, testing and version-control practices.
