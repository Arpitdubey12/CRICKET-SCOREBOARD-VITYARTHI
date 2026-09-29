# Project Statement

## Project Title

**User Input Cricket Scoreboard**

## Problem Statement

Keeping a cricket score manually involves repeatedly tracking runs, wickets, balls, overs, player statistics and the current match situation. When these values are maintained manually, calculation mistakes can occur.

The User Input Cricket Scoreboard provides a simple Python-based solution. It accepts team and player information and then processes ball-by-ball match input to maintain the score and generate a basic cricket scorecard.

## Scope of the Project

The project covers:

- Creation of two cricket teams
- Entry of 11 players for each team
- Selection of match overs
- Ball-by-ball scoring
- Wicket recording
- Wide-ball handling
- Strike rotation
- Batter statistics
- Bowler statistics
- Batting and bowling scorecards
- Second-innings target calculation
- Final match-result calculation
- Basic input validation

The project is currently designed as a command-line application and does not depend on an external database.

## Target Users

The intended users are:

- Students learning Python
- Beginners learning object-oriented programming
- Students interested in applying programming to a sports-related problem
- Users who want to simulate a simple cricket match

## High-Level Features

### Team and Player Management
The system creates two teams and stores 11 players for each team.

### Ball-by-Ball Scoring
The user enters the result of each delivery. The system updates runs, wickets, legal balls, wides and player statistics.

### Batting Statistics
The system records runs, balls faced, fours, sixes and calculates strike rate.

### Bowling Statistics
The system records legal deliveries, runs conceded and wickets, then calculates overs and economy rate.

### Scorecard
At the end of each innings, the application displays a batting and bowling scorecard.

### Match Result
The second innings receives the required target, and the application determines whether the chasing team wins, the first team wins, or the match is tied.

## Project Objective

The objective is to build a small but complete real-world application using Python programming concepts, while keeping the implementation understandable and modular.
