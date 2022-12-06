"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

Input:
---
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
---

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

Step 1:
---
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
---
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

Step 2:
---
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
 ---
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

Step 3:
---
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
---

Finally, one crate is moved from stack 1 to stack 2:

Step 4:
---
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
---
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.
"""

import sys

# What are the top crates in each stack after the rearrangement procedure?
# The input is in two sets, separated by a blank line.
# The first set is in the format [x1] [x2] ... [x3] where xi is the label of the crate in stack i. The last line of the first set is a sequence of the label i and can be ignored.
# The second set is in the format move x1 from x2 to x3 where x1 is the label of the crate to move, x2 is the stack to move it from, and x3 is the stack to move it to.
def part1(lines):
    stacks = {}
    col_count = len(lines[0]) // 4
    for i in range(col_count):
        stacks[i+1] = []
    for line in lines:
        if line.strip() == "":
            continue
        if line.split()[0][0] == '[':
            for i in range(col_count):
                crate_in_stack = line[i*4:i*4+3]
                if crate_in_stack[0] != '[':
                    continue
                stacks[i+1].append(crate_in_stack)
        elif line.split()[0] == 'move':
            crate_count = int(line.split()[1])
            from_stack = int(line.split()[3])
            to_stack = int(line.split()[5])
            for i in range(crate_count):
                # move from start of from_stack to start of to_stack
                stacks[to_stack].insert(0, stacks[from_stack].pop(0))
    # return the first entry from each stack
    return "".join([stacks[i][0][1] for i in range(1, col_count+1)])

"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

Input:
---
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3
---
Moving a single crate from stack 2 to stack 1 behaves the same as before:

Step 2:
---
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
---
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

Step 3:
---
        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
---
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

Step 4:
---
        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
---
 
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

Step 5:
---
        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
---
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.
"""

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
def part2(lines):
    stacks = {}
    col_count = len(lines[0]) // 4
    for i in range(col_count):
        stacks[i+1] = []
    for line in lines:
        if line.strip() == "":
            continue
        if line.split()[0][0] == '[':
            for i in range(col_count):
                crate_in_stack = line[i*4:i*4+3]
                if crate_in_stack[0] != '[':
                    continue
                stacks[i+1].append(crate_in_stack)
        elif line.split()[0] == 'move':
            crate_count = int(line.split()[1])
            from_stack = int(line.split()[3])
            to_stack = int(line.split()[5])
            # move the first crate_count entries from from_stack to the beginning of to_stack
            stacks[to_stack] = stacks[from_stack][:crate_count] + stacks[to_stack]
            stacks[from_stack] = stacks[from_stack][crate_count:]
    # return the first entry from each stack
    return "".join([stacks[i][0][1] for i in range(1, col_count+1)])

if __name__ == '__main__':
    # Read in the input
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print(part2(lines))
