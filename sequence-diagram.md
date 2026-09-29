# Sequence Diagram Description

User -> Main: Start application
Main -> Input Handler: Request team/player information
Input Handler -> Main: Return validated information
Main -> Innings: Start innings
Innings -> Input Handler: Request bowler and ball result
Input Handler -> Innings: Return result
Innings -> Player/Team: Update statistics
Innings -> Scoreboard: Send completed innings data
Scoreboard -> User: Display scorecard
Main -> Utils: Calculate match result
Utils -> User: Display final result
