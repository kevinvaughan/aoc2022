"""
Given a list of this format:
---
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
---
Sum each block of numbers and return the block with the largest total.
"""
def maximum_block(list):
    max_block = 0
    current_block = 0
    for i in list:
        if i == '':
            if current_block > max_block:
                max_block = current_block
            current_block = 0
        else:
            current_block += int(i)
    return max_block

"""
Given the same list, return the sum of the 'count' largest blocks
"""
def maximum_blocks(list, count):
    max_blocks = []
    current_block = 0
    for i in list:
        if i == '':
            max_blocks.append(current_block)
            max_blocks.sort()
            if len(max_blocks) > count:
                max_blocks.pop(0)
            current_block = 0
        else:
            current_block += int(i)
    return sum(max_blocks)

with open("day1-input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
print(maximum_block(content))
print(maximum_blocks(content, 3))