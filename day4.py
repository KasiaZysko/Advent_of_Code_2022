from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session.
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=4)
    data = puzzle.input_data
    data = [line for line in data.split("\n")]
    data = [[(int(num.split("-")[0]), int(num.split("-")[1])) for num in character.split(",")] for character in data]
    return data


def range_subset(range1, range2):
    return range1.start in range2 and range1[-1] in range2 or range2.start in range1 and range2[-1] in range1


def part_1():
    data = get_puzzle()
    same_range = [range_subset(range(r[0][0], r[0][1] + 1), range(r[1][0], r[1][1] + 1)) for r in data]
    return sum(same_range)


def part_2():
    data = get_puzzle()
    same_range = [sum(set(range(r[0][0], r[0][1] + 1)).intersection(range(r[1][0], r[1][1] + 1))) > 0 for r in data]
    return sum(same_range)


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
