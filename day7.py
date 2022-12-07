from aocd.models import Puzzle
from collections import defaultdict

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session.
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=7)
    data = puzzle.input_data
    data = [line for line in data.split("\n")]
    data = [line.strip("\n").rsplit(' ', 1) for line in data]
    return data


def directory_info(entry):
    return (True, entry[1]) if entry[0] == "$ cd" else (False, int(entry[0])) if entry[0][0].isdigit() else None


def dir_collection():
    current_path = list()
    dir_tree = defaultdict(lambda: 0)
    directory_list = [directory_info(i) for i in get_puzzle() if directory_info(i) is not None]
    for dir_change, info in directory_list:
        if dir_change:
            current_path.pop() if info == ".." else current_path.append(info)
        else:
            for i in range(len(current_path)):
                dir_tree["".join(current_path[0:i+1])] += info
    return dir_tree


def part_1():
    max_size = 100000
    dir_tree = dir_collection()
    return sum(i for i in dir_tree.values() if i <= max_size)


def part_2():
    total_space = 70000000
    required_space = 30000000
    dir_tree = dir_collection()
    space_to_del = required_space - (total_space - dir_tree["/"])
    return min(i for i in dir_tree.values() if i - space_to_del >= 0)


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
