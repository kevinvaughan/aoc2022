"""
--- Day 11: Monkey in the Middle ---
To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation, you realize the monkeys operate based on how worried you are about each item.

You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items, and how the monkey makes decisions based on your worry level.

For example:
---
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
---

Each monkey has several attributes:

Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
Test shows how the monkey uses your worry level to decide where to throw an item next.
If true shows what happens with an item if the Test was true.
If false shows what happens with an item if the Test was false.
After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a round.

When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.

In the above example, the first round proceeds as follows:
---
Monkey 0:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 98.
    Worry level is multiplied by 19 to 1862.
    Monkey gets bored with item. Worry level is divided by 3 to 620.
    Current worry level is not divisible by 23.
    Item with worry level 620 is thrown to monkey 3.
Monkey 1:
  Monkey inspects an item with a worry level of 54.
    Worry level increases by 6 to 60.
    Monkey gets bored with item. Worry level is divided by 3 to 20.
    Current worry level is not divisible by 19.
    Item with worry level 20 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 65.
    Worry level increases by 6 to 71.
    Monkey gets bored with item. Worry level is divided by 3 to 23.
    Current worry level is not divisible by 19.
    Item with worry level 23 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 75.
    Worry level increases by 6 to 81.
    Monkey gets bored with item. Worry level is divided by 3 to 27.
    Current worry level is not divisible by 19.
    Item with worry level 27 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 6 to 80.
    Monkey gets bored with item. Worry level is divided by 3 to 26.
    Current worry level is not divisible by 19.
    Item with worry level 26 is thrown to monkey 0.
Monkey 2:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by itself to 6241.
    Monkey gets bored with item. Worry level is divided by 3 to 2080.
    Current worry level is divisible by 13.
    Item with worry level 2080 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 60.
    Worry level is multiplied by itself to 3600.
    Monkey gets bored with item. Worry level is divided by 3 to 1200.
    Current worry level is not divisible by 13.
    Item with worry level 1200 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 97.
    Worry level is multiplied by itself to 9409.
    Monkey gets bored with item. Worry level is divided by 3 to 3136.
    Current worry level is not divisible by 13.
    Item with worry level 3136 is thrown to monkey 3.
Monkey 3:
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 3 to 77.
    Monkey gets bored with item. Worry level is divided by 3 to 25.
    Current worry level is not divisible by 17.
    Item with worry level 25 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 500.
    Worry level increases by 3 to 503.
    Monkey gets bored with item. Worry level is divided by 3 to 167.
    Current worry level is not divisible by 17.
    Item with worry level 167 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 620.
    Worry level increases by 3 to 623.
    Monkey gets bored with item. Worry level is divided by 3 to 207.
    Current worry level is not divisible by 17.
    Item with worry level 207 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 1200.
    Worry level increases by 3 to 1203.
    Monkey gets bored with item. Worry level is divided by 3 to 401.
    Current worry level is not divisible by 17.
    Item with worry level 401 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 3136.
    Worry level increases by 3 to 3139.
    Monkey gets bored with item. Worry level is divided by 3 to 1046.
    Current worry level is not divisible by 17.
    Item with worry level 1046 is thrown to monkey 1.
---
After round 1, the monkeys are holding items with these worry levels:

Monkey 0: 20, 23, 27, 26
Monkey 1: 2080, 25, 167, 207, 401, 1046
Monkey 2: 
Monkey 3:

Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw them all before the round ended.

This process continues for a few more rounds:

After round 2, the monkeys are holding items with these worry levels:
Monkey 0: 695, 10, 71, 135, 350
Monkey 1: 43, 49, 58, 55, 362
Monkey 2: 
Monkey 3: 

After round 3, the monkeys are holding items with these worry levels:
Monkey 0: 16, 18, 21, 20, 122
Monkey 1: 1468, 22, 150, 286, 739
Monkey 2: 
Monkey 3: 

After round 4, the monkeys are holding items with these worry levels:
Monkey 0: 491, 9, 52, 97, 248, 34
Monkey 1: 39, 45, 43, 258
Monkey 2: 
Monkey 3: 

etc.

After round 20, the monkeys are holding items with these worry levels:
Monkey 0: 10, 12, 14, 26, 34
Monkey 1: 245, 93, 53, 199, 115
Monkey 2: 
Monkey 3: 

Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys if you want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds:

Monkey 0 inspected items 101 times.
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
Monkey 3 inspected items 105 times.
In this example, the two most active monkeys inspected items 101 and 105 times. The level of monkey business in this situation can be found by multiplying these together: 10605.

Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
"""

"""
Input lines are sets of monkeys each separated by a blank line and follows this format:

---
Monkey <MONKEY NUMBER>:
  Starting items: <COMMA SEPERATED LIST OF WORRY LEVELS>
  Operation: <FUNCTION TO CALCULATE NEW WORRY LEVEL FROM CURRENT>
  Test: Divisible by <NUMBER TO CHECK IF CURRENT WORRY LEVEL IS DIVISIBLE BY>
    If true: throw to monkey <TARGET MONKEY IF DIVISIBLE BY TEST>
    If false: throw to monkey <TARGET MONKEY IF NOT DIVISIBLE BY TEST>
---

For example:
---
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
---

"""

# Return a dict of monkeys keyed by monkey number
import copy
from functools import reduce
import json
import sys

def parse_monkeys(lines):
    monkeys = {}
    monkey = None
    for line in lines:
        line = line.strip()
        if line.startswith('Monkey'):
            monkey = int(line.split(' ')[1].strip(':'))
            monkeys[monkey] = {"inspect_count": 0}
        elif line.startswith('Starting items:'):
            monkeys[monkey]['items'] = [int(x) for x in line.split(':')[1].split(',')]
        elif line.startswith('Operation:'):
            operation = line.split('=')[1].strip()
            monkeys[monkey]['operation'] = lambda old,op=operation: eval(op)
            monkeys[monkey]['operand'] = operation.split(' ')[-1]
        elif line.startswith('Test:'):
            monkeys[monkey]['test'] = int(line.split(':')[1].split(' ')[-1])
        elif line.startswith('If true:'):
            monkeys[monkey]['if_true'] = int(line.split(':')[1].split(' ')[-1])
        elif line.startswith('If false:'):
            monkeys[monkey]['if_false'] = int(line.split(':')[1].split(' ')[-1])
    return monkeys

# @profile
def process_round(monkeys, round_count, reduce_worry_level=True):
    # print("monkey", "worry_level", "new_worry_level", "test", "result", "dest_monkey")
    # multiply the 'test' value of all of the monkeys
    super_mod = reduce(lambda x,y: x*y, [monkeys[monkey]['test'] for monkey in monkeys])
    
    for _ in range(1,round_count+1):
        # The monkey dictionary is structured like this, keyed on monkey number:
        # "3": { // monkey number
        #     "inspect_count": number, // number of items inspected
        #     "items": array, // list of worry levels for items held
        #     "operation": lambda function, // operation to perform on worry level before running divisor test
        #     "test": divisor, // divisor test to determine if item is thrown to if_true or if_false
        #     "if_true": number, // monkey number to throw item to if test is true
        #     "if_false": number // monkey number to throw item to if test is false
        # }
        for monkey in monkeys: 
            this_monkey = monkeys[monkey]
            item_count = len(this_monkey['items'])
            for item_idx in range(item_count):
                this_monkey['inspect_count'] += 1
                worry_level = this_monkey['items'][item_idx] % super_mod
                new_worry_level = this_monkey['operation'](worry_level)
                if reduce_worry_level:
                    # divide by 3 and round down
                    new_worry_level = new_worry_level // 3
                # if worry_level is divisible by test, move from this monkey to if_true, else move to if_false
                if new_worry_level % this_monkey['test'] == 0:
                    # print(monkey, worry_level, new_worry_level, monkeys[monkey]['test'], "true", monkeys[monkey]['if_true'])
                    monkeys[this_monkey['if_true']]['items'].append(new_worry_level)
                else:
                    # print(monkey, worry_level, new_worry_level, monkeys[monkey]['test'], "false", monkeys[monkey]['if_false'])
                    monkeys[this_monkey['if_false']]['items'].append(new_worry_level)
            # the monkey threw all their items, so clear the list
            this_monkey['items'] = []

    print('---')
    print('After round %d, the monkeys are holding items with these worry levels:' % round_count)
    for monkey in monkeys:
        print('Monkey %d. inspected %d, items: %s' % (monkey, monkeys[monkey]['inspect_count'], monkeys[monkey]['items']))
        # print('Monkey %d. inspected %d' % (monkey, monkeys[monkey]['inspect_count']))
    return monkeys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 %s <input>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    monkeys = parse_monkeys(lines)

    if len(sys.argv) > 2: 
        count = int(sys.argv[2])
    else:
        count = 20

    # monkeys = process_round(monkeys, count)
    monkeys = process_round(monkeys, count, reduce_worry_level=False)

    # find the two most active monkeys
    most_active = sorted(monkeys, key=lambda x: monkeys[x]['inspect_count'], reverse=True)[:2]
    print('The two most active monkeys are %d and %d' % (most_active[0], most_active[1]))
    print('The level of monkey business is %d' % (monkeys[most_active[0]]['inspect_count'] * monkeys[most_active[1]]['inspect_count']))