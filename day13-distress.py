
import numpy as py
import pandas as pd
import scipy.ndimage as nd
import json
import functools




def load_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    pairs = []
    for i in range(0, len(lines), 3):
        pairs.append((eval(lines[i]), eval(lines[i+1])))
    return pairs

pairs = load_input('day13-input.txt')
pairs





# Returns true if pair is in the right order, false otherwise
def compare_items(pair, debug_print=False):
    # If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
    # If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
    # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2]
    left_side, right_side = pair
    if isinstance(left_side, int) and isinstance(right_side, int):
        if debug_print: print("2 ints:", left_side, right_side)
        if left_side < right_side:
            return True
        elif left_side > right_side:
            return False
        else:
            return None
    elif isinstance(left_side, list) and isinstance(right_side, list):
        if debug_print: print("2 lists: <{}>({}) <{}>({})".format(left_side, len(left_side), right_side, len(right_side)))
        while len(left_side) > 0 and len(right_side) > 0:
            if debug_print: print(" items:", left_side[0], right_side[0])
            subcomp = compare_items((left_side[0], right_side[0]))
            if subcomp is not None:
                return subcomp
            left_side = left_side[1:]
            right_side = right_side[1:]
        if len(left_side) == 0 and len(right_side) > 0:
            if debug_print: print("left side is shorter", len(left_side), len(right_side))
            return True
        elif len(left_side) > 0 and len(right_side) == 0:
            if debug_print: print("right side is shorter", len(left_side), len(right_side))
            return False
        else:
            return None
    elif isinstance(left_side, int):
        if debug_print: print("left int:", left_side, right_side)
        subcomp = compare_items(([left_side], right_side))
        if subcomp is not None:
            return subcomp
    elif isinstance(right_side, int):
        if debug_print: print("right int:", left_side, right_side)
        subcomp = compare_items((left_side, [right_side]))
        if subcomp is not None:
            return subcomp



correct_idx_sum = 0
for idx,pair in enumerate(pairs):
    if compare_items(pair):
        correct_idx_sum += idx + 1
    print(compare_items(pair))
# print(compare_items(pairs[4], debug_print=True))

print(correct_idx_sum)





# flatten pairs = [(pair1, pair2), (pair3, pair4), ...] in to [pair1, pair2, pair3, pair4, ...]
flat_list = [item for sublist in pairs for item in sublist]
flat_list.append([[2]])
flat_list.append([[6]])
print(flat_list)


# comparison ordering
# True < None < False

# sort by comparison of two list items
def compare(item1, item2):
    comparison = compare_items((item1, item2))
    if comparison is None:
        return 0
    elif comparison:
        return -1
    else:
        return 1

sorted_list = sorted(flat_list, key=functools.cmp_to_key(compare))
print(sorted_list)
decoder_start = sorted_list.index([[2]]) + 1
decoder_end = sorted_list.index([[6]]) + 1
print(decoder_start, decoder_end, decoder_start * decoder_end)



