"""

Pathfinding with a hillclimbing algorithm.

For the input:
1. Elevation is given as a letter, with 'a' being the lowest
2. 'S' is the start position
3. 'E' is the end position

The algorithm will find the shortest path from S to E, using only
adjacent squares (no diagonal movement). Each step can only be
taken if the elevation of the next square is at most 1 higher than
the current square, but can be lower.

Example input:
---
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
---

The output is a grid replaced with the path taken from S to E, where
each step on the path is marked with a symbol showing the direction
the path exits each square moving up (^), down (v), left (<), or right (>).
E should still be marked, and unvisited squares should be marked with a '.'.

---
v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
---

"""

import sys

# Recursive function to find the path 
def next_step(map_array, position, end_position, current_path, visited, result_paths):
    # create a copy of current_path and add position to it
    path = current_path[:]
    path.append(position)
    # If we're already longer than a solved path, bail
    if len(result_paths) > 0:
        if len(path) >= min([len(x) for x in result_paths]):
            return None

    # if we are at the end, return the path
    if position == end_position:
        return path

    # if we have already visited this position, and the path is longer than when we did, bail
    # could be further optimized by keeping track of the shortest path to each position
    if position in visited.keys():
        if visited[position] <= len(path):
            return None

    # get a list of possible neighbors
    neighbors = possible_neighbors(map_array, position)
    # for each neighbor, if it is not in visited, call next_step
    for neighbor in neighbors:
        if neighbor not in path:
            p = next_step(map_array, neighbor, end_position, path, visited, result_paths)
            if p:
                result_paths.append(p)

    visited[position] = len(path)

    return None

def possible_neighbors(map_array, position):
    """Return a list of possible neighbors to move to."""
    (x, y) = position
    neighbors = []
    if x > 0 and map_array[y][x-1] <= (map_array[y][x] + 1):
        neighbors.append((map_array[y][x-1] ,(x-1, y)))
    if x < len(map_array[0]) - 1 and map_array[y][x+1] <= (map_array[y][x] + 1):
        neighbors.append((map_array[y][x+1], (x+1, y)))
    if y > 0 and map_array[y-1][x] <= (map_array[y][x] + 1):
        neighbors.append((map_array[y-1][x], (x, y-1)))
    if y < len(map_array) - 1 and map_array[y+1][x] <= (map_array[y][x] + 1):
        neighbors.append((map_array[y+1][x], (x, y+1)))
    neighbors.sort(key=lambda x: x[0], reverse=True) # prefer to climb over plateau
    return [x[1] for x in neighbors]

def map_height(input_grid):
    """Return a grid with the path from S to E marked with arrows."""
    # Find the start and end positions
    map_grid = input_grid[:]
    for y, row in enumerate(map_grid):
        for x, c in enumerate(row):
            if c == 'S':
                start = (x, y)
                map_grid[y][x] = 0
            elif c == 'E':
                end = (x, y)
                map_grid[y][x] = 25
            else:
                map_grid[y][x] = ord(c) - ord('a')

    return (map_grid, start, end)


def main():
    """Main program."""
    # The input grid
    input_grid = []

    # Read the input grid from a file given on the command line
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            for line in f:
                input_grid.append(list(line.strip()))

    # Print the input grid
    print("input\n","\n".join(" ".join(str(c) for c in row) for row in input_grid))

    # Print the path grid
    height_map = [[x[:] for x in row] for row in input_grid]
    (height_map, start, end) = map_height(height_map)
    print("height map")
    print("\n".join("".join("%3s" % c for c in row) for row in height_map))
    print(start, end)

    shortest_path = None
    search_count = 0
    result_paths = []
    for y, row in enumerate(height_map):
        for x, c in enumerate(row):
            if c == 0:
                search_count += 1
                print(search_count, " starting at ", (x, y))
                # array of arrays of paths
                visited = {}
                next_step(height_map, (x,y), end, [], visited, result_paths)
                if len(result_paths) > 0:
                    if shortest_path == None:
                        shortest_path = result_paths[0]
                    for path in result_paths:
                        if len(path) < len(shortest_path):
                            shortest_path = path

    # create a value copy of the height map
    
    output_map = [[x[:] for x in row] for row in input_grid]
    # replace all the numbers with '.'
    for y, row in enumerate(output_map):
        for x, c in enumerate(row):
            if start == (x, y):
                output_map[y][x] = 'S'
            elif end == (x, y):
                output_map[y][x] = 'E'
            else:
                output_map[y][x] = '.'

    # step through path and replace with arrows
    for i in range(len(shortest_path) - 1):
        (x, y) = shortest_path[i]
        print(input_grid[y][x], end=' ')
        (x2, y2) = shortest_path[i+1]
        if x2 == x:
            if y2 > y:
                output_map[y][x] = 'v'
            else:
                output_map[y][x] = '^'
        else:
            if x2 > x:
                output_map[y][x] = '>'
            else:
                output_map[y][x] = '<'

    print("\noutput")
    print("\n".join("".join("%s" % c for c in row) for row in output_map))
    print("path length", len(shortest_path))

    

if __name__ == '__main__':
    main()