# Knowledge Representation - Poject 2 Argumentation

# Pre-requisites 
- Python 3.8 or higher 

## Overview

This tool facilitates a preferred discussion game between a user and the computer, based on a loaded argumentation framework stored in a example JSON file. The game involves a proponent (computer) defending a specific argument against an opponent (user) attempting to attack it. The goal of the proponent is to demonstrate the existence of a preferred extension that contains the claimed argument.

## Getting Started

To initiate the game, provide the tool with the following parameters:

- **JSON file name:** Specify the name of the JSON file containing the argumentation framework.
- **Claimed argument:** Input a string denoting the specific argument the proponent will defend.

## Rules of the Game

1. **Proponent's Turn:**
   - The proponent starts by presenting the claimed argument.
   - The opponent selects an argument to attack from the proponent's previous statements.

2. **Opponent's Turn:**
   - The opponent can only choose arguments that attack a previous argument presented by the proponent.
   - The attacked arguments can be from the current or earlier rounds.

3. **Proponent's Response:**
   - The proponent must respond with an argument that attacks the opponent's selected argument from the preceding round.

4. **Repetition Rules:**
   - The opponent cannot use the same argument twice.
   - The proponent can reuse arguments.

## Game End Conditions

The game concludes with the determination of a winner based on the following conditions:

1. If the opponent uses an argument previously used by the proponent, the opponent wins (indicating a contradiction).
2. If the proponent uses an argument previously used by the opponent, the opponent wins (highlighting a contradiction).
3. If the proponent cannot make a move, the opponent wins.
4. If the opponent exhausts all choices, the proponent wins.

## Example Usage

```bash
python assingment_2.py
```