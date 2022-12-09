"""
--- Day 9: Rope Bridge ---

This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):
---
....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...
---
If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
---
.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -> ... -> .T.
...    .H.    .H.
...    ...    ...
---
Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
---
.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -> ...H. -> ..TH.
.T...    .T...    .....
.....    .....    .....
---
You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.

For example:
---
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
---
This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):
---
== Initial State ==

......
......
......
......
H.....  (H covers T, s)

== R 4 ==

......
......
......
......
TH....  (T covers s)

......
......
......
......
sTH...

......
......
......
......
s.TH..

......
......
......
......
s..TH.

== U 4 ==

......
......
......
....H.
s..T..

......
......
....H.
....T.
s.....

......
....H.
....T.
......
s.....

....H.
....T.
......
......
s.....

== L 3 ==

...H..
....T.
......
......
s.....

..HT..
......
......
......
s.....

.HT...
......
......
......
s.....

== D 1 ==

..T...
.H....
......
......
s.....

== R 4 ==

..T...
..H...
......
......
s.....

..T...
...H..
......
......
s.....

......
...TH.
......
......
s.....

......
....TH
......
......
s.....

== D 1 ==

......
....T.
.....H
......
s.....

== L 5 ==

......
....T.
....H.
......
s.....

......
....T.
...H..
......
s.....

......
......
..HT..
......
s.....

......
......
.HT...
......
s.....

......
......
HT....
......
s.....

== R 2 ==

......
......
.H....  (H covers T)
......
s.....

......
......
.TH...
......
s.....
---
After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:
---
..##..
...##.
.####.
....#.
s###..
---
So, there are 13 positions the tail visited at least once.

1. How many positions does the tail visit at least once?
"""

import sys

def part1(moves):
    # Simulate rope
    # Use input moves to move the head of the rope
    # Keep the tail of the rope within 1 square of the head (in any direction, or overlapping)
    # Track all of the positions that the tail visits
    # Return the number of positions that the tail visits at least once

    # Start at origin
    head = (0, 0)
    tail = (0, 0)
    visited = set()
    visited.add(tail)

    for move in moves:
        direction = move[0]
        distance = int(move[1:])
        for _ in range(distance):
            # Move head
            if direction == 'R':
                head = (head[0] + 1, head[1])
            elif direction == 'L':
                head = (head[0] - 1, head[1])
            elif direction == 'U':
                head = (head[0], head[1] + 1)
            elif direction == 'D':
                head = (head[0], head[1] - 1)

            # If tail is more than 1 position away from head, move tail closer
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                # Move tail
                if head[0] == tail[0] and head[1] == tail[1]:
                    # Head and tail are in same position
                    continue
                elif head[0] == tail[0]:
                    # Head and tail are in same column
                    if head[1] > tail[1]:
                        tail = (tail[0], tail[1] + 1)
                    else:
                        tail = (tail[0], tail[1] - 1)
                elif head[1] == tail[1]:
                    # Head and tail are in same row
                    if head[0] > tail[0]:
                        tail = (tail[0] + 1, tail[1])
                    else:
                        tail = (tail[0] - 1, tail[1])
                else:
                    # Head and tail are in different rows and columns
                    # move the tail 1 step diagonally towards the head
                    if head[0] > tail[0]:
                        tail = (tail[0] + 1, tail[1])
                    else:
                        tail = (tail[0] - 1, tail[1])
                    if head[1] > tail[1]:
                        tail = (tail[0], tail[1] + 1)
                    else:
                        tail = (tail[0], tail[1] - 1)

            visited.add(tail)

    return len(visited)

"""
--- Part Two ---

A rope snaps! Suddenly, the river is getting a lot closer than you remember. The bridge is still there, but some of the ropes that broke are now whipping toward you as you fall through the air!

The ropes are moving too quickly to grab; you only have a few seconds to choose how to arch your body to avoid being hit. Fortunately, your simulation can be extended to support longer ropes.

Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope and moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same rules as before.

Using the same series of motions as the above example, but with the knots marked Head, 1, 2, 3, ... etc, tail. Each knot is 1 unit away from the previous knot.

2. Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
"""

def part2(moves):
    # Simulate rope
    # Use input moves to move the head of the rope
    # Keep the tail of the rope within 1 square of the head (in any direction, or overlapping)
    # Track all of the positions that the tail visits
    # Return the number of positions that the tail visits at least once

    # Start at origin
    rope = [(0, 0) for _ in range(10)]
    visited = set()
    visited.add(rope[0])

    for move in moves:
        direction = move[0]
        distance = int(move[1:])
        for _ in range(distance):
            
            # Move head
            if direction == 'R':
                rope[0] = (rope[0][0] + 1, rope[0][1])
            elif direction == 'L':
                rope[0] = (rope[0][0] - 1, rope[0][1])
            elif direction == 'U':
                rope[0] = (rope[0][0], rope[0][1] + 1)
            elif direction == 'D':
                rope[0] = (rope[0][0], rope[0][1] - 1)

            # Move rest of rope
            for i in range(1, len(rope)):
                if abs(rope[i][0] - rope[i-1][0]) > 1 or abs(rope[i][1] - rope[i-1][1]) > 1:
                    # Move knot
                    if rope[i][0] == rope[i-1][0] and rope[i][1] == rope[i-1][1]:
                        # Knot and previous knot are in same position
                        continue
                    elif rope[i][0] == rope[i-1][0]:
                        # Knot and previous knot are in same column
                        if rope[i][1] > rope[i-1][1]:
                            rope[i] = (rope[i][0], rope[i][1] - 1)
                        else:
                            rope[i] = (rope[i][0], rope[i][1] + 1)
                    elif rope[i][1] == rope[i-1][1]:
                        # Knot and previous knot are in same row
                        if rope[i][0] > rope[i-1][0]:
                            rope[i] = (rope[i][0] - 1, rope[i][1])
                        else:
                            rope[i] = (rope[i][0] + 1, rope[i][1])
                    else:
                        # Knot and previous knot are in different rows and columns
                        # move the knot 1 step diagonally towards the previous knot
                        if rope[i][0] > rope[i-1][0]:
                            rope[i] = (rope[i][0] - 1, rope[i][1])
                        else:
                            rope[i] = (rope[i][0] + 1, rope[i][1])
                        if rope[i][1] > rope[i-1][1]:
                            rope[i] = (rope[i][0], rope[i][1] - 1)
                        else:
                            rope[i] = (rope[i][0], rope[i][1] + 1)

            # track the position of the last knot
            visited.add(rope[-1])
    
    return len(visited)
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 %s <input>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # Parse input
    moves = []
    for line in lines:
        moves.append(line.strip())

    # print(part1(moves))
    print(part2(moves))