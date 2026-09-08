## Rock, Paper, Scissors

A command-line Rock, Paper, Scissors game built in Python, played against the computer, with score tracking across rounds.

## Features
Play against the computer using random.choice()
Score tracking across multiple rounds
Input validation — handles lowercase/uppercase input and stray whitespace using .strip().upper()
"Play again?" loop so you can keep playing until you choose to stop
Final score summary when the game ends
How to run
python rock_paper_scissors.py

## Then follow the prompts:

Enter your name
Type rock, paper, or scissors (any casing works)
See the computer's choice and the round's result
Choose to play again (y) or stop (anything else) to see your final score
## What I learned
Using random.choice() to pick randomly from a list, as opposed to random.randint() for numbers
Building an if/elif/else chain to check multiple winning combinations using and/or
A tricky bug: user input containing a leading/trailing space (e.g. " ROCK") doesn't match "ROCK" even though it looks identical when printed — fixed with .strip()
Why an if doesn't always need a matching else — when there's nothing extra to do in the "otherwise" case, the loop just continues naturally

## Tech Stack
Python 3, standard library only (random)

## Possible improvements
Add a "best of X rounds" mode instead of playing indefinitely
Track and display win streaks
