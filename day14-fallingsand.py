# %%
import sys
import numpy as np
import pandas as pd
import json


# %%
# Data is a list of paths, one path per line
# Each path is a list of points, and a line is drawn between each point
# Each point is a list of coordinates
# Example path input: "498,4 -> 498,6 -> 496,6"
# Lines parsed from example: [498,4] -> [498,6], [498,6] -> [496,6]

# Load a dataframe from a file with a default value of '.' and a value of '#' for every point in the paths
def load_df_from_file(filename, default_value='.', path_value='#'):
    with open(filename, 'r') as f:
        paths = [path.split(' -> ') for path in f.read().splitlines()]
        # Get all the points in the paths
        points = [point for path in paths for point in path]
        # Get the min and max x and y values
        min_x = min([int(point.split(',')[0]) for point in points])
        max_x = max([int(point.split(',')[0]) for point in points])
        min_y = 0
        # min_y = min([int(point.split(',')[1]) for point in points])
        max_y = max([int(point.split(',')[1]) for point in points])
        # Create a dataframe with the default value, maintaining coordinates as keys
        df = pd.DataFrame(np.full((max_y - min_y + 1, max_x - min_x + 1), default_value), index=range(min_y, max_y + 1), columns=range(min_x, max_x + 1))
        # Fill in the values for each path
        for path in paths:
            for i in range(len(path) - 1):
                x1, y1 = path[i].split(',')
                x2, y2 = path[i + 1].split(',')
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # If the line is vertical
                if x1 == x2:
                    # If the line goes down
                    if y1 < y2:
                        df.iloc[y1 - min_y:y2 - min_y + 1, x1 - min_x] = path_value
                    # If the line goes up
                    else:
                        df.iloc[y2 - min_y:y1 - min_y + 1, x1 - min_x] = path_value
                # If the line is horizontal
                else:
                    # If the line goes right
                    if x1 < x2:
                        df.iloc[y1 - min_y, x1 - min_x:x2 - min_x + 1] = path_value
                    # If the line goes left
                    else:
                        df.iloc[y1 - min_y, x2 - min_x:x1 - min_x + 1] = path_value
        return df

input_df = load_df_from_file('day14-input.txt')
input_sample_df = load_df_from_file('day14-inputsample.txt')

# %%

# Until a '+' can no longer move down, it moves 1 block at a time based on these rules:
# 1. If the block below is '.', it moves down and its previous location is replaced with '.'
# 2. Otherwise, if the block down and to the left is '.', it moves down and to the left and its previous location is replaced with '.'
# 3. Otherwise, if the block down and to the right is '.', it moves down and to the right
# 4. Otherwise, it stops moving and turns to a 'o'
# 5. Once it becomes an 'o', it stops moving
# 6. A '+' is created at the original coordinates of the '+' for each unit of sand

def move_down(df, row, col):
    # If the block below is '.', it moves down and its previous location is replaced with '.'
    if df.loc[row + 1, col] == '.':
        # print("moved down from ({}, {}) to ({}, {})".format(row, col, row + 1, col))
        df.loc[row, col] = '.'
        df.loc[row + 1, col] = '+'
        return row + 1, col
    # Otherwise, if the block down and to the left is '.', it moves down and to the left and its previous location is replaced with '.'
    elif df.loc[row + 1, col - 1] == '.':
        # print("moved down and left from ({}, {}) to ({}, {})".format(row, col, row + 1, col - 1))
        df.loc[row, col] = '.'
        df.loc[row + 1, col - 1] = '+'
        return row + 1, col - 1
    # Otherwise, if the block down and to the right is '.', it moves down and to the right
    elif df.loc[row + 1, col + 1] == '.':
        # print("moved down and right from ({}, {}) to ({}, {})".format(row, col, row + 1, col + 1))
        df.loc[row, col] = '.'
        df.loc[row + 1, col + 1] = '+'
        return row + 1, col + 1
    # Otherwise, it stops moving and turns to a 'o'
    else:
        # print("stopped moving at ({}, {})".format(row, col))
        df.loc[row, col] = 'o'
        return row, col

def move_down_until_stopped(df, row, col):
    # Once it becomes an 'o', it stops moving
    while df.loc[row, col] != 'o':
        row, col = move_down(df, row, col)
    return row, col

def drop_sand(df):
    # create copy of input_df
    input_df_copy = input_df.copy()
    i = 0
    while True:
        i += 1
        row, col = (0, 500)
        df.loc[0, 500] = '+'
        try:
            row, col = move_down_until_stopped(df, row, col)
            if (row, col) == (0, 500):
                print("stopped at sand {}".format(i))
                return df
        except:
            print("broke at sand {}".format(i - 1))
            return df


# %%

display(drop_sand(input_sample_df.copy()))
display(drop_sand(input_df.copy()))


# %%
def add_floor(df):
    # height of df
    height = len(df.index)

    cols_to_add = height * 2 - len(df.columns)
    # add cols_to_add number of columns to the left side all with values of '.'
    df = pd.concat([pd.DataFrame(np.full((len(df.index), cols_to_add), '.'), index=df.index, columns=range(min(df.columns) - cols_to_add, min(df.columns))) , df], axis=1)
    # do the same to the right
    df = pd.concat([df, pd.DataFrame(np.full((len(df.index), cols_to_add), '.'), index=df.index, columns=range(max(df.columns) + 1, max(df.columns) + cols_to_add + 1))], axis=1)

    df.loc[len(df.index)] = ['.' for i in range(len(df.columns))]
    df.loc[len(df.index)] = ['#' for i in range(len(df.columns))]
    return df

display(input_sample_df)
display(add_floor(input_sample_df.copy()))

# %%

final = drop_sand(add_floor(input_df.copy()))
display(final)


