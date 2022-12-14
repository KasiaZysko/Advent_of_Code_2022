import ast
import math
from functools import cmp_to_key
from itertools import chain

from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session..
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=13)
    data = puzzle.input_data
    data = [list(map(ast.literal_eval, section.splitlines())) for section in data.split('\n\n')]
    return data


def compare_sides(left, right):
    for i in range(max(len(left), len(right))):
        if i == len(left):
            return True
        if i == len(right):
            return False
        if type(left[i]) is int and type(right[i]) is int:
            if left[i] is not right[i]:
                return left[i] < right[i]
        else:
            result = compare_sides(left[i] if type(left[i]) is list else [left[i]],
                                   right[i] if type(right[i]) is list else [right[i]])
            if result is not None:
                return result


def change_result_to_int(result: bool):
    if result:
        return -1
    elif result is None:
        return 0
    else:
        return 1


def part_1():
    data = get_puzzle()
    comparison = [i + 1 for i in range(len(data)) if compare_sides(data[i][0], data[i][1])]
    return sum(comparison)


def part_2():
    data = get_puzzle()
    data_plain = list(chain(*data)) + [[2], [6]]
    sorted_list = sorted(data_plain,
                         key=cmp_to_key(lambda left, right: change_result_to_int(compare_sides(left, right))))
    return math.prod([i + 1 for i, e in enumerate(sorted_list) if e == [2] or e == [6]])


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
