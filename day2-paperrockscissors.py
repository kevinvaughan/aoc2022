"""
Scoring the game of Paper Rock Scissors
Given a list of this format, where each row represents 1 round of play:
---
A Y
B X
C Z
---
And the following rules of gameplay:
1) Play choices: A and X both represent ROCK, B and Y both represent PAPER, and C and Z both represent SCISSORS
2) Round Outcome: ROCK beats SCISSORS, PAPER beats ROCK, and SCISSORS beats PAPER
3) Play choice points: Playing X earns 1 point, Y earns 2 points, and Z earns 3 points
4) Outcome points: Winning earns 6 points, draws earn 3 points, and a loss earns 0 points
5) Score for the round = Points for play + Points 

For example:
---
A Y = (2 points for playing Y, 6 points for winning = round score of 8)
B X = (1 point for playing X, 0 points for losing = round score of 1)
C Z = (3 points for playing Z, 3 points for a draw = round score 6)
----
"""

# Take in a list of pairs [opponent play, your play] and return the total score earned
def total_score(list):
    score = 0
    
    for i in range(len(list)): # Iterate through the list of pairs, one pair at a time
        play = list[i][0]
        choice = list[i][2]
        if choice == 'Y':
            if play == 'A': choice = 'X'
            if play == 'B': choice = 'Y'
            if play == 'C': choice = 'Z'
        elif choice == 'X':
            if play == 'A': choice = 'Z'
            if play == 'B': choice = 'X'
            if play == 'C': choice = 'Y'
        elif choice == 'Z':
            if play == 'A': choice = 'Y'
            if play == 'B': choice = 'Z'
            if play == 'C': choice = 'X'
        play = play + choice

        # is play one of 'AY', 'BZ', or 'CX'
        if play == 'AY' or play == 'BZ' or play == 'CX':
            score += 6
        elif play == "AX" or play == "BY" or play == "CZ": 
            score += 3
        
        if (choice == 'X'): score += 1
        if (choice == 'Y'): score += 2
        if (choice == 'Z'): score += 3
    return score

with open("day2-input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
print(total_score(content))

