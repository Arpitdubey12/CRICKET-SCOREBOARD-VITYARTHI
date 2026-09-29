# Class Diagram Description

## Player
Attributes:
- name
- runs
- balls
- fours
- sixes
- out
- dismissal
- balls_bowled
- runs_conceded
- wickets

Methods:
- strike_rate()
- bowling_overs()
- economy_rate()

## Team
Attributes:
- name
- players
- score
- wickets
- balls
- extras

Methods:
- overs()
- run_rate()

Other modules:
- innings.py: match-flow logic
- scoreboard.py: scorecard display
- input_handler.py: input and validation
- bowling.py: bowling helpers
- utils.py: result calculation
