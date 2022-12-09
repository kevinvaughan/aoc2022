"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390
Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
The top-middle 5 is visible from the top and right.
The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.
"""

"""
1. Create a function to answer this: Consider your map; how many trees are visible from outside the grid?
2. Call that function with input from a file passed in on the command line, which is a 2d list of numbers
"""

import sys
import numpy
import pandas

def count_visible_trees(map):
    """
    Count the number of trees visible from outside the grid.
    """
    # Convert the map to a numpy array
    map_array = numpy.array(map)
    # Get the dimensions of the map
    map_height = map_array.shape[0]
    map_width = map_array.shape[1]
    # Create a dataframe to hold the results
    results = pandas.DataFrame(index=range(map_height), columns=range(map_width))
    # Loop through the rows
    for row in range(map_height):
        # Loop through the columns
        for col in range(map_width):
            # Get the height of the current tree
            tree_height = map_array[row, col]
            # Get the heights of the trees to the left
            left_heights = map_array[row, :col]
            # Get the heights of the trees to the right
            right_heights = map_array[row, col+1:]
            # Get the heights of the trees above
            above_heights = map_array[:row, col]
            # Get the heights of the trees below
            below_heights = map_array[row+1:, col]
            # Check if the current tree is visible from the left
            if len(left_heights) == 0 or tree_height > max(left_heights):
                results.loc[row, col] = 1
            # Check if the current tree is visible from the right
            if len(right_heights) == 0 or tree_height > max(right_heights):
                results.loc[row, col] = 1
            # Check if the current tree is visible from above
            if len(above_heights) == 0 or tree_height > max(above_heights):
                results.loc[row, col] = 1
            # Check if the current tree is visible from below
            if len(below_heights) == 0 or tree_height > max(below_heights):
                results.loc[row, col] = 1
    # Count the number of trees visible from outside the grid
    return results.sum().sum()

"""
--- Part Two ---

Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

Example Input:
---
30373
25512
65332
33549
35390
---
Considering the middle 5 in the second row, the following trees are visible:
Looking up, its view is not blocked; it can see 1 tree (of height 3).
Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
Looking right, its view is not blocked; it can see 2 trees.
Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

Example Input:
---
30373
25512
65332
33549
35390
---
Consider the tree of height 5 in the middle of the fourth row, the following trees are visible:
Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
Looking left, its view is not blocked; it can see 2 trees.
Looking down, its view is also not blocked; it can see 1 tree.
Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
This tree's scenic score is 8 (2 * 2 * 1 * 2)

Out of all of the trees, this is the ideal spot for the tree house with the highest scenic score: 8.
"""

def highest_scenic_score(map):
    """
    Consider each tree on your map. What is the highest scenic score possible for any tree?
    """
    # Convert the map to a numpy array
    map_array = numpy.array(map)
    # Get the dimensions of the map
    map_height = map_array.shape[0]
    map_width = map_array.shape[1]

    # Create a dataframe to hold the results
    results = pandas.DataFrame(index=range(map_height), columns=range(map_width))
    # Loop through the rows (but not the edges, as they'll have a 0 that makes this pointless)
    for row in range(1, map_height - 1):
        # Loop through the columns (but not the edges, as they'll have a 0 that makes this pointless)
        for col in range(1, map_width - 1):
            # Get the height of the current tree
            tree_height = map_array[row, col]

            # for this column, what is the next row up that is taller than this tree?
            next_up = 0
            for i in range(row - 1, -1, -1):
                if map_array[i, col] >= tree_height:
                    next_up = i
                    break

            # for this column, what is the next row down that is taller than this tree?
            next_lower = 0
            for i in range(row + 1, map_height):
                if map_array[i, col] >= tree_height:
                    next_lower = i
                    break

            # for this row, what is the next column to the left that is taller than this tree?
            next_left = 0
            for i in range(col - 1, -1, -1):
                if map_array[row, i] >= tree_height:
                    next_left = i
                    break

            # for this row, what is the next column to the right that is taller than this tree?
            next_right = 0
            for i in range(col + 1, map_width):
                if map_array[row, i] >= tree_height:
                    next_right = i
                    break

            # distance up
            distance_up = row - next_up

            # distance down
            if (next_lower == 0):
                distance_down = map_height - row - 1
            else:
                distance_down = next_lower - row

            # distance left
            distance_left = col - next_left

            # distance right
            if (next_right == 0):
                distance_right = map_width - col - 1
            else:
                distance_right = next_right - col

            results.loc[row, col] = distance_up * distance_down * distance_left * distance_right

    # Return the highest scenic score
    return results.max().max()

if __name__ == "__main__":
    # Get the input file from the command line
    input_file = sys.argv[1]
    # Read the input file
    with open(input_file, 'r') as f:
        # Read the input file as a list of lists
        map = [list(line.strip()) for line in f]
    # Convert the map to a list of lists of integers
    map = [[int(x) for x in row] for row in map]
    # Count the number of trees visible from outside the grid
    print(count_visible_trees(map))
    print(highest_scenic_score(map))