from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session..
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=6)
    data = puzzle.input_data
    data = [x for x in data]
    return data


def start_of_marker(i):
    data = get_puzzle()
    values = [len(set(data[x:x + i])) for x in range(len(data) - i-1)]
    return values.index(i) + i


def part_1():
    return start_of_marker(4)


def part_2():
    return start_of_marker(14)


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")