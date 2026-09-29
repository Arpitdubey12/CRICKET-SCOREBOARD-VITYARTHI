User Input Cricket Scoreboard

Project Overview

User Input Cricket Scoreboard is a Python console-based cricket scoring application for a two-team limited-overs match.

The program allows the user to enter:

Team names

11 players for each team

Number of overs

Ball-by-ball match results

It automatically maintains batting, bowling, extras, score, wickets, overs, run rate, strike rate, and the final match result.

Features

User-defined team names

User-defined 11-player squads

User-defined number of overs

Ball-by-ball scoring

Supports:

0, 1, 2, 3, 4, 6 runs

Wicket (W)

Wide (WD)

Automatic strike rotation for odd runs

Automatic strike change at the end of each over

Batting scorecard

Bowling scorecard

Extras tracking

Strike rate calculation

Bowling economy calculation

Target calculation for the second innings

Automatic winner/tie detection

Input validation for player names, overs, bowlers, and ball results

Technologies Used

Programming Language: Python 3

Concepts: Object-Oriented Programming, Classes, Objects, Functions, Loops, Conditional Statements, Exception Handling, String Formatting

Project Structure

User-Input-Cricket-Scoreboard/
│
├── cricket_scoreboard.py
└── README.md

Main Classes

1. Player

Stores individual batting and bowling statistics.

Important attributes:

name

runs

balls

fours

sixes

out

dismissal

balls_bowled

runs_conceded

wickets

The bowling_overs() method converts legal balls into cricket overs format.

2. Team

Stores team-level information:

Team name

List of players

Total score

Wickets

Legal balls faced

Extras

Important Functions

Function

Purpose

get_players()

Takes 11 player names from the user

get_bowler()

Selects a bowler from the bowling team

get_ball_result()

Validates and returns each ball result

play_innings()

Controls the complete innings

show_scorecard()

Displays batting and bowling statistics

main()

Controls the complete match

How the Program Works

Step 1: Enter Teams

The program asks for the names of Team 1 and Team 2.

Step 2: Enter Players

The user enters 11 players for each team.

Step 3: Enter Overs

The user specifies the number of overs.

Step 4: First Innings

Team 1 bats while Team 2 supplies the bowler.

For every delivery, the user enters one of:

0
1
2
3
4
6
W
WD

A wide adds one run but does not count as a legal delivery.

Step 5: Scorecard

At the end of the first innings, the program displays:

Batter

Dismissal status

Runs

Balls

Fours

Sixes

Strike rate

Extras

Total score

Run rate

Bowling figures

Step 6: Second Innings

Team 2 receives a target equal to:

Team 1 score + 1

The innings ends when the target is reached, all wickets fall, or the allocated overs are completed.

Step 7: Result

The program displays whether:

Team 1 won by runs

Team 2 won by wickets

The match was tied

Example Result

============================================================
                         RESULT
============================================================
Team B won by 6 wickets!
************************************************************

OOP Concepts Demonstrated

This project demonstrates practical use of:

Classes

Objects

Constructors (__init__)

Instance attributes

Instance methods

Object interaction

Encapsulation of player and team data

Input Validation

The program checks:

Empty player names

Invalid number of overs

Invalid bowler selection

Invalid ball results

Non-numeric inputs where numbers are required

Current Limitations

This version intentionally keeps the scoring model simple. It does not currently handle:

No-ball runs

Byes and leg-byes

Run-out of the non-striker

Stumping/caught dismissal types

Free hits

Bowling restrictions

Batting order changes

Toss and innings choice

Player-specific bowling restrictions

Future Scope

Possible improvements include:

Add no-ball, bye, and leg-bye support.

Add dismissal types such as caught, bowled, LBW, run-out, and stumped.

Add toss functionality.

Add automatic bowler-over limits.

Add a graphical user interface.

Save match data to a file or database.

Add match history.

Export scorecards to PDF/CSV.

Add player statistics across multiple matches.

Build a web version of the scoreboard.

How to Run

Install Python 3, save the source code as:

cricket_scoreboard.py

Then run:

python cricket_scoreboard.py

Learning Outcomes

After completing this project, a student can practice:

Python OOP

Functions and modular programming

Input validation

Loops and conditionals

Data management using objects

Basic cricket scoring logic

Formatted console output

Author

Project: User Input Cricket Scoreboard
Language: Python
Type: Console-based Mini Project
