# System Architecture

The project follows a simple modular command-line architecture.

User -> Input Handler -> Match/Innings Logic -> Player/Team Data -> Scoreboard -> Result

Main components:
- Input Handler: validates and collects user input.
- Player/Team: stores match data.
- Innings: processes deliveries and controls match flow.
- Bowling: supports bowling statistics.
- Scoreboard: displays calculated statistics.
- Utils: contains reusable result logic.
- Main: connects the modules.
