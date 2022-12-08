from functools import reduce

from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session.
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=8)
    data = puzzle.input_data
    data = [line for line in data.split("\n")]
    data = [[int(x) for x in line] for line in data]
    pivot_data = list(map(list, zip(*data)))
    return data, pivot_data


def range_tree(data_test, data_pivot, x, y):
    rows_list = [max(data_test[x][y + 1:]),
                 max(data_test[x][:y]),
                 max(data_pivot[y][x + 1:]),
                 max(data_pivot[y][:x])]
    return len([*filter(lambda z: z < data_test[x][y], rows_list)]) > 0


def append_value(n):
    try:
        return n.index(False) + 1
    except ValueError:
        return len(n)


def range_tree_2(data_test, data_pivot, x, y):
    rows_list = [[k < data_test[x][y] for k in data_test[x][y + 1:]],
                 [k < data_test[x][y] for k in data_test[x][:y]][::-1],
                 [k < data_test[x][y] for k in data_pivot[y][x + 1:]],
                 [k < data_test[x][y] for k in data_pivot[y][:x]][::-1]]

    return reduce((lambda i, j: i * j), map(append_value, rows_list))


def part_1():
    data, pivot_data = get_puzzle()
    result = [[range_tree(data, pivot_data, x, y) for y in range(1, len(data[x]) - 1)] for x in
              range(1, len(data) - 1)]

    return sum([sum(x) for x in result]) + len(data) * 2 + (len(data) - 2) * 2


def part_2():
    data, pivot_data = get_puzzle()
    result = [[range_tree_2(data, pivot_data, x, y) for y in range(1, len(data[x]) - 1)] for x in
              range(1, len(data) - 1)]
    return max([max(r) for r in result])


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
