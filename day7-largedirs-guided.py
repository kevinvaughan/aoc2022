"""
Given input like this:
---
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
---

A directory is a node in a tree. The root node is /, and each node has a size, which is the sum of the sizes of all of its children. The size of a file is the size of the file itself. For the input above, this could be viewed as a tree like this:
---
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
---

The total sizes of the directories above can be found as follows:
---
The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
---

To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)
"""

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
import json
import sys


def part1(lines):
    # Create a dictionary to store the file system
    file_system = {}
    # Create a list to store the current directory
    current_dir = []
    # Create a list to store the total size of the directories
    total_size = []

    for line in lines:
        # Remove the newline character
        line = line.strip()
        # Split the line into a list
        line = line.split()
        # If the line starts with $, it is a command
        if line[0] == '$':
            # If the command is cd, change the current directory
            if line[1] == 'cd':
                # If the argument is .., move up one directory
                if line[2] == '..':
                    # If the current directory is not the outermost directory, move up one directory
                    if current_dir != []:
                        current_dir.pop()
                # If the argument is /, move to the outermost directory
                elif line[2] == '/':
                    current_dir = []
                # If the argument is a directory, move to that directory
                else:
                    # Add the directory to the current directory
                    current_dir.append(line[2])
        elif line[0] != 'dir':
            # file, add size to current directory and all parent directories up to root
            for i in range(len(current_dir)+1):
                # Get the current directory
                current = '/'.join(current_dir[:i])
                # If the current directory is not in the file system, add it
                if current not in file_system:
                    file_system[current] = 0
                # Add the size of the file to the current directory
                file_system[current] += int(line[0])

    # Find all of the directories with a total size of at most 100000
    for key in file_system:
        if file_system[key] <= 100000:
            total_size.append(file_system[key])
    
    # Return the sum of the total sizes of those directories
    return sum(total_size)

"""
The total disk size is 70000000. At least 30000000 must be available.
Amount of space available is total disk size - total size of root directory.
Amount of space needed is the size of the smallest directory that, if deleted, would increase the amount of space available to at least 30000000.
"""

# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
def part2(lines):
    # Create a dictionary to store the file system
    file_system = {}
    # Create a list to store the current directory
    current_dir = []
    # Create a list to store the total size of the directories
    total_size = []

    for line in lines:
        # Remove the newline character
        line = line.strip()
        # Split the line into a list
        line = line.split()
        # If the line starts with $, it is a command
        if line[0] == '$':
            # If the command is cd, change the current directory
            if line[1] == 'cd':
                # If the argument is .., move up one directory
                if line[2] == '..':
                    # If the current directory is not the outermost directory, move up one directory
                    if current_dir != []:
                        current_dir.pop()
                # If the argument is /, move to the outermost directory
                elif line[2] == '/':
                    current_dir = []
                # If the argument is a directory, move to that directory
                else:
                    # Add the directory to the current directory
                    current_dir.append(line[2])
        elif line[0] != 'dir':
            # file, add size to current directory and all parent directories up to root
            for i in range(len(current_dir)+1):
                # Get the current directory
                current = '/'.join(current_dir[:i])
                # If the current directory is not in the file system, add it
                if current not in file_system:
                    file_system[current] = 0
                # Add the size of the file to the current directory
                file_system[current] += int(line[0])

    space_needed = 30000000 - (70000000 - file_system[''])
    
    # filter file_system values to only include directories greater than space_needed and return the smallest
    return min([value for key, value in file_system.items() if value > space_needed])


if __name__ == '__main__':
    # Read in the input
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
